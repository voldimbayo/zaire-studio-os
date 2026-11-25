# Architecture d'Acte Narratif (`NAR-01`)

- **Acte** : `ACTE-[I / II / III]`
- **Titre** : `[Titre dramatique]`
- **Communes Principales** : `[DST-*]`
- **Personnages Pivots** : `[CHR-*]`

## 1. Progression Dramatique & Alignement Gameplay
| Séquence | Objectif Dramatique | Mission Associée (`MSN-*`) | Système Gameplay Sollicité (`SYS-*`) |
| :--- | :--- | :--- | :--- |
| 1 | `[Introduction / Incident]` | `MSN-MAIN-...` | `SYS-...` |

## 2. Embranchements & Conséquences Monde Ouvert
| Point de Choix | Option A (Impact Monde) | Option B (Impact Monde) | Variable d'État Persistante |
| :--- | :--- | :--- | :--- |
| `[Pivot]` | `[Conséquence A]` | `[Conséquence B]` | `WorldState.Act...` |

## Contraintes Studio & Validation Pré-Handoff (`NAR-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `NAR-06, DIR-03`
