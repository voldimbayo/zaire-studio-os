# Spécification Master Material & Contrôle PSO (`ART-08`)

- **Nom Master Material** : `M_Zaire_...`
- **Domaine** : `[Environment / Character / Vehicle / Water]`
- **Shading Model / Blend Mode** : `[Default Lit / Subsurface Profile | Opaque / Masked]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Budget Instructions & Permutations PSO
- **Instructions Pixel Shader / Vertex Shader** : `[XXX / XXX]`
- **Texture Samplers Utilisés** : `[<= 6 via Shared:Wrap]`
- **Static Switches Autorisés (`<= 3`)** : `[Liste -> Total permutations = 2^N]`

## 2. Mapping Custom Primitive Data (Zéro PSO Supplémentaire)
| Index Float | Nom Paramètre | Plage Valeurs | Effet Visuel Dynamique |
| :--- | :--- | :--- | :--- |
| `Data[0]` | `TintHueShift` | `[0.0 - 1.0]` | `[Variation sans nouvelle instance]` |

## Contraintes Studio & Validation Pré-Handoff (`ART-08`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-06, ENG-07, DIR-04`
