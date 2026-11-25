# Les 3 Piliers Créatifs de ZAÏRE (`DIR-03`)

1. **Pilier 1 — Kinshasa Vivante & Souveraine ("Mégapole Électrique")** :
   La ville n'est pas un simple décor statique mais un organisme vivant, sonore, dense et stratifié où chaque commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`) possède son propre pouls architectural, social et musical.
2. **Pilier 2 — Ingéniosité Urbaine & Vélocité ("Flux & Débrouillardise")** :
   Le joueur triomphe par sa lecture de la ville : maîtrise des réseaux humains, parkour urbain fluide, pilotage nerveux des motos Wewa (`VEH-MOTO-WEWA-01`) et utilisation tactique de la foule et de la météo équatoriale.
3. **Pilier 3 — Tension Sociale &Ancrage Humain ("Du Port aux Ngandas")** :
   Chaque conflit mêle enjeux intimes familiaux (`FAM-KABONGO` vs `FAM-MUKENDI`) et luttes d'influence économiques sur le bassin du fleuve Congo, portés par des dialogues bilingues français/lingala crédibles.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-03` — Strate DAG 0)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-01`
- **Audit des Entrées (`inputs`)** :
  - `creative-proposals` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/world-bible/cultural-guidelines.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `art-and-narrative-deliverables` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `creative-vision-review.md` : Doit respecter le gabarit `templates/creative-vision-review.md` et passer l'audit croisé.
  - `creative-pillar-scorecard.md` : Doit respecter le gabarit `templates/creative-vision-review.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-01`, `WLD-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Présence d'un cliché générique ('Afrique exotisée' ou argot non kinois) | Blocage / Dégradation si ignoré | Opposer un VETO_CREATIVE immédiat et renvoyer le livrable vers WLD-02 pour correction | Escalade vers Bloquer toute promotion au statut CONFIRMED |
| Mode de Défaillance 2: Mécanique de gameplay contredisant l'identité de Koffi (CHR-PROTAG-KOFFI) | Blocage / Dégradation si ignoré | Demander à DIR-05 et GD-01/GD-02 d'intégrer une alternative d'infiltration sociale ou de négociation | Escalade vers Maintenir l'alignement ludo-narratif du protagoniste |
| Mode de Défaillance 3: Uniformité visuelle ou sonore entre deux communes | Blocage / Dégradation si ignoré | Exiger de ART-01 et AUD-01 une différenciation marquée des palettes chromatiques et ambiances | Escalade vers Se référer aux signatures de kinshasa-districts.md |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-03`)

- [ ] **Contrôle DoD #1** : Le livrable obtient un score >= 4/5 sur chacun des 3 piliers créatifs de ZAÏRE.
- [ ] **Contrôle DoD #2** : Zéro stéréotype ou anachronisme culturel détecté (conformité à `cultural-guidelines.md`).
- [ ] **Contrôle DoD #3** : Alignement explicite entre l'intention dramatique, l'espace urbain et la mécanique jouable.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
