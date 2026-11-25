"""Validateur Unicode Lingala (ɛ, ɔ) et budget d'expansion UI (+35 %) pour AUD-04."""

from __future__ import annotations

import argparse
import json
import sys


def validate_localization_entries(entries: list[dict]) -> list[str]:
    """Vérifie la présence des glyphes Unicode lingala, du préfixe locuteur XAG et l'expansion <= +35%."""
    errors: list[str] = []
    for item in entries:
        key = item.get("loc_key", "UNKNOWN")
        src_text = str(item.get("source_fr_cd", ""))
        target_text = str(item.get("target_text", ""))
        max_container_chars = int(item.get("ui_container_max_chars", 0))
        requires_open_vowels = bool(item.get("requires_lingala_open_vowels", False))
        is_subtitle = bool(item.get("is_subtitle", False))

        if not key or key == "TXT_MISSING":
            errors.append(f"Clé de localisation manquante ou invalide ({key!r}).")
        if requires_open_vowels and not ("ɛ" in src_text or "ɔ" in src_text or "ɛ" in target_text or "ɔ" in target_text):
            errors.append(f"Clé {key}: glyphes Unicode lingala ('ɛ' ou 'ɔ') manquants.")
        if is_subtitle and not (src_text.startswith("[") and "]" in src_text):
            errors.append(f"Clé {key}: sous-titre dépourvu du préfixe locuteur XAG (ex: '[KOFFI]').")
        required_budget = int(len(src_text) * 1.35)
        if max_container_chars < required_budget or len(target_text) > max_container_chars:
            errors.append(
                f"Clé {key}: risque de troncature UI (container={max_container_chars}, requis +35%={required_budget})."
            )

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide un lot de chaînes localisées (AUD-04).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de chaînes localisées à valider (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample_batch = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_batch = [
            {
                "loc_key": "SUB_MSN001_AMINA_02",
                "source_fr_cd": "[AMINA] : Kɛbá Koffi, les hommes de Mukendi contrôlent la grue ! Tɔ́kɛndɛ́ !",
                "target_text": "[AMINA] : Watch out Koffi, Mukendi's men already control the main crane! Let's go!",
                "ui_container_max_chars": 115,
                "requires_lingala_open_vowels": True,
                "is_subtitle": True,
            }
        ]
    errs = validate_localization_entries(sample_batch)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Lot de localisation AUD-04 validé (Unicode 'ɛ'/'ɔ', préfixe locuteur XAG et budget +35% OK).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
