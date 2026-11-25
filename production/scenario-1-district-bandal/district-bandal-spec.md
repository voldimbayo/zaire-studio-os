# Spécification Complète de Quartier — `DST-BANDAL` (Bandalungwa-Sud)

- **ID Registre** : `DST-BANDAL` (`CONFIRMED`)
- **Landmark Directeur** : `LOC-BANDAL-LUMUMBA-HUB` (Carrefour & Marché Central de Bandal-Sud)
- **Gameplay Tag** : `World.District.Bandal`
- **Sources Vérifiées** : `SRC-001`, `SRC-004`, `SRC-005`, `SRC-012`, `SRC-013`, `SRC-019`, `SRC-021`, `SRC-023`

## 1. Urbanisme & Morphologie Viaire (`WLD-01`, `WLD-03`, `ENG-04`)
- **Grille UE 5.8 World Partition** : Cellules de `12800 cm` (`128 m × 128 m`), Data Layers `DL_Bandal_DayMarket` et `DL_Bandal_NightNganda`.
- **Hiérarchie Routière** :
  - *Avenue Inga / Axe Central* : 2 × 2 voies de `380 cm` + sous-voie centrale inter-file Wewa de `150 cm` (`VEH-MOTO-WEWA-01`) + trottoirs de `400 cm` sous auvents commerciaux (`180 cm`).
  - *Ruelles Résidentielles* : Chaussée mixte asphalte/latérite de `520 cm` (`>= 350 cm` requis) bordée de caniveaux de drainage de `60 cm`.

## 2. Économie Urbaine & Activités (`GD-01`, `GD-03`, `AI-04`)
- **Commerces & Services** : Ateliers de réparation moto Wewa, studios d'enregistrement rumba/ndombolo, terrasses de *ngandas* (`LEX-011`) et marché vivrier.
- **Modulation par `SYS-WLD-REPUTATION`** : Remise de `-15 %` au palier *Enfant du Quartier* (`>= 600 pts`) et intervention protectrice des riverains lors des contrôles de `ORG-POLICE-PCR`.
