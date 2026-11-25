# Protocole de Profilage Unreal Insights & PSO Precaching (`ENG-07`)

## 1. Grille de Contrôle P99 Obligatoire (`knowledge/technical-specs/performance-budgets.csv`)
| ID Budget | Sous-Système | Plafond 60 FPS | Plafond 30 FPS | Skill Responsable |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | Frametime Global P99 | `<= 16.6 ms` | `<= 33.3 ms` | `ENG-07` |
| `PERF-CPU-GAME` | Game Thread Total | `<= 6.5 ms` | `<= 12.0 ms` | `ENG-01` |
| `PERF-CPU-NPCAI` | NPC AI (`<= 24` acteurs) | `<= 2.5 ms` | `<= 3.0 ms` | `AI-01` |
| `PERF-CPU-MASS` | Mass Crowd & Traffic (`600+`) | `<= 2.0 ms` | `<= 2.5 ms` | `AI-02` / `AI-03` |
| `PERF-CPU-CHAOS` | Chaos Physics & Vehicles | `<= 1.5 ms` | `<= 2.0 ms` | `ENG-05` |
| `PERF-CPU-ANIM` | Animation & Motion Matching | `<= 1.8 ms` | `<= 2.5 ms` | `ART-05` |
| `PERF-GPU-LUMEN` | Lumen GI & Reflections | `<= 4.5 ms` | `<= 7.0 ms` | `ART-07` / `ENG-06` |
| `PERF-GPU-NANITE` | Nanite Raster & VisBuffer | `<= 2.5 ms` | `<= 4.0 ms` | `ART-04` / `ENG-06` |
| `PERF-GPU-NIAGARA` | Niagara VFX | `<= 1.5 ms` | `<= 2.0 ms` | `ART-09` |
| `PERF-MEM-VRAM` | VRAM Totale Allouée | `<= 6144 MB` | `<= 8192 MB` | `DIR-04` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-07` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ENG-01`, `ENG-02`, `ENG-03`, `ENG-04`, `ENG-05`, `ENG-06`, `ART-07`, `ART-09`, `AI-01`, `AI-02`, `AI-03`
- **Audit des Entrées (`inputs`)** :
  - `all-engineering-subsystems-eng-01-to-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lighting-art-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `niagara-vfx-art-09` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/technical-specs/performance-budgets.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `performance-budget-report.md` : Doit respecter le gabarit `templates/performance-budget-report.md` et passer l'audit croisé.
  - `pso-precaching-protocol.md` : Doit respecter le gabarit `templates/performance-budget-report.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-04`, `DIR-07`, `PRD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Un sous-système dépasse son budget dans check_perf_budget.py (ex: PERF-GPU-LUMEN = 5.4 ms > 4.5 ms) | Blocage / Dégradation si ignoré | Marquer immédiatement la zone ou le système au statut BLOCKED et assigner un ticket d'optimisation prioritaire au skill responsable (ART-07 / ENG-06) | Escalade vers Interdire la promotion CONFIRMED tant que P99 > 16.6 ms |
| Mode de Défaillance 2: Hitch ponctuel (> 25 ms sur 1 frame) détecté lors du premier coup de machette ou de la première explosion Niagara | Blocage / Dégradation si ignoré | Capturer le PSO manquant via les logs de PSO Precaching et l'ajouter à la passe d'échauffement (warmup) du build nocturne ENG-08 | Escalade vers Éliminer 100 % des shader compilation stutters |
| Mode de Défaillance 3: Consommation VRAM dépassant 5900 MB (proche du plafond de 6144 MB) | Blocage / Dégradation si ignoré | Auditer le pool de textures via memreport -full, rétrograder les textures non-héroïques de 4K vers 2K et resserrer le budget du pool Streaming Virtual Texturing | Escalade vers Prévenir tout crash Out-Of-Memory (OOM) |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-07`)

- [ ] **Contrôle DoD #1** : `python skills/07-engineering/eng-07-performance-engineer/scripts/check_perf_budget.py` retourne un code `0` (`passed: true`).
- [ ] **Contrôle DoD #2** : Le percentile P99 du frametime global est `<= 16.6 ms` (Mode Performance) et `<= 33.3 ms` (Mode Qualité).
- [ ] **Contrôle DoD #3** : Zéro fuite mémoire (memory leak) constatée après 2 heures de boucle d'exploration Gauntlet (`PRD-05`).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
