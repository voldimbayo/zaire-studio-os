# ZAÏRE STUDIO OS v1.0.0 — Independent Release Review (`independent-review.md`)

- **Date of Review**: `2026-11-26`
- **Review Scope**: Full read-only inspection of all 57 `SKILL.md` files and subdirectories (`references/`, `templates/`, `examples/`, `scripts/`), `research/`, `architecture/`, `knowledge/`, `schemas/`, `tools/`, `tests/`, `audit/`, and all 67 ZIP packages in `releases/`.
- **Modification Policy**: Zero existing files were modified, overwritten, deleted, or regenerated during this review.
- **Executive Verdict**: **`PARTIAL` (Conditionally Ready for Architecture/Prompt Orchestration; NOT Production-Complete for Direct Engine Execution or Multi-Agent Artifact Synthesis)**

---

## 1. Executive Summary & Classification Matrix

While the previous internal Phase 4 report (`audit/final-report.md`) declared a clean `PASS` across all internal checks, an independent forensic review of the actual file contents, code paths, and architectural contracts reveals that **several internal validators are self-referential (testing hardcoded mock dictionaries rather than actual generated artifacts)**, that **Phase 2 architecture contained latent circular dependencies that were silently broken in Phase 3 without updating the Phase 2 specifications**, and that **many `references/` and `templates/` files inside the 57 skills are ultra-brief stubs (3 to 18 lines)**.

| Review Dimension | Classification | Independent Verdict Summary |
| :--- | :--- | :--- |
| **1. Meaningful & Actionable Instructions (57 `SKILL.md`)** | **`PARTIAL`** | All 57 `SKILL.md` files (93–101 lines each) contain concrete UE5/Houdini/Wwise metrics, SOPs, and decision tables, but are generated from a single boilerplate factory (`tools/skill_builder.py`), and their companion `references/` (6–18 lines) and `templates/` (3–25 lines) are thin skeletons rather than deep domain references. |
| **2. Non-Overlapping Responsibilities across 57 Skills** | **`PASS`** | Clear separation of concerns across the 9 poles (`00-direction` to `08-production-quality`), with explicit `Scope Guard` prohibitions preventing cross-role encroachment (e.g., `WLD-05` Blockout vs `WLD-06` Environment Design vs `ART-02` Environment Art). |
| **3. Logical Consistency of Dependencies & Orchestration** | **`PARTIAL`** | The Phase 2 specification (`architecture/skill-dependencies.md`) contained **2 latent circular dependencies** (`WLD-05 <-> ART-05` and `AI-03 <-> ENG-04`). Phase 3 (`tools/registry_data.py`) silently dropped edges to make the graph acyclic without updating `architecture/skill-dependencies.md`, creating 5 specification-to-code mismatches. |
| **4. Source Verification & Claim Support (`SRC-001`..`SRC-020`)** | **`PARTIAL`** | All 20 `SRC-*` IDs exist in `research/source-registry.csv` and are never hallucinated, **but** zero sources were verified from full primary texts (`17` are labeled *"Consultée (Extrait/Index)"* and `3` *"Repérée (À approfondir)"*), and several academic books cited in prose (Heussner, Totten, Adams & Dormans, Swink, Hodent, Farnell, Phillips) are omitted from `source-registry.csv`. |
| **5. Functional Scenarios (Real Outputs vs Artificial Validators)** | **`FAIL`** | `tools/run_functional_scenarios.py` **does not generate any new district, protagonist, mission, traffic, or crowd design artifacts**. It merely invokes `build_dag_plan.py` and runs the skill scripts in their default self-test mode (which validate hardcoded inline Python dictionaries like `BLK-GOMBE-PORT-01` and `DLG-MSN-001-PORT`). |
| **6. ZIP Packages & Claude.ai Usability** | **`PARTIAL`** | All 57 individual ZIPs (`releases/skills/*.zip`), 9 departmental ZIPs (`releases/departments/*.zip`), and the full bundle pass `zipfile.testzip()`. However, **9 departmental ZIPs cannot be uploaded directly as Claude.ai Custom Skills** (Claude.ai requires a single root skill folder containing `SKILL.md`), and individual skill ZIPs reference `knowledge/...` paths that do not exist inside the skill ZIP unless manually uploaded to a Claude Project. |
| **7. Engine Verification (Unreal Engine 5.8, Houdini 22, Wwise)** | **`NOT TESTED`** | **0% runtime execution** in Unreal Engine 5.8, SideFX Houdini 22, or Audiokinetic Wwise. Furthermore, the codebase targets UE 5.0–5.6 / Houdini 20.5–21 conventions (`research/research-gaps.md`) and lacks specific adaptations for **UE 5.8** (MegaLights, Mutable, Scene Graph/Verse, Chaos Flesh/VDM) and **Houdini 22** (Copernicus 2.0, APEX rigging). |

