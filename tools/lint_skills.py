"""Linter structurel et qualitatif des Agent Skills (`skills/*/*/SKILL.md`).

Contrôle pour chaque skill implémenté :
1. Validité du frontmatter YAML et conformité au schéma Anthropic Agent Skills (`name`, `description`, `metadata`).
2. Concordance exacte entre le nom de dossier, `frontmatter.name` et `CANONICAL_SKILLS`.
3. Présence des sections opérationnelles requises :
   - Conditions d'Activation & Périmètre
   - Limites & Interdictions
   - Procédures Opérationnelles & Règles de Décision
   - Chargement Progressif des Références & Modèles
   - Exemples d'Entrées & Sorties
   - Critères d'Acceptation & Validation (DoD)
4. Absence de formulations génériques creuses ("Tu es un expert exceptionnel...").
5. Validité et sécurité de tous les chemins relatifs (`references/...`, `templates/...`, `examples/...`, `scripts/...`) cités dans `SKILL.md`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT, YamlParseError, extract_frontmatter, resolve_safe_path
from tools.registry_data import SKILLS_BY_SLUG
from tools.validate_registry import load_source_ids

NAME_REGEX = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SRC_REF_REGEX = re.compile(r"\b(SRC-\d{3})\b")
LOCAL_FILE_REF_REGEX = re.compile(
    r"`((?:references|templates|examples|scripts)/[a-zA-Z0-9_./-]+)`"
)

FORBIDDEN_GENERIC_PHRASES: tuple[str, ...] = (
    "tu es un expert exceptionnel",
    "produis un travail de qualité",
    "fais de ton mieux",
    "sois créatif et professionnel",
)

REQUIRED_SECTION_KEYWORDS: tuple[tuple[str, str], ...] = (
    ("Conditions d'Utilisation", "Conditions"),
    ("Limites", "Limites"),
    ("Procédures", "Procédures"),
    ("Règles de Décision", "Décision"),
    ("Chargement Progressif", "Références"),
    ("Exemples", "Exemples"),
    ("Critères de Validation", "Validation"),
)


def lint_single_skill(skill_dir: Path) -> list[str]:
    """Vérifie la conformité complète d'un dossier de skill."""
    errors: list[str] = []
    slug = skill_dir.name
    dept_name = skill_dir.parent.name
    skill_md_path = skill_dir / "SKILL.md"

    if not skill_md_path.exists():
        return [f"{dept_name}/{slug}: fichier SKILL.md manquant."]

    spec = SKILLS_BY_SLUG.get(slug)
    if spec is None:
        errors.append(f"{dept_name}/{slug}: skill non répertorié dans CANONICAL_SKILLS.")
    elif spec.department != dept_name:
        errors.append(
            f"{dept_name}/{slug}: mauvais département (attendu {spec.department!r})."
        )

    raw_text = skill_md_path.read_text(encoding="utf-8")
    try:
        frontmatter, body = extract_frontmatter(raw_text)
    except YamlParseError as exc:
        return [f"{dept_name}/{slug}: erreur YAML frontmatter -> {exc}"]

    fm_name = str(frontmatter.get("name") or "").strip()
    fm_desc = str(frontmatter.get("description") or "").strip()
    metadata = frontmatter.get("metadata")

    if fm_name != slug:
        errors.append(
            f"{dept_name}/{slug}: frontmatter.name ({fm_name!r}) != nom du dossier ({slug!r})."
        )
    if not NAME_REGEX.match(fm_name) or len(fm_name) > 64:
        errors.append(f"{dept_name}/{slug}: frontmatter.name non conforme aux contraintes Anthropic.")

    if len(fm_desc) < 50 or len(fm_desc) > 1024:
        errors.append(
            f"{dept_name}/{slug}: frontmatter.description doit faire entre 50 et 1024 caractères (actuel={len(fm_desc)})."
        )

    if not isinstance(metadata, dict):
        errors.append(f"{dept_name}/{slug}: bloc metadata YAML manquant ou invalide.")
    else:
        meta_id = str(metadata.get("id") or "").strip()
        meta_dept = str(metadata.get("department") or "").strip()
        inputs = metadata.get("inputs")
        outputs = metadata.get("outputs")
        upstreams = metadata.get("upstream_dependencies")

        if spec and meta_id != spec.skill_id:
            errors.append(
                f"{dept_name}/{slug}: metadata.id ({meta_id!r}) != {spec.skill_id!r}."
            )
        if meta_dept != dept_name:
            errors.append(
                f"{dept_name}/{slug}: metadata.department ({meta_dept!r}) != {dept_name!r}."
            )
        if not isinstance(inputs, list) or not inputs:
            errors.append(f"{dept_name}/{slug}: metadata.inputs doit être une liste non vide.")
        if not isinstance(outputs, list) or not outputs:
            errors.append(f"{dept_name}/{slug}: metadata.outputs doit être une liste non vide.")
        if not isinstance(upstreams, list):
            errors.append(
                f"{dept_name}/{slug}: metadata.upstream_dependencies doit être une liste."
            )
        elif spec and tuple(str(u).strip() for u in upstreams) != spec.upstream_ids:
            errors.append(
                f"{dept_name}/{slug}: metadata.upstream_dependencies ({upstreams}) != catalogue ({list(spec.upstream_ids)})."
            )

    valid_srcs = load_source_ids(WORKSPACE_ROOT)
    if valid_srcs:
        for md_file in skill_dir.rglob("*.md"):
            md_txt = md_file.read_text(encoding="utf-8")
            for src_match in set(SRC_REF_REGEX.findall(md_txt)):
                if src_match not in valid_srcs:
                    rel_md = md_file.relative_to(skill_dir).as_posix()
                    errors.append(
                        f"{dept_name}/{slug} ({rel_md}): référence source fantôme {src_match!r} absente de research/source-registry.csv."
                    )

    lowered_body = body.lower()
    for forbidden in FORBIDDEN_GENERIC_PHRASES:
        if forbidden in lowered_body:
            errors.append(
                f"{dept_name}/{slug}: formulation générique interdite détectée ({forbidden!r})."
            )

    for label, keyword in REQUIRED_SECTION_KEYWORDS:
        if keyword.lower() not in lowered_body:
            errors.append(
                f"{dept_name}/{slug}: section obligatoire '{label}' (mot-clé {keyword!r}) absente de SKILL.md."
            )

    referenced_files = LOCAL_FILE_REF_REGEX.findall(body)
    if not referenced_files:
        errors.append(
            f"{dept_name}/{slug}: SKILL.md doit référencer au moins un fichier local dans references/ ou templates/."
        )

    for rel_ref in set(referenced_files):
        try:
            target_path = resolve_safe_path(skill_dir, rel_ref)
        except ValueError as exc:
            errors.append(f"{dept_name}/{slug}: {exc}")
            continue
        if not target_path.exists():
            errors.append(
                f"{dept_name}/{slug}: fichier référencé introuvable ({rel_ref!r})."
            )
        elif target_path.is_file() and target_path.stat().st_size < 150:
            errors.append(
                f"{dept_name}/{slug}: fichier référencé trop court ou vide ({rel_ref!r})."
            )

    for ref_file in (skill_dir / "references").glob("*.md"):
        line_count = len(ref_file.read_text(encoding="utf-8").splitlines())
        if line_count < 35:
            errors.append(
                f"{dept_name}/{slug}: référence {ref_file.name} trop superficielle ({line_count} lignes < 35 requises)."
            )

    for tpl_file in (skill_dir / "templates").glob("*"):
        if tpl_file.is_file():
            tpl_lines = tpl_file.read_text(encoding="utf-8").splitlines()
            if tpl_file.suffix == ".csv":
                if len(tpl_lines) < 2 or "," not in tpl_lines[0]:
                    errors.append(
                        f"{dept_name}/{slug}: template CSV {tpl_file.name} invalide (en-tête + au moins 1 ligne d'exemple attendus)."
                    )
            elif len(tpl_lines) < 10:
                errors.append(
                    f"{dept_name}/{slug}: template {tpl_file.name} trop court ({len(tpl_lines)} lignes < 10 requises)."
                )

    for subdir_name in ("references", "templates", "examples"):
        subdir = skill_dir / subdir_name
        if not subdir.exists() or not any(subdir.iterdir()):
            errors.append(
                f"{dept_name}/{slug}: sous-dossier obligatoire {subdir_name}/ absent ou vide."
            )

    return errors


