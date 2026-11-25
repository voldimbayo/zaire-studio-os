# Exemple `ENG-07` — Audit de Performance de `DST-MATONGE` (Heure de Pointe + Pluie)

- **Parcours / Commune Testée** : Traversée `LOC-GOMBE-PORT` -> `LOC-MATONGE-VICTOIRE` en `VEH-MOTO-WEWA-01` sous `World.Weather.TropicalStorm`
- **Mode Cible** : `Mode Performance (60 FPS / <= 16.6 ms)`
- **Résultat `check_perf_budget.py`** : `PASS (0 violation)`
- **Marge P99 (Headroom)** : `+0.75 ms` (`15.85 ms` mesuré pour `16.60 ms` max)

## 1. Relevé détaillé par Sous-Système (Unreal Insights / RenderDoc)
| ID Budget | Plafond | Mesuré P95 | Mesuré P99 | Statut |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | `16.60 ms` | `14.40 ms` | `15.85 ms` | **OK** |
| `PERF-CPU-GAME` | `6.50 ms` | `5.30 ms` | `5.90 ms` | **OK** |
| `PERF-CPU-NPCAI` (`18 acteurs`) | `2.50 ms` | `1.85 ms` | `2.10 ms` | **OK** |
| `PERF-CPU-MASS` (`600 piétons + 75 véh.`) | `2.00 ms` | `1.55 ms` | `1.75 ms` | **OK** |
| `PERF-CPU-CHAOS` | `1.50 ms` | `1.05 ms` | `1.25 ms` | **OK** |
| `PERF-GPU-LUMEN` | `4.50 ms` | `3.95 ms` | `4.25 ms` | **OK** |
| `PERF-GPU-NANITE` | `2.50 ms` | `1.95 ms` | `2.20 ms` | **OK** |
| `PERF-GPU-NIAGARA` | `1.50 ms` | `0.95 ms` | `1.15 ms` | **OK** |
| `PERF-MEM-VRAM` | `6144 MB` | `5480 MB` | `5620 MB` | **OK** |

## 2. Statut PSO Precaching & Streaming
- **Hitches PSO (> 5 ms)** : `0` (100 % des PSO des 8 Master Materials `ART-08` pré-cachés au chargement asynchrone).
