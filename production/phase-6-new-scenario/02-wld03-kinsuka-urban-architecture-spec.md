# Spécification de Typologie Urbaine & Morphologie de Colline (`WLD-03`)

- **Identifiant de Tâche DAG** : `TSK-P6-002` (Vague 2 — Strate DAG `1`, Orchestration `ORC-2026-P6-001`)
- **Zone / Commune** : `DST-NGALIEMA` (`CONFIRMED`) — Secteur `LOC-NGALIEMA-KINSUKA-CROSSING` (*Carrefour & Passerelle du Marché des Rapides de Kinsuka* — **`PROPOSED`**)
- **Code Typologie Canonique (`WLD-03` SOP #1)** : Tissu Composite de Côte `TYP-KALAMU-RES` (Parcellaire Résidentiel Organique) + `TYP-INDUS-PORT` (Extraction Artisanale de Moellons & Nœud PCR) + Poche `TYP-MATONGE-COMM` (Passerelle-Marché) — *Profil hybride proposé pour indexation Couche 2 : `TYP-NGALIEMA-HILLSIDE-HYBRID` (**`PROPOSED`**)*
- **Statut du Livrable & Plafond d'Entités** : **`PROPOSED`** *(Promotion vers `CONFIRMED` soumise à co-signature ultérieure `DIR-06` + `DIR-07` selon `ARB-P6-004`)*
- **Statut Données SIG/OSM & Topographie DEM** : **`RESEARCH_REQUIRED`** (`RR-KINSUKA-OSM-001`, `RR-KINSUKA-DEM-002`) — *Règles géométriques compensatoires ci-dessous fournies au statut **`PROPOSED`** (`Engineering Recommendation` conforme à `spatial-metrics.md`)*
- **Statut d'Exécution Moteur / Binaires (UE 5.8 / Houdini 22.0 / Wwise)** : **`NOT TESTED`** — *Toutes les cibles de performance citées constituent des allocations synthétiques (**`SYNTHETIC_TARGET_ALLOCATION`**)*

---

## 0. Séparation Stricte : Données Terrain Non Vérifiées (`RESEARCH_REQUIRED`) vs Règles Paramétriques (`PROPOSED`)

Conformément au Scope Guard de `WLD-03` et aux arbitrages `DIR-01`, aucune micro-mesure géographique réelle non vérifiée de Kinsuka n'est présentée comme fait établi :

| ID Recherche | Domaine | Éléments Réels Strictement Isolés en `RESEARCH_REQUIRED` | Règle Paramétrique Compensatoire (`PROPOSED` — `Engineering Recommendation`) |
| :--- | :--- | :--- | :--- |
| **`RR-KINSUKA-OSM-001`** | SIG / Voirie OpenStreetMap (`DST-NGALIEMA`) | Largeurs exactes d'emprise des chaussées primaires/secondaires réelles à Kinsuka, nomenclature odonymique officielle des ruelles secondaires, pourcentages réels de pente routière (%), géométrie exacte des passerelles existantes et section réelle des collecteurs d'érosion. | Application stricte des gabarits `spatial-metrics.md` (`400 cm` voie lourde, `350 cm` voie standard, `>= 130 cm` / cible `150 cm` inter-file Wewa, `200 cm` transition asphalte-latérite) et subdivision parcellaire compensatoire `1500 × 2500 cm` (FMEA #1) pour permettre la génération `ENG-04` sans inventer de monuments erronés. |
| **`RR-KINSUKA-DEM-002`** | Topographie DEM & Hydrologie (Rapides de Kinsuka) | Altimétrie absolue (m NGM / SRTM / Copernicus haute résolution), bathymétrie/débit exacts des rapides du fleuve Congo et dénivelé métrique réel entre l'axe routier supérieur, les carrières de grès/quartzite et la berge rocheuse. | Étagement relatif local paramétré en `4` paliers (`T0` à `T3`, de `Z = 0 cm` berge rocheuse à `Z = +2880 cm` coteau résidentiel) avec gradins de carrière calibrés à `280 cm` (plage *Ledge Grab* `260–300 cm`) et pente longitudinale routière bornée entre `6.0 %` et `8.0 %` max pour la stabilité `ZoneGraph` / `SYS-PHYS-CHAOS`. |
| **`RR-KINSUKA-ACOUSTIC-004`** *(Réf. Croisée `WLD-02`/`AUD-04`)* | Signature Sensorielle `DST-NGALIEMA` | Niveau réel de pression acoustique (dB SPL) des rapides de Kinsuka et du concassage manuel (Section 2 de `kinshasa-districts.md` muette sur `DST-NGALIEMA`, cf. `ARB-P6-002`). | Contribution strictement architecturale et morphologique de `WLD-03` en Section 1.3 (**`PROPOSED`**) : écrans minéraux (gabions, soutènements) et ouvertures visuelles vers le fleuve, sans prescrire de mixage Wwise (`AUD-04`). |

---

## 1. Règles Géométriques d'Îlots, Topographie de Colline & Bâti (en cm UE5 — `1 UU = 1 cm`)

### 1.1 Organisation Topographique Multi-Niveaux Surplombant les Rapides (`PROPOSED`)
Le secteur `LOC-NGALIEMA-KINSUKA-CROSSING` (**`PROPOSED`**) s'inscrit dans une poche active de **`2 × 2` cellules `World Partition`** (`25600 cm × 25600 cm`, soit `256 m × 256 m` à raison de `12800 cm` par cellule `SYS-WLD-STREAMING`, `SRC-001`), structurée en amphithéâtre décroissant du Sud-Est (coteau Ngaliema) vers le Nord-Ouest (Rapides de Kinsuka sur le fleuve Congo) :

1. **Palier `T0` — Berge Rocheuse & Horizon des Rapides (`Z = 0 cm` à `+400 cm`, Zone Hors-Jeu / Limite Diégétique)** :
   - Affleurements de grès/quartzite sombre et rapides tumultueux servant de macro-landmark permanent (`SYS-WLD-LANDMARKS`).
   - Séparation physique de sécurité avec l'espace jouable par un mur de gabions continu et enrochements cyclopéens de **`110 cm` à `220 cm`** de haut (empêchant toute chute accidentelle de véhicule `SYS-TRAFFIC-ZONE` tout en conservant la ligne de mire caméra à `165 cm` hauteur d'œil de `CHR-PROTAG-KOFFI`).
2. **Palier `T1` — Terrasses d'Extraction & Cours de Concassage Artisanal (`Z = +400 cm` à `+1240 cm`)** :
   - **3 gradins successifs** réglés sur un pas vertical paramétrique de **`280 cm`** (`+400 cm`, `+680 cm`, `+960 cm`, raccordés à `+1240 cm`), directement exploitables par le saut d'accroche vertical (*Ledge Grab* `260–300 cm` de `spatial-metrics.md`) ou par des volées d'escaliers maçonnés/taillés (`hauteur de marche <= 20 cm`, `profondeur >= 30 cm`, `pente <= 38°`, largeur libre `350 cm`).
3. **Palier `T2` — Sillon Routier Principal en Pente, Encoche PCR & Front Commercial (`Z = +1240 cm` aval à `+2200 cm` amont)** :
   - L'artère principale gravit le coteau sur `16000 cm` (`160 m` linéaires) avec une pente longitudinale régulière de **`6.0 %`** comportant un segment de compression de **`8.0 %`** (`3200 cm` de long) immédiatement en amont de l'encoche `ORG-POLICE-PCR`, provoquant le ralentissement mécanique crédible des poids lourds `VEH-BUS-TRANSCO-01` et l'immobilisation du convoi `VEH-CONVOY-DIPLO-01` (**`PROPOSED`**).
4. **Palier `T3` — Passerelle-Marché en Surplomb & Parcellaire Résidentiel Supérieur (`Z = +2080 cm` à `+2880 cm`)** :
   - Au point médian du goulot (`Z_chaussée = +1600 cm`), la passerelle piétonne commerciale franchit l'artère à **`Z = +2080 cm`** (assurant un **tirant d'air libre sous poutre de `480 cm`**, supérieur de `150 cm` à la hauteur de `VEH-BUS-TRANSCO-01` fixée à `330 cm`), reliant de plain-pied le parvis du marché amont aux escaliers plongeant vers les carrières `T1`.

