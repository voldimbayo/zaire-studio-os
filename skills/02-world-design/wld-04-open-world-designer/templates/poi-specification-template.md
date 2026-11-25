# Spécification de Point d'Intérêt Open World (`WLD-04`)

- **ID Lieu** : `LOC-[DST]-[SLUG]`
- **Commune Parente** : `DST-...`
- **Catégorie de POI** : `LANDMARK_TIER_1` | `MISSION_HUB` | `SYSTEMIC_ARENA` | `SAFEHOUSE`
- **Cellules World Partition (128m)** : `[Ex: Grid_X12_Y04]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Fonction Ludique & Intégration Monde Ouvert
- **Missions / Systèmes Rattachés** : `[MSN-* / SYS-*]`
- **Accès & Approches** : `[Axes routiers, fluviaux ou piétons]`
- **Lignes de Mire (Sightlines)** : `[Landmarks visibles depuis ce POI]`

## 2. Budget Streaming & Data Layers (`ENG-01`)
- **Data Layers Associés** : `[DL_Base, DL_Mission_..., DL_Night_...]`
- **Distance minimale au POI lourd voisin** : `[>= 250 m]`

## Contraintes Studio & Validation Pré-Handoff (`WLD-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, ENG-01, WLD-05`
