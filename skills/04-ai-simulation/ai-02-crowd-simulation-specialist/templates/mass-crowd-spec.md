# Spécification Simulation de Foule Mass Entity (`AI-02`)

- **Système** : `SYS-CROWD-MASS`
- **Commune Cible** : `DST-...`
- **Budget CPU Max (`PERF-CPU-MASS`)** : `<= 2.0 ms` (60 FPS)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Distribution par Anneau LOD & Validation Budget
- **Acteurs Hydratés (LOD 0, `< 25 m`)** : `[<= 18]`
- **Entités Mass LOD 1 (`25 - 80 m`)** : `[XXX]`
- **Entités Mass LOD 2 VAT (`80 - 250 m`)** : `[XXX]`
- **Coût CPU Estimé (`check_mass_budget.py`)** : `[X.XX ms]`

## 2. Courbes de Densité Horaire & Réactivité Météo
| Créneau Horaire / Événement | Densité Active (%) | Profils PNJ Dominants (`ART-03`) | Comportement ZoneGraph |
| :--- | :--- | :--- | :--- |
| `Journée (08h-18h)` | `100 %` | `[Profils]` | `[Comportement]` |

## Contraintes Studio & Validation Pré-Handoff (`AI-02`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-07, PRD-05, DIR-04`
