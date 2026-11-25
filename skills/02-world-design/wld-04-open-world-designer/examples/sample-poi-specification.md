# Exemple `WLD-04` — Spécification de `LOC-LIMETE-ECHANGEUR`

- **ID Lieu** : `LOC-LIMETE-ECHANGEUR`
- **Commune Parente** : `DST-LIMETE`
- **Catégorie de POI** : `LANDMARK_TIER_1` & `MISSION_HUB`
- **Cellules World Partition (128m)** : `Grid_X24_Y10` à `Grid_X25_Y11`
- **Statut** : `CONFIRMED`

## 1. Fonction Ludique & Intégration Monde Ouvert
- **Missions / Systèmes Rattachés** : `SYS-WLD-LANDMARKS` (repère vertical directeur de tout l'Est de Kinshasa), hub d'observation et d'interception radio pour l'Acte II.
- **Accès & Approches** : Connecté directement à l'anneau routier du Boulevard Lumumba (bretelles rapides `VEH-MOTO-WEWA-01`) et accessible à pied via l'esplanade piétonne.
- **Lignes de Mire (Sightlines)** : Visible jusqu'à `2.5 km` depuis `DST-MATONGE` et `DST-KALAMU` grâce à sa flèche de 210 mètres en béton brut.

## 2. Budget Streaming & Data Layers (`ENG-01`)
- **Data Layers Associés** : `DL_Limete_Permanent_HLOD0`, `DL_Act2_Syndicate_Blockade`.
- **Distance minimale au POI lourd voisin** : `420 m` (dépôt logistique sud de Limete), garantissant zéro surcharge CPU simultanée.
