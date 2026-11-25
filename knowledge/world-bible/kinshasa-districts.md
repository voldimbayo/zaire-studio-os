# Référentiel des Communes & Quartiers de Kinshasa (`kinshasa-districts.md`)

Ce document constitue la référence géographique et spatiale officielle de **Couche 2 (Knowledge Base)** pour tous les skills des départements *World Design*, *Narrative*, *Art*, *Audio*, *AI* et *Engineering*.

---

## 1. Vue d'Ensemble et Zonage Open World

| ID Registre | Commune / Quartier | Typologie Urbaine | Densité Foule (`AI-02`) | Densité Trafic (`AI-03`) | Landmark Majeur (`WLD-04`) | Statut |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `DST-GOMBE` | **La Gombe** | Grille orthogonale, tours modernes, ministères, berges fluviales, port | Moyenne (250 PNJ) | Haute (axes larges) | `LOC-GOMBE-PORT` / `LOC-GOMBE-BD30JUIN` | `CONFIRMED` |
| `DST-MATONGE` | **Matonge (Kalamu)** | Tissu dense commercial, terrasses musicales, marchés nocturnes | Très Haute (600+ PNJ) | Très Haute (mixte Wewa/Taxis) | `LOC-MATONGE-VICTOIRE` | `CONFIRMED` |
| `DST-LIMETE` | **Limete** | Zone industrielle, entrepôts, habitat résidentiel et échangeur routier | Moyenne (300 PNJ) | Haute (poids lourds & bus) | `LOC-LIMETE-ECHANGEUR` | `CONFIRMED` |
| `DST-KALAMU` | **Kalamu** | Tissu résidentiel populaire, ateliers mécaniques, cours intérieures | Haute (450 PNJ) | Moyenne (ruelles & avenues) | Pont et axe Kasa-Vubu | `CONFIRMED` |
| `DST-BANDAL` | **Bandalungwa-Sud (Bandal)** | Tissu mixte résidentiel, culturel et commercial, studios, ngandas, marchés | Haute (520 PNJ) | Haute (carrefours Wewa & PCR) | `LOC-BANDAL-LUMUMBA-HUB` | `CONFIRMED` |
| `DST-NGALIEMA` | **Ngaliema** | Topographie vallonnée, rapides du fleuve Congo, villas et pentes latérite | Faible à Moyenne (200 PNJ) | Moyenne | Rapides de Kinsuka | `CONFIRMED` |
| `DST-MASINA` | **Masina** | Tissu urbain dense le long du Boulevard Lumumba (Est) | Très Haute (550+ PNJ) | Très Haute | Marché de la Liberté | `RESEARCH_REQUIRED` |

---

## 2. Signatures Sensorielles par Commune

### `DST-GOMBE` — La Gombe
- **Architecture (`WLD-03` / `ART-02`)** : Immeubles modernes en verre et béton brut, bâtiments administratifs, larges trottoirs arborés le long du Boulevard du 30 Juin (`LOC-GOMBE-BD30JUIN`), installations industrielles lourdes au Port ONATRA (`LOC-GOMBE-PORT`).
- **Éclairage (`ART-07`)** : Réflexions intenses Lumen sur le fleuve Congo et les façades vitrées ; éclairage public nocturne froid (LED 5000K).
- **Paysage Sonore (`AUD-01` / `AUD-02`)** : Sirènes fluviales des barges, trafic rapide, groupes électrogènes insonorisés, réverbération longue entre les tours.

### `DST-MATONGE` — Matonge
- **Architecture (`WLD-03` / `ART-02`)** : Bâtiments bas à 1-3 étages, galeries commerçantes colorées, enseignes peintes à la main, câblages électriques aériens denses, étals de rue modulaires autour de `LOC-MATONGE-VICTOIRE`.
- **Éclairage (`ART-07`)** : Néons chauds et saturés la nuit (ambre, magenta, vert émeraude), braseros de cuisine de rue, contrastes forts sous la pluie équatoriale.
- **Paysage Sonore (`AUD-01` / `AUD-03`)** : Diffusion multi-sources de rumba congolaise et ndombolo (`ORG-RADIO-KIN`), klaxons de motos Wewa (`VEH-MOTO-WEWA-01`), conversations animées en lingala et français kinois.

### `DST-LIMETE` — Limete
- **Architecture (`WLD-03` / `ART-02`)** : Structure monumentale en béton de la Tour de l'Échangeur (`LOC-LIMETE-ECHANGEUR`, 210 mètres de haut), hangars métalliques à toiture en tôle ondulée patinée, dépôts de conteneurs.
- **Éclairage (`ART-07`)** : Silhouette monumentale se découpant sur le ciel équatorial au crépuscule (Sky Atmosphere + Volumetric Clouds), projecteurs sodium haute pression (2200K) dans les zones industrielles.
- **Paysage Sonore (`AUD-01` / `AUD-02`)** : Grondement continu du Boulevard Lumumba, machinerie industrielle, vent en altitude autour de l'Échangeur.
