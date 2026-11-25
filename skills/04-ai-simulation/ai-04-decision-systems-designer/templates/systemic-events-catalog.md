# Catalogue d'Événements Systémiques & Utility AI (`AI-04`)

- **Commune Cible** : `DST-...`
- **Rayon d'Exclusion Mission Principale** : `80 mètres`
- **Plafond Acteurs Hydratés par Événement** : `<= 4 acteurs AI-01`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Table de Pondération Utility AI
| ID Événement | Commune (`World.District.*`) | Fenêtre Horaire | Météo Compatible | Cooldown (min) | Acteurs Hydratés |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EVT-SYS-...` | `World.District...` | `[HH:MM-HH:MM]` | `[Sec / Pluie]` | `15 min` | `[2-4]` |

## 2. Déroulé Systémique & Récompense Émergente
- **Mise en situation** : `[Description]`
- **Interaction Joueur Optionnelle** : `[Action possible]`
- **Impact `SYS-WLD-REPUTATION` / Économie (`GD-03`)** : `[Gain]`

## Contraintes Studio & Validation Pré-Handoff (`AI-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, NAR-06, WLD-04`
