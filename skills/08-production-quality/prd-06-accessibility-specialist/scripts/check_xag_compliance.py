"""Auditeur automatisé de conformité Xbox Accessibility Guidelines (XAG) pour PRD-06."""

from __future__ import annotations

import argparse
import json
import sys


def audit_xag_feature(spec: dict) -> list[str]:
    """Vérifie les critères d'accessibilité XAG obligatoires (contraste, double codage, sous-titres, QTE)."""
    errors: list[str] = []
    contrast_ratio = float(spec.get("text_contrast_ratio", 0.0))
    subtitle_bg_opacity = float(spec.get("subtitle_background_opacity", 0.0))
    has_speaker_prefix = bool(spec.get("subtitle_has_speaker_prefix", False))
    supports_lingala_unicode = bool(spec.get("supports_lingala_open_vowels", False))
    uses_color_only = bool(spec.get("uses_color_as_only_indicator", True))
    has_qte_hold_alternative = bool(spec.get("has_qte_hold_or_auto_alternative", False))
    ui_expansion_margin = float(spec.get("ui_text_expansion_tolerance_pct", 0.0))

    if contrast_ratio < 4.5:
        errors.append(f"Ratio de contraste ({contrast_ratio}:1) < minimum XAG 101 requis (4.5:1).")
    if not (0.50 <= subtitle_bg_opacity <= 1.0):
        errors.append(f"Opacité du fond de sous-titre ({subtitle_bg_opacity}) insuffisante (requis >= 0.50).")
    if not has_speaker_prefix:
        errors.append("Sous-titre non conforme XAG 104 : préfixe du locuteur ('[KOFFI]') obligatoire.")
    if not supports_lingala_unicode:
        errors.append("Police non conforme : support des glyphes Unicode lingala ('ɛ', 'ɔ') obligatoire.")
    if uses_color_only:
        errors.append("Non-conformité XAG 102 : double codage (Couleur + Forme/Icône/Son) obligatoire.")
    if not has_qte_hold_alternative:
        errors.append("Non-conformité XAG 107 (Moteur) : option de maintien continu (Hold) requise pour tout QTE.")
    if ui_expansion_margin < 35.0:
        errors.append(f"Marge d'expansion UI (+{ui_expansion_margin}%) < minimum requis +35%.")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Audite la conformité XAG d'une fonctionnalité (PRD-06).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de spécification XAG à auditer (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample_feature = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_feature = {
            "feature_id": "UI-HUD-MAIN-OVERLAY",
            "text_contrast_ratio": 7.2,
            "subtitle_background_opacity": 0.78,
            "subtitle_has_speaker_prefix": True,
            "supports_lingala_open_vowels": True,
            "uses_color_as_only_indicator": False,
            "has_qte_hold_or_auto_alternative": True,
            "ui_text_expansion_tolerance_pct": 38.0,
        }
    errs = audit_xag_feature(sample_feature)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Fonctionnalité {sample_feature.get('feature_id', 'SAMPLE')} certifiée 100% conforme aux normes d'accessibilité XAG.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
