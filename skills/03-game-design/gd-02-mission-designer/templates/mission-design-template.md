# Mission Design Document (`GD-02`)

- **ID Mission** : `MSN-[MAIN/SIDE]-[NUM]-[SLUG]`
- **Titre** : `[Titre de la Mission]`
- **Lieu & Commune** : `LOC-...` (`DST-...`)
- **Plafond PNJ `AI-01` Actifs** : `[<= 24]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Approches Tactiques Multiples
- **Approche A (Infiltration / Social `SYS-STEALTH`)** : `[Mécanique]`
- **Approche B (Mêlée / Action `SYS-CMB-MELEE`)** : `[Mécanique]`
- **Approche C (Mobilité / Exfiltration `VEH-*`)** : `[Mécanique]`

## 2. Machine à États & Protection Anti-Soft-Lock
| Étape ID | Objectif Joueur | Condition Transition Succès | Handler Anti-Soft-Lock (Véhicule détruit / Fuite / Alerte) |
| :--- | :--- | :--- | :--- |
| `ST-01` | `[Objectif]` | `[Condition]` | `[Action de récupération sans blocage]` |

## Contraintes Studio & Validation Pré-Handoff (`GD-02`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `NAR-06, AI-01, PRD-04, DIR-05`
