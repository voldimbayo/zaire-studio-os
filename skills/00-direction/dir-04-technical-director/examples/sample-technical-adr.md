# ADR-TECH-004 : Architecture Hybride des Foules de Matonge (`AI-01` + `AI-02`)

- **Statut** : `CONFIRMED`
- **Autorité** : `DIR-04 (Technical Director)`
- **Sous-systèmes Impactés** : `PERF-CPU-NPCAI`, `PERF-CPU-MASS`, `SYS-CROWD-MASS`, `DST-MATONGE`

## 1. Problématique & Contrainte Budgétaire
Le Rond-Point Victoire (`LOC-MATONGE-VICTOIRE`) requiert plus de 500 citoyens visibles simultanément pour être crédible, alors que 500 `ACharacter` dotés de `UCharacterMovementComponent` et de Behavior Trees consommeraient > 18 ms sur le Game Thread.

## 2. Architecture Retenue
- **Couche Proche (0 à 25 m du joueur)** : Plafond strict de **24 `ACharacter`** gérés par `AI-01` (State Trees + Smart Objects + ragdoll Chaos complet).
- **Couche Médiane et Lointaine (25 m à 250 m)** : Jusqu'à **600 entités ECS `MassEntity`** (`AI-02`) circulant sur `ZoneGraph` avec animations partagées par Vertex Animation Textures (VAT) et instanciation Nanite/HISM.
- **Hydratation Dynamique** : Conversion asynchrone sans hitch entre représentation Mass LOD et `ACharacter` lorsque le joueur interagit ou déclenche un combat.

## 3. Seuils de Validation (`ENG-07` / `PRD-05`)
- **Budget CPU `AI-01` (24 acteurs)** : `<= 2.5 ms`
- **Budget CPU `AI-02` (600 entités Mass)** : `<= 2.0 ms`
- **Budget VRAM Kits Modulaires PNJ (`ART-03`)** : `<= 768 MB`
