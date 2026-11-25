# Spécification Character Art & Modularité (`ART-03`)

- **ID Personnage / Kit Foule** : `CHR-...` | `NPC-KIT-...`
- **Commune / Faction** : `DST-...` | `ORG-...`
- **Squelette Cible** : `SK_Zaire_Master_Humanoid`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Budgets Géométriques, Textures & Groom
- **Polycount (LOD 0 / LOD 1 / LOD 2)** : `[XXk / XXk / XXk tris]`
- **Calibration Shader Peau (Albédo / Dual Lobe Roughness)** : `[Valeurs]`
- **Stratégie Cheveux (Strands vs Hair Cards)** : `[Règle par LOD]`

## 2. Table des Slots Modulaires & Variations (`AI-02`)
| Slot Modulaire | Nombre de Variantes Mesh | Atlas / Palette Shader | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `UpperBody` | `[N]` | `[Custom Data / Atlas]` | `[XX MB]` |

## Contraintes Studio & Validation Pré-Handoff (`ART-03`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ART-01, ART-04, WLD-02, ENG-07`
