# Rapport d'Audit de Performance & Budgets UE5 (`ENG-07`)

- **Parcours / Commune Testée** : `DST-...` (`LOC-...`)
- **Mode Cible** : `Mode Performance (60 FPS / <= 16.6 ms)`
- **Résultat `check_perf_budget.py`** : `PASS` | `FAIL (BLOCKED)`
- **Marge P99 (Headroom)** : `[+X.XX ms]`

## 1. Relevé détaillé par Sous-Système (Unreal Insights / RenderDoc)
| ID Budget | Plafond (ms/MB) | Mesuré P95 | Mesuré P99 | Statut (`OK` / `OVER_BUDGET`) |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | `16.6 ms` | `[XX.X ms]` | `[XX.X ms]` | `OK` |

## 2. Statut PSO Precaching & Streaming
- **Hitches PSO (> 5 ms)** : `[0 détecté]`
- **Actions d'Optimisation Requises** : `[Aucune / Tickets assignés]`

## Contraintes Studio & Validation Pré-Handoff (`ENG-07`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-04, DIR-07, PRD-05`
