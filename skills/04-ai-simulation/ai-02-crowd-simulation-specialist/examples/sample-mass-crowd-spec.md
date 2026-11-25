# Exemple `AI-02` — Simulation de Foule de `DST-MATONGE` (`LOC-MATONGE-VICTOIRE`)

- **Système** : `SYS-CROWD-MASS`
- **Commune Cible** : `DST-MATONGE`
- **Budget CPU Max (`PERF-CPU-MASS`)** : `<= 2.0 ms` (60 FPS)
- **Statut** : `CONFIRMED`

## 1. Distribution par Anneau LOD & Validation Budget
- **Acteurs Hydratés (LOD 0, `< 25 m`)** : `18 acteurs` (commerçants, passants proches, ambianceurs).
- **Entités Mass LOD 1 (`25 - 80 m`)** : `180 entités` sur les trottoirs de `500 cm` du Rond-Point Victoire.
- **Entités Mass LOD 2 VAT (`80 - 250 m`)** : `420 entités` sur les avenues radiales.
- **Coût CPU Estimé (`check_mass_budget.py`)** : **`1.566 ms`** (600 entités Mass + 18 acteurs hydratés -> **CONFORME `< 2.0 ms`**).

## 2. Courbes de Densité Horaire & Réactivité Météo
| Créneau Horaire / Événement | Densité Active (%) | Profils PNJ Dominants (`ART-03`) | Comportement ZoneGraph |
| :--- | :--- | :--- | :--- |
| `Marché Matinal (07h-12h)` | `90 % (540 PNJ)` | Commerçants, livreurs, étudiants | Flux continu le long des étals et arrêts bus `ORG-TRANSCO`. |
| `Soirée Musicale (18h-23h)` | `100 % (600 PNJ)` | Citoyens, Sapeurs, clients de ngandas | Regroupement en grappes statiques autour des terrasses diffusant `ORG-RADIO-KIN`. |
| `Averse (World.Weather.TropicalStorm)` | `40 % en rue / 60 % sous auvents` | Tous profils | Migration rapide (`1.6x`) vers les galeries couvertes (`180 cm` de porte-à-faux). |
