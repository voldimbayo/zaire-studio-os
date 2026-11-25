# Spécification Architecture d'Animation UE5 (`ART-05`)

- **Cible Squelette** : `SK_Zaire_Master_Humanoid` (`CHR-...` / `AI-01`)
- **Budget CPU Max (`PERF-CPU-ANIM`)** : `<= 1.8 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Configuration Motion Matching & Motion Warping
- **Pose Search Channels** : `[Trajectory, Pose, Velocity]`
- **Cibles Motion Warping (`WLD-05`)** : `[Tags & fenêtres cm]`

## 2. Synchronisation Frame Data Combat (`GD-05`)
| Montage Asset | Gameplay Tag | Startup (`f`) | Active Hitbox (`ANS_`) | Recovery / Cancel (`f`) |
| :--- | :--- | :--- | :--- | :--- |
| `AM_...` | `Ability.Melee...` | `f01 - fXX` | `fXX - fYY` | `fYY - fZZ` |

## Contraintes Studio & Validation Pré-Handoff (`ART-05`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `GD-05, WLD-05, ENG-07`
