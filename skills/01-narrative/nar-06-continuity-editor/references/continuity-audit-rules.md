# Protocole d'Audit de Continuité & Anti-Paradoxe (`NAR-06`)

## 1. Les 4 Axes de Vérification Canonique
1. **Intégrité d'Entité** : Tout `CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*` cité existe dans `knowledge/entities-registry.csv` et n'est ni `DEPRECATED` ni `BLOCKED`.
2. **Cohérence d'État (State Continuity)** : Vérification des préconditions de quête (ex: `CHR-ALLY-AMINA` ne peut pas guider Koffi par radio si l'émetteur de `ORG-RADIO-KIN` est en panne dans la quête courante).
3. **Cohérence Spatiale & Temps de Trajet** : Un personnage ne peut pas se téléporter instantanément de `LOC-GOMBE-PORT` à `LOC-LIMETE-ECHANGEUR` au sein de la même scène.
4. **Cohérence Linguistique** : Respect des glyphes Unicode (`ɛ`, `ɔ`) et de la voix définie par `NAR-03`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-06` — Strate DAG 5)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-01`, `NAR-02`, `NAR-03`, `NAR-04`, `NAR-05`, `GD-02`
- **Audit des Entrées (`inputs`)** :
  - `all-narrative-deliverables-nar-01-to-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `mission-state-machines-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/entities-registry.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `continuity-audit-report.md` : Doit respecter le gabarit `templates/continuity-checklist.md` et passer l'audit croisé.
  - `narrative-conflict-tickets.csv` : Doit respecter le gabarit `templates/continuity-checklist.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-06`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Quête secondaire accessible alors que son donneur CHR-* est indisponible dans l'Acte courant | Blocage / Dégradation si ignoré | Émettre un verdict CONTINUITY_BLOCKED et exiger de GD-02 l'ajout d'une précondition Gameplay Tag sur la machine à états | Escalade vers Empêcher tout paradoxe narratif en monde ouvert |
| Mode de Défaillance 2: Contradiction biographique ou territoriale entre deux fiches (ex: QG d'une faction situé dans deux communes différentes) | Blocage / Dégradation si ignoré | Bloquer la promotion et renvoyer les deux fiches à NAR-03/NAR-05 pour alignement sur entities-registry.csv | Escalade vers Noter le conflit dans narrative-conflict-tickets.csv |
| Mode de Défaillance 3: Usage d'un terme lingala altéré sans ses caractères Unicode (ex: 'Tokende' au lieu de 'Tɔ́kɛndɛ́') | Blocage / Dégradation si ignoré | Demander la normalisation orthographique immédiate selon lingala-french-glossary.csv | Escalade vers Garantir la qualité LQA avec AUD-04 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-06`)

- [ ] **Contrôle DoD #1** : 0 contradiction d'état de personnage, de lieu ou de chronologie sur l'ensemble du graphe de quêtes audité.
- [ ] **Contrôle DoD #2** : 100 % des IDs référencés dans les scripts et dialogues existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle DoD #3** : Conformité orthographique totale avec `knowledge/world-bible/lingala-french-glossary.csv`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
