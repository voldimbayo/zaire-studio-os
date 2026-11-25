# Definition of Done (DoD) & Seuils Qualité Studio (`DIR-07`)

## 1. Les 6 Critères Obligatoires de la Definition of Done
1. **Format & Gabarit** : Livrable structuré exactement selon le fichier `templates/` du skill.
2. **Intégrité des IDs** : 100 % des identifiants (`CHR-*`, `LOC-*`, `MSN-*`, etc.) présents et valides dans `knowledge/entities-registry.csv`.
3. **Traçabilité** : Sources techniques (`SRC-*`) et culturelles citées ; incertitudes isolées en `RESEARCH_REQUIRED`.
4. **Périmètre Respecté** : Zéro empiètement sur un autre skill du DAG.
5. **Budgets & Standards** : Frametime `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS), couloirs `>= 350 cm`, Texel Density `10.24 px/cm`, expansion UI `+35 %`, support Unicode lingala (`ɛ`, `ɔ`).
6. **Validation Croisée** : Signature des auditeurs (`NAR-06`, `ENG-07`, `PRD-04`, `PRD-06`).

## 2. Seuils Quantitatifs d'Acceptation QA
- **Couverture Tests Automatisés (`PRD-05`)** : `>= 80 %` des systèmes critiques (`SYS-*`).
- **Taux de Reproductibilité Bugs (`PRD-04`)** : `>= 90 %` (avec coordonnées World Partition, seed et état de quête).
- **Taux de Faux Positifs Gauntlet** : `< 2 %`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-07` — Strate DAG 5)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `PRD-04`, `PRD-05`, `PRD-06`, `ENG-07`
- **Audit des Entrées (`inputs`)** :
  - `qa-test-plans-prd-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gauntlet-reports-prd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `xag-audits-prd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `perf-reports-eng-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `quality-gate-verdict.md` : Doit respecter le gabarit `templates/quality-gate-verdict.md` et passer l'audit croisé.
  - `certification-checklist-report.md` : Doit respecter le gabarit `templates/quality-gate-verdict.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-01`, `DIR-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Présence d'un bug de Sévérité A (Crash, Soft-Lock narratif, corruption de sauvegarde, dépassement VRAM OOM) | Blocage / Dégradation si ignoré | Placer immédiatement l'entité ou le build au statut BLOCKED | Escalade vers Ouvrir un ticket critique prioritaire via DIR-01 vers ENG-01/ENG-07/GD-02 |
| Mode de Défaillance 2: Interface UI ou mécanique de jeu dépourvue de double codage daltonisme ou de support d'expansion texte +35 % | Blocage / Dégradation si ignoré | Refuser la validation qualité pour non-conformité XAG | Escalade vers Renvoyer vers GD-07, AUD-04 et PRD-06 |
| Mode de Défaillance 3: 100 % des 6 critères DoD validés et tests Gauntlet/XAG/Continuité réussis | Blocage / Dégradation si ignoré | Cosigner avec DIR-06 la promotion de l'entité au statut CONFIRMED | Escalade vers Archiver le certificat qualité du jalon |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-07`)

- [ ] **Contrôle DoD #1** : Les 6 critères de la Definition of Done universelle sont explicitement cochés et justifiés.
- [ ] **Contrôle DoD #2** : 0 anomalie bloquante (Sévérité A) ouverte sur le périmètre audité.
- [ ] **Contrôle DoD #3** : Conformité XAG vérifiée (visuelle, auditive, motrice, cognitive).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
