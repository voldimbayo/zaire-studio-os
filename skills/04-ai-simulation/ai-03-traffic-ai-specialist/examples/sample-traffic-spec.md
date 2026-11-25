# Exemple `AI-03` — Trafic du Rond-Point Victoire (`LOC-MATONGE-VICTOIRE`)

- **Système** : `SYS-TRAFFIC-ZONE`
- **Axe / Carrefour** : `LOC-MATONGE-VICTOIRE` (`DST-MATONGE`)
- **Plafond Véhicules Actifs** : `75 véhicules MassTraffic` (coût CPU inclus dans l'enveloppe `PERF-CPU-MASS <= 2.0 ms`)
- **Statut** : `CONFIRMED`

## 1. Répartition de la Flotte & Règles de Voies
| ID Véhicule | Proportion (%) | Voies Autorisées | Comportement Spécifique ZoneGraph |
| :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `45 %` | Toutes voies + sous-voies inter-files (`150 cm`) | Slalom actif dès que le flux principal descend sous `20 km/h`. |
| `VEH-TAXI-JAUNE-01` | `40 %` | Voies moyennes et extérieures (`380 cm`) | Arrêts de `8 s` sur les encoches de dépose-minute devant les galeries. |
| `VEH-BUS-TRANSCO-01` | `15 %` | Voie centrale prioritaire (`380-400 cm`) | Allure régulière, priorité forcée à l'insertion dans le rond-point. |

## 2. Algorithme de Résolution d'Interblocage (Deadlock Watchdog)
- **Seuil de détection immobilisation** : `8.0 secondes` avec vitesse moyenne du noeud d'intersection `< 2.0 km/h`.
- **Action de déblocage prioritaire** : Gel temporaire (`4.0 s`) des feux/entrées radiales, dégagement forcé de l'anneau intérieur et recyclage discret des véhicules bloqués hors du cône de caméra à `> 110 m`.
- **Rayon de bascule Cinématique -> Chaos Physics (`ENG-05`)** : `35 mètres` autour de Koffi (ou instantané en cas d'impact projectile/véhicule).
