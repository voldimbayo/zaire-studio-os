# Garde-Fous Techniques Unreal Engine 5 (`DIR-04`)

## 1. Enveloppes Budgétaires Incompressibles (Kinshasa Open World)
- **Frametime Total P99** : `16.6 ms` (60 FPS) / `33.3 ms` (30 FPS).
- **Game Thread** : `<= 6.5 ms` (`AI-01` <= 2.5 ms, `AI-02/03` Mass <= 2.0 ms, `ENG-05` Chaos <= 1.5 ms).
- **GPU Passes** : `ART-07` Lumen GI + Reflections `<= 4.5 ms`, `ART-04` Nanite `<= 2.5 ms`, `ART-09` Niagara `<= 1.5 ms`.
- **VRAM** : `<= 6144 MB` en cible standard (pools stricts : Virtual Textures, Render Targets Lumen/VSM, Meshes Nanite).

## 2. Règles d'Architecture Obligatoires
1. **World Partition & Data Layers (`ENG-01`)** : Taille de cellule `12800 cm` (128 m), rayon de chargement adapté à la vitesse maximale des motos Wewa (`VEH-MOTO-WEWA-01`).
2. **Zéro Chargement Synchrone** : Usage exclusif de `FStreamableManager::RequestAsyncLoad` et `TSoftObjectPtr<T>`.
3. **PSO Precache** : Collecte obligatoire des Pipeline State Objects sur chaque build nocturne (`ENG-08`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-04` — Strate DAG 0)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-01`
- **Audit des Entrées (`inputs`)** :
  - `technical-proposals` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/technical-specs/performance-budgets.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `profiling-reports-eng-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `technical-adr.md` : Doit respecter le gabarit `templates/technical-adr.md` et passer l'audit croisé.
  - `hardware-budget-allocation.csv` : Doit respecter le gabarit `templates/technical-adr.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-07`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Système dépassant son budget CPU/GPU alloué dans performance-budgets.csv | Blocage / Dégradation si ignoré | Opposer un VETO_TECHNIQUE et imposer une architecture orientée données (Mass Entity) ou du time-slicing | Escalade vers Marquer le système BLOCKED jusqu'à retour sous le seuil P99 |
| Mode de Défaillance 2: Utilisation de LoadSynchronous() ou de Static Switches abusifs dans un Master Material | Blocage / Dégradation si ignoré | Rejeter l'implémentation et imposer FStreamableManager / Custom Primitive Data | Escalade vers Ajouter une règle bloquante dans le validateur pré-commit ENG-03 |
| Mode de Défaillance 3: Densité de foule demandée > 24 acteurs dans un marché (ex: DST-MATONGE) | Blocage / Dégradation si ignoré | Imposer le découpage : max 24 ACharacter complets (AI-01) + jusqu'à 600 entités Mass Crowd (AI-02) avec hydratation à 25m | Escalade vers Valider l'enveloppe CPU Mass <= 2.0 ms |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-04`)

- [ ] **Contrôle DoD #1** : Le budget frametime cumulé des sous-systèmes reste `<= 16.6 ms` (Performance) et `<= 33.3 ms` (Qualité).
- [ ] **Contrôle DoD #2** : Le budget VRAM total est maintenu `<= 6144 MB` (Performance) / `<= 8192 MB` (Qualité).
- [ ] **Contrôle DoD #3** : Chaque ADR technique définit une métrique de vérification automatisable dans Unreal Insights / Gauntlet.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