### 1.2 Matrice des 4 Sous-Typologies d'Îlots & Bâti (`WLD-03` DoD #1 & #2 — `PROPOSED`)
Toutes les constructions s'alignent sur la grille modulaire `spatial-metrics.md` (`10 cm`, `50 cm`, `100 cm`, **`400 cm` par étage**) avec hauteur sous plafond intérieure minimale absolue de **`320 cm`** (anti-clipping SpringArm caméra 3e personne) et portes normalisées (`120 × 220 cm` simple ; `240–400 × 300 cm` double/atelier) :

| Code Îlot (`PROPOSED`) | Preset Canonique | Dimensions Moyennes d'Îlot & Parcelle (`cm`) | Hauteur de Bâti (Étages / `cm`) | Retrait de Façade (`cm`) | Densité Câblage / Végétation | Matériaux Dominants & Couverts (`ART-02` / `WLD-05`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`BLK-KINSUKA-QUARRY-01`** *(Terrasses des Carriers — `ORG-SYNDICAT-CARRIERES-KINSUKA` `PROPOSED`)* | `TYP-INDUS-PORT` | Îlot-terrasse : **`3200 × 6400 cm`**<br>Cour d'atelier : **`1600 × 2400 cm`** | **0 à 1 étage**<br>(`320 cm` libre sous tôle à **`400 cm`** hors-tout — abri syndical `CHR-ALLY-MAMA-LUZOLO` `PROPOSED`) | **`400 cm` à `600 cm`** (aire de pesée, stockage gabions et arènes `>= 600 cm` compatibles mêlée `>= 500 cm`) | **Câblage : Faible** (poteaux bois `600 cm` isolés)<br>**Végétation : Moyenne-Éparse** (vétiver anti-érosif, graminées sur talus) | Latérite ocre-rouge, moellons de grès/quartzite, gabions (`100 cm` couvert bas ; piles de sacs/pierres `200 cm × >= 80 cm` couvert haut), tôle rouillée, bâches bleues. |
| **`BLK-KINSUKA-MARKET-02`** *(Front Commercial & Parvis Passerelle)* | `TYP-MATONGE-COMM` | Îlot linéaire : **`2400 × 7200 cm`**<br>Parcelle : **`1200 × 2400 cm`** *(ou fallback `1500 × 2500 cm`)* | **1 à 3 étages**<br>(**`400 cm` à `1200 cm`** ; RDC `360 cm` plafond libre + dalle `40 cm`) | **`300 cm` à `500 cm`** (galerie marchande sous auvent, hors emprise trottoir `Mass Crowd`) | **Câblage : Très Haute** (faisceaux électriques sur poteaux béton `800 cm`, tirant d'air `>= 520 cm`)<br>**Végétation : Faible** (manguiers/badamiers ponctuels d'ombrage) | Parpaings enduits patinés de poussière latérite, enseignes peintes à la main (`fr-CD`/`ln-CD`), béton brut humide, bois d'œuvre, étals bas (`100 cm` vault). |
| **`BLK-KINSUKA-HILLSIDE-RES-03`** *( Habitat Organique de Pente & Villas Crête)* | `TYP-KALAMU-RES` | Îlot organique : **`4500 × 7500 cm`**<br>Parcelle compensatoire OSM : **`1500 × 2500 cm`** *(crête : `2500 × 3500 cm`)* | **1 à 2 étages**<br>(**`400 cm` à `800 cm`** sur soubassement pierre de rattrapage `100–280 cm`) | **`200 cm` à `400 cm`** derrière mur de clôture maçonné (`200–240 cm` couvert haut) | **Câblage : Moyenne** (branchements domestiques aériens)<br>**Végétation : Haute** (palmiers, bananiers, bougainvilliers stabilisant les talus) | Soubassement moellons de Kinsuka, parpaings bruts ou crépis ocre/blanc cassé, portails fer forgé (`120 × 220 cm` / `280 × 300 cm`), toitures bac acier/tôle. |
| **`BLK-KINSUKA-PCR-NODE-04`** *(Poste de Contrôle `ORG-POLICE-PCR`)* | `TYP-INDUS-PORT` *(Infra Routière)* | Plateforme nivelée : **`2000 × 3600 cm`** en épaulement du carrefour | **1 étage**<br>(**`400 cm`** extérieur ; **`320 cm`** plafond intérieur libre guérite) | **`400 cm`** par rapport à l'encoche `VEH-*` (quai d'inspection + esplanade arrière `600 × 800 cm`) | **Câblage : Moyenne** (mât projecteur + antenne relais)<br>**Végétation : Nulle à Très Faible** (dégagement lignes de vue `SYS-STEALTH`) | Béton banché blanc/bleu institutionnel délavé, chicanes béton armé (`100 cm` haut), barrières métalliques rouge/blanc, bordures hautes anti-franchissement (`25 cm`). |

