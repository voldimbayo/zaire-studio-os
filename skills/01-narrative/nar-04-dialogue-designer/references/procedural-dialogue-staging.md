# Mise en Scène Procédurale & Architecture de Barks (`NAR-04`)

## 1. Pipeline de Cadrage Automatique (Inspiré d'Ubisoft GDC 2019 `SRC-014`)
Chaque ligne de dialogue porte deux métadonnées exploitées par le système caméra UE5 :
- `emotion_tag` : Pilote l'animation procédurale faciale/gestuelle (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`).
- `camera_framing` : Pilote la sélection de caméra virtuelle (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`).

## 2. Calibrage UI & Accessibilité (`PRD-06` / `AUD-04`)
- **Maximum 20 mots par noeud** (environ 110 caractères en français, laissant la marge de +35 % d'expansion multilingue sans troncature).
- **Préfixe Locuteur Obligatoire** : Exporté sous la forme `[KOFFI]` ou `[AMINA]` pour les sous-titres enrichis XAG.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`NAR-04` — Strate DAG 2)

- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :
  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.
  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.
  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-02`, `NAR-03`, `GD-02`
- **Audit des Entrées (`inputs`)** :
  - `mission-scripts-nar-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `character-bibles-nar-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `quest-states-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lingala-french-glossary.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `dialogue-tree.json` : Doit respecter le gabarit `templates/dialogue-tree-schema.json` et passer l'audit croisé.
  - `contextual-barks-table.csv` : Doit respecter le gabarit `templates/dialogue-tree-schema.json` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `GD-02`, `AUD-04`, `NAR-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Réplique dépassant 20 mots dans un noeud de dialogue | Blocage / Dégradation si ignoré | Scinder la réplique en 2 noeuds consécutifs ou condenser le texte | Escalade vers Garantir la conformité au validateur validate_dialogue_json.py et aux normes XAG |
| Mode de Défaillance 2: Noeud non terminal dépourvu de transition sortante (impasse) | Blocage / Dégradation si ignoré | Relier le noeud à une sortie de repli valide ou marquer explicitement is_terminal: true | Escalade vers Corriger avant tout handoff vers AUD-04 et ENG-02 |
| Mode de Défaillance 3: Dialogue de mission susceptible d'être interrompu par une averse ou une collision routière | Blocage / Dégradation si ignoré | Ajouter les hooks système ON_INTERRUPT et ON_RESUME reliés à la machine à états GD-02 | Escalade vers Empêcher toute perte de progression narrative |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`NAR-04`)

- [ ] **Contrôle DoD #1** : `python skills/01-narrative/nar-04-dialogue-designer/scripts/validate_dialogue_json.py` valide le graphe avec 0 erreur.
- [ ] **Contrôle DoD #2** : 100 % des répliques font `<= 20 mots` et identifient le locuteur via un ID `CHR-*` valide.
- [ ] **Contrôle DoD #3** : Les barks contextuels couvrent au moins 4 variations par déclencheur pour éviter la répétition auditive.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
