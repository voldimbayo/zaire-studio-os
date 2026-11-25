# Spécification de Conduite & Tuning Véhicule (`GD-06`)

- **ID Véhicule** : `VEH-[CAT]-[SLUG]`
- **Gameplay Tag** : `Vehicle.Type.[Nom]`
- **Gabarit (L × l × H en cm)** : `[XXX × XXX × XXX cm]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Paramètres Dynamiques Chaos Vehicles (`ENG-05`)
- **Masse Totale (kg)** : `[XXXX kg]`
- **Centre de Gravité (Offset Z cm)** : `[-XX cm]`
- **Vitesse Max & Accélération (0-60 km/h)** : `[XX km/h | X.X s]`
- **Assistance & Stabilisation** : `[Règles gyroscopiques / anti-retournement]`

## 2. Réponse par Surface & Météo
| Surface (`ChaosPhysicalMaterial`) | Multiplicateur Grip Latéral | Multiplicateur Freinage | Effet Caméra / Audio (`AUD-02`) |
| :--- | :--- | :--- | :--- |
| `PM_Asphalt_Dry` | `1.20` | `1.15` | `[Effet]` |

## Contraintes Studio & Validation Pré-Handoff (`GD-06`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, ENG-05, AI-03`
