# Métriques Spatiales & Gabarits Gameplay — Unreal Engine 5 (`spatial-metrics.md`)

Ce document fixe les **standards géométriques immuables** de **ZAÏRE STUDIO OS**. Tous les skills de *World Design* (`WLD-04`, `WLD-05`, `WLD-06`), *Art* (`ART-02`, `ART-04`, `ART-05`), *Game Design* (`GD-05`, `GD-06`) et *Engineering* (`ENG-04`, `ENG-05`) doivent s'y conformer.

---

## 1. Unité Moteur & Grille Modulaire
- **Échelle de base UE5** : `1 Unité Unreal (UU) = 1 cm`.
- **Grille de Snapping Architecturale (`ART-04` / `WLD-06`)** : Pas de grille principaux à `10 cm`, `50 cm`, `100 cm` et `400 cm`.
- **Texel Density Standard (`ART-04` / `ART-02`)** :
  - Environnements à hauteur d'œil (0 à 3 m du sol) : **`10.24 px/cm`** (soit une texture `2048x2048` pour un module de `200x200 cm`).
  - Étages supérieurs de bâtiments (3 à 15 m) : **`5.12 px/cm`**.
  - Arrière-plans et HLOD distants : **`1.28 px/cm`**.

---

## 2. Gabarit Personnage & Locomotion (`CHR-PROTAG-KOFFI` / PNJ)
- **Capsule de Collision Joueur** : Hauteur = `180 cm`, Rayon = `42 cm`.
- **Hauteur des Yeux (Caméra 1re référence)** : `165 cm`.
- **Franchissement & Parkour (`WLD-05` / `ART-05`)** :
  - Hauteur maximale de marche d'escalier (Step Height) : `20 cm` (profondeur minimale `30 cm`, pente maximale escalier `40°`).
  - Franchissement bas (Vault / Couvert bas) : **`100 cm`** (tolérance `90 cm` à `110 cm`).
  - Couvert haut (Full Cover debout) : **`200 cm`** minimum (largeur minimale d'un pilier de couvert : `80 cm`).
  - Saut d'accroche vertical (Ledge Grab) : **`260 cm`** à **`300 cm`** maximum.
  - Hauteur sous plafond standard (Intérieurs kinois) : **`320 cm`** minimum (afin d'éviter toute collision de la SpringArm caméra 3e personne).

---

## 3. Largeurs de Circulation & Caméra (`WLD-05` / `AI-01` / `AI-02`)
- **Couloir Intérieur / Ruelle Étroite Jouable** :
  - Largeur minimale absolue : **`350 cm`** (`3.5 m`) pour garantir le passage de 2 PNJ de front et la rotation fluide de la caméra 3e personne sans clipping.
  - Largeur recommandée en zone de mêlée (`GD-05`) : **`500 cm`** (`5.0 m`) minimum.
- **Portes Franchissables** :
  - Porte simple : Largeur **`120 cm`** × Hauteur **`220 cm`**.
  - Double porte / Entrepôt portuaire : Largeur **`240 cm`** à **`400 cm`** × Hauteur **`300 cm`**.

---

## 4. Gabarits Voirie & Véhicules (`WLD-03` / `GD-06` / `AI-03` / `ENG-04`)
- **Moto-Taxi Wewa (`VEH-MOTO-WEWA-01`)** : Longueur `205 cm`, Largeur `80 cm`. Largeur minimale d'inter-file (slalom trafic `AI-03`) : **`130 cm`**.
- **Taxi Collectif (`VEH-TAXI-JAUNE-01`)** : Longueur `440 cm`, Largeur `180 cm`, Hauteur `150 cm`.
- **Bus Urbain (`VEH-BUS-TRANSCO-01`)** : Longueur `1200 cm`, Largeur `255 cm`, Hauteur `330 cm`.
- **Voie Routière Standard (`ZoneGraph`)** : Largeur **`350 cm`** par voie sur avenue urbaine ; **`400 cm`** par voie sur boulevard lourd (`LOC-GOMBE-BD30JUIN`, Boulevard Lumumba).
- **Trottoir Piéton (`Mass Crowd`)** : Largeur minimale **`250 cm`** ; jusqu'à **`600 cm`** dans les zones de marché (`DST-MATONGE`).
