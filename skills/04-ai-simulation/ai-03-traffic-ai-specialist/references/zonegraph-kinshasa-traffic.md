# Simulation de Trafic Urbain sous UE5 ZoneGraph & MassTraffic (`AI-03`)

## 1. Comportements Spécifiques Kinois Modélisés
1. **Slalom Inter-File (`VEH-MOTO-WEWA-01`)** : Sous-voies virtuelles générées entre les voies principales de `350-400 cm`, offrant un couloir libre de `130-150 cm`.
2. **Arrêts Collectifs (`VEH-TAXI-JAUNE-01`)** : Déboîtement sur la bande d'arrêt latérale (`220 cm`) près des marchés pendant `6 à 12 secondes` pour déposer des passants `AI-02`.
3. **Priorité Anneau Circulaire (`LOC-MATONGE-VICTOIRE`)** : Priorité accordée aux véhicules engagés sur l'anneau intérieur pour évacuer le carrefour, avec cessions de passage dynamiques aux bus `VEH-BUS-TRANSCO-01`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AI-03` — Strate DAG 3)

- **Architecture IA Hybride : State Trees, MassEntity & ZoneGraph (UE 5.8)** (`SRC-004`, `SRC-013`, `SRC-015`, `SRC-020`, `SRC-032`) :
  - **IA Individuelle (`AI-01`, Budget `<= 2.5 ms`)** : Plafond strict de `24 acteurs ACharacter` actifs simultanément ; `State Trees` UE 5.8 + time-slicing EQS (`<= 0.35 ms/frame`).
  - **Foule ECS (`AI-02`, Budget `<= 2.0 ms` pour `500-800 entités`)** : Anneau 0 (`0-25 m`, `<= 18` acteurs hydratés), Anneau 1 (`25-80 m`, Skeletal Mesh URO 30Hz + RVO), Anneau 2 (`80-250 m`, ISM animé par Vertex Animation Texture VAT).
  - **Trafic & Escalade Policière PCR (`AI-03`, `AI-04`)** : Réseau `ZoneGraph` généré en amont par `ENG-04` ; sous-voies virtuelles inter-files (`130-150 cm`) pour `VEH-MOTO-WEWA-01` lorsque le flux descend sous `20 km/h` ; Watchdog Anti-Deadlock (`8.0 s`) ; escalade graduée `SYS-LAW-ESCALATION` (`State.Law.AlertLevel.1..3`) avec `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ENG-04`, `GD-06`, `WLD-03`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `urban-road-specs-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `vehicle-profiles-gd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `houdini-zonegraph-splines-eng-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `traffic-rules-specification.md` : Doit respecter le gabarit `templates/traffic-rules-spec.md` et passer l'audit croisé.
  - `intersection-priority-matrix.csv` : Doit respecter le gabarit `templates/traffic-rules-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `PRD-05`, `ENG-07`, `GD-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Collision ou proximité immédiate (< 15 m) entre le joueur et un véhicule MassTraffic | Blocage / Dégradation si ignoré | Promouvoir instantanément l'entité MassTraffic de sa spline cinématique vers un acteur Chaos Vehicle physique complet (ENG-05) | Escalade vers Garantir des réactions de choc et d'évitement réalistes |
| Mode de Défaillance 2: Saturation d'un rond-point (ex: LOC-MATONGE-VICTOIRE) menaçant de bloquer une mission de course Wewa | Blocage / Dégradation si ignoré | Déclencher le protocole Anti-Deadlock après 8s d'immobilisation et maintenir en permanence un couloir inter-file de 150 cm franchissable à moto | Escalade vers Éviter tout soft-lock routier sur MSN-SIDE-014-WEWA |
| Mode de Défaillance 3: Dépassement du budget CPU combiné Mass Crowd + Mass Traffic (> 2.0 ms) | Blocage / Dégradation si ignoré | Réduire le plafond de véhicules simulés de 120 à 85 en privilégiant la densité dans le cône de vision avant du joueur | Escalade vers Respecter PERF-CPU-MASS |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AI-03`)

- [ ] **Contrôle DoD #1** : Le trafic soutient un test d'endurance de 2 heures (`PRD-05`) sur `LOC-MATONGE-VICTOIRE` et `LOC-GOMBE-BD30JUIN` avec 0 deadlock permanent.
- [ ] **Contrôle DoD #2** : Les motos IA `VEH-MOTO-WEWA-01` utilisent les couloirs inter-files `>= 130 cm` sans collision fantôme.
- [ ] **Contrôle DoD #3** : Aucune apparition ou disparition (pop-in/out) de véhicule n'est visible dans le frustum caméra du joueur.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
