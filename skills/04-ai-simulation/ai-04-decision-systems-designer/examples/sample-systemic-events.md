# Exemple `AI-04` — Événements Systémiques de `DST-MATONGE` & `DST-KALAMU`

- **Commune Cible** : `DST-MATONGE` & `DST-KALAMU`
- **Rayon d'Exclusion Mission Principale** : `80 mètres`
- **Plafond Acteurs Hydratés par Événement** : `<= 4 acteurs AI-01`
- **Statut** : `CONFIRMED`

## 1. Table de Pondération Utility AI
| ID Événement | Commune | Fenêtre Horaire | Météo Compatible | Cooldown (min) | Acteurs Hydratés |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EVT-SYS-WEWA-BREAKDOWN` | `World.District.Kalamu` | `06h00 - 20h00` | Sec uniquement | `15 min` | `2` (Chauffeur Wewa + Passager) |
| `EVT-SYS-CARTEL-SHAKEDOWN` | `World.District.Matonge` | `18h00 - 02h00` | Toutes météos | `20 min` | `3` (2 Vigiles `ORG-CARTEL-FLEUVE` + 1 Commerçant) |
| `EVT-SYS-RADIO-CROWD` | `World.District.Matonge` | `17h00 - 23h00` | Sec uniquement | `15 min` | `4` (Auditeurs + Vendeur autour d'un poste `ORG-RADIO-KIN`) |

## 2. Déroulé Systémique & Récompense Émergente (`EVT-SYS-CARTEL-SHAKEDOWN`)
- **Mise en situation** : Deux collecteurs de `ORG-CARTEL-FLEUVE` tentent de saisir la recette du soir d'un disquaire près de `LOC-MATONGE-VICTOIRE`.
- **Interaction Joueur Optionnelle** : Koffi peut intervenir par intimidation sociale (si réputation Matonge `>= 250`), payer la dette (`1 500 FC`) ou repousser les vigiles en mêlée (`SYS-CMB-MELEE`).
- **Impact `SYS-WLD-REPUTATION` / Économie (`GD-03`)** : `+40 points` de réputation à `DST-MATONGE` et déblocage d'un indice oral sur les rondes portuaires de `LOC-GOMBE-PORT`.
