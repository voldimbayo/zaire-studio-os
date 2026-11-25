# Spécification d'Architecture IA PNJ (`AI-01`)

- **ID Profil IA** : `AI-PRF-[SLUG]`
- **Archétypes Associés (`GD-05`)** : `[ENM-* / CHR-*]`
- **Plafond Acteurs Simultanés** : `[<= 24]`
- **Budget CPU Alloué** : `<= 2.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Hiérarchie UE5 State Tree
| État State Tree | Condition d'Entrée (Tags / Perception) | Tâches & Smart Objects | Bark Associé (`NAR-04`) |
| :--- | :--- | :--- | :--- |
| `ST_Patrol` | `[Condition]` | `[Action]` | `BRK-...` |

## 2. Configuration des Requêtes EQS & Attack Tokens
- **Requête EQS Couverture / Flanquement** : `[Générateur, espacement cm, tests]`
- **Gestion des Attack Tokens (`GD-05`)** : `[Règle d'acquisition et de relâchement]`

## Contraintes Studio & Validation Pré-Handoff (`AI-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-07, GD-05, WLD-05`