- **Référence Texel Density (`spatial-metrics.md` pour `ART-02` / `ART-04`)** : `10.24 px/cm` de `0` à `300 cm` (murs bas, étals, gabions, guérite PCR) ; `5.12 px/cm` de `300` à `1500 cm` (étages R+1/R+2 et charpente supérieure de la passerelle) ; `1.28 px/cm` pour les îlots rocheux lointains et la rive opposée des rapides en HLOD.

### 1.3 Proposition Architecturale pour la Fiche Sensorielle `DST-NGALIEMA` (`ARB-P6-002` — `PROPOSED`)
Pour pallier l'absence de `DST-NGALIEMA` en Section 2 de `knowledge/world-bible/kinshasa-districts.md`, `WLD-03` soumet le volet morphologique suivant (**`PROPOSED`**) :
- **Signature Architecturale & Urbaine (`DST-NGALIEMA` — Secteur Kinsuka)** : Tissu péri-fluvial escarpé articulant des soutènements massifs en moellons de grès gris-ocre taillés localement, des pentes de latérite rouge ravinées par des caniveaux d'érosion profonds, une artère de transit asphaltée sous forte contrainte topographique et des belvédères accidentels ouvrant des cadrages plongeants sur l'écume blanche des Rapides de Kinsuka (`SYS-WLD-LANDMARKS`).

---

