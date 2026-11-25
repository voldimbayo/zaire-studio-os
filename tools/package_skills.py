"""Générateur d'index et packager ZIP (Claude.ai & Archive Système Complète).

Produit :
1. `docs/skills-index.md` : Table de bord en temps réel des skills implémentés et vérifiés par département.
2. `releases/skills/<skill-name>.zip` : 57 archives ZIP autonomes prêtes à être importées dans Claude.ai.
3. `releases/zaire-studio-os-v<VERSION>-full.zip` : Archive complète du système ZAÏRE STUDIO OS.
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT
from tools.lint_skills import lint_single_skill
from tools.registry_data import CANONICAL_SKILLS


def update_skills_index(workspace: Path = WORKSPACE_ROOT) -> Path:
    """Met à jour `docs/skills-index.md` avec l'état réel d'implémentation et de validation."""
    docs_dir = workspace / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    index_path = docs_dir / "skills-index.md"

    implemented = 0
    validated = 0
    rows: list[str] = []

    for spec in CANONICAL_SKILLS:
        skill_dir = workspace / "skills" / spec.department / spec.slug
        if skill_dir.exists() and (skill_dir / "SKILL.md").exists():
            implemented += 1
            errs = lint_single_skill(skill_dir)
            if not errs:
                validated += 1
                status_badge = "CONFIRMED (Tests OK)"
            else:
                status_badge = f"ERROR ({len(errs)})"
            has_scripts = "Oui" if (skill_dir / "scripts").exists() else "Non"
        else:
            status_badge = "PENDING"
            has_scripts = "-"

        rows.append(
            f"| `{spec.skill_id}` | `{spec.slug}` | `{spec.department}` | Strate {spec.stratum} | {has_scripts} | **{status_badge}** |"
        )

    content = [
        "# Index Maître des Skills — ZAÏRE STUDIO OS (`skills-index.md`)",
        "",
        f"- **Progression Globale** : **{implemented} / {len(CANONICAL_SKILLS)}** skills implémentés",
        f"- **Skills Validés (Linter + YAML + Références)** : **{validated} / {len(CANONICAL_SKILLS)}**",
        "",
        "| ID | Nom du Skill (Kebab-Case) | Département | Strate DAG | Scripts Dédiés | Statut d'Implémentation |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
        *rows,
        "",
    ]
    new_text = "\n".join(content)
    # N'écrire que si le contenu change : préserve la date du fichier et rend
    # l'archive complète (qui l'embarque) reproductible d'un packaging à l'autre.
    if not index_path.exists() or index_path.read_text(encoding="utf-8") != new_text:
        index_path.write_text(new_text, encoding="utf-8")
    return index_path


def package_individual_skill(skill_dir: Path, output_dir: Path, workspace: Path = WORKSPACE_ROOT) -> Path:
    """Crée une archive ZIP individuelle compatible Claude.ai pour un skill.

    Inclut un instantané read-only de `knowledge/entities-registry.csv` dans
    `references/entities-registry-snapshot.csv` afin que le skill reste autonome
    même lorsqu'il est importé hors d'un Projet Claude.ai préconfiguré.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = skill_dir.name
    zip_path = output_dir / f"{slug}.zip"
    registry_snapshot = workspace / "knowledge" / "entities-registry.csv"

    with zipfile.ZipFile(zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(skill_dir.rglob("*")):
            if file_path.is_file() and "__pycache__" not in file_path.parts:
                arcname = f"{slug}/{file_path.relative_to(skill_dir).as_posix()}"
                zf.write(file_path, arcname=arcname)
        if registry_snapshot.exists():
            zf.write(
                registry_snapshot,
                arcname=f"{slug}/references/entities-registry-snapshot.csv",
            )

    return zip_path


def package_department_bundle(dept_dir: Path, output_dir: Path) -> Path:
    """Crée une archive ZIP regroupant tous les skills d'un département."""
    output_dir.mkdir(parents=True, exist_ok=True)
    dept_name = dept_dir.name
    zip_path = output_dir / f"{dept_name}.zip"

    with zipfile.ZipFile(zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(dept_dir.rglob("*")):
            if file_path.is_file() and "__pycache__" not in file_path.parts:
                arcname = f"{dept_name}/{file_path.relative_to(dept_dir).as_posix()}"
                zf.write(file_path, arcname=arcname)

    return zip_path


def package_all_releases(workspace: Path = WORKSPACE_ROOT) -> tuple[list[Path], list[Path], Path]:
    """Génère les archives individuelles Claude.ai, les archives par département et l'archive globale."""
    version_file = workspace / "VERSION"
    version = version_file.read_text(encoding="utf-8").strip() if version_file.exists() else "1.0.0"

    releases_dir = workspace / "releases"
    skills_zip_dir = releases_dir / "skills"
    depts_zip_dir = releases_dir / "departments"
    skills_zip_dir.mkdir(parents=True, exist_ok=True)
    depts_zip_dir.mkdir(parents=True, exist_ok=True)

    individual_zips: list[Path] = []
    department_zips: list[Path] = []
    skills_root = workspace / "skills"
    if skills_root.exists():
        for dept_dir in sorted(skills_root.glob("*")):
            if dept_dir.is_dir():
                department_zips.append(package_department_bundle(dept_dir, depts_zip_dir))
        for skill_dir in sorted(skills_root.glob("*/*")):
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                individual_zips.append(package_individual_skill(skill_dir, skills_zip_dir, workspace))

    full_zip_path = releases_dir / f"zaire-studio-os-v{version}-full.zip"
    included_roots = (
        "README.md",
        "CLAUDE.md",
        "CHANGELOG.md",
        "VERSION",
        "research",
        "architecture",
        "knowledge",
        "schemas",
        "templates",
        "skills",
        "production",
        "tools",
        "tests",
        "docs",
        "audit",
    )

    with zipfile.ZipFile(full_zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for item_name in included_roots:
            target = workspace / item_name
            if not target.exists():
                continue
            if target.is_file():
                zf.write(target, arcname=f"zaire-studio-os/{target.name}")
            else:
                for subfile in sorted(target.rglob("*")):
                    if subfile.is_file() and "__pycache__" not in subfile.parts:
                        rel = subfile.relative_to(workspace).as_posix()
                        zf.write(subfile, arcname=f"zaire-studio-os/{rel}")

    return individual_zips, department_zips, full_zip_path


def package_plugin(workspace: Path = WORKSPACE_ROOT) -> Path:
    """Crée l'archive plug-in Claude importable (`releases/zaire-studio-os-v<VERSION>-plugin.zip`).

    Structure attendue par l'import de plug-ins Claude :
    - `.claude-plugin/plugin.json` à la racine (manifeste) ;
    - `skills/<skill-name>/SKILL.md` à plat (un seul niveau, sans dossier de département) ;
    - aucune archive ZIP imbriquée (refusée par l'import).
    """
    version_file = workspace / "VERSION"
    version = version_file.read_text(encoding="utf-8").strip() if version_file.exists() else "1.0.0"
    releases_dir = workspace / "releases"
    releases_dir.mkdir(parents=True, exist_ok=True)
    plugin_zip = releases_dir / f"zaire-studio-os-v{version}-plugin.zip"
    registry_snapshot = workspace / "knowledge" / "entities-registry.csv"

    manifest = {
        "name": "zaire-studio-os",
        "version": version,
        "description": (
            "Système multi-agents de production AAA pour ZAÏRE (open world, Kinshasa, Unreal Engine 5) : "
            "7 skills de direction et 50 skills métiers orchestrés en DAG."
        ),
        "author": {"name": "ZAÏRE STUDIO"},
        "keywords": ["game-dev", "unreal-engine-5", "open-world", "narrative", "kinshasa"],
    }

    def _is_packable(path: Path) -> bool:
        return path.is_file() and "__pycache__" not in path.parts and path.suffix.lower() != ".zip"

    with zipfile.ZipFile(plugin_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        # Horodatage fixe : sans lui, writestr() utilise l'heure courante et l'archive
        # change à chaque packaging (diff binaire inutile dans Git).
        manifest_info = zipfile.ZipInfo(".claude-plugin/plugin.json", date_time=(1980, 1, 1, 0, 0, 0))
        manifest_info.compress_type = zipfile.ZIP_DEFLATED
        manifest_info.external_attr = 0o644 << 16
        zf.writestr(manifest_info, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        readme = workspace / "README.md"
        if readme.exists():
            zf.write(readme, arcname="README.md")
        for skill_dir in sorted((workspace / "skills").glob("*/*")):
            if not (skill_dir.is_dir() and (skill_dir / "SKILL.md").exists()):
                continue
            slug = skill_dir.name
            for file_path in sorted(skill_dir.rglob("*")):
                if _is_packable(file_path):
                    zf.write(file_path, arcname=f"skills/{slug}/{file_path.relative_to(skill_dir).as_posix()}")
            if registry_snapshot.exists():
                zf.write(registry_snapshot, arcname=f"skills/{slug}/references/entities-registry-snapshot.csv")
        knowledge_dir = workspace / "knowledge"
        for file_path in sorted(knowledge_dir.rglob("*")) if knowledge_dir.exists() else []:
            if _is_packable(file_path):
                zf.write(file_path, arcname=file_path.relative_to(workspace).as_posix())

    return plugin_zip


def main() -> int:
    idx_path = update_skills_index(WORKSPACE_ROOT)
    ind_zips, dept_zips, full_zip = package_all_releases(WORKSPACE_ROOT)
    plugin_zip = package_plugin(WORKSPACE_ROOT)
    print(f"[OK] Plug-in Claude importable : {plugin_zip.relative_to(WORKSPACE_ROOT)}")
    print(f"[OK] Index mis à jour : {idx_path.relative_to(WORKSPACE_ROOT)}")
    print(f"[OK] {len(ind_zips)} archive(s) ZIP individuelle(s) générée(s) dans releases/skills/")
    print(f"[OK] {len(dept_zips)} archive(s) ZIP départementale(s) générée(s) dans releases/departments/")
    print(f"[OK] Archive globale générée : {full_zip.relative_to(WORKSPACE_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
