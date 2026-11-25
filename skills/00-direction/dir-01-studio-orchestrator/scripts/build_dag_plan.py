"""Planificateur topologique DAG déterministe pour DIR-01 (Studio Orchestrator).

Généré automatiquement depuis la source unique de vérité `tools/registry_data.py` (`CANONICAL_SKILLS`).
"""

from __future__ import annotations

import argparse
import json
import sys


DEFAULT_DEPENDENCIES: dict[str, list[str]] = {
    "DIR-01": [],
    "DIR-02": ['DIR-01'],
    "DIR-03": ['DIR-01'],
    "DIR-04": ['DIR-01'],
    "DIR-05": ['DIR-01', 'DIR-03'],
    "DIR-06": ['PRD-03', 'NAR-06'],
    "DIR-07": ['PRD-04', 'PRD-05', 'PRD-06', 'ENG-07'],
    "NAR-01": ['DIR-03', 'WLD-01', 'WLD-02'],
    "NAR-02": ['NAR-01', 'NAR-03', 'GD-02'],
    "NAR-03": ['NAR-01', 'WLD-01', 'WLD-02'],
    "NAR-04": ['NAR-02', 'NAR-03', 'GD-02'],
    "NAR-05": ['WLD-01', 'WLD-02', 'NAR-01'],
    "NAR-06": ['NAR-01', 'NAR-02', 'NAR-03', 'NAR-04', 'NAR-05', 'GD-02'],
    "WLD-01": ['DIR-03', 'WLD-02', 'WLD-03'],
    "WLD-02": ['DIR-03'],
    "WLD-03": ['DIR-03', 'DIR-04'],
    "WLD-04": ['WLD-01', 'WLD-03', 'GD-01', 'DIR-04', 'DIR-05'],
    "WLD-05": ['WLD-04', 'GD-02', 'GD-05', 'DIR-05'],
    "WLD-06": ['WLD-05', 'ART-01', 'WLD-02', 'WLD-03'],
    "GD-01": ['DIR-03', 'DIR-05'],
    "GD-02": ['NAR-01', 'WLD-04', 'GD-01'],
    "GD-03": ['GD-01', 'GD-02', 'DIR-02'],
    "GD-04": ['GD-01', 'GD-05', 'NAR-01'],
    "GD-05": ['GD-01', 'DIR-05'],
    "GD-06": ['WLD-03', 'GD-01', 'DIR-05'],
    "GD-07": ['GD-01', 'GD-02', 'ART-01'],
    "AI-01": ['GD-05', 'WLD-05', 'DIR-04'],
    "AI-02": ['WLD-04', 'ART-03', 'DIR-04'],
    "AI-03": ['ENG-04', 'GD-06', 'WLD-03', 'DIR-04'],
    "AI-04": ['WLD-01', 'GD-01', 'NAR-04'],
    "ART-01": ['DIR-03', 'WLD-02', 'WLD-03'],
    "ART-02": ['WLD-06', 'ART-04'],
    "ART-03": ['NAR-03', 'WLD-02', 'ART-01', 'ART-04'],
    "ART-04": ['DIR-04', 'ART-01'],
    "ART-05": ['WLD-05', 'GD-05', 'ART-06'],
    "ART-06": ['NAR-02', 'GD-05'],
    "ART-07": ['ART-01', 'WLD-05', 'ART-02', 'DIR-04'],
    "ART-08": ['ART-02', 'ART-03', 'ART-04', 'DIR-04'],
    "ART-09": ['ART-01', 'GD-05', 'ART-07', 'DIR-04'],
    "AUD-01": ['DIR-03', 'WLD-01', 'WLD-02'],
    "AUD-02": ['AUD-01', 'GD-05', 'GD-06', 'WLD-06'],
    "AUD-03": ['AUD-01', 'WLD-02', 'GD-01', 'GD-05'],
    "AUD-04": ['NAR-04', 'GD-07', 'WLD-02'],
    "ENG-01": ['DIR-04', 'WLD-04', 'ART-04'],
    "ENG-02": ['GD-01', 'GD-02', 'GD-03', 'GD-04', 'GD-05', 'GD-06', 'GD-07', 'ENG-01'],
    "ENG-03": ['ART-04', 'ENG-01'],
    "ENG-04": ['WLD-03', 'ART-02', 'GD-06'],
    "ENG-05": ['GD-06', 'ART-02', 'DIR-04'],
    "ENG-06": ['DIR-04', 'ART-07', 'ART-08'],
    "ENG-07": ['ENG-01', 'ENG-02', 'ENG-03', 'ENG-04', 'ENG-05', 'ENG-06', 'ART-07', 'ART-09', 'AI-01', 'AI-02', 'AI-03'],
    "ENG-08": ['ENG-01', 'ENG-02', 'ENG-03', 'ENG-07'],
    "PRD-01": ['DIR-01', 'DIR-02'],
    "PRD-02": ['DIR-02', 'DIR-04', 'WLD-02'],
    "PRD-03": ['NAR-05', 'WLD-01', 'GD-01', 'ENG-01'],
    "PRD-04": ['GD-02', 'WLD-04', 'ENG-02'],
    "PRD-05": ['PRD-04', 'ENG-07', 'ENG-08'],
    "PRD-06": ['GD-07', 'GD-05', 'AUD-04'],
}