def lint_skills_in_workspace(
    workspace: Path = WORKSPACE_ROOT,
    department_filter: str | None = None,
    require_all_57: bool = False,
) -> tuple[int, list[str]]:
    """Audite tous les skills présents (ou d'un département donné)."""
    skills_root = workspace / "skills"
    errors: list[str] = []
    checked_count = 0

    if not skills_root.exists():
        return 0, ["Le répertoire skills/ n'existe pas encore."]

    pattern = f"{department_filter}/*" if department_filter else "*/*"
    skill_dirs = sorted([p for p in skills_root.glob(pattern) if p.is_dir()])

    for skill_dir in skill_dirs:
        checked_count += 1
        errors.extend(lint_single_skill(skill_dir))

    if require_all_57:
        implemented_slugs = {p.name for p in skill_dirs}
        missing = sorted(set(SKILLS_BY_SLUG.keys()) - implemented_slugs)
        if missing:
            errors.append(
                f"Skills manquants ({len(missing)}/57) : {', '.join(missing[:10])}..."
            )

    return checked_count, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Linter des Agent Skills ZAÏRE STUDIO OS.")
    parser.add_argument("--department", help="Filtrer sur un département précis (ex: 00-direction)")
    parser.add_argument(
        "--require-all",
        action="store_true",
        help="Exiger que les 57 skills du catalogue soient tous implémentés.",
    )
    args = parser.parse_args()

    count, errors = lint_skills_in_workspace(
        WORKSPACE_ROOT, department_filter=args.department, require_all_57=args.require_all
    )
    if errors:
        print(f"[ERREUR] Linting échoué sur {count} skill(s) ({len(errors)} erreur(s)) :")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"[OK] {count} skill(s) vérifié(s) avec succès (0 erreur).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
