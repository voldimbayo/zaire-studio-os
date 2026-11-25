# Registre Canonique des Dépendances Inter-Skills (`canonical-dependency-registry.md`)

- **Version du Système** : `1.1.0`
- **Source Unique de Vérité Code** : [tools/registry_data.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/registry_data.py) (`CANONICAL_SKILLS`)
- **Spécification Architecturale Associée** : [architecture/skill-dependencies.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/architecture/skill-dependencies.md)
- **Vérification Automatisée** : `python tools/check_dag_cycles.py` et `tests/test_foundation.py` (100 % de parité exigée entre ce registre, `tools/registry_data.py`, `dir-01-studio-orchestrator/scripts/build_dag_plan.py` et les 57 fichiers `SKILL.md`).

---

## 1. Résolution Explicite des Cycles et Divergences de Phase 2 (Workstream 1)

| Cas Investigé | État Initial (Phase 2 / Phase 3 v1.0.0) | Décision de Réconciliation Canonique (Phase 5 v1.1.0) | Garantie DAG |
| :--- | :--- | :--- | :--- |
| **`ENG-04` ↔ `AI-03`** | Phase 2 déclarait un cycle `AI-03 -> ENG-04` et `ENG-04 -> AI-03`. Phase 3 v1.0.0 avait coupé `ENG-04` des dépendances d'`AI-03`, ce qui exécutait `AI-03` *avant* `ENG-04`. | **`ENG-04` précède `AI-03`** : `ENG-04` (Strate 3, vague amont) dépend de `("WLD-03", "ART-02", "GD-06")` et génère les splines `ZoneGraph` à partir d'OSM et des gabarits véhicules (`130-150 cm` Wewa). `AI-03` (Strate 3, vague aval) dépend de `("ENG-04", "GD-06", "WLD-03", "DIR-04")`. | **0 cycle** ; `ENG-04` est toujours planifié dans une vague antérieure à `AI-03`. |
| **`WLD-05` ↔ `ART-05`** | Phase 2 déclarait un cycle `WLD-05 -> ART-05` et `ART-05 -> WLD-05`. | **Découplage par `DIR-05` (Strate 0)** : `DIR-05` fige les métriques spatiales (`spatial-metrics.md` : couloir `>= 350 cm`, vault `100 cm`, ledge `260-300 cm`). `WLD-05` (Strate 2) dépend de `("WLD-04", "GD-02", "GD-05", "DIR-05")`. `ART-05` (Strate 3) dépend de `("WLD-05", "GD-05", "ART-06")`. | **0 cycle** ; `WLD-05` valide le blockout avant que `ART-05` ne cale le Motion Warping. |
| **`WLD-04`** | Phase 2 demandait `GD-01` en amont de `WLD-04`, mais v1.0.0 avait inversé `GD-01 -> WLD-04`. | `GD-01` (Strate 1) dépend de `("DIR-03", "DIR-05")`. `WLD-04` (Strate 1) dépend de `("WLD-01", "WLD-03", "GD-01", "DIR-04", "DIR-05")`. | **0 cycle** ; les Core Loops (`GD-01`) alimentent le zonage Open World (`WLD-04`). |
| **`ENG-02`** | v1.0.0 omettait `GD-03`, `GD-04` et `GD-07` des dépendances de `ENG-02`. | `ENG-02` (Strate 4) dépend désormais de l'intégralité du département Game Design : `("GD-01", "GD-02", "GD-03", "GD-04", "GD-05", "GD-06", "GD-07", "ENG-01")`. | **0 cycle** ; couvre l'économie, la progression et Common UI en C++. |
| **`ENG-07`** | v1.0.0 omettait `ENG-03` et les systèmes `AI-01..03` des dépendances de `ENG-07`. | `ENG-07` (Strate 4) dépend de `("ENG-01", "ENG-02", "ENG-03", "ENG-04", "ENG-05", "ENG-06", "ART-07", "ART-09", "AI-01", "AI-02", "AI-03")`. | **0 cycle** ; le profilage P99 agrège tous les sous-systèmes CPU/GPU. |

---

## 2. Table Maîtresse des 57 Skills et Dépendances Canoniques

