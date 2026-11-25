"""Validateur structurel de graphes de dialogue interactifs JSON pour NAR-04."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID_EMOTION_TAGS = frozenset({"NEUTRAL", "TENSE", "ANGRY", "WARM", "URGENT", "IRONIC"})
VALID_CAMERA_FRAMINGS = frozenset({"OTS_LEFT", "OTS_RIGHT", "CLOSE_UP", "TWO_SHOT", "WIDE_ESTABLISHING"})


def validate_dialogue_graph(payload: dict) -> list[str]:
    """Vérifie l'absence d'impasse (dead-end), la limite de 20 mots par bulle et les tags caméra/émotion."""
    errors: list[str] = []
    nodes = payload.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        return ["Le graphe de dialogue doit contenir une liste 'nodes' non vide."]

    node_ids = {n.get("node_id") for n in nodes if isinstance(n, dict) and n.get("node_id")}
    for idx, node in enumerate(nodes, start=1):
        nid = node.get("node_id", f"INDEX_{idx}")
        speaker = node.get("speaker_id", "")
        text = str(node.get("line_text", "")).strip()
        emotion = node.get("emotion_tag", "")
        camera = node.get("camera_framing", "")
        next_nodes = node.get("next_nodes", [])
        is_terminal = bool(node.get("is_terminal", False))

        if not speaker.startswith("CHR-"):
            errors.append(f"Noeud {nid}: speaker_id ({speaker!r}) doit commencer par 'CHR-'.")
        word_count = len(text.split())
        if word_count == 0 or word_count > 20:
            errors.append(f"Noeud {nid}: réplique hors calibre UI ({word_count} mots, max=20).")
        if emotion not in VALID_EMOTION_TAGS:
            errors.append(f"Noeud {nid}: emotion_tag invalide ({emotion!r}).")
        if camera not in VALID_CAMERA_FRAMINGS:
            errors.append(f"Noeud {nid}: camera_framing invalide ({camera!r}).")
        if not is_terminal and not next_nodes:
            errors.append(f"Noeud {nid}: impasse narrative détectée (non terminal sans next_nodes).")
        for target in next_nodes:
            if target not in node_ids:
                errors.append(f"Noeud {nid}: transition vers un node_id inexistant ({target!r}).")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide un graphe de dialogue JSON (NAR-04).")
    parser.add_argument("--file", help="Chemin du fichier JSON à valider (optionnel, mode auto-test sinon)")
    args = parser.parse_args()

    if args.file:
        data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        data = {
            "dialogue_id": "DLG-MSN-001-PORT",
            "nodes": [
                {
                    "node_id": "N01",
                    "speaker_id": "CHR-PROTAG-KOFFI",
                    "line_text": "Mbote vieux! J'ai le laissez-passer ONATRA pour le quai numéro quatre.",
                    "emotion_tag": "WARM",
                    "camera_framing": "OTS_LEFT",
                    "is_terminal": False,
                    "next_nodes": ["N02"],
                },
                {
                    "node_id": "N02",
                    "speaker_id": "CHR-ALLY-AMINA",
                    "line_text": "Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue principale. Tɔ́kɛndɛ́!",
                    "emotion_tag": "URGENT",
                    "camera_framing": "CLOSE_UP",
                    "is_terminal": True,
                    "next_nodes": [],
                },
            ],
        }

    errs = validate_dialogue_graph(data)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Graphe de dialogue {data.get('dialogue_id', 'SAMPLE')} validé ({len(data['nodes'])} noeuds, 0 impasse).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
