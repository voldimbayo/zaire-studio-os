# Spécification de Typologie Urbaine (`WLD-03`)

- **Zone / Commune** : `DST-...` (`LOC-...`)
- **Code Typologie** : `TYP-[GOMBE-GRID / MATONGE-COMM / KALAMU-RES / INDUS-PORT]`
- **Statut Données SIG/OSM** : `CONFIRMED` | `RESEARCH_REQUIRED`

## 1. Règles Géométriques d'Îlots & Bâti (en cm UE5)
- **Dimensions moyennes d'îlot** : `[Longueur x Largeur cm]`
- **Hauteur de bâti (Étages / cm)** : `[Min - Max étages (400 cm/étage)]`
- **Matériaux dominants (`ART-02`)** : `[Béton, latérite, tôle, verre...]`

## 2. Profil de Voirie & Réseau (`ENG-04` / `AI-03`)
| Type de Voie | Nombre de Voies | Largeur par Voie (cm) | Trottoir (cm) | Véhicules Autorisés (`VEH-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `[Artère / Ruelle]` | `[N]` | `[350 / 400]` | `[250-600]` | `[VEH-*]` |

## Contraintes Studio & Validation Pré-Handoff (`WLD-03`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `WLD-04, ENG-04, AI-03`
