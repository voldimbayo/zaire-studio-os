"""Auditeur de budget de performance frametime (P99 <= 16.6 ms / 33.3 ms) et VRAM pour ENG-07."""

from __future__ import annotations

import argparse
import json
import sys


def evaluate_frame_profile(metrics: dict, mode: str = "perf_60fps") -> dict:
    """Compare un relevé de profilage Unreal Insights aux budgets officiels ZAÏRE STUDIO OS."""
    limits = (
        {
            "total_frame_p99_ms": 16.6,
            "cpu_game_thread_ms": 6.5,
            "cpu_npc_ai_ms": 2.5,
            "cpu_mass_crowd_traffic_ms": 2.0,
            "cpu_chaos_physics_ms": 1.5,
            "cpu_animation_ms": 1.8,
            "gpu_lumen_ms": 4.5,
            "gpu_nanite_ms": 2.5,
            "gpu_niagara_vfx_ms": 1.5,
            "vram_used_mb": 6144.0,
        }
        if mode == "perf_60fps"
        else {
            "total_frame_p99_ms": 33.3,
            "cpu_game_thread_ms": 12.0,
            "cpu_npc_ai_ms": 3.0,
            "cpu_mass_crowd_traffic_ms": 2.5,
            "cpu_chaos_physics_ms": 2.0,
            "cpu_animation_ms": 2.5,
            "gpu_lumen_ms": 7.0,
            "gpu_nanite_ms": 4.0,
            "gpu_niagara_vfx_ms": 2.0,
            "vram_used_mb": 8192.0,
        }
    )

    violations: list[str] = []
    for key, max_val in limits.items():
        actual = float(metrics.get(key, 0.0))
        if actual > max_val:
            violations.append(f"{key}: mesuré={actual} > plafond={max_val}")

    return {
        "mode": mode,
        "district_tested": metrics.get("district_id", "DST-MATONGE"),
        "passed": len(violations) == 0,
        "violations": violations,
        "headroom_p99_ms": round(limits["total_frame_p99_ms"] - float(metrics.get("total_frame_p99_ms", 0.0)), 2),
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Audite un profil de performance UE5 (ENG-07).")
    parser.add_argument("--mode", choices=["perf_60fps", "quality_30fps"], default="perf_60fps")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de capture Unreal Insights à auditer (optionnel)")
    args = parser.parse_args()

    if args.file:
        from pathlib import Path
        sample_capture = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_capture = {
            "district_id": "DST-MATONGE",
            "total_frame_p99_ms": 15.85,
            "cpu_game_thread_ms": 5.9,
            "cpu_npc_ai_ms": 2.1,
            "cpu_mass_crowd_traffic_ms": 1.75,
            "cpu_chaos_physics_ms": 1.25,
            "cpu_animation_ms": 1.55,
            "gpu_lumen_ms": 4.25,
            "gpu_nanite_ms": 2.2,
            "gpu_niagara_vfx_ms": 1.15,
            "vram_used_mb": 5620.0,
        }
    report = evaluate_frame_profile(sample_capture, args.mode)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
