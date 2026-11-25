"""Validateur de métriques spatiales de blockout Level Design pour WLD-05."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_blockout_metrics(spec: dict) -> list[str]:
    """Vérifie la conformité d'un blockout aux gabarits UE5 de spatial-metrics.md."""
    errors: list[str] = []
    min_corridor = float(spec.get("min_corridor_width_cm", 0))
    ceiling = float(spec.get("min_ceiling_height_cm", 0))
    low_cover = float(spec.get("low_cover_height_cm", 0))
    high_cover = float(spec.get("high_cover_height_cm", 0))
    wewa_gap = float(spec.get("min_wewa_lane_gap_cm", 0))

    if min_corridor < 350.0:
        errors.append(f"Largeur couloir ({min_corridor} cm) < minimum requis 350 cm (risque collision caméra).")
    if ceiling < 320.0:
        errors.append(f"Hauteur sous plafond ({ceiling} cm) < minimum requis 320 cm.")
    if not (90.0 <= low_cover <= 110.0):
        errors.append(f"Hauteur couvert bas ({low_cover} cm) hors plage [90, 110] cm (cible 100 cm).")
    if high_cover < 200.0:
        errors.append(f"Hauteur couvert haut ({high_cover} cm) < minimum requis 200 cm.")
    if wewa_gap < 130.0:
        errors.append(f"Passage inter-file moto Wewa ({wewa_gap} cm) < minimum requis 130 cm.")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide les métriques spatiales d'un blockout WLD-05.")
    parser.add_argument("--file", help="Fichier JSON de métriques blockout (optionnel)")
    args = parser.parse_args()

    if args.file:
        payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        payload = {
            "blockout_id": "BLK-GOMBE-PORT-01",
            "location_id": "LOC-GOMBE-PORT",
            "min_corridor_width_cm": 400.0,
            "min_ceiling_height_cm": 360.0,
            "low_cover_height_cm": 100.0,
            "high_cover_height_cm": 220.0,
            "min_wewa_lane_gap_cm": 150.0,
        }

    errs = validate_blockout_metrics(payload)
    if errs:
        for err in errs:
            print(f"[ERREUR] {err}")
        return 1
    print(f"[OK] Blockout {payload.get('blockout_id')} conforme à 100% aux métriques spatiales UE5.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
