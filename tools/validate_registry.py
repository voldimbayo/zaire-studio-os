"""Validateur d'intégrité référentielle de la Knowledge Base (`knowledge/`).

Vérifie :
1. L'unicité et le format strict des identifiants dans `knowledge/entities-registry.csv`.
2. La correspondance préfixe d'ID <-> catégorie (`CHR-` -> `CHARACTER`, etc.).
3. La validité des statuts (`CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`).
4. L'existence réelle de toutes les dépendances inter-entités et des skills propriétaires/valideurs.
5. La cohérence du journal d'audit `knowledge/status-audit-log.csv` et du glossaire Lingala Unicode.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT
from tools.registry_data import SKILLS_BY_ID

CATEGORY_PREFIX_MAP: dict[str, str] = {
    "CHARACTER": "CHR-",
    "FAMILY": "FAM-",
    "ORGANIZATION": "ORG-",
    "DISTRICT": "DST-",
    "LOCATION": "LOC-",
    "MISSION": "MSN-",
    "ITEM": "ITM-",
    "VEHICLE": "VEH-",
    "SYSTEM": "SYS-",
}

VALID_STATUSES: frozenset[str] = frozenset(
    {"CONFIRMED", "PROPOSED", "RESEARCH_REQUIRED", "BLOCKED", "DEPRECATED"}
)

ID_REGEX = re.compile(r"^(CHR|FAM|ORG|DST|LOC|MSN|ITM|VEH|SYS)-[A-Z0-9-]+$")
DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_source_ids(workspace: Path = WORKSPACE_ROOT) -> set[str]:
    """Charge les identifiants SRC-* depuis research/source-registry.csv."""
    source_csv = workspace / "research" / "source-registry.csv"
    if not source_csv.exists():
        return set()
    source_ids: set[str] = set()
    with source_csv.open(mode="r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in ("source_id", "id", "ID", "Source_ID"):
                if key in row and row[key]:
                    source_ids.add(row[key].strip())
            if not source_ids and row:
                first_val = next(iter(row.values()))
                if first_val and first_val.startswith("SRC-"):
                    source_ids.add(first_val.strip())
    return source_ids


def validate_knowledge_base(workspace: Path = WORKSPACE_ROOT) -> list[str]:
    """Exécute tous les contrôles d'intégrité sur `knowledge/` et retourne la liste des erreurs."""
    errors: list[str] = []
    registry_path = workspace / "knowledge" / "entities-registry.csv"
    audit_path = workspace / "knowledge" / "status-audit-log.csv"
    glossary_path = workspace / "knowledge" / "world-bible" / "lingala-french-glossary.csv"
    budgets_path = workspace / "knowledge" / "technical-specs" / "performance-budgets.csv"

    for required_file in (registry_path, audit_path, glossary_path, budgets_path):
        if not required_file.exists():
            errors.append(f"Fichier requis manquant : {required_file}")
    if errors:
        return errors

    entities: dict[str, dict[str, str]] = {}
    valid_source_ids = load_source_ids(workspace)
    with registry_path.open(mode="r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for line_idx, row in enumerate(reader, start=2):
            entity_id = (row.get("id") or "").strip()
            category = (row.get("category") or "").strip()
            status = (row.get("status") or "").strip()
            owner_skill = (row.get("owner_skill") or "").strip()
            district_id = (row.get("district_id") or "").strip()
            last_updated = (row.get("last_updated") or "").strip()

            if not ID_REGEX.match(entity_id):
                errors.append(f"Ligne {line_idx}: format d'ID invalide ({entity_id!r}).")
            if entity_id in entities:
                errors.append(f"Ligne {line_idx}: ID dupliqué ({entity_id!r}).")
            entities[entity_id] = row

            expected_prefix = CATEGORY_PREFIX_MAP.get(category)
            if not expected_prefix:
                errors.append(f"Ligne {line_idx} ({entity_id}): catégorie invalide ({category!r}).")
            elif not entity_id.startswith(expected_prefix):
                errors.append(
                    f"Ligne {line_idx} ({entity_id}): le préfixe ne correspond pas à {category} ({expected_prefix})."
                )

            if status not in VALID_STATUSES:
                errors.append(f"Ligne {line_idx} ({entity_id}): statut invalide ({status!r}).")

            if owner_skill not in SKILLS_BY_ID:
                errors.append(
                    f"Ligne {line_idx} ({entity_id}): owner_skill inconnu ({owner_skill!r})."
                )

            for validator in filter(None, (row.get("validated_by") or "").split("|")):
                if validator not in SKILLS_BY_ID:
                    errors.append(
                        f"Ligne {line_idx} ({entity_id}): valideur inconnu ({validator!r})."
                    )

            if not DATE_REGEX.match(last_updated):
                errors.append(
                    f"Ligne {line_idx} ({entity_id}): date last_updated invalide ({last_updated!r})."
                )

            if district_id != "GLOBAL" and not district_id.startswith("DST-"):
                errors.append(
                    f"Ligne {line_idx} ({entity_id}): district_id invalide ({district_id!r})."
                )

            sources_raw = [
                s.strip() for s in (row.get("sources") or "").split("|") if s.strip()
            ]
            for src_id in sources_raw:
                if valid_source_ids and src_id not in valid_source_ids:
                    errors.append(
                        f"Ligne {line_idx} ({entity_id}): source inconnue {src_id!r} (absente de research/source-registry.csv)."
                    )

    for entity_id, row in entities.items():
        district_id = (row.get("district_id") or "").strip()
        if district_id != "GLOBAL" and district_id not in entities:
            errors.append(
                f"Entité {entity_id}: district_id {district_id!r} absent du registre."
            )
        deps = [d.strip() for d in (row.get("dependencies") or "").split("|") if d.strip()]
        for dep_id in deps:
            if dep_id not in entities:
                errors.append(
                    f"Entité {entity_id}: dépendance fantôme {dep_id!r} absente du registre."
                )

    with audit_path.open(mode="r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for line_idx, row in enumerate(reader, start=2):
            ent_id = (row.get("entity_id") or "").strip()
            new_st = (row.get("new_status") or "").strip()
            actor = (row.get("actor_skill") or "").strip()
            if ent_id not in entities:
                errors.append(f"Audit log ligne {line_idx}: entité inconnue {ent_id!r}.")
            if new_st not in VALID_STATUSES:
                errors.append(f"Audit log ligne {line_idx}: nouveau statut invalide {new_st!r}.")
            if actor not in SKILLS_BY_ID:
                errors.append(f"Audit log ligne {line_idx}: actor_skill inconnu {actor!r}.")

    with glossary_path.open(mode="r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        unicode_vowels_found = False
        for row in reader:
            term = row.get("lingala_unicode") or ""
            if "ɛ" in term or "ɔ" in term:
                unicode_vowels_found = True
        if not unicode_vowels_found:
            errors.append(
                "Le glossaire Lingala doit contenir les voyelles ouvertes Unicode ('ɛ', 'ɔ')."
            )

    return errors


def main() -> int:
    errors = validate_knowledge_base(WORKSPACE_ROOT)
    if errors:
        print(f"[ERREUR] Validation du registre échouée ({len(errors)} problème(s)) :")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("[OK] Knowledge Base et Registre d'Entités validés sans erreur.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
