# Spécification Pipeline Procédural Houdini HDA & UE5 PCG (`ENG-04`)

- **Nom de l'Outil HDA / Graphe PCG** : `HDA_Zaire_...` | `PCG_Zaire_...`
- **Commune / Typologie Cible (`WLD-03`)** : `DST-...` (`TYP-...`)
- **Global Seed Déterministe** : `19600630`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Attributs du Nuage de Points (Houdini -> UE5 PCG)
| Nom Attribut | Type | Source (`WLD-03` / OSM) | Utilisation dans UE5 PCG / ZoneGraph |
| :--- | :--- | :--- | :--- |
| `@kit_piece_id` | `string` | Règle façade | Sélectionne le `SM_Kit_*` dans la DataTable `ART-02`. |

## 2. Règles d'Exclusion Gameplay (`WLD-05`) & Optimisation Instances
- **Tags de Volumes d'Exclusion** : `PCG_Exclude_ManualArena`, `PCG_Exclude_NavPath_350cm`
- **Regroupement d'Instances** : `ISM packé par cellule World Partition de 12800 cm`

## Contraintes Studio & Validation Pré-Handoff (`ENG-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `WLD-04, ENG-07, AI-03`