DEFAULT_STRATA: dict[str, int] = {
    "DIR-01": 0,
    "DIR-02": 0,
    "DIR-03": 0,
    "DIR-04": 0,
    "DIR-05": 0,
    "DIR-06": 5,
    "DIR-07": 5,
    "NAR-01": 1,
    "NAR-02": 2,
    "NAR-03": 2,
    "NAR-04": 2,
    "NAR-05": 2,
    "NAR-06": 5,
    "WLD-01": 1,
    "WLD-02": 1,
    "WLD-03": 1,
    "WLD-04": 1,
    "WLD-05": 2,
    "WLD-06": 2,
    "GD-01": 1,
    "GD-02": 2,
    "GD-03": 2,
    "GD-04": 2,
    "GD-05": 2,
    "GD-06": 2,
    "GD-07": 2,
    "AI-01": 3,
    "AI-02": 3,
    "AI-03": 3,
    "AI-04": 3,
    "ART-01": 1,
    "ART-02": 3,
    "ART-03": 3,
    "ART-04": 1,
    "ART-05": 3,
    "ART-06": 3,
    "ART-07": 3,
    "ART-08": 3,
    "ART-09": 3,
    "AUD-01": 1,
    "AUD-02": 3,
    "AUD-03": 3,
    "AUD-04": 3,
    "ENG-01": 1,
    "ENG-02": 4,
    "ENG-03": 4,
    "ENG-04": 3,
    "ENG-05": 4,
    "ENG-06": 4,
    "ENG-07": 4,
    "ENG-08": 4,
    "PRD-01": 1,
    "PRD-02": 1,
    "PRD-03": 5,
    "PRD-04": 5,
    "PRD-05": 5,
    "PRD-06": 5,
}


def compute_waves(selected_skills: list[str], dep_map: dict[str, list[str]] | None = None) -> list[list[str]]:
    """Regroupe les skills sélectionnés en vagues d'exécution parallèles selon leurs dépendances et strates."""
    if not selected_skills:
        raise ValueError("La liste des skills sélectionnés ne peut pas être vide.")
    graph = dep_map or DEFAULT_DEPENDENCIES
    unknown = sorted(s for s in selected_skills if s not in graph)
    if unknown:
        raise ValueError(f"Skill(s) inconnu(s) du catalogue ZAÏRE STUDIO OS : {', '.join(unknown)}")
    active_set = set(selected_skills)
    remaining = set(active_set)
    completed: set[str] = set()
    waves: list[list[str]] = []

    while remaining:
        deps_satisfied = [
            skill
            for skill in remaining
            if all((dep not in active_set) or (dep in completed) for dep in graph[skill])
        ]
        if not deps_satisfied:
            raise ValueError(f"Cycle de dépendances détecté parmi : {sorted(remaining)}")
        min_stratum = min(DEFAULT_STRATA.get(s, 0) for s in deps_satisfied)
        ready = sorted(s for s in deps_satisfied if DEFAULT_STRATA.get(s, 0) == min_stratum)
        waves.append(ready)
        completed.update(ready)
        remaining -= set(ready)

    return waves


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Génère un plan d'exécution DAG en JSON.")
    parser.add_argument(
        "--skills",
        required=True,
        help="Liste d'IDs de skills séparés par des virgules (ex: WLD-02,WLD-03,GD-02,NAR-02,NAR-06)",
    )
    parser.add_argument(
        "--output",
        help="Chemin du fichier JSON de sortie (optionnel)",
    )
    args = parser.parse_args()
    skills = [s.strip().upper() for s in args.skills.split(",") if s.strip()]
    try:
        waves = compute_waves(skills)
    except ValueError as exc:
        print(f"[ERREUR] {exc}", file=sys.stderr)
        return 1
    payload = {
        "orchestrator": "DIR-01",
        "requested_skills_count": len(skills),
        "waves": [{"wave_index": idx + 1, "parallel_skills": w} for idx, w in enumerate(waves)],
    }
    formatted = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(formatted + "\n", encoding="utf-8")
    print(formatted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
