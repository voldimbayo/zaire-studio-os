# Méthodologie de Conception des Personnages Kinois (`NAR-03`)

## 1. Grille Socio-Linguistique de Kinshasa
- **Profil Élite Technocratique / Sécuritaire (`DST-GOMBE`, ex: `CHR-ANTAG-MUKENDI`)** : Syntaxe française froide, chirurgicale, usage rare mais tranchant du lingala d'autorité pour intimider.
- **Profil Artiste / Média Urbain (`DST-MATONGE`, ex: `CHR-ALLY-AMINA`)** : Débit vif, métaphores empruntées à la rumba et à la radio (`ORG-RADIO-KIN`), code-switching fluide et chaleureux.
- **Profil Artisan / Coursier de Terrain (`DST-KALAMU`, ex: `CHR-PROTAG-KOFFI`)** : Pragmatique, économe en mots sous pression, maîtrise des codes du port (`Libongo`) comme de la rue (`Wewa`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-03` — Strate DAG 2)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-01`, `WLD-01`, `WLD-02`
- **Audit des Entrées (`inputs`)** :
  - `narrative-architecture-nar-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `kinshasa-world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-guidelines-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `character-bible-sheet.md` : Doit respecter le gabarit `templates/character-bible-template.md` et passer l'audit croisé.
  - `family-lineage-dossier.md` : Doit respecter le gabarit `templates/character-bible-template.md` et passer l'audit croisé.
  - `character-relationship-matrix.csv` : Doit respecter le gabarit `templates/character-bible-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `WLD-02`, `NAR-06`, `DIR-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Deux personnages majeurs partagent le même registre de langue et la même posture morale | Blocage / Dégradation si ignoré | Différencier immédiatement leur sociolecte (ex: français technocratique de la Gombe vs phrasé imagé et musical de Matonge) | Escalade vers Valider l'authenticité sociolinguistique avec WLD-02 |
| Mode de Défaillance 2: Personnage créé sans lien avec le tissu social ou familial de Kinshasa | Blocage / Dégradation si ignoré | Rattacher le personnage à une famille (FAM-*), une faction (ORG-*) ou un lieu de vie (LOC-*) | Escalade vers Interdire les archétypes génériques apatrides |
| Mode de Défaillance 3: Incohérence de ton détectée dans un script NAR-02 | Blocage / Dégradation si ignoré | Émettre une demande de réécriture ciblée des répliques hors-caractère | Escalade vers Consigner l'observation pour NAR-06 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-03`)

- [ ] **Contrôle DoD #1** : Chaque fiche `CHR-*` comporte une voix reconnaissable à l'aveugle sans lire le nom du locuteur.
- [ ] **Contrôle DoD #2** : Les relations avec les autres `CHR-*`, `FAM-*` et `ORG-*` sont bidirectionnelles et explicites.
- [ ] **Contrôle DoD #3** : Les recommandations vestimentaires et d'attitude fournissent un brief actionnable pour `ART-03` et `ART-06`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
