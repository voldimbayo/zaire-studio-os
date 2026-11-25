"""Calculateur de budget CPU ECS Mass Crowd & Hydratation pour AI-02."""

from __future__ import annotations

import argparse
import json
import sys


def evaluate_crowd_budget(
    hydrated_actors: int = 18,
    mass_lod1_count: int = 180,
    mass_lod2_count: int = 420,
    mode: str = "perf_60fps",
) -> dict:
    """Calcule le coût CPU estimé (en ms) de la simulation de foule par commune."""
    # Coûts unitaires moyens mesurés sous UE5 Mass Entity / ZoneGraph
    npc_ai_ms = round(hydrated_actors * 0.095, 3)  # Budget AI-01 max 2.5 ms (24 acteurs max)
    mass_cpu_ms = round((mass_lod1_count * 0.0045) + (mass_lod2_count * 0.0018), 3)

    max_npc_budget = 2.5 if mode == "perf_60fps" else 3.0
    max_mass_budget = 2.0 if mode == "perf_60fps" else 2.5

    within_budget = (
        hydrated_actors <= 24
        and npc_ai_ms <= max_npc_budget
        and mass_cpu_ms <= max_mass_budget
    )
    return {
        "mode": mode,
        "hydrated_actors_ai01": hydrated_actors,
        "mass_entities_total": mass_lod1_count + mass_lod2_count,
        "estimated_ai01_cpu_ms": npc_ai_ms,
        "estimated_mass_cpu_ms": mass_cpu_ms,
        "max_mass_budget_ms": max_mass_budget,
        "within_budget": within_budget,
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Vérifie le budget CPU Mass Crowd (AI-02).")
    parser.add_argument("--hydrated", type=int, default=18, help="Nombre d'acteurs hydratés ACharacter (max 24)")
    parser.add_argument("--lod1", type=int, default=180, help="Entités Mass LOD1 (25m - 80m)")
    parser.add_argument("--lod2", type=int, default=420, help="Entités Mass LOD2 (80m - 250m)")
    parser.add_argument("--file", help="Fichier JSON de configuration Mass Crowd à valider (optionnel)")
    parser.add_argument("--output", help="Chemin de sauvegarde du rapport JSON (optionnel)")
    args = parser.parse_args()

    hydrated, lod1, lod2 = args.hydrated, args.lod1, args.lod2
    mode = "perf_60fps"
    if args.file:
        from pathlib import Path
        cfg = json.loads(Path(args.file).read_text(encoding="utf-8"))
        hydrated = int(cfg.get("hydrated_actors_ai01", hydrated))
        lod1 = int(cfg.get("mass_lod1_count", lod1))
        lod2 = int(cfg.get("mass_lod2_count", lod2))
        mode = str(cfg.get("mode", mode))

    result = evaluate_crowd_budget(hydrated, lod1, lod2, mode)
    formatted = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(formatted + "\n", encoding="utf-8")
    print(formatted)
    return 0 if result["within_budget"] else 1


if __name__ == "__main__":
    sys.exit(main())
