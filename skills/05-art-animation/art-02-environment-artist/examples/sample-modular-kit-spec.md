# Exemple `ART-02` — Kit Modulaire `KIT-GOMBE-PORT` & Matériaux Tropicaux

- **ID Kit** : `KIT-GOMBE-PORT`
- **Brief Source (`WLD-06`)** : `ENV-GOMBE-PORT-01`
- **Texel Density** : `10.24 px/cm` (0-3m) / `5.12 px/cm` (Charpentes hautes)
- **Statut** : `CONFIRMED`

## 1. Inventaire des Modules Géométriques Nanite
| Nom Static Mesh | Dimensions (L × l × H cm) | Pivot | Nanite | Collision Simple |
| :--- | :--- | :--- | :--- | :--- |
| `SM_Port_HangarWall_400a` | `400 × 30 × 400` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` calée sur `BLK-GOMBE-PORT-01` |
| `SM_Port_ISOContainer_600a` | `600 × 240 × 240` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` (Couvert haut `240 cm`) |
| `SM_Port_CargoCrate_100a` | `200 × 100 × 100` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` (Vault `100 cm`) |

## 2. Bibliothèque de Matériaux PBR & RVT
| ID Matériau | BaseColor (sRGB) | Roughness | Packing Texture | Blend RVT Sol |
| :--- | :--- | :--- | :--- | :--- |
| `MI_Concrete_Dock_Wet` | `68 - 165 sRGB` | `0.25 (flaques) - 0.72` | `2K BaseColor + Normal + ORM` | `Oui (Transition limon fluvial 50 cm)` |
| `MI_Corrugated_Iron_Rust` | `55 - 180 sRGB` | `0.45 - 0.82` | `2K Trim Sheet + Custom Data Tint` | `Non (Toitures & Bardages)` |
| `MI_Laterite_Road_Blend` | `85 - 175 sRGB` | `0.30 (boue) - 0.85 (sec)` | `RVT Master Layer` | `Source RVT Principale` |