---

## 2. Critical Defects Discovered

### `CRIT-01` — Functional Scenario Runner Validates Hardcoded Self-Test Dictionaries Instead of Generating Scenario Artifacts (`FAIL`)
- **Evidence**: Inspection of [tools/run_functional_scenarios.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/run_functional_scenarios.py#L40-L246).
- **Analysis**:
  - Phase 4 required executing 5 end-to-end functional scenarios (e.g., Scenario 1: *"Concevoir un quartier fictif inspiré de Kinshasa..."*; Scenario 4: *"Concevoir une simulation de circulation comprenant taxis, motos, embouteillages, chauffeurs et interventions policières"*).
  - Instead of producing actual deliverable files for the new fictional district (`DST-BANDAL` is only mentioned in a comment on line 8 of `run_functional_scenarios.py` and nowhere else in the repository) or for police traffic interventions, `run_functional_scenarios.py` simply passes a comma-separated list of skill IDs to `build_dag_plan.py` and then calls `check_spatial_metrics.py`, `simulate_economy.py`, `check_3d_standards.py`, `validate_dialogue_json.py`, `check_l10n_unicode.py`, `check_xag_compliance.py`, `check_perf_budget.py`, and `check_mass_budget.py` **with no `--file` argument**.
  - When called without `--file`, every one of those scripts validates its own hardcoded sample dictionary (e.g., `BLK-GOMBE-PORT-01`, `SM_Kit_Port_Wall_400a`, `DLG-MSN-001-PORT`) and prints `[OK]`.
- **Impact**: The 5 functional scenarios prove only that the DAG topological sort runs on 5 lists of skill IDs and that the 9 scripts pass their own internal unit-test fixtures. They do **not** demonstrate real multi-agent deliverable synthesis.

### `CRIT-02` — Undocumented Divergence Between Phase 2 Dependency Matrix and Phase 3 Code to Hide Circular Dependencies (`PARTIAL`)
- **Evidence**: Comparison of [architecture/skill-dependencies.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/architecture/skill-dependencies.md#L49-L68) against [tools/registry_data.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/registry_data.py#L22-L90) and `DEFAULT_DEPENDENCIES` in [build_dag_plan.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py#L12-L70).
- **Analysis**:
  In Phase 2 (`architecture/skill-dependencies.md`), the critical dependency table explicitly specified:
  1. `WLD-05` (Level Designer) depends on `ART-05` (Animation), **and** `ART-05` depends on `WLD-05` -> **Direct 2-node cycle (`WLD-05 <-> ART-05`)**.
  2. `AI-03` (Traffic AI) depends on `ENG-04` (Houdini), **and** `ENG-04` depends on `AI-03` -> **Direct 2-node cycle (`AI-03 <-> ENG-04`)**.
  To make `tools/check_dag_cycles.py` pass in Phase 3, `tools/registry_data.py` silently altered 5 dependency definitions without updating `architecture/skill-dependencies.md`:
  - **`WLD-04`**: Architecture requires `['DIR-04', 'GD-01', 'WLD-01', 'WLD-03']`; Code uses `['DIR-04', 'DIR-05', 'WLD-01', 'WLD-03']` (`GD-01` dropped).
  - **`WLD-05`**: Architecture requires `['ART-05', 'GD-02', 'GD-05', 'WLD-04']`; Code uses `['GD-02', 'GD-05', 'WLD-04']` (`ART-05` dropped to break cycle).
  - **`AI-03`**: Architecture requires `['ENG-04', 'GD-06', 'WLD-03']`; Code uses `['DIR-04', 'GD-06', 'WLD-03']` (`ENG-04` dropped to break cycle).
  - **`ENG-02`**: Architecture requires `GD-01..GD-06` + `ENG-01`; Code omits `GD-03` (Economy) and `GD-04` (Progression).
  - **`ENG-07`**: Architecture requires `ENG-01..ENG-06` + `ART-07`, `ART-09`; Code omits `ENG-03` (Tools Programmer).
- **Impact**: In Scenario 1 and Scenario 4, `build_dag_plan.py` schedules `AI-03` (Traffic AI) in Wave 10/11 **before** `ENG-04` (Houdini) in Wave 12, even though `AI-03`'s `SKILL.md` states its required input is `houdini-zonegraph-splines-eng-04`.

### `CRIT-03` — Code Duplication of the 57-Skill DAG Graph Between `tools/registry_data.py` and `build_dag_plan.py` (`PARTIAL`)
- **Evidence**: [tools/registry_data.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/registry_data.py#L22-L90) vs [skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py#L12-L85).
- **Analysis**: `DEFAULT_DEPENDENCIES` and `DEFAULT_STRATA` are hardcoded as a duplicate dictionary inside `build_dag_plan.py` (and inside the string literal `BUILD_DAG_SCRIPT` in `tools/departments/dept_00_direction.py`), violating the single-source-of-truth and no-duplication engineering rules. No test in `tests/` verifies that `build_dag_plan.py`'s `DEFAULT_DEPENDENCIES` matches `CANONICAL_SKILLS` in `tools/registry_data.py`.

---

## 3. Structural & Architectural Weaknesses

### 3.1 Architecture Drift on Directory Naming (`assets/` vs `templates/` + `examples/`)
- **Finding (`PARTIAL`)**: [architecture/file-structure.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/architecture/file-structure.md#L130-L139) and [architecture/system-architecture.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/architecture/system-architecture.md#L15) specify that every skill directory contains `SKILL.md`, `references/`, and `assets/`. The Phase 3 implementation replaced `assets/` with `templates/` and `examples/` (and `scripts/`) to match the Phase 3 prompt, and added `schemas/`, `templates/`, `tests/`, `docs/`, `releases/`, and `audit/` at the root, **without updating `architecture/file-structure.md` or `architecture/quality-standards.md`** (which still references `assets/` on line 48).

### 3.2 Fragile Custom YAML Parser (`tools/__init__.py`)
- **Finding (`PARTIAL`)**: [tools/__init__.py](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/tools/__init__.py#L51-L115) implements `parse_simple_yaml()` in 65 lines of pure Python to avoid a `PyYAML` dependency. While it succeeds on the 57 generated `SKILL.md` files, read-only testing confirms it fails on standard YAML constructs:
  - **Multiline block scalars (`|` or `>`)**: Raises `YamlParseError: Ligne 2: syntaxe clé:valeur attendue`.
  - **Quoted strings containing commas inside inline lists (`["a, b", "c"]`)**: `_parse_scalar` splits naively on `,` (`inner.split(",")`), corrupting quoted list elements.
  - **Inline comments after unquoted values (`version: 1.0.0 # initial`)**: Retains `# initial` as part of the string value.
  - **JSON Schema Enforcement**: The JSON schemas in `schemas/skill-frontmatter.schema.json`, `schemas/entity-registry.schema.json`, and `schemas/task-envelope.schema.json` are never programmatically evaluated by a JSON Schema validator; validation rules are re-coded imperatively in `lint_skills.py` and `validate_registry.py`.

---

## 4. Assessment of the 57 Skills: Depth, Superficiality & Missing Capabilities

### 4.1 Uniform Template Generation & Thin Reference/Template Files (`PARTIAL`)
All 57 skills were generated via `tools/skill_builder.py` from `tools/departments/dept_00_direction.py` through `dept_08_production_quality.py`.
- **Strengths**:
  - Every `SKILL.md` (93–101 lines, ~600–760 words) is well-structured, completely free of generic filler (*"Tu es un expert exceptionnel"*), and grounded in specific Kinshasa entities (`LOC-GOMBE-PORT`, `LOC-MATONGE-VICTOIRE`, `LOC-LIMETE-ECHANGEUR`, `VEH-MOTO-WEWA-01`) and UE5 budgets (`16.6 ms`, `350 cm` corridors, `10.24 px/cm` texel density, `<= 24` `AI-01` NPCs, `600` `AI-02` Mass entities).
- **Superficial Sub-files (`references/` and `templates/`)**:
  - Because progressive disclosure is meant to offload heavy technical specifications from `SKILL.md` into `references/` and `templates/`, `references/` files should be more detailed than `SKILL.md`. In reality, **all 57 `references/` files are only 6 to 18 lines long**, and **17 `templates/` CSV files are only 3 to 5 lines long** (1 header line + 2 or 3 sample rows):
    - `prd-02-risk-manager`: `references/risk-scoring-and-mitigation.md` is **6 lines**; `templates/risk-register-template.csv` is **4 lines**; `examples/sample-risk-register.md` is **8 lines**.
    - `art-06-motion-capture-specialist`: `references/mocap-pipeline-and-retargeting.md` is **7 lines**; `templates/mocap-shotlist-template.csv` is **4 lines**.
    - `gd-03-economy-designer`: `references/faucets-and-sinks-math.md` is **7 lines**; `templates/economy-balance-sheet.csv` is **4 lines**.
    - `aud-04-voice-localization-specialist`: `templates/localized-string-table.csv` is **3 lines**.
    - `eng-03-tools-programmer`: `references/ue5-data-validation-and-tools.md` is **7 lines**.

### 4.2 Only 9 of 57 Skills Have Executable Scripts (`PARTIAL`)
Only 1 skill per department (9/57 total: `DIR-01`, `NAR-04`, `WLD-05`, `GD-03`, `AI-02`, `ART-04`, `AUD-04`, `ENG-07`, `PRD-06`) has a `scripts/` directory. The other 48 skills (including highly algorithmic roles such as `NAR-06` Continuity Editor, `GD-04` Progression Designer, `GD-05` Combat Frame-Data Designer, `AI-03` Traffic Deadlock Calculator, `ART-08` Shader PSO Permutation Calculator, `PRD-02` Risk Matrix Calculator, and `PRD-03` Documentation Specialist) have no executable scripts.

### 4.3 Missing Capabilities Across the Studio OS
1. **No Live Telemetry / Analytics Skill (`PROD-05` dropped between Phase 1 and Phase 2)**:
   - In [research/technical-reference.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/research/technical-reference.md#L65-L78) and [research/skills-coverage-matrix.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/research/skills-coverage-matrix.md#L9), `PROD-05` (*LiveOps & Telemetry Analytics*, producing heatmaps of player deaths/bottlenecks in Kinshasa) was classified as a required domain. In Phase 2/3, it was silently dropped and is only tangentially mentioned as an input to `GD-03`.
2. **No Dedicated Police / Law-Enforcement Escalation System (`SYS-LAW-*`)**:
   - Scenario 4 requires *"interventions policières"* in traffic. While `AI-01` and `AI-04` mention syndicate guards (`ORG-CARTEL-FLEUVE`) and shakedowns, `knowledge/entities-registry.csv` and `knowledge/technical-specs/gameplay-tags-taxonomy.csv` contain **zero entity (`ORG-POLICE-*`), zero system (`SYS-LAW-*`), and zero Gameplay Tag (`State.World.WantedLevel.*`)** for police dispatch, roadblocks, or pursuit escalation.
3. **No Facial Rigging / FACS / Lingala Viseme Mapping in `ART-06` or `AUD-04`**:
   - While `ART-06` cites `MetaHuman Animator` and `AUD-04` cites Unicode vowels `ɛ` and `ɔ`, neither skill defines phonetic-to-viseme mapping rules for Lingala open vowels and pre-nasalized consonants (`mb`, `nd`, `ng`, `nz`) which standard English MetaHuman phoneme solvers frequently misalign.

---

## 5. Source Verification Findings (`PARTIAL`)

Inspection of [research/source-registry.csv](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/research/source-registry.csv) and [audit/source-verification.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/audit/source-verification.md) reveals:
1. **Existence & Honesty (`PASS`)**: All 20 registered sources (`SRC-001` through `SRC-020`) correspond to real, verifiable industry documentation, GDC talks, books, or public GitHub repositories. The registry honestly labels 17 of them as *"Consultée (Extrait/Index)"* and 3 (`SRC-008`, `SRC-014`, `SRC-020`) as *"Repérée (À approfondir)"*.
2. **Secondary URLs Used for GDC Talks (`PARTIAL`)**:
   - `SRC-008` (*Procedurally Crafting Manhattan for Marvel's Spider-Man*) points to an unofficial third-party GitHub markdown list (`https://github.com/davidgm94/engine-resources/blob/master/.old-gdc.md`) rather than the official GDC Vault record.
   - `SRC-014` (*Procedural Generation of Cinematic Dialogues in Assassin's Creed Odyssey*) points to a session index (`https://thetoolsmiths.org/codex/gdc/procedural_content_generation/sessions`) rather than slides or transcript.
   - `SRC-015` (*Player Locomotion in Red Dead Redemption 2*) points to a brief GDC promotional preview article (`gdconf.com/article/...`) rather than technical talk proceedings.
3. **Unregistered Academic & Industry Sources Cited in `architecture/skills-catalog.md` (`PARTIAL`)**:
   - Over a dozen books and standards are cited as authoritative references in `architecture/skills-catalog.md` and `research/technical-reference.md`—including **Filip De Boeck** (*Kinshasa: Tales of the Invisible City*), **Heussner et al.** (*The Game Narrative Toolbox*), **Totten** (*An Architectural Approach to Level Design*), **Adams & Dormans** (*Game Mechanics*), **Swink** (*Game Feel*), **Hodent** (*The Gamer's Brain*), **Farnell** (*Designing Sound*), **Phillips** (*A Composer's Guide to Game Music*), **O'Hagan & Mangiron** (*Game Localization*), **Bhatti** (*Docs for Developers*), and **Microsoft Xbox Accessibility Guidelines (XAG)**—yet **none of them have a `SRC-*` entry in `research/source-registry.csv`**.

---

## 6. ZIP Package & Claude.ai Compatibility Inspection (`PARTIAL`)

Read-only inspection of `releases/` confirmed:
1. **Archive Integrity (`PASS`)**:
   - `releases/skills/*.zip`: 57 archives, all pass `zipfile.testzip()`, each structured with a single root folder `<skill-slug>/SKILL.md` + `references/` + `templates/` + `examples/` (+ `scripts/`).
   - `releases/departments/*.zip`: 9 archives (`00-direction.zip` .. `08-production-quality.zip`), all pass `zipfile.testzip()`.
   - `releases/zaire-studio-os-v1.0.0-full.zip`: 657,152 bytes, passes `zipfile.testzip()`.
2. **Claude.ai Custom Skill Upload Limitation on Departmental ZIPs (`PARTIAL`)**:
   - Claude.ai's *Custom Skills* uploader requires a ZIP archive with `SKILL.md` inside a single skill root directory. The 9 departmental ZIPs (`releases/departments/00-direction.zip`, etc.) contain multiple nested skill subdirectories (`00-direction/dir-01-studio-orchestrator/SKILL.md`, `00-direction/dir-02-executive-producer/SKILL.md`, ...) and **will be rejected by Claude.ai's Skill uploader** if a user attempts to upload a departmental ZIP directly as a skill. [docs/claude-ai-installation-guide.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/docs/claude-ai-installation-guide.md) mentions the departmental archives on line 11 without warning users that they are archival bundles that must be unzipped before uploading individual skills to Claude.ai.
3. **Unbundled Cross-References to `knowledge/` Inside Individual Skill ZIPs (`PARTIAL`)**:
   - Every `SKILL.md` instructs the agent to read `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, and `knowledge/technical-specs/spatial-metrics.md`. Those files are **not** packaged inside `releases/skills/<skill-slug>.zip`. While `docs/claude-ai-installation-guide.md` explains how to upload `knowledge/` into a Claude.ai *Project*, an individual skill ZIP used standalone in a regular Claude.ai chat outside a configured Project lacks access to those files.

---

## 7. Untested Systems in Unreal Engine 5.8, SideFX Houdini 22 & Audiokinetic Wwise (`NOT TESTED`)

All engine-level integrations are strictly **`NOT TESTED`** (0% binary or runtime verification). Furthermore, inspecting the technical specifications against the specific target versions **Unreal Engine 5.8**, **Houdini 22**, and **Wwise** reveals version-gap limitations:

| Target Platform | Subsystem / Pipeline | Status | Specific Technical Gap & Untested Scope |
| :--- | :--- | :--- | :--- |
| **Unreal Engine 5.8** | **C++20 / UBT Compilation (`ENG-01`..`03`)** | **`NOT TESTED`** | C++ class headers (`UZaireDistrictStreamingSubsystem`, `UZaireGA_MeleeParry`, `UZaireNaniteAndTextureValidator`) have never been compiled against UE 5.8 headers or UnrealHeaderTool (UHT). |
| **Unreal Engine 5.8** | **Lighting (`ART-07`, `ENG-06`) — MegaLights** | **`NOT TESTED`** | `ART-07` restricts overlapping VSM shadow-casting local lights to `<= 3` based on UE 5.1–5.4 Lumen/VSM constraints, without accounting for or testing UE 5.5–5.8 **MegaLights** (stochastic direct lighting allowing hundreds of shadow-casting area/neon lights in scenes like nocturnal `DST-MATONGE`). |
| **Unreal Engine 5.8** | **Modular Characters (`ART-03`, `AI-02`) — Mutable** | **`NOT TESTED`** | `ART-03` specifies custom 5-slot mesh merging and `CustomPrimitiveData`, without testing or integrating Unreal Engine's native **Mutable Character Customization** plugin (`CustomizableObject`) for runtime mesh/texture merging and LOD generation. |
| **Unreal Engine 5.8** | **Animation (`ART-05`) — Next-Gen AnimNext / Choosers** | **`NOT TESTED`** | `ART-05` specifies traditional `Animation Blueprints` + `Pose Search`, without testing UE 5.5–5.8 **AnimNext** and **Chooser Tables** for data-driven animation selection at scale. |
| **Unreal Engine 5.8** | **MassEntity / MassTraffic (`AI-02`, `AI-03`)** | **`NOT TESTED`** | The custom sub-lane splitting algorithm (`130-150 cm` Wewa motorcycle corridors) and intersection deadlock watchdog (`8.0 s`) are prose specifications only; no C++ `UMassProcessor` or `ZoneGraph` lane profile has been compiled or profiled in Unreal Insights. |
| **Unreal Engine 5.8** | **Gauntlet Automation (`PRD-05`) & PSO Precache (`ENG-07`)** | **`NOT TESTED`** | `UZaireGauntletTraversalController` and `.upipelinecache` warmup have never been executed on a cooked IoStore `.utoc`/`.ucas` build. |
| **SideFX Houdini 22** | **HDA / PDG & UE5 PCG Bridge (`ENG-04`)** | **`NOT TESTED`** | No `.hda` or `.hip` file exists in the workspace. Specifications rely on UE 5.0/5.1 *City Sample* (`SRC-004`, `SRC-005`) and do not test **Houdini 22** features (**Copernicus 2.0** GPU texture/heightfield processing for Congo River DEM/RVT masks, **APEX** procedural rigging, or the updated **Houdini Engine for UE 5.8 PCG** data-asset interop). |
| **Audiokinetic Wwise** | **Wwise Authoring / WAAPI / SoundBanks (`AUD-01`..`03`)** | **`NOT TESTED`** | No `.wproj`, `.wwu`, or WAAPI script exists. The 64-physical-voice ceiling, `-23 LUFS` HDR ducking, Spatial Audio `AkRoom`/`AkPortal` diffraction, and `SW_Music_LicenseMode = STREAMER_SAFE` switch have never been profiled in Wwise Profiler. |

---

## 8. Prioritized Recommendations for Remediation

### Priority 1 — Critical (Must Fix Before Claiming Functional Verification)
1. **`[P0-1]` Replace Mock Self-Tests in `tools/run_functional_scenarios.py` with Real Artifact Generation & Validation**:
   - Have `run_functional_scenarios.py` generate and write actual scenario deliverable files (e.g., `DST-BANDAL` district profile, blockout metrics JSON, dialogue tree JSON, localization table JSON, XAG audit JSON, and performance profile JSON) and pass them via `--file` to the 9 validators.
2. **`[P0-2]` Reconcile the Dependency Graph Between `architecture/skill-dependencies.md` and `tools/registry_data.py`**:
   - Update `architecture/skill-dependencies.md` to match the acyclic DAG in `tools/registry_data.py` (explaining how `WLD-05 <-> ART-05` and `AI-03 <-> ENG-04` are resolved via Strate 1 spatial metrics and `WLD-03` road specs), **or** introduce a two-stage handoff node so `ENG-04` exports `ZoneGraph` splines before `AI-03` configures traffic rules.
3. **`[P0-3]` Eliminate DAG Dictionary Duplication in `build_dag_plan.py`**:
   - Add a unit test in `tests/test_foundation.py` asserting that `DEFAULT_DEPENDENCIES` and `DEFAULT_STRATA` in `skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py` are 100% identical to `CANONICAL_SKILLS` in `tools/registry_data.py`.

### Priority 2 — High (Content Depth & Missing Domain Systems)
4. **`[P1-1]` Expand the 57 `references/` and `templates/` Files from 6–18 Line Stubs to Production Depth**:
   - Enrich the `references/` files (especially `PRD-02`, `ART-06`, `ART-07`, `AUD-03`, `AUD-04`, `GD-03`, `ENG-03`) with complete decision trees, parameter tables, and edge-case checklists (50–120 lines each).
5. **`[P1-2]` Add Police / Law-Enforcement Entities and Gameplay Tags for Traffic & Open-World Escalation**:
   - Register `ORG-POLICE-PCR` (Police de Circulation Routière), `SYS-LAW-ESCALATION`, and `State.World.AlertLevel.*` in `knowledge/entities-registry.csv` and `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.
6. **`[P1-3]` Restore Telemetry & Analytics Coverage (`PROD-05`)**:
   - Either add a dedicated telemetry specification to `PRD-05` / `GD-03` or add a 58th skill covering playtest heatmap instrumentation.

### Priority 3 — Medium (Tooling Hardening, Sources & Engine Modernisation)
7. **`[P2-1]` Harden `parse_simple_yaml()` & Add Explicit Warning in `claude-ai-installation-guide.md`**:
   - Support quoted commas in inline lists and multiline block scalars (`|` / `>`) in `tools/__init__.py`.
   - Clarify in `docs/claude-ai-installation-guide.md` that `releases/departments/*.zip` are multi-skill archival bundles that must be unzipped before uploading individual skills to Claude.ai, and bundle a read-only snapshot of `knowledge/entities-registry.csv` inside each standalone skill ZIP.
8. **`[P2-2]` Register All Cited Academic Books in `research/source-registry.csv` & Update Engine Specs for UE 5.8 / Houdini 22**:
   - Assign `SRC-021`..`SRC-032` to the cited books (De Boeck, Heussner, Totten, Adams & Dormans, Swink, Hodent, Farnell, Phillips, XAG).
   - Add UE 5.8 (**MegaLights**, **Mutable**, **AnimNext/Choosers**) and Houdini 22 (**Copernicus 2.0**) technical guidelines to `ART-03`, `ART-05`, `ART-07`, `ENG-04`, and `ENG-06`.
