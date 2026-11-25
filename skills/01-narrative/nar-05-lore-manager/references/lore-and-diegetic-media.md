# Architecture du Lore & Médias Diégétiques (`NAR-05`)

## 1. Factions & Organisations Clés (`ORG-*`)
- `ORG-CARTEL-FLEUVE` (**Syndicat du Fleuve**) : Consortium paramilitaire et logistique contrôlé par `CHR-ANTAG-MUKENDI` à `DST-GOMBE` (`LOC-GOMBE-PORT`).
- `ORG-TRANSCO` (**Réseau de Transport Urbain**) : Opérateur des grands bus structurant les axes routiers majeurs (`VEH-BUS-TRANSCO-01`).
- `ORG-RADIO-KIN` (**Radio Lokole 104.5 FM**) : Voix culturelle et citoyenne émettant depuis `DST-MATONGE`, animée par `CHR-ALLY-AMINA`.

## 2. Catégories de Médias Diégétiques
1. **Bulletins Radio Réactifs (`AUD-03`)** : Flashs de 15 à 25 secondes diffusés entre deux morceaux de rumba après chaque mission.
2. **Signalétique & Enseignes Peintes (`WLD-06`/`ART-02`)** : Textes d'ateliers mécaniques, salons de coiffure, ngandas et consignes portuaires.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-05` — Strate DAG 2)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-01`, `WLD-02`, `NAR-01`
- **Audit des Entrées (`inputs`)** :
  - `kinshasa-world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-research-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `narrative-architecture-nar-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `organization-dossier.md` : Doit respecter le gabarit `templates/organization-dossier-template.md` et passer l'audit croisé.
  - `diegetic-media-pack.md` : Doit respecter le gabarit `templates/organization-dossier-template.md` et passer l'audit croisé.
  - `master-timeline.csv` : Doit respecter le gabarit `templates/organization-dossier-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `WLD-02`, `NAR-06`, `PRD-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Besoin d'une référence à une institution réelle de Kinshasa | Blocage / Dégradation si ignoré | Utiliser un équivalent fictionnel respectueux ou le statut RESEARCH_REQUIRED pour validation juridique PRD-02 et culturelle WLD-02 | Escalade vers Éviter tout risque de diffamation ou d'inexactitude |
| Mode de Défaillance 2: Mission principale terminée par le joueur | Blocage / Dégradation si ignoré | Générer systématiquement 2 variantes de bulletin radio (ORG-RADIO-KIN) correspondant aux 2 approches possibles du joueur | Escalade vers Renforcer la réactivité du monde ouvert |
| Mode de Défaillance 3: Texte d'enseigne urbaine destiné aux textures 3D (ART-02) | Blocage / Dégradation si ignoré | Fournir le texte exact avec vérification orthographique française/lingala Unicode | Escalade vers Empêcher toute faute de frappe gravée dans les textures PBR |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-05`)

- [ ] **Contrôle DoD #1** : Chaque dossier `ORG-*` est relié à au moins un quartier `DST-*` et un personnage `CHR-*`.
- [ ] **Contrôle DoD #2** : La chronologie ne comporte aucun chevauchement ou paradoxe temporel.
- [ ] **Contrôle DoD #3** : Les textes diégétiques respectent la charte linguistique (`cultural-guidelines.md`).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
