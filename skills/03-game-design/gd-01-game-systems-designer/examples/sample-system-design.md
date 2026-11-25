# Exemple `GD-01` — Spécification de `SYS-STEALTH` (Infiltration Urbaine & Sociale)

- **ID Système** : `SYS-STEALTH`
- **Nom du Système** : Infiltration Urbaine & Sociale
- **Statut** : `CONFIRMED`

## 1. Boucle Fonctionnelle & Règles Métier
- **Objectif Joueur** : Traverser ou saboter les zones contrôlées par `ORG-CARTEL-FLEUVE` (comme `LOC-GOMBE-PORT`) sans déclencher d'alarme générale.
- **Règles de Fonctionnement** : Combine 3 vecteurs : (1) Dissimulation géométrique derrière couverts (`100 cm`/`200 cm`), (2) Dissimulation sociale par document ou tenue (`ITM-DOC-PASSEPORT`), (3) Masquage acoustique par l'environnement kinois (pluie tropicale, groupes électrogènes, passage de barges).

## 2. Architecture UE5 GAS & Gameplay Tags (`ENG-02`)
| Tag / Attribut | Rôle GAS | Effet Systémique |
| :--- | :--- | :--- |
| `State.Character.Stealth.Concealed` | `Owned` (en couvert/ombre) | Réduit le multiplicateur de détection visuelle `AI-01` à `0.25x`. |
| `State.Character.Stealth.Disguised` | `Owned` (avec `ITM-DOC-PASSEPORT`) | Autorise la marche normale devant les vigiles à distance `> 400 cm`. |
| `State.Character.Combat.Engaged` | `Blocked` / `Cancel` | Annule immédiatement l'état furtif et active l'alerte d'escouade. |

## 3. Matrice d'Interactions Émergentes
- **Interaction avec Météo (`World.Weather.TropicalStorm`)** : Le bruit de la pluie sur les toits en tôle masque les bruits de course et d'élimination silencieuse.
- **Interaction avec Foule (`SYS-CROWD-MASS`)** : Se fondre dans un groupe d'au moins 6 dockers ou passants octroie un camouflage social temporaire.
