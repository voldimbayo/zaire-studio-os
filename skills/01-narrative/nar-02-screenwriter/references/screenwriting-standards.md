# Standards Scénaristiques & Cinématiques Temps Réel (`NAR-02`)

## 1. Règles de Rythme (Pacing AAA)
- **Durée maximale d'une Cutscene UE5 Sequencer** : `90 secondes` (au-delà, basculer en dialogue interactif `NAR-04` ou en phase jouable).
- **Continuité Caméra (Méthode Naughty Dog `SRC-011`)** : Les transitions entre gameplay et cinématique s'effectuent en plan-séquence sans fondu au noir, en conservant le même rig d'éclairage Lumen.
- **Usage du Code-Switching** : Le lingala intervient naturellement sur les salutations (`Mbote`), les exclamations d'urgence (`Kɛbá!`, `Tɔ́kɛndɛ́`) et les termes culturels (`Libongo`, `Wewa`, `Mosolo`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-02` — Strate DAG 2)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-01`, `NAR-03`, `GD-02`
- **Audit des Entrées (`inputs`)** :
  - `narrative-architecture-nar-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `character-bibles-nar-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `mission-design-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `mission-script.md` : Doit respecter le gabarit `templates/mission-script-template.md` et passer l'audit croisé.
  - `cinematic-beatsheet.md` : Doit respecter le gabarit `templates/mission-script-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `NAR-03`, `WLD-02`, `NAR-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Cinématique passive dépassant 90 secondes consécutives | Blocage / Dégradation si ignoré | Convertir la moitié de l'exposition en séquence jouable (Walk-and-Talk dans le port ou dialogue en moto Wewa) | Escalade vers Synchroniser avec GD-02 et WLD-05 |
| Mode de Défaillance 2: Besoin d'une expression en lingala non présente dans lingala-french-glossary.csv | Blocage / Dégradation si ignoré | Baliser la réplique avec [RESEARCH_REQUIRED: WLD-02] au lieu d'inventer une traduction approximative | Escalade vers Soumettre la demande lexicale à WLD-02 |
| Mode de Défaillance 3: Action dramatique exigeant une animation unique non standard | Blocage / Dégradation si ignoré | Annoter le beat avec [MOCAP_REQ: ART-06] pour inclusion dans la shotlist Motion Capture | Escalade vers Vérifier le budget d'animation avec ART-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-02`)

- [ ] **Contrôle DoD #1** : Le script respecte scrupuleusement les identifiants `CHR-*`, `LOC-*` et `MSN-*` du registre.
- [ ] **Contrôle DoD #2** : Chaque scène indique l'heure, la météo (`ART-07`), l'ambiance sonore (`AUD-02`) et le minutage estimé.
- [ ] **Contrôle DoD #3** : Le principe 'Show, Don't Tell' est appliqué : l'action visuelle à Kinshasa prime sur les monologues explicatifs.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
