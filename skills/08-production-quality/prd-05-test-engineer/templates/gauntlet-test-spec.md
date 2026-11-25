# Spécification de Suite de Tests Automatisés Gauntlet (`PRD-05`)

- **Nom de la Suite / Contrôleur** : `UZaireGauntlet...Controller` | `AFT_Zaire_...`
- **Systèmes Critiques Couverts (`SYS-*`)** : `[Liste]`
- **Taux de Couverture / Faux Positifs** : `[>= 80 % | < 2 %]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Protocole de Synchronisation Événementielle (Zéro `Sleep`)
| Étape du Test | Commande Latente / Delegate Attendu | Assertion Vérifiée | Timeout Sécurité |
| :--- | :--- | :--- | :--- |
| `Step 1` | `OnWorldPartitionStreamingCompleted` | `Cellules chargées == true` | `30 s` |

## 2. Seuils de Régression CI/CD (`ENG-07` / `ENG-08`)
- **Critère d'échec automatique du build** : `[P99 > 16.6 ms / Soft-lock / Assert Fail]`

## Contraintes Studio & Validation Pré-Handoff (`PRD-05`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `PRD-04, ENG-08, DIR-07`