| ID | Slug | Département | Strate | Dépendances Amont (`upstream_dependencies`) |
| :--- | :--- | :--- | :--- | :--- |
| `DIR-01` | `dir-01-studio-orchestrator` | `00-direction` | 0 | *(Aucune — Racine DAG)* |
| `DIR-02` | `dir-02-executive-producer` | `00-direction` | 0 | `DIR-01` |
| `DIR-03` | `dir-03-creative-director` | `00-direction` | 0 | `DIR-01` |
| `DIR-04` | `dir-04-technical-director` | `00-direction` | 0 | `DIR-01` |
| `DIR-05` | `dir-05-lead-game-designer` | `00-direction` | 0 | `DIR-01`, `DIR-03` |
| `DIR-06` | `dir-06-documentation-director` | `00-direction` | 5 | `PRD-03`, `NAR-06` |
| `DIR-07` | `dir-07-quality-director` | `00-direction` | 5 | `PRD-04`, `PRD-05`, `PRD-06`, `ENG-07` |
| `NAR-01` | `nar-01-narrative-architect` | `01-narrative` | 1 | `DIR-03`, `WLD-01`, `WLD-02` |
| `NAR-02` | `nar-02-screenwriter` | `01-narrative` | 2 | `NAR-01`, `NAR-03`, `GD-02` |
| `NAR-03` | `nar-03-character-writer` | `01-narrative` | 2 | `NAR-01`, `WLD-01`, `WLD-02` |
| `NAR-04` | `nar-04-dialogue-designer` | `01-narrative` | 2 | `NAR-02`, `NAR-03`, `GD-02` |
| `NAR-05` | `nar-05-lore-manager` | `01-narrative` | 2 | `WLD-01`, `WLD-02`, `NAR-01` |
| `NAR-06` | `nar-06-continuity-editor` | `01-narrative` | 5 | `NAR-01`, `NAR-02`, `NAR-03`, `NAR-04`, `NAR-05`, `GD-02` |
| `WLD-01` | `wld-01-worldbuilding-architect` | `02-world-design` | 1 | `DIR-03`, `WLD-02`, `WLD-03` |
| `WLD-02` | `wld-02-cultural-researcher` | `02-world-design` | 1 | `DIR-03` |
| `WLD-03` | `wld-03-urban-researcher` | `02-world-design` | 1 | `DIR-03`, `DIR-04` |
| `WLD-04` | `wld-04-open-world-designer` | `02-world-design` | 1 | `WLD-01`, `WLD-03`, `GD-01`, `DIR-04`, `DIR-05` |
| `WLD-05` | `wld-05-level-designer` | `02-world-design` | 2 | `WLD-04`, `GD-02`, `GD-05`, `DIR-05` |
| `WLD-06` | `wld-06-environment-designer` | `02-world-design` | 2 | `WLD-05`, `ART-01`, `WLD-02`, `WLD-03` |
| `GD-01` | `gd-01-game-systems-designer` | `03-game-design` | 1 | `DIR-03`, `DIR-05` |
| `GD-02` | `gd-02-mission-designer` | `03-game-design` | 2 | `NAR-01`, `WLD-04`, `GD-01` |
| `GD-03` | `gd-03-economy-designer` | `03-game-design` | 2 | `GD-01`, `GD-02`, `DIR-02` |
| `GD-04` | `gd-04-progression-designer` | `03-game-design` | 2 | `GD-01`, `GD-05`, `NAR-01` |
| `GD-05` | `gd-05-combat-designer` | `03-game-design` | 2 | `GD-01`, `DIR-05` |
| `GD-06` | `gd-06-vehicle-designer` | `03-game-design` | 2 | `WLD-03`, `GD-01`, `DIR-05` |
| `GD-07` | `gd-07-ui-ux-designer` | `03-game-design` | 2 | `GD-01`, `GD-02`, `ART-01` |
| `AI-01` | `ai-01-npc-ai-architect` | `04-ai-simulation` | 3 | `GD-05`, `WLD-05`, `DIR-04` |
| `AI-02` | `ai-02-crowd-simulation-specialist` | `04-ai-simulation` | 3 | `WLD-04`, `ART-03`, `DIR-04` |
| `AI-03` | `ai-03-traffic-ai-specialist` | `04-ai-simulation` | 3 | `ENG-04`, `GD-06`, `WLD-03`, `DIR-04` |
| `AI-04` | `ai-04-decision-systems-designer` | `04-ai-simulation` | 3 | `WLD-01`, `GD-01`, `NAR-04` |
| `ART-01` | `art-01-art-director` | `05-art-animation` | 1 | `DIR-03`, `WLD-02`, `WLD-03` |
| `ART-02` | `art-02-environment-artist` | `05-art-animation` | 3 | `WLD-06`, `ART-04` |
| `ART-03` | `art-03-character-artist` | `05-art-animation` | 3 | `NAR-03`, `WLD-02`, `ART-01`, `ART-04` |
| `ART-04` | `art-04-3d-pipeline-specialist` | `05-art-animation` | 1 | `DIR-04`, `ART-01` |
| `ART-05` | `art-05-animation-specialist` | `05-art-animation` | 3 | `WLD-05`, `GD-05`, `ART-06` |
| `ART-06` | `art-06-motion-capture-specialist` | `05-art-animation` | 3 | `NAR-02`, `GD-05` |
| `ART-07` | `art-07-lighting-specialist` | `05-art-animation` | 3 | `ART-01`, `WLD-05`, `ART-02`, `DIR-04` |
| `ART-08` | `art-08-technical-artist` | `05-art-animation` | 3 | `ART-02`, `ART-03`, `ART-04`, `DIR-04` |
| `ART-09` | `art-09-vfx-specialist` | `05-art-animation` | 3 | `ART-01`, `GD-05`, `ART-07`, `DIR-04` |
| `AUD-01` | `aud-01-audio-director` | `06-audio-localization` | 1 | `DIR-03`, `WLD-01`, `WLD-02` |
| `AUD-02` | `aud-02-sound-designer` | `06-audio-localization` | 3 | `AUD-01`, `GD-05`, `GD-06`, `WLD-06` |
| `AUD-03` | `aud-03-music-designer` | `06-audio-localization` | 3 | `AUD-01`, `WLD-02`, `GD-01`, `GD-05` |
| `AUD-04` | `aud-04-voice-localization-specialist` | `06-audio-localization` | 3 | `NAR-04`, `GD-07`, `WLD-02` |
| `ENG-01` | `eng-01-unreal-engine-specialist` | `07-engineering` | 1 | `DIR-04`, `WLD-04`, `ART-04` |
| `ENG-02` | `eng-02-gameplay-programmer` | `07-engineering` | 4 | `GD-01`, `GD-02`, `GD-03`, `GD-04`, `GD-05`, `GD-06`, `GD-07`, `ENG-01` |
| `ENG-03` | `eng-03-tools-programmer` | `07-engineering` | 4 | `ART-04`, `ENG-01` |
| `ENG-04` | `eng-04-houdini-specialist` | `07-engineering` | 3 | `WLD-03`, `ART-02`, `GD-06` |
| `ENG-05` | `eng-05-physics-engineer` | `07-engineering` | 4 | `GD-06`, `ART-02`, `DIR-04` |
| `ENG-06` | `eng-06-rendering-engineer` | `07-engineering` | 4 | `DIR-04`, `ART-07`, `ART-08` |
| `ENG-07` | `eng-07-performance-engineer` | `07-engineering` | 4 | `ENG-01`, `ENG-02`, `ENG-03`, `ENG-04`, `ENG-05`, `ENG-06`, `ART-07`, `ART-09`, `AI-01`, `AI-02`, `AI-03` |
| `ENG-08` | `eng-08-build-engineer` | `07-engineering` | 4 | `ENG-01`, `ENG-02`, `ENG-03`, `ENG-07` |
| `PRD-01` | `prd-01-production-planner` | `08-production-quality` | 1 | `DIR-01`, `DIR-02` |
| `PRD-02` | `prd-02-risk-manager` | `08-production-quality` | 1 | `DIR-02`, `DIR-04`, `WLD-02` |
| `PRD-03` | `prd-03-documentation-specialist` | `08-production-quality` | 5 | `NAR-05`, `WLD-01`, `GD-01`, `ENG-01` |
| `PRD-04` | `prd-04-qa-architect` | `08-production-quality` | 5 | `GD-02`, `WLD-04`, `ENG-02` |
| `PRD-05` | `prd-05-test-engineer` | `08-production-quality` | 5 | `PRD-04`, `ENG-07`, `ENG-08` |
| `PRD-06` | `prd-06-accessibility-specialist` | `08-production-quality` | 5 | `GD-07`, `GD-05`, `AUD-04` |
