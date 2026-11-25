# Spécification Trafic ZoneGraph & Anti-Deadlock (`AI-03`)

- **Système** : `SYS-TRAFFIC-ZONE`
- **Axe / Carrefour** : `LOC-...` (`DST-...`)
- **Plafond Véhicules Actifs** : `[XX véhicules MassTraffic]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Répartition de la Flotte & Règles de Voies
| ID Véhicule | Proportion (%) | Voies Autorisées | Comportement Spécifique ZoneGraph |
| :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `[XX %]` | `[Principales + Inter-file >= 130cm]` | `[Règle]` |

## 2. Algorithme de Résolution d'Interblocage (Deadlock Watchdog)
- **Seuil de détection immobilisation** : `[X secondes à < Y km/h]`
- **Action de déblocage prioritaire** : `[Protocole]`
- **Rayon de bascule Cinématique -> Chaos Physics (`ENG-05`)** : `[XX mètres]`

## Contraintes Studio & Validation Pré-Handoff (`AI-03`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `PRD-05, ENG-07, GD-06`
