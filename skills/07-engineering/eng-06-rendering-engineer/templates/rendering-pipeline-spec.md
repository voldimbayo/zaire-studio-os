# Spécification Pipeline de Rendu & Scalabilité (`ENG-06`)

- **Passe Graphique / Feature** : `[Lumen / Nanite / VSM / Water / TSR]`
- **Budget GPU Mode Perf (60 FPS)** : `[<= X.X ms]`
- **Budget GPU Mode Qualité (30 FPS)** : `[<= Y.Y ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Configuration des Passes RHI & CVar (`DefaultEngine.ini` / `Scalability.ini`)
| CVar / Paramètre | Valeur Perf (60 FPS) | Valeur Qualité (30 FPS) | Justification Technique |
| :--- | :--- | :--- | :--- |
| `r.Lumen...` | `[Val]` | `[Val]` | `[Impact RenderDoc]` |

## 2. Contrôles de Stabilité Temporelle & Cache VSM
- **Taux de Cache VSM Cible** : `[>= 92 %]`
- **Gestion Anti-Ghosting TSR** : `[Paramètre]`

## Contraintes Studio & Validation Pré-Handoff (`ENG-06`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-04, ENG-07, ART-07`
