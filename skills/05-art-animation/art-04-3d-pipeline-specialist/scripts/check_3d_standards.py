"""Validateur de normes géométriques 3D, Texel Density et Nanite pour ART-04."""

from __future__ import annotations

import argparse
import json
import sys


def validate_3d_asset_spec(spec: dict) -> list[str]:
    """Vérifie la conformité d'un asset 3D aux standards ART-04 (Texel Density, WPO, Pivot)."""
    errors: list[str] = []
    tier = spec.get("tier", "EYE_LEVEL")
    td = float(spec.get("texel_density_px_per_cm", 0.0))
    uses_nanite = bool(spec.get("nanite_enabled", False))
    uses_transparency = bool(spec.get("has_translucent_material", False))
    wpo_cull_dist_cm = float(spec.get("wpo_disable_distance_cm", 0.0))
    pivot_snapped = bool(spec.get("pivot_on_grid", False))

    if tier == "EYE_LEVEL" and abs(td - 10.24) > 0.5:
        errors.append(f"Texel density ({td} px/cm) non conforme au standard hauteur d'oeil (10.24 px/cm).")
    if uses_nanite and uses_transparency:
        errors.append("Nanite est interdit sur les matériaux Translucides (utiliser Opaque ou Masked avec WPO cull).")
    if wpo_cull_dist_cm > 3500.0:
        errors.append(f"Distance de désactivation WPO ({wpo_cull_dist_cm} cm) > maximum autorisé 3500 cm (35m).")
    if not pivot_snapped:
        errors.append("Le pivot de l'asset doit être aligné sur la grille modulaire (10/50/100/400 cm).")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide la spécification technique d'un asset 3D (ART-04).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON d'asset 3D à valider (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample = {
            "asset_id": "SM_Kit_Port_Wall_400a",
            "tier": "EYE_LEVEL",
            "texel_density_px_per_cm": 10.24,
            "nanite_enabled": True,
            "has_translucent_material": False,
            "wpo_disable_distance_cm": 0.0,
            "pivot_on_grid": True,
        }
    errs = validate_3d_asset_spec(sample)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Asset {sample.get('asset_id', 'SAMPLE')} conforme aux standards 3D Nanite & Texel Density (10.24 px/cm).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
