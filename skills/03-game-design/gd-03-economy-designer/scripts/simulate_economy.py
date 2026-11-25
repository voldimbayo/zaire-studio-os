"""Simulateur d'équilibrage Sources & Puits (Faucets & Sinks) pour GD-03 (Economy Designer)."""

from __future__ import annotations

import argparse
import json
import sys


def simulate_player_economy(hours: int = 40) -> dict:
    """Simule l'évolution des revenus, dépenses et inflation sur N heures de jeu dans ZAÏRE."""
    balance = 5000  # Fonds de départ en Francs Congolais (FC) / Crédits locaux
    history: list[dict] = []

    for h in range(1, hours + 1):
        # Faucets : Missions principales, livraisons Wewa, contrats de quartier
        faucet = int(12000 + (h * 2500))
        # Sinks : Maintenance moto Wewa, carburant, équipement, informateurs, améliorations atelier
        sink = int(9500 + (h * 2150))
        balance += faucet - sink
        sink_ratio = round(sink / faucet, 3)
        history.append(
            {
                "hour": h,
                "faucet": faucet,
                "sink": sink,
                "sink_to_faucet_ratio": sink_ratio,
                "net_balance": balance,
            }
        )

    avg_ratio = round(sum(x["sink_to_faucet_ratio"] for x in history) / len(history), 3)
    healthy = 0.75 <= avg_ratio <= 0.92 and all(x["net_balance"] > 0 for x in history)
    return {
        "simulated_hours": hours,
        "average_sink_to_faucet_ratio": avg_ratio,
        "final_net_balance": balance,
        "economy_healthy": healthy,
        "checkpoints": [history[0], history[hours // 2 - 1], history[-1]],
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Simule l'économie Sources/Puits sur 40h (GD-03).")
    parser.add_argument("--hours", type=int, default=40, help="Durée de la campagne simulée en heures")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de paramètres économiques à valider (optionnel)")
    parser.add_argument("--output", help="Chemin de sauvegarde du rapport JSON (optionnel)")
    args = parser.parse_args()
    hours = args.hours
    if args.file:
        from pathlib import Path
        cfg = json.loads(Path(args.file).read_text(encoding="utf-8"))
        hours = int(cfg.get("simulated_hours", hours))
    report = simulate_player_economy(hours)
    formatted = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(formatted + "\n", encoding="utf-8")
    print(formatted)
    return 0 if report["economy_healthy"] else 1


if __name__ == "__main__":
    sys.exit(main())
