# Brief de Design Environnemental (`WLD-06`)

- **ID Brief** : `ENV-[LOC]-[NUM]`
- **Blockout Source Validé** : `BLK-...` (`WLD-05`)
- **Lieu & Commune** : `LOC-...` (`DST-...`)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Narration Environnementale en 3 Couches
- **Couche 1 (Architecture & Patine)** : `[Matériaux, usure, météo]`
- **Couche 2 (Activité Sociale & Signalétique `NAR-05`)** : `[Enseignes, mobilier, vie locale]`
- **Couche 3 (Affordance Gameplay `WLD-05`)** : `[Marquage visuel des couverts et accroches]`

## 2. Manifeste des Kits Modulaires Requis (`ART-02` / `ART-04`)
| Kit ID | Dimensions Grille (cm) | Texel Density (px/cm) | Réutilisabilité | Usage Collision |
| :--- | :--- | :--- | :--- | :--- |
| `KIT-...` | `400x400` | `10.24` | `Haute` | `Conforme BLK` |

## Contraintes Studio & Validation Pré-Handoff (`WLD-06`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ART-01, WLD-05, ART-08`
