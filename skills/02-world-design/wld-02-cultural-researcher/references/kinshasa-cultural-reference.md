# Référentiel Socio-Culturel & Linguistique de Kinshasa (`WLD-02`)

## 1. Phonologie & Orthographe Unicode du Lingala Kinois
Le système vocalique du lingala distingue 7 voyelles : `a, e, ɛ, i, o, ɔ, u`.
- `ɛ` (U+025B — *e ouvert*, comme dans *Kɛbá!*, *Tɔ́kɛndɛ́*).
- `ɔ` (U+0254 — *o ouvert*, comme dans *Tɔ́kɛndɛ́*, *Bilɔkɔ*).
Toute chaîne destinée à l'interface UE5 (`GD-07`) ou aux sous-titres (`AUD-04`) doit préserver ces points de code UTF-8.

## 2. Repères Sociologiques Contemporains
- **Mobilité Urbaine** : Coexistence des grands bus (`ORG-TRANSCO`), des taxis collectifs jaunes (*Ketchs*, `VEH-TAXI-JAUNE-01`) et des motos-taxis (*Wewa*, `VEH-MOTO-WEWA-01`).
- **Sociabilité** : Les *ngandas* (`LEX-011`) de Matonge et Kalamu servent de carrefours d'information, de débat et de diffusion musicale.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-02` — Strate DAG 1)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`
- **Audit des Entrées (`inputs`)** :
  - `research-requests` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/world-bible/cultural-guidelines.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/world-bible/lingala-french-glossary.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `cultural-research-brief.md` : Doit respecter le gabarit `templates/cultural-brief-template.md` et passer l'audit croisé.
  - `glossary-expansion-entries.csv` : Doit respecter le gabarit `templates/cultural-brief-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `PRD-03`, `DIR-03`, `DIR-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Terme argotique ou culturel d'origine incertaine ou non attesté à Kinshasa | Blocage / Dégradation si ignoré | Rejeter le terme et proposer une alternative attestée de lingala kinois ou marquer RESEARCH_REQUIRED | Escalade vers Protéger l'authenticité culturelle du jeu |
| Mode de Défaillance 2: Texte en lingala soumis avec des caractères ASCII dégradés ('e'/'o' au lieu de 'ɛ'/'ɔ') | Blocage / Dégradation si ignoré | Corriger systématiquement la graphie Unicode et mettre à jour lingala-french-glossary.csv | Escalade vers Synchroniser avec AUD-04 et GD-07 |
| Mode de Défaillance 3: Représentation vestimentaire ou architecturale caricaturale | Blocage / Dégradation si ignoré | Émettre une directive corrective immédiate appuyée sur la réalité urbaine contemporaine de Kinshasa | Escalade vers Escalader à DIR-03 en cas de blocage |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-02`)

- [ ] **Contrôle DoD #1** : 100 % des termes lingala fournis incluent la graphie Unicode (`ɛ`, `ɔ`), la phonétique et le contexte d'usage.
- [ ] **Contrôle DoD #2** : Les sources documentaires sont citées et exemptes de tout stéréotype 'Afrique générique'.
- [ ] **Contrôle DoD #3** : Le brief culturel est directement exploitable par `NAR-02`, `NAR-04`, `ART-02`, `ART-03` et `AUD-03`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
