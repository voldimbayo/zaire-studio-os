# Exemple `WLD-06` — Brief Environnemental `ENV-GOMBE-PORT-01` (`LOC-GOMBE-PORT`)

- **ID Brief** : `ENV-GOMBE-PORT-01`
- **Blockout Source Validé** : `BLK-GOMBE-PORT-01` (`WLD-05`)
- **Lieu & Commune** : `LOC-GOMBE-PORT` (`DST-GOMBE`)
- **Statut** : `CONFIRMED`

## 1. Narration Environnementale en 3 Couches
- **Couche 1 (Architecture & Patine)** : Quais en béton armé strié avec flaques d'eau réfléchissant les grues (Lumen Reflections), hangars à charpente métallique rivetés, rouille tropicale et traces de pneus de chariots élévateurs.
- **Couche 2 (Activité Sociale & Signalétique `NAR-05`)** : Panneaux réglementaires portuaires bilingues, conteneurs marqués au pochoir, guérite de contrôle avec poste radio diffusant `ORG-RADIO-KIN` à bas volume.
- **Couche 3 (Affordance Gameplay `WLD-05`)** : Sangles d'arrimage jaune vif et projecteurs de chantier orientant l'œil vers l'échelle de la grue ouest (`+400 cm`) et les caisses de couvert bas (`100 cm`).

## 2. Manifeste des Kits Modulaires Requis (`ART-02` / `ART-04`)
| Kit ID | Dimensions Grille (cm) | Texel Density (px/cm) | Réutilisabilité | Usage Collision |
| :--- | :--- | :--- | :--- | :--- |
| `KIT-PORT-WALL-400` | `400 × 400 × 30` | `10.24` | `Haute (Hangars Gombe & Limete)` | Box simple calée sur `BLK-GOMBE-PORT-01` |
| `KIT-ISO-CONTAINER-600` | `600 × 240 × 240` | `10.24` | `Très Haute (Variations couleurs Custom Data)` | Couvert haut `240 cm` + toit franchissable |
| `KIT-CARGO-CRATE-100` | `200 × 100 × 100` | `10.24` | `Très Haute` | Couvert bas `100 cm` certifié Vault |
