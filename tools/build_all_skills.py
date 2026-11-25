"""Point d'entrée unique pour régénérer, auditer et packager les 57 Agent Skills de ZAÏRE STUDIO OS."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT
from tools.check_dag_cycles import check_all_dags
from tools.departments.dept_00_direction import build_department_00
from tools.departments.dept_01_narrative import build_department_01
from tools.departments.dept_02_world_design import build_department_02
from tools.departments.dept_03_game_design import build_department_03
from tools.departments.dept_04_ai_simulation import build_department_04
from tools.departments.dept_05_art_animation import build_department_05
from tools.departments.dept_06_audio_localization import build_department_06
from tools.departments.dept_07_engineering import build_department_07
from tools.departments.dept_08_production_quality import build_department_08
from tools.lint_skills import lint_skills_in_workspace
from tools.package_skills import package_all_releases, update_skills_index
from tools.validate_registry import validate_knowledge_base


def build_all_departments(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 57 skills à travers les 9 départements."""
    builders = (
        build_department_00,
        build_department_01,
        build_department_02,
        build_department_03,
        build_department_04,
        build_department_05,
        build_department_06,
        build_department_07,
        build_department_08,
    )
    created: list[Path] = []
    for builder in builders:
        created.extend(builder(workspace))
    return created


def main() -> int:
    created = build_all_departments(WORKSPACE_ROOT)
    print(f"[OK] {len(created)} skills générés.")

    reg_errors = validate_knowledge_base(WORKSPACE_ROOT)
    dag_errors = check_all_dags(WORKSPACE_ROOT)
    count, lint_errors = lint_skills_in_workspace(WORKSPACE_ROOT, require_all_57=True)

    all_errors = reg_errors + dag_errors + lint_errors
    if all_errors:
        for err in all_errors:
            print(f"[ERREUR] {err}")
        return 1

    update_skills_index(WORKSPACE_ROOT)
    ind_zips, dept_zips, full_zip = package_all_releases(WORKSPACE_ROOT)
    print(
        f"[OK] Système complet validé ({count}/57 skills, {len(ind_zips)} ZIP Claude.ai, "
        f"{len(dept_zips)} ZIP Départements, archive {full_zip.name})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
