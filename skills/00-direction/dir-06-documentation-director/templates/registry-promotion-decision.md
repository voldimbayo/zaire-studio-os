# Décision de Gouvernance Documentaire (`DIR-06`)

- **Date d'Audit** : `YYYY-MM-DD`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)` | `FAIL`

## 1. Transitions de Statuts Décidées
| ID Entité | Ancien Statut | Nouveau Statut | Valideurs | Justification & Sources (`SRC-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `LOC-...` | `PROPOSED` | `CONFIRMED` | `DIR-03, DIR-06, DIR-07` | `[Justification]` |

## 2. Anomalies Référentielles Rejetées
- `[Aucune / Liste des IDs fantômes ou mal formés]`

## Contraintes Studio & Validation Pré-Handoff (`DIR-06`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-01, DIR-07`
