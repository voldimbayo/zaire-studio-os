# Spécification de Kit Architectural & Matériaux PBR (`ART-02`)

- **ID Kit** : `KIT-[DST/LOC]-[SLUG]`
- **Brief Source (`WLD-06`)** : `ENV-...`
- **Texel Density** : `10.24 px/cm` (RDC) / `5.12 px/cm` (Étages)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Inventaire des Modules Géométriques Nanite
| Nom Static Mesh | Dimensions (L × l × H cm) | Pivot | Nanite | Collision Simple |
| :--- | :--- | :--- | :--- | :--- |
| `SM_Kit_...` | `400 × 30 × 400` | `Coin Inf-Gauche` | `Oui` | `Box exacte BLK` |

## 2. Bibliothèque de Matériaux PBR & RVT
| ID Matériau | BaseColor (sRGB min-max) | Roughness | Packing Texture | Blend RVT Sol |
| :--- | :--- | :--- | :--- | :--- |
| `MI_...` | `[45 - 210]` | `[0.35 - 0.85]` | `BC7 + ORM` | `Oui (50 cm)` |

## Contraintes Studio & Validation Pré-Handoff (`ART-02`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ART-04, ART-08, ART-01, WLD-05`