## 2. Profil de Voirie, Hiérarchie Réseau & Circulations Piétonnes (`ENG-04` / `AI-03`)

### 2.1 Tableau Maître des Profils de Voirie & Franchissements (en cm UE5 — `PROPOSED`)
Toutes les largeurs ci-dessous respectent sans dérogation `spatial-metrics.md` (`400 cm` voie lourde, `350 cm` voie standard, `>= 130 cm` inter-file Wewa avec cible retenue à **`150 cm`**, `>= 250 cm` trottoir `Mass Crowd`, **`>= 350 cm`** corridor piéton jouable, et **`200 cm`** de bande de transition asphalte-latérite) :

| ID Tronçon (`PROPOSED`) | Type de Voie / Ouvrage | Nb de Voies | Largeur par Voie (`cm`) | Couloir Inter-File Wewa (`cm`) | Trottoir / Corridor Piéton Libre (`cm`) | Drainage & Transition (`cm`) | Véhicules Autorisés (`VEH-*`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **`AXE-KINSUKA-ARTERIAL-01`** | Artère Principale de Côte (Asphalte lourd, pente `6 %–8 %`) | **4** (`2 × 2`) | **`400 cm`** *(chaussée roulable `1600 cm` + séparateur médian `150 cm`)* | **`150 cm`** garanti (`>= 130 cm` min strict entre files montantes et descendantes) | **`350 cm` à `450 cm`** par rive *(libre d'obstacles, compatible `SYS-CROWD-MASS` & caméra)* | Caniveaux béton latéraux `80 × 60 cm` (dalles piétonnes larges de `400 cm` tous les `2400 cm`) | `VEH-BUS-TRANSCO-01`, `VEH-TAXI-JAUNE-01`, `VEH-MOTO-WEWA-01`, `VEH-POLICE-PICKUP-01`, `VEH-CONVOY-DIPLO-01` (`PROPOSED`) |
| **`AXE-KINSUKA-PCR-BAY-02`** | Encoche de Contrôle `ORG-POLICE-PCR` (Pull-Out Bay asphaltée) | **1** *(délestage latéral)* | **`400 cm`** *(longueur utile `2400 cm` + biseaux d'insertion/sortie `2 × 800 cm`)* | **`150 cm`** en sortie de filtre chicane (dégagement moto/urgence) | **`400 cm`** (quai d'inspection PCR, prolongé par esplanade `600 × 800 cm`) | Bordure chasse-roue `25 cm` + grille avaloir pluvial transversal `100 cm` | `VEH-POLICE-PICKUP-01`, `VEH-CONVOY-DIPLO-01` (`PROPOSED`), `VEH-TAXI-JAUNE-01`, `VEH-BUS-TRANSCO-01` *(contrôle)*, `VEH-MOTO-WEWA-01` |
| **`AXE-KINSUKA-QUARRY-LAT-03`** | Piste Collectrice des Carrières (Latérite compactée, pente `6 %–9 %`) | **2** (`2 × 1`) | **`350 cm`** *(chaussée `700 cm` conforme FMEA #2, hors bus lourds)* | **`130 cm` à `150 cm`** (dépassement souple Wewa) | **`350 cm`** sur berge amont / **`250 cm`** accotement aval non-mission | **Bande de transition Asphalte-Latérite de `200 cm`** avec caniveau ouvert à grille (FMEA #3 RVT) + fossé pierre `60 cm` | `VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`, `VEH-POLICE-PICKUP-01` *(interdit à `VEH-BUS-TRANSCO-01`)* |
| **`AXE-KINSUKA-QUARRY-SPUR-05`** | Venelles & Rampes Internes de Concassage (Latérite/Grès) | **1** *(mixte léger)* | **`450 cm` à `550 cm`** *(emprise unique partagée)* | Filtrage d'entrée par plots moellons espacés de **`150 cm`** *(bloque 4x4/Taxis `>= 180 cm`)* | Intégré (`>= 350 cm` libre permanent ; placettes de concassage `>= 600 cm`) | Rigole centrale ou latérale en pierre sèche `50 cm` (franchissable à pied/Wewa) | `VEH-MOTO-WEWA-01` uniquement (`80 cm` large) + Piétons (`CHR-PROTAG-KOFFI` / PNJ) |
| **`AXE-KINSUKA-OVERPASS-PED-04`** | Passerelle du Marché & Terrasses Piétonnes Étagées (Tirant d'air `480 cm`) | **0** *(100 % piéton)* | N/A *(Tablier structurel total : **`650 cm`**)* | Plots anti-moto aux pieds d'escaliers *(espacement `120 cm` ou marches `20 × 30 cm`)* | **`400 cm` central strictement libre** *(encadré par `2 × 125 cm` d'étals bas `100 cm`)* ; escaliers/terrasses **`350–400 cm`** | Gargouilles d'évacuation pluviale hors gabarit routier | Aucun véhicule (`SYS-CROWD-MASS` + `CHR-PROTAG-KOFFI` + PNJ `AI-01`) |

### 2.2 Mécanique Spatiale du Goulot d'Étranglement & Inter-File Wewa (`AI-03` / `GD-02`)
1. **Génération Géométrique de la Congestion Sans Deadlock (`AI-03`)** :
   - En amont immédiat de `AXE-KINSUKA-PCR-BAY-02`, une chicane mobile de `ORG-POLICE-PCR` neutralise partiellement la voie extérieure montante sur `1200 cm` pour orienter les contrôles vers l'encoche de `400 cm`, forçant la convergence des `VEH-BUS-TRANSCO-01` (`1200 × 255 × 330 cm`) et `VEH-TAXI-JAUNE-01` (`440 × 180 × 150 cm`) sur la pente à `8.0 %`.
   - Le véhicule cible `VEH-CONVOY-DIPLO-01` (**`PROPOSED`**) dispose d'une enveloppe géométrique maximale autorisée par `WLD-03` de **`<= 520 cm` (L) × `<= 215 cm` (l) × `<= 205 cm` (H)** *(prescription purement dimensionnelle d'insertion urbaine, sans aucun paramètre physique Chaos Vehicle relevant de `GD-06`)*. Il s'inscrit ainsi dans une voie de `400 cm` (ou `350 cm`) en conservant `>= 185 cm` de marge latérale cumulée.
2. **Garantie Mathématique du Couloir Inter-File `VEH-MOTO-WEWA-01` (`>= 130 cm` / Cible `150 cm`)** :
   - Sur `AXE-KINSUKA-ARTERIAL-01` (`2` voies montantes de `400 cm` = `800 cm`), même lorsque `VEH-BUS-TRANSCO-01` (`255 cm`) et `VEH-CONVOY-DIPLO-01` (`<= 215 cm`) ou `VEH-TAXI-JAUNE-01` (`180 cm`) sont immobilisés côte à côte, une bande virtuelle `ZoneGraph` dédiée de **`150 cm`** (`>= 130 cm` requis par `spatial-metrics.md`) est réservée entre les axes de voies (et doublée d'une bande de dégagement de `150 cm` le long du séparateur médian), permettant à `VEH-MOTO-WEWA-01` (`205 × 80 cm`) de slalomer sans collision latérale et à `CHR-PROTAG-KOFFI` (capsule `84 cm` diamètre) de s'infiltrer entre les carrosseries (`SYS-STEALTH`).
3. **Couloir de Dégagement d'Urgence (`VEH-POLICE-PICKUP-01` & `ORG-URGENCE-FLUVIALE`)** :
   - L'encoche `AXE-KINSUKA-PCR-BAY-02` (`400 cm` large) combinée à la voie descendante intérieure (`400 cm`) et au séparateur médian franchissable à profil bas (`15 cm` chanfreiné hors plots PCR) garantit un couloir de dégagement continu `>= 400 cm` pour les interventions `SYS-LAW-ESCALATION` (Niveaux 2 et 3).

### 2.3 Export Structuré `road-network-hierarchy.csv` Intégré (`ENG-04` / `AI-03` — `PROPOSED`)
Conformément au contrat de sortie `WLD-03` tout en respectant l'artefact unique de `TSK-P6-002`, le schéma tabulaire suivant est directement ingérable par les attributs de splines Houdini (`ENG-04`) et les profils `ZoneGraph` (`AI-03`) :

```csv
segment_id,status,hierarchy_tier,surface_material,lanes_count,lane_width_cm,wewa_interlane_gap_cm,clear_sidewalk_width_cm,asphalt_laterite_transition_cm,vertical_clearance_cm,parametric_slope_pct,real_osm_dem_status,allowed_vehicles
AXE-KINSUKA-ARTERIAL-01,PROPOSED,PRIMARY_ARTERIAL,ASPHALT_HEAVY,4,400,150,350,0,480,6.0_TO_8.0,RESEARCH_REQUIRED_RR-KINSUKA-OSM-001,VEH-BUS-TRANSCO-01|VEH-TAXI-JAUNE-01|VEH-MOTO-WEWA-01|VEH-POLICE-PICKUP-01|VEH-CONVOY-DIPLO-01
AXE-KINSUKA-PCR-BAY-02,PROPOSED,CHECKPOINT_PULLOUT,ASPHALT_STRIPED,1,400,150,400,0,9999,2.0,RESEARCH_REQUIRED_RR-KINSUKA-OSM-001,VEH-POLICE-PICKUP-01|VEH-CONVOY-DIPLO-01|VEH-TAXI-JAUNE-01|VEH-BUS-TRANSCO-01|VEH-MOTO-WEWA-01
AXE-KINSUKA-QUARRY-LAT-03,PROPOSED,SECONDARY_COLLECTOR,LATERITE_COMPACTED,2,350,140,350,200,9999,6.0_TO_9.0,RESEARCH_REQUIRED_RR-KINSUKA-OSM-001|RR-KINSUKA-DEM-002,VEH-MOTO-WEWA-01|VEH-TAXI-JAUNE-01|VEH-POLICE-PICKUP-01
AXE-KINSUKA-QUARRY-SPUR-05,PROPOSED,TERTIARY_TRACK,LATERITE_SANDSTONE,1,450,150,350,200,9999,4.0_TO_8.0,RESEARCH_REQUIRED_RR-KINSUKA-DEM-002,VEH-MOTO-WEWA-01
AXE-KINSUKA-OVERPASS-PED-04,PROPOSED,PEDESTRIAN_OVERPASS,CONCRETE_STEEL_DECK,0,0,0,400,0,320,0.0_DECK_35DEG_STAIRS,RESEARCH_REQUIRED_RR-KINSUKA-OSM-001,NONE_PEDESTRIAN_ONLY
```

---

## 3. Contraintes Studio, Streaming & Validation Pré-Handoff (`WLD-03`)

- **Budgets Cibles UE 5.8 (`SYNTHETIC_TARGET_ALLOCATION` / `NOT TESTED`)** :
  - Frametime global cible : **`<= 16.6 ms`** (Mode Performance 60 FPS) / **`<= 33.3 ms`** (Mode Qualité 30 FPS).
  - Densité locale calibrée selon `ARB-P6-001` : **`<= 24` PNJ individuels `AI-01` actifs** (`<= 2.5 ms` CPU `SYNTHETIC_TARGET_ALLOCATION`) + **`180 à 220` entités `SYS-CROWD-MASS`** concentrées sur la passerelle-marché et les trottoirs du carrefour (`<= 2.0 ms` CPU `SYNTHETIC_TARGET_ALLOCATION`, rayon d'hydratation `<= 2500 cm` / `25 m`).
  - Grille `SYS-WLD-STREAMING` (`World Partition`) : Cellules de **`12800 cm`** (`OFPA`), espacement minimal de **`25600 cm` (`256 m`)** garanti vis-à-vis de toute autre arène lourde (`> 20` PNJ `AI-01`) dans `DST-NGALIEMA`.
  - Conformité `spatial-metrics.md` vérifiée : `1 UU = 1 cm` | Corridors jouables `>= 350 cm` (`400 cm` sur passerelle) | Poches mêlée `>= 500 cm` (`>= 600 cm` cours carrières & parvis PCR) | Plafonds `>= 320 cm` | Couverts `100 cm` / `>= 200 cm` | Ledge Grab `280 cm` (`[260, 300] cm`) | Escalier `<= 20 cm` × `>= 30 cm` (`<= 40°`).
- **Entités Registre Référencées (`knowledge/entities-registry.csv` & `00-dir01-execution-plan.json`)** :
  - **`CONFIRMED`** : `DST-NGALIEMA`, `CHR-PROTAG-KOFFI`, `ORG-POLICE-PCR`, `ORG-TRANSCO`, `ORG-CARTEL-FLEUVE`, `ORG-URGENCE-FLUVIALE`, `VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`, `VEH-BUS-TRANSCO-01`, `VEH-POLICE-PICKUP-01`, `SYS-WLD-STREAMING`, `SYS-WLD-LANDMARKS`, `SYS-TRAFFIC-ZONE`, `SYS-CROWD-MASS`, `SYS-STEALTH`, `SYS-CMB-MELEE`, `SYS-PHYS-CHAOS`, `SYS-LAW-ESCALATION`, `SYS-TELEMETRY-ANALYTICS` *(ainsi que `DST-GOMBE`, `DST-MATONGE`, `DST-KALAMU`, `DST-LIMETE` au titre de la nomenclature typologique canonique)*.
  - **`PROPOSED` (Phase 6 — Plafond `ARB-P6-004`)** : `LOC-NGALIEMA-KINSUKA-CROSSING`, `MSN-MAIN-009-KINSUKA-CONVOY`, `CHR-ALLY-MAMA-LUZOLO`, `ORG-SYNDICAT-CARRIERES-KINSUKA`, `VEH-CONVOY-DIPLO-01`, `ITM-DOC-KINSUKA-LEDGER`.
- **Sources Mobilisées (`research/source-registry.csv`)** :
  - `SRC-001` (*World Partition in Unreal Engine*, Epic Games, 2025 — Consultée Extrait/Index)
  - `SRC-004` (*City Sample Quick Start for Generating a City and Freeway using Houdini*, Epic Games / SideFX, 2024 — Consultée Extrait/Index)
  - `SRC-005` (*Procedural Cyberpunk City with Unreal*, SideFX, 2021 — Consultée Extrait/Index)
  - `SRC-012` (*Level Design Workshop: Blockmesh and Lighting Tips*, Shaver & Yang, GDC 2018 — Consultée Extrait/Index)
  - `SRC-019` (*World Building Guide*, Epic Games, 2025 — Consultée Extrait/Index)
  - `SRC-021` (*Kinshasa: Tales of the Invisible City*, De Boeck & Plissart, 2014 — Métadonnées Vérifiées via Recherche Web, texte intégral non consulté)
  - `SRC-023` (*An Architectural Approach to Level Design*, Totten, 2019 — Référence Bibliographique, texte intégral non consulté en session)
  - `SRC-035` (*SideFX Houdini Documentation — Copernicus & APEX*, SideFX, 2026 — Vérifiée via Recherche Web)
  - *Complétées par des recommandations d'ingénierie internes (`Engineering Recommendation` — `PROPOSED`) pour le paramétrage compensatoire des cotes UE 5.8.*
- **Auditeurs Requis (Validation Croisée)** : `WLD-04` *(non instancié dans la tranche de 13 skills selon `ARB-P6-005` — revue absorbée par `WLD-05` et `DIR-07`)*, `ENG-04`, `AI-03`.

### Checklist d'Auto-Validation DoD (`WLD-03`)
- [x] Toutes les cotes routières, d'ouvrages et parcellaires sont exprimées en centimètres UE5 (`1 UU = 1 cm`).
- [x] Chaque sous-typologie d'îlot (`BLK-KINSUKA-QUARRY-01` à `04`) définit le nombre d'étages min/max, le retrait de façade et la densité de câblage/végétation.
- [x] Compatibilité géométrique validée pour le générateur procédural `ENG-04` (bande RVT `200 cm`, grille `12800 cm`, fallback parcellaire `1500 × 2500 cm`) et le graphe routier `AI-03` (voies `350/400 cm`, inter-file Wewa `150 cm >= 130 cm`, tirant d'air passerelle `480 cm > 330 cm`).
- [x] Respect strict du Scope Guard : aucun code VEX/HDA Houdini, aucun mesh 3D/shader, aucun tuning physique véhicule, aucun identifiant fantôme hors registre.

---

## 4. Paquet de Passation Aval (Handoff Section) & Anomalies Signalées

### 4.1 Directives Ciblées par Consommateur Aval (Vagues 3 à 6)
1. **Vers `GD-02` (`TSK-P6-003` — Vague 3, `03-gd02-msn-main-009-kinsuka-convoy.md`)** :
   - Exploiter la topologie à **3 niveaux d'approche** autour du point d'immobilisation de `VEH-CONVOY-DIPLO-01` (`PROPOSED`) en amont de `AXE-KINSUKA-PCR-BAY-02` : (a) **Surplomb vertical** depuis `AXE-KINSUKA-OVERPASS-PED-04` (`+480 cm` au-dessus de la chaussée, corridor foule `400 cm`), (b) **Flanc minéral aval** via les 3 gradins de `280 cm` des carrières `BLK-KINSUKA-QUARRY-01` contrôlées par `CHR-ALLY-MAMA-LUZOLO` (`PROPOSED`) et `ORG-SYNDICAT-CARRIERES-KINSUKA` (`PROPOSED`), et (c) **Infiltration au ras de l'asphalte** dans le couloir inter-file de `150 cm` entre `VEH-BUS-TRANSCO-01` et les taxis.
   - Implanter toute confrontation mêlée éventuelle (`SYS-CMB-MELEE`, `>= 500 cm` requis) exclusivement dans les cours de concassage (`1600 × 2400 cm`), l'esplanade arrière du poste PCR (`600 × 800 cm`) ou les paliers majeurs de la passerelle (`600 × 600 cm`), et maintenir le plafond strict `<= 24` PNJ `AI-01`.
2. **Vers `WLD-05` (`TSK-P6-005` — Vague 4, `05-wld05-kinsuka-crossing-blockout.md`)** :
   - Construire le blockout gris (`SRC-012`) sur l'emprise de `2 × 2` cellules `World Partition` (`25600 × 25600 cm`) en respectant les paliers `T0` (`0..+400 cm`), `T1` (`+400..+1240 cm` par sauts de `280 cm`), `T2` (`+1240..+2200 cm`) et `T3` (`+2080..+2880 cm`).
   - Garantir le tirant d'air de **`480 cm`** sous la passerelle `AXE-KINSUKA-OVERPASS-PED-04`, les gardes-corps/étals bas à **`100 cm`** (`[90, 110] cm`), les piliers porteurs `>= 200 cm × 80 cm`, les marches d'escalier `<= 20 cm × >= 30 cm` (`<= 38°`), et les Data Layers `DL_Kinsuka_Base_Urban`, `DL_Kinsuka_Market_Day` et `DL_MSN_MAIN_009_Convoy` (`PROPOSED`).
   - Conserver `RR-KINSUKA-DEM-002` en `RESEARCH_REQUIRED` pour tout calage altimétrique absolu futur.
3. **Vers `ENG-04` (`TSK-P6-008` — Vague 5, `08-eng04-kinsuka-houdini-zonegraph-pipeline.md`)** :
   - Consommer le bloc CSV intégré en Section 2.3 pour générer procéduralement les splines routières et les parcelles de repli `1500 × 2500 cm` (tant que `RR-KINSUKA-OSM-001` et `RR-KINSUKA-DEM-002` demeurent `RESEARCH_REQUIRED`).
   - Générer systématiquement la **bande de transition de `200 cm` avec caniveau ouvert** (FMEA #3) aux jonctions entre `AXE-KINSUKA-ARTERIAL-01` (asphalte) et `AXE-KINSUKA-QUARRY-LAT-03` / `SPUR-05` (latérite) pour piloter les masques RVT Copernicus (`SRC-035`), et mapper les 4 sous-typologies d'îlots sur les presets canoniques `TYP-INDUS-PORT`, `TYP-MATONGE-COMM` et `TYP-KALAMU-RES` afin d'éviter toute rupture de switch HDA (`NOT TESTED`).
4. **Vers `AI-03` (`TSK-P6-009` — Vague 6, `09-ai03-kinsuka-traffic-zonegraph-spec.md`)** :
   - Taguer `AXE-KINSUKA-ARTERIAL-01` en voies lourdes `400 cm` avec spline virtuelle inter-file `VEH-MOTO-WEWA-01` de **`150 cm`** (`>= 130 cm` min), taguer `AXE-KINSUKA-PCR-BAY-02` (`400 × 2400 cm`) comme voie de délestage/inspection `ORG-POLICE-PCR`, interdire `VEH-BUS-TRANSCO-01` sur `AXE-KINSUKA-QUARRY-LAT-03` (`2 × 350 cm` latérite, FMEA #2) et filtrer `AXE-KINSUKA-QUARRY-SPUR-05` en exclusivité `VEH-MOTO-WEWA-01` (plots espacés de `150 cm`).

### 4.2 Contradictions, Ambiguïtés & Points d'Arbitrage Signalés à l'Orchestrateur (`DIR-01` / `DIR-07`)
1. **`AMB-WLD03-001` (Écart de Nommage Template dans `00-dir01-execution-plan.json`)** : L'enveloppe JSON `TSK-P6-002` mentionne `"required_output_template": "urban-architecture-spec-template.md"`, tandis que le référentiel canonique de `skills/02-world-design/wld-03-urban-researcher/templates/` se nomme `urban-typology-spec.md` et que `SKILL.md` prévoit également une sortie `road-network-hierarchy.csv`. **Résolution appliquée** : Stricte conformité à `templates/urban-typology-spec.md` et intégration directe du jeu de données `road-network-hierarchy.csv` en Section 2.3 du fichier unique `02-wld03-kinsuka-urban-architecture-spec.md` attendu par le DAG.
2. **`AMB-WLD03-002` (Couverture des 4 Codes Typologiques Canoniques face au Relief de `DST-NGALIEMA`)** : `WLD-03` SOP #1 ne liste que 4 archétypes historiques de plaine/port (`TYP-GOMBE-GRID`, `TYP-MATONGE-COMM`, `TYP-KALAMU-RES`, `TYP-INDUS-PORT`), alors que `kinshasa-districts.md` définit `DST-NGALIEMA` par sa topographie vallonnée de pentes latérite et de rapides (et omet sa fiche en Section 2, cf. `ARB-P6-002`). **Résolution appliquée** : Décomposition en 4 sous-îlots rattachés chacun à un code canonique existant pour la rétrocompatibilité `ENG-04`, assortie d'une proposition d'extension `TYP-NGALIEMA-HILLSIDE-HYBRID` (`PROPOSED`) pour mise à jour ultérieure par `WLD-01` / `DIR-06`.
3. **`AMB-WLD03-003` (Complétude Véhicules & Enveloppe `VEH-CONVOY-DIPLO-01` entre Vague 2 et Vagues 3–6)** : Le champ `context_entities` de `TSK-P6-002` dans le JSON n'énumérait explicitement que `VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01` et `VEH-BUS-TRANSCO-01`, alors que le scénario maître (`00-dir01-orchestration-brief.md`) et les tâches aval (`GD-02`, `AI-03`) exigent l'insertion géométrique de l'encoche `ORG-POLICE-PCR` (`VEH-POLICE-PICKUP-01`, `CONFIRMED`) et du convoi `VEH-CONVOY-DIPLO-01` (`PROPOSED`) dans les voies de `350–400 cm`. **Résolution appliquée** : Intégration des gabarits routiers d'accueil (`<= 520 × 215 × 205 cm` max sur voie de `400 cm`) sans empiéter sur le Scope Guard de `GD-06` (zéro tuning Chaos Vehicle).
