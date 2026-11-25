# Règles d'Urbanisme Ludique & Pacing Open World (`WLD-04`)

## 1. Grille UE5 World Partition & Streaming
- **Taille de Cellule Standard** : `12800 cm × 12800 cm` (`128 m × 128 m`).
- **Distance Minimale Inter-Missions Majeures** : `>= 256 m` (2 cellules complètes) pour permettre le déchargement complet (`Data Layers`) de l'arène précédente lors d'une fuite en `VEH-MOTO-WEWA-01`.

## 2. Hiérarchie des Landmarks (`SYS-WLD-LANDMARKS`)
- **Tier 1 (Macro-Repères Régionaux, visibles à > 1.5 km via HLOD)** : `LOC-LIMETE-ECHANGEUR` (Tour de 210 m à l'Est), Fleuve Congo & Grues de `LOC-GOMBE-PORT` (Nord), Skyline des tours de `DST-GOMBE`.
- **Tier 2 (Repères de Commune, visibles à 300-600 m)** : `LOC-MATONGE-VICTOIRE`, château d'eau, antenne émettrice de `ORG-RADIO-KIN`.
- **Tier 3 (Micro-Repères de Rue, < 100 m)** : Fresques murales, enseignes lumineuses de ngandas, arbres remarquables.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-04` — Strate DAG 1)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-01`, `WLD-03`, `GD-01`, `DIR-04`, `DIR-05`
- **Audit des Entrées (`inputs`)** :
  - `world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `urban-typology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `streaming-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `poi-specification.md` : Doit respecter le gabarit `templates/poi-specification-template.md` et passer l'audit croisé.
  - `world-pacing-matrix.csv` : Doit respecter le gabarit `templates/poi-specification-template.md` et passer l'audit croisé.
  - `landmark-sightlines-map.md` : Doit respecter le gabarit `templates/poi-specification-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `ENG-01`, `WLD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Deux POI lourds ( > 20 PNJ AI-01 actifs) placés à moins de 150 mètres l'un de l'autre | Blocage / Dégradation si ignoré | Espacer les POI d'au moins 250 mètres (2 cellules World Partition de 128m) ou placer une barrière d'occlusion visuelle (bâtiment coudé) | Escalade vers Prévenir tout pic simultané sur le Game Thread et le streaming |
| Mode de Défaillance 2: Quartier où le joueur perd ses repères cardinaux sans ouvrir la carte UI | Blocage / Dégradation si ignoré | Ouvrir un cône de visibilité (sightline) sur l'axe routier vers le landmark majeur de la commune | Escalade vers Garantir la navigation diégétique SYS-WLD-LANDMARKS |
| Mode de Défaillance 3: POI situé dans une commune au statut RESEARCH_REQUIRED | Blocage / Dégradation si ignoré | Marquer le POI au statut RESEARCH_REQUIRED ou PROPOSED [CONCEPT] | Escalade vers Attendre la validation WLD-03 avant blockout WLD-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-04`)

- [ ] **Contrôle DoD #1** : Chaque `LOC-*` possède un ID valide, des coordonnées de cellule World Partition et une fonction claire dans les Core Loops.
- [ ] **Contrôle DoD #2** : Aucun chevauchement de rayon d'activation IA critique (`AI-01`) entre deux POI adjacents.
- [ ] **Contrôle DoD #3** : Orientation cardinale possible sans mini-carte grâce aux lignes de mire documentées.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
