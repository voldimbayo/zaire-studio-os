# Exemple `ENG-04` — Génération Procédurale des Îlots et Routes de `DST-MATONGE`

- **Nom de l'Outil HDA / Graphe PCG** : `HDA_Zaire_UrbanBlock_Gen` & `PCG_Matonge_StreetDressing`
- **Commune / Typologie Cible (`WLD-03`)** : `DST-MATONGE` (`TYP-MATONGE-COMM`)
- **Global Seed Déterministe** : `19600630`
- **Statut** : `CONFIRMED`

## 1. Attributs du Nuage de Points (Houdini -> UE5 PCG)
| Nom Attribut | Type | Source (`WLD-03` / OSM) | Utilisation dans UE5 PCG / ZoneGraph |
| :--- | :--- | :--- | :--- |
| `@road_lane_width` | `float` | `350.0` ou `380.0 cm` | Génère les voies véhicules `ZoneGraph` et insère une sous-voie Wewa (`150 cm`) entre deux files. |
| `@building_floors` | `int` | `1 à 3` (`TYP-MATONGE-COMM`) | Empile un RDC commercial (`400 cm` avec auvent `180 cm`) + `0 à 2` étages (`350 cm`). |
| `@cpd_tint_rgb` | `vector3` | Palette `ART-01` Matonge | Écrit directement dans `CustomPrimitiveData[0..2]` de `M_Zaire_Env_Standard` (0 PSO ajouté). |

## 2. Règles d'Exclusion Gameplay (`WLD-05`) & Optimisation Instances
- **Exclusion** : Toute arène de mission ou trottoir principal applique un filtre `Difference` dans le graphe PCG garantissant un couloir piéton libre de `>= 350 cm` exempt de poteaux ou d'étals.
- **Performance** : Un îlot complet de `80 m × 45 m` est compilé en seulement `14 composants ISM Nanite` par cellule de `128 m`.
