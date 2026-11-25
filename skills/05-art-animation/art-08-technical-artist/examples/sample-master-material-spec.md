# Exemple `ART-08` — Spécification de `M_Zaire_Env_Standard`

- **Nom Master Material** : `M_Zaire_Env_Standard`
- **Domaine** : Architecture & Props Modulaires Nanite (`ART-02`, `ENG-04`)
- **Shading Model / Blend Mode** : `Default Lit | Opaque`
- **Statut** : `CONFIRMED`

## 1. Budget Instructions & Permutations PSO
- **Instructions Pixel Shader / Vertex Shader** : `128 PS / 42 VS` (Plafond `<= 140 PS` respecté).
- **Texture Samplers Utilisés** : `4 Samplers` (`BaseColor`, `Normal`, `ORM`, `RVT_TerrainSample` en `Shared:Wrap`).
- **Static Switches Autorisés (`2 switches = 4 PSO max`)** : `bUseRVTBaseBlend`, `bUseWorldAlignedMacroDirt`.

## 2. Mapping Custom Primitive Data (Zéro PSO Supplémentaire)
| Index Float | Nom Paramètre | Plage Valeurs | Effet Visuel Dynamique |
| :--- | :--- | :--- | :--- |
| `Data[0..2]` | `InstanceColorTint` | `RGB [0.2 - 1.0]` | Permet de colorer 500 conteneurs ou façades de `DST-MATONGE` en 1 seul draw call instancié. |
| `Data[3]` | `DynamicWetnessAndMud` | `[0.0 - 1.0]` | Piloté par `World.Weather.TropicalStorm` : fonce l'albédo poreux et abaisse la Roughness à `0.22`. |
