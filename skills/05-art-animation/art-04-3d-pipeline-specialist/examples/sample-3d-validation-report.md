# Exemple `ART-04` — Audit de Validation 3D du Lot `KIT-GOMBE-PORT`

## 1. Résultat du Validateur (`scripts/check_3d_standards.py`)
- **Lot Audité** : `KIT-GOMBE-PORT` (`14 Static Meshes`, `18 Textures`)
- **Statut Global** : `PASSED (0 erreur bloquante)`

## 2. Détail des Contrôles par Asset
| Asset | Nomenclature | Pivot Grille | Texel Density | Nanite / Translucide | WPO Cull | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SM_Port_HangarWall_400a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Nanite Opaque (OK)` | `N/A (0 cm)` | **VALIDÉ** |
| `SM_Port_WindowGlass_200a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Non-Nanite Translucent (OK)` | `N/A (0 cm)` | **VALIDÉ** |
| `SM_Palm_Tropical_01a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Nanite Masked (OK)` | `3200 cm (<= 3500)` | **VALIDÉ** |
