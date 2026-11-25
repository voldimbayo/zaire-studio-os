# Architecture UE5 State Trees, EQS & Perception (`AI-01`)

## 1. Budget & Plafonds d'Exécution (`PERF-CPU-NPCAI`)
- **Enveloppe CPU Max** : `2.5 ms` sur Game Thread / Worker Threads (`<= 24` acteurs `ACharacter` actifs).
- **Fréquence de Tick Perception** : `10 Hz` (`0.1 s`) pour les ennemis à `< 20 m` ; `4 Hz` (`0.25 s`) entre `20 m` et `60 m`.
- **Budget EQS** : Time-slicing réglé à `0.35 ms/frame` max pour l'évaluation des points de couverture.

## 2. Modulation Sensorielle par Gameplay Tags
| Gameplay Tag Actif | Multiplicateur Cône Visuel | Multiplicateur Rayon Auditif | Comportement Garde |
| :--- | :--- | :--- | :--- |
| `State.Character.Stealth.Concealed` | `0.25x` | `1.00x` | Ignore le joueur sauf à distance `< 300 cm` en plein axe. |
| `State.Character.Stealth.Disguised` | `0.15x` (zone autorisée) | `1.00x` | Salue ou contrôle verbalement (`BRK-PORT-01`) sans alerte immédiate. |
| `World.Weather.TropicalStorm` | `0.70x` (pluie dense) | `0.60x` (masquage pluie) | Cherche un abri Smart Object sous les auvents si non alerté. |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AI-01` — Strate DAG 3)

- **Architecture IA Hybride : State Trees, MassEntity & ZoneGraph (UE 5.8)** (`SRC-004`, `SRC-013`, `SRC-015`, `SRC-020`, `SRC-032`) :
  - **IA Individuelle (`AI-01`, Budget `<= 2.5 ms`)** : Plafond strict de `24 acteurs ACharacter` actifs simultanément ; `State Trees` UE 5.8 + time-slicing EQS (`<= 0.35 ms/frame`).
  - **Foule ECS (`AI-02`, Budget `<= 2.0 ms` pour `500-800 entités`)** : Anneau 0 (`0-25 m`, `<= 18` acteurs hydratés), Anneau 1 (`25-80 m`, Skeletal Mesh URO 30Hz + RVO), Anneau 2 (`80-250 m`, ISM animé par Vertex Animation Texture VAT).
  - **Trafic & Escalade Policière PCR (`AI-03`, `AI-04`)** : Réseau `ZoneGraph` généré en amont par `ENG-04` ; sous-voies virtuelles inter-files (`130-150 cm`) pour `VEH-MOTO-WEWA-01` lorsque le flux descend sous `20 km/h` ; Watchdog Anti-Deadlock (`8.0 s`) ; escalade graduée `SYS-LAW-ESCALATION` (`State.Law.AlertLevel.1..3`) avec `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-05`, `WLD-05`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `combat-archetypes-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `level-blockouts-wld-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `npc-ai-architecture.md` : Doit respecter le gabarit `templates/npc-ai-architecture.md` et passer l'audit croisé.
  - `eqs-and-statetree-spec.md` : Doit respecter le gabarit `templates/npc-ai-architecture.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-07`, `GD-05`, `WLD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Mission demandant plus de 24 PNJ actifs dans la même zone | Blocage / Dégradation si ignoré | Conserver au maximum 24 acteurs AI-01 et transférer tous les figurants/travailleurs vers AI-02 Mass Crowd avec hydratation à la demande | Escalade vers Respecter le plafond absolu PERF-CPU-NPCAI <= 2.5 ms |
| Mode de Défaillance 2: Requête EQS provoquant un pic > 0.5 ms sur le Game Thread | Blocage / Dégradation si ignoré | Réduire la densité de la grille de points EQS (espacement 150 cm au lieu de 50 cm) et activer le tri préalable par distance avant les raycasts de visibilité | Escalade vers Garantir la fluidité 60 FPS |
| Mode de Défaillance 3: PNJ bloqué devant un obstacle dynamique ou un véhicule garé de travers | Blocage / Dégradation si ignoré | Activer un NavModifier dynamique autour des véhicules à l'arrêt et un fallback de contournement Smart Link (escalade couvert 100 cm) | Escalade vers Éliminer tout blocage NavMesh |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AI-01`)

- [ ] **Contrôle DoD #1** : Le coût CPU cumulé des 24 acteurs `AI-01` est `<= 2.5 ms` (60 FPS) / `<= 3.0 ms` (30 FPS).
- [ ] **Contrôle DoD #2** : Le système d'Attack Tokens empêche formellement plus de 2 assauts de mêlée simultanés.
- [ ] **Contrôle DoD #3** : Les seuils de détection visuelle et auditive s'adaptent aux Gameplay Tags de météo et de déguisement.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
