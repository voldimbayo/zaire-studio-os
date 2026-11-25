# Graphe des Dépendances Inter-Skills (`skill-dependencies.md`)

## 1. Règle Anti-Cycles (DAG Strict) & Réconciliation Canonique (Phase 5)
L'architecture de **ZAÏRE STUDIO OS (v1.1.0)** interdit toute dépendance circulaire directe entre skills métiers. Les flux de production suivent un **Graphe Orienté Acyclique (DAG)** en 6 strates, gouverné par une source unique de vérité ([tools/registry_data.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/registry_data.py) et [docs/canonical-dependency-registry.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/docs/canonical-dependency-registry.md)).

### Résolution Architecturale des Cycles Potentiels (ADR-05)
1. **Découplage `WLD-05` (Level Designer) -> `ART-05` (Animation Specialist)** :
   - Les métriques spatiales de base (`1 UU = 1 cm`, couloir `>= 350 cm`, couvert bas/vault `100 cm`, saut d'accroche `260-300 cm`) sont gelées dès la **Strate 0** par `DIR-05` (Lead Game Designer) dans `knowledge/technical-specs/spatial-metrics.md`.
   - `WLD-05` (Strate 2) dépend de `("WLD-04", "GD-02", "GD-05", "DIR-05")` et applique ces métriques pour produire le blockout.
   - `ART-05` (Strate 3) dépend de `("WLD-05", "GD-05", "ART-06")` et calibre les cibles `Motion Warping` et `Control Rig IK` sur la géométrie de blockout validée.
2. **Ordonnancement `ENG-04` (Houdini Specialist) -> `AI-03` (Traffic AI Specialist)** :
   - `ENG-04` (Strate 3, vague amont) dépend de `("WLD-03", "ART-02", "GD-06")` : il ingère la morphologie viaire OSM (`WLD-03`), les kits modulaires (`ART-02`) et les gabarits véhicules (`GD-06` : couloir inter-file `130-150 cm`) pour générer les splines et profils de voies `ZoneGraph`.
   - `AI-03` (Strate 3, vague aval) dépend de `("ENG-04", "GD-06", "WLD-03", "DIR-04")` : il s'exécute **après** `ENG-04`, garantissant que le réseau `ZoneGraph` existe avant la configuration des règles de priorité `MassTraffic`, du slalom des motos Wewa et des barrages de la Police de Circulation Routière (`ORG-POLICE-PCR`).

---

## 2. Diagramme de Flux Principal (Strates 0 à 5)

```
[STRATE 0 : DIRECTION & CADRAGE MÉTRIQUE / BUDGÉTAIRE]
  DIR-01 (Orchestrator) ---> DIR-02 (Exec Prod) + DIR-03 (Creative Dir) + DIR-04 (Tech Dir) ---> DIR-05 (Lead GD)
          |
          v
[STRATE 1 : FONDATIONS CULTURELLES, URBAINES, SYSTÉMIQUES & MOTEUR]
  WLD-02 (Cultural Res) + WLD-03 (Urban Res) ---> WLD-01 (Worldbuilding) ---> NAR-01 (Narrative Arch)
  GD-01 (Game Systems) + WLD-01 + WLD-03 -------> WLD-04 (Open World)
  ART-01 (Art Director) ---> ART-04 (3D Pipeline) ---> ENG-01 (UE5 Specialist)
  AUD-01 (Audio Director) | PRD-01 (Production Planner) | PRD-02 (Risk Manager)
          |
          v
[STRATE 2 : CONCEPTION DÉTAILLÉE (MISSIONS, PERSONNAGES, MÉCANIQUES, BLOCKOUT)]
  NAR-03 (Char Writer) & NAR-05 (Lore Mgr) ---> NAR-02 (Screenwriter) ---> NAR-04 (Dialogue Des)
  GD-02 (Mission Des) + GD-03 (Economy) + GD-04 (Progression) + GD-05 (Combat) + GD-06 (Vehicle) + GD-07 (UI/UX)
  WLD-05 (Level Designer) ---> WLD-06 (Environment Designer)
          |
          v
[STRATE 3 : PRODUCTION DE CONTENU, HOUDINI ZONEGRAPH & SIMULATION IA]
  ART-02 (Env Art) + ART-03 (Char Art) + ART-06 (MoCap) ---> ART-05 (Animation)
  ART-07 (Lighting) + ART-08 (Tech Art) + ART-09 (VFX)
  ENG-04 (Houdini HDA/PCG & ZoneGraph) ---> AI-03 (Traffic AI)
  AI-01 (NPC AI) + AI-02 (Crowd Sim) + AI-04 (Decision Systems)
  AUD-02 (Sound Des) + AUD-03 (Music Des) + AUD-04 (Voice & L10n)
          |
          v
[STRATE 4 : INGÉNIERIE D'INTÉGRATION, PHYSIQUE, RENDU & OPTIMISATION]
  ENG-02 (Gameplay Prog) + ENG-03 (Tools Prog) + ENG-05 (Physics) + ENG-06 (Rendering Eng)
          |
          v
  ENG-07 (Performance Eng) ---> ENG-08 (Build Eng)
          |
          v
[STRATE 5 : AUDIT, VALIDATION & CERTIFICATION]
  NAR-06 (Continuity Ed) + PRD-03 (Doc Spec) + PRD-04 (QA Arch) ---> PRD-05 (Test Eng) + PRD-06 (Accessibility)
          |
          v
  DIR-06 (Doc Dir) & DIR-07 (Quality Dir) => [CONFIRMED]
```

---

## 3. Matrice Canonique des Dépendances Critiques (100 % Alignant `tools/registry_data.py`)

| Skill Aval | Dépend de (Skills Amont Exactes) | Artefact Transmis (Handoff) | Condition de Déclenchement |
| :--- | :--- | :--- | :--- |
| `WLD-01` (Worldbuilding) | `DIR-03`, `WLD-02`, `WLD-03` | Dossiers culturels & morphologie urbaine | Statut `PROPOSED` ou `CONFIRMED` |
| `NAR-01` (Narrative Arch) | `DIR-03`, `WLD-01`, `WLD-02` | World Bible & identité des communes (`DST-*`) | Piliers créatifs validés |
| `NAR-02` (Screenwriter) | `NAR-01`, `NAR-03`, `GD-02` | Architecture actes, fiches `CHR-*`, structure `MSN-*` | IDs `CHR-*` et `MSN-*` enregistrés |
| `NAR-04` (Dialogue Des) | `NAR-02`, `NAR-03`, `GD-02` | Scripts de scènes & variables d'état de quête | Beat sheet validée |
| `GD-01` (Game Systems) | `DIR-03`, `DIR-05` | Piliers créatifs & directives Core Loops | Taxonomie Gameplay Tags initialisée |
| `WLD-04` (Open World) | `WLD-01`, `WLD-03`, `GD-01`, `DIR-04`, `DIR-05` | Typologie urbaine, Core Loops, budgets streaming | Grille World Partition définie |
| `WLD-05` (Level Designer) | `WLD-04`, `GD-02`, `GD-05`, `DIR-05` | Briefs POI/Mission & métriques spatiales `DIR-05` | Métriques spatiales gelées (`350 cm`) |
| `WLD-06` (Env Designer) | `WLD-05`, `ART-01`, `WLD-02`, `WLD-03` | Blockouts gameplay validés & Art Bible | Playtest blockout réussi |
| `ART-02` (Env Artist) | `WLD-06`, `ART-04` | Environment Briefs & normes 3D/Nanite | Règles Texel Density (`10.24 px/cm`) |
| `ART-03` (Character Art) | `NAR-03`, `WLD-02`, `ART-01`, `ART-04` | Fiches personnages, références vestimentaires, normes 3D | Concept validé par `ART-01` |
| `ART-05` (Animation) | `WLD-05`, `GD-05`, `ART-06` | Blockout validé, Frame Data 60 FPS, MoCap nettoyée | Squelette maître validé |
| `ENG-04` (Houdini) | `WLD-03`, `ART-02`, `GD-06` | Règles voirie OSM, kits modulaires, gabarits véhicules | HDA testé sur tuile pilote |
| `AI-02` (Crowd Sim) | `WLD-04`, `ART-03`, `DIR-04` | Densité par quartier, kits PNJ modulaires, budget CPU | Architecture Mass Entity prête |
| `AI-03` (Traffic AI) | `ENG-04`, `GD-06`, `WLD-03`, `DIR-04` | Splines routières `ZoneGraph` (`ENG-04`) & profils `VEH-*` | Réseau `ZoneGraph` généré par `ENG-04` |
| `ENG-02` (Gameplay Prog) | `GD-01`, `GD-02`, `GD-03`, `GD-04`, `GD-05`, `GD-06`, `GD-07`, `ENG-01` | GDD systémiques complets & architecture C++/GAS | Gameplay Tags enregistrés |
| `ENG-07` (Performance) | `ENG-01`, `ENG-02`, `ENG-03`, `ENG-04`, `ENG-05`, `ENG-06`, `ART-07`, `ART-09`, `AI-01`, `AI-02`, `AI-03` | Systèmes C++, Houdini, IA, éclairage et VFX assemblés | Profilage Unreal Insights |
| `AUD-04` (Voice & L10n) | `NAR-04`, `GD-07`, `WLD-02` | Dialogues finaux, textes UI, glossaire lingala Unicode | String Freeze prononcé |
| `PRD-05` (Test Eng) | `PRD-04`, `ENG-07`, `ENG-08` | Plans de test QA, budgets perf, pipeline CI/CD | Build nocturne disponible |
| `DIR-06` / `DIR-07` | `NAR-06`, `PRD-03`, `PRD-04`, `PRD-05`, `PRD-06`, `ENG-07` | Audits continuité, documentation, QA, Perf et XAG | 100 % des critères DoD remplis |
