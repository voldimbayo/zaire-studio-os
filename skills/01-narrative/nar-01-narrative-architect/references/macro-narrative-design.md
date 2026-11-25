# Architecture Narrative Interactive en Monde Ouvert (`NAR-01`)

## 1. Structure en 3 Actes de ZAÏRE
- **Acte I — Les Courants du Fleuve (`DST-KALAMU` & `DST-GOMBE`)** : Koffi Kabongo (`CHR-PROTAG-KOFFI`) découvre la mainmise du Syndicat du Fleuve (`ORG-CARTEL-FLEUVE`, dirigé par `CHR-ANTAG-MUKENDI`) sur les docks d'ONATRA (`LOC-GOMBE-PORT`).
- **Acte II — La Fréquence de Matonge (`DST-MATONGE` & `DST-LIMETE`)** : Alliance avec Amina Nzuzi (`CHR-ALLY-AMINA`) et `ORG-RADIO-KIN` pour fédérer les coursiers Wewa et les artisans face au blocus logistique autour de `LOC-LIMETE-ECHANGEUR`.
- **Acte III — L'Orage Équatorial (`DST-GOMBE` & `DST-NGALIEMA`)** : Confrontation finale entre les réseaux citoyens et la dynastie `FAM-MUKENDI` lors de la grande crue de la saison des pluies.

## 2. Règle de Convergence "Diamond Pattern"
Les choix du joueur dans l'Acte II altèrent l'allié dominant et le niveau d'alerte de `DST-GOMBE` en Acte III sans dupliquer les 100 % de la carte ouverte.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-01` — Strate DAG 1)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `WLD-01`, `WLD-02`
- **Audit des Entrées (`inputs`)** :
  - `creative-pillars-dir-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `kinshasa-world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-briefs-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `narrative-architecture.md` : Doit respecter le gabarit `templates/act-structure-template.md` et passer l'audit croisé.
  - `branching-consequences-matrix.csv` : Doit respecter le gabarit `templates/act-structure-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `NAR-06`, `DIR-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Embranchement créant une divergence exponentielle ingérable en production | Blocage / Dégradation si ignoré | Appliquer le modèle 'Diamond Branching' (divergence locale forte sur le quartier, reconvergence sur les jalons d'actes avec mémoire d'état persistante) | Escalade vers Faire valider le coût de production par DIR-02 |
| Mode de Défaillance 2: Arc narratif déconnecté de l'environnement urbain de Kinshasa | Blocage / Dégradation si ignoré | Rattacher obligatoirement le conflit à une institution ou réalité locale (port ONATRA, transport, coupures réseau, scène musicale) | Escalade vers Consulter WLD-01 et WLD-02 |
| Mode de Défaillance 3: Mort potentielle d'un personnage clé avant sa dernière mission critique | Blocage / Dégradation si ignoré | Interdire la létalité hors noeud canonique ou prévoir un remplaçant systémique documenté | Escalade vers Soumettre le graphe d'état à NAR-06 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-01`)

- [ ] **Contrôle DoD #1** : Chaque acte définit son conflit central, ses communes (`DST-*`), ses factions (`ORG-*`) et son évolution du protagoniste (`CHR-PROTAG-KOFFI`).
- [ ] **Contrôle DoD #2** : 100 % des embranchements majeurs produisent un impact mesurable sur `SYS-WLD-REPUTATION` ou sur les Data Layers du quartier.
- [ ] **Contrôle DoD #3** : Aucune contradiction avec les 3 piliers créatifs de `DIR-03`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
