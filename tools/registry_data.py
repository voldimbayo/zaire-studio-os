"""Catalogue canonique des 57 Agent Skills de ZAÏRE STUDIO OS (v1.1.0).

Ce module est la SOURCE UNIQUE DE VÉRITÉ (Single Source of Truth) pour :
- La topologie des 57 skills à travers les 9 départements.
- Leurs strates d'exécution (0 à 5).
- Leurs dépendances amont (`upstream_ids`) strictement acycliques (DAG), réconciliées entre :
  * `architecture/skill-dependencies.md`
  * `docs/canonical-dependency-registry.md`
  * `skills/00-direction/dir-01-studio-orchestrator/scripts/build_dag_plan.py`
  * Les 57 fichiers `SKILL.md` sur disque.

Décisions d'Architecture de Réconciliation (Phase 5 Workstream 1) :
1. Résolution `ENG-04 -> AI-03` : `ENG-04` (Houdini Specialist, Strate 3) dépend de `("WLD-03", "ART-02", "GD-06")`
   et génère les splines routières `ZoneGraph` à partir des données OSM (`WLD-03`), des kits modulaires (`ART-02`)
   et des gabarits véhicules (`GD-06`). `AI-03` (Traffic AI Specialist, Strate 3) dépend de `("ENG-04", "GD-06", "WLD-03", "DIR-04")`
   et s'exécute APRÈS `ENG-04`, garantissant que le réseau `ZoneGraph` est disponible avant la configuration de `MassTraffic`.
2. Résolution `WLD-05 -> ART-05` : Les métriques spatiales de base (`1 UU = 1 cm`, couloir `>= 350 cm`, vault `100 cm`,
   ledge grab `260-300 cm`) sont gelées en Strate 0/1 par `DIR-05` dans `knowledge/technical-specs/spatial-metrics.md`.
   `WLD-05` (Level Designer, Strate 2) dépend de `("WLD-04", "GD-02", "GD-05", "DIR-05")` pour construire le blockout.
   `ART-05` (Animation Specialist, Strate 3) dépend de `("WLD-05", "GD-05", "ART-06")` pour caler le Motion Warping
   sur les blockouts validés. Zéro cycle.
3. Alignement complet des dépendances de `WLD-04`, `ENG-02` et `ENG-07` avec `architecture/skill-dependencies.md` :
   - `WLD-04` dépend de `("WLD-01", "WLD-03", "GD-01", "DIR-04", "DIR-05")` (`GD-01` est donc en Strate 1 amont).
   - `ENG-02` dépend de `("GD-01", "GD-02", "GD-03", "GD-04", "GD-05", "GD-06", "GD-07", "ENG-01")`.
   - `ENG-07` dépend de `("ENG-01", "ENG-02", "ENG-03", "ENG-04", "ENG-05", "ENG-06", "ART-07", "ART-09", "AI-01", "AI-02", "AI-03")`.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SkillSpec:
    skill_id: str
    slug: str
    title: str
    department: str
    stratum: int
    upstream_ids: tuple[str, ...]


CANONICAL_SKILLS: tuple[SkillSpec, ...] = (
    # 00-direction (7 skills : DIR-01..05 en Strate 0, DIR-06..07 en Strate 5 Gatekeeping)
    SkillSpec("DIR-01", "dir-01-studio-orchestrator", "Studio Orchestrator", "00-direction", 0, ()),
    SkillSpec("DIR-02", "dir-02-executive-producer", "Executive Producer", "00-direction", 0, ("DIR-01",)),
    SkillSpec("DIR-03", "dir-03-creative-director", "Creative Director", "00-direction", 0, ("DIR-01",)),
    SkillSpec("DIR-04", "dir-04-technical-director", "Technical Director", "00-direction", 0, ("DIR-01",)),
    SkillSpec("DIR-05", "dir-05-lead-game-designer", "Lead Game Designer", "00-direction", 0, ("DIR-01", "DIR-03")),
    SkillSpec("DIR-06", "dir-06-documentation-director", "Documentation Director", "00-direction", 5, ("PRD-03", "NAR-06")),
    SkillSpec("DIR-07", "dir-07-quality-director", "Quality Director", "00-direction", 5, ("PRD-04", "PRD-05", "PRD-06", "ENG-07")),
    # 01-narrative (6 skills)
    SkillSpec("NAR-01", "nar-01-narrative-architect", "Narrative Architect", "01-narrative", 1, ("DIR-03", "WLD-01", "WLD-02")),
    SkillSpec("NAR-02", "nar-02-screenwriter", "Screenwriter", "01-narrative", 2, ("NAR-01", "NAR-03", "GD-02")),
    SkillSpec("NAR-03", "nar-03-character-writer", "Character Writer", "01-narrative", 2, ("NAR-01", "WLD-01", "WLD-02")),
    SkillSpec("NAR-04", "nar-04-dialogue-designer", "Dialogue Designer", "01-narrative", 2, ("NAR-02", "NAR-03", "GD-02")),
    SkillSpec("NAR-05", "nar-05-lore-manager", "Lore Manager", "01-narrative", 2, ("WLD-01", "WLD-02", "NAR-01")),
    SkillSpec("NAR-06", "nar-06-continuity-editor", "Continuity Editor", "01-narrative", 5, ("NAR-01", "NAR-02", "NAR-03", "NAR-04", "NAR-05", "GD-02")),
    # 02-world-design (6 skills)
    SkillSpec("WLD-01", "wld-01-worldbuilding-architect", "Worldbuilding Architect", "02-world-design", 1, ("DIR-03", "WLD-02", "WLD-03")),
    SkillSpec("WLD-02", "wld-02-cultural-researcher", "Cultural Researcher", "02-world-design", 1, ("DIR-03",)),
    SkillSpec("WLD-03", "wld-03-urban-researcher", "Urban Researcher", "02-world-design", 1, ("DIR-03", "DIR-04")),
    SkillSpec("WLD-04", "wld-04-open-world-designer", "Open World Designer", "02-world-design", 1, ("WLD-01", "WLD-03", "GD-01", "DIR-04", "DIR-05")),
    SkillSpec("WLD-05", "wld-05-level-designer", "Level Designer", "02-world-design", 2, ("WLD-04", "GD-02", "GD-05", "DIR-05")),
    SkillSpec("WLD-06", "wld-06-environment-designer", "Environment Designer", "02-world-design", 2, ("WLD-05", "ART-01", "WLD-02", "WLD-03")),
    # 03-game-design (7 skills)
    SkillSpec("GD-01", "gd-01-game-systems-designer", "Game Systems Designer", "03-game-design", 1, ("DIR-03", "DIR-05")),
    SkillSpec("GD-02", "gd-02-mission-designer", "Mission Designer", "03-game-design", 2, ("NAR-01", "WLD-04", "GD-01")),
    SkillSpec("GD-03", "gd-03-economy-designer", "Economy Designer", "03-game-design", 2, ("GD-01", "GD-02", "DIR-02")),
    SkillSpec("GD-04", "gd-04-progression-designer", "Progression Designer", "03-game-design", 2, ("GD-01", "GD-05", "NAR-01")),
    SkillSpec("GD-05", "gd-05-combat-designer", "Combat Designer", "03-game-design", 2, ("GD-01", "DIR-05")),
    SkillSpec("GD-06", "gd-06-vehicle-designer", "Vehicle Designer", "03-game-design", 2, ("WLD-03", "GD-01", "DIR-05")),
    SkillSpec("GD-07", "gd-07-ui-ux-designer", "UI/UX Designer", "03-game-design", 2, ("GD-01", "GD-02", "ART-01")),
    # 04-ai-simulation (4 skills)
    SkillSpec("AI-01", "ai-01-npc-ai-architect", "NPC AI Architect", "04-ai-simulation", 3, ("GD-05", "WLD-05", "DIR-04")),
    SkillSpec("AI-02", "ai-02-crowd-simulation-specialist", "Crowd Simulation Specialist", "04-ai-simulation", 3, ("WLD-04", "ART-03", "DIR-04")),
    SkillSpec("AI-03", "ai-03-traffic-ai-specialist", "Traffic AI Specialist", "04-ai-simulation", 3, ("ENG-04", "GD-06", "WLD-03", "DIR-04")),
    SkillSpec("AI-04", "ai-04-decision-systems-designer", "Decision Systems Designer", "04-ai-simulation", 3, ("WLD-01", "GD-01", "NAR-04")),
    # 05-art-animation (9 skills)
    SkillSpec("ART-01", "art-01-art-director", "Art Director", "05-art-animation", 1, ("DIR-03", "WLD-02", "WLD-03")),
    SkillSpec("ART-02", "art-02-environment-artist", "Environment Artist", "05-art-animation", 3, ("WLD-06", "ART-04")),
    SkillSpec("ART-03", "art-03-character-artist", "Character Artist", "05-art-animation", 3, ("NAR-03", "WLD-02", "ART-01", "ART-04")),
    SkillSpec("ART-04", "art-04-3d-pipeline-specialist", "3D Pipeline Specialist", "05-art-animation", 1, ("DIR-04", "ART-01")),
    SkillSpec("ART-05", "art-05-animation-specialist", "Animation Specialist", "05-art-animation", 3, ("WLD-05", "GD-05", "ART-06")),
    SkillSpec("ART-06", "art-06-motion-capture-specialist", "Motion Capture Specialist", "05-art-animation", 3, ("NAR-02", "GD-05")),
    SkillSpec("ART-07", "art-07-lighting-specialist", "Lighting Specialist", "05-art-animation", 3, ("ART-01", "WLD-05", "ART-02", "DIR-04")),
    SkillSpec("ART-08", "art-08-technical-artist", "Technical Artist", "05-art-animation", 3, ("ART-02", "ART-03", "ART-04", "DIR-04")),
    SkillSpec("ART-09", "art-09-vfx-specialist", "VFX Specialist", "05-art-animation", 3, ("ART-01", "GD-05", "ART-07", "DIR-04")),
    # 06-audio-localization (4 skills)
    SkillSpec("AUD-01", "aud-01-audio-director", "Audio Director", "06-audio-localization", 1, ("DIR-03", "WLD-01", "WLD-02")),
    SkillSpec("AUD-02", "aud-02-sound-designer", "Sound Designer", "06-audio-localization", 3, ("AUD-01", "GD-05", "GD-06", "WLD-06")),
    SkillSpec("AUD-03", "aud-03-music-designer", "Music Designer", "06-audio-localization", 3, ("AUD-01", "WLD-02", "GD-01", "GD-05")),
    SkillSpec("AUD-04", "aud-04-voice-localization-specialist", "Voice and Localization Specialist", "06-audio-localization", 3, ("NAR-04", "GD-07", "WLD-02")),
    # 07-engineering (8 skills : ENG-01 en Strate 1, ENG-04 en Strate 3 pour précéder AI-03, ENG-02..08 en Strate 4)
    SkillSpec("ENG-01", "eng-01-unreal-engine-specialist", "Unreal Engine Specialist", "07-engineering", 1, ("DIR-04", "WLD-04", "ART-04")),
    SkillSpec("ENG-02", "eng-02-gameplay-programmer", "Gameplay Programmer", "07-engineering", 4, ("GD-01", "GD-02", "GD-03", "GD-04", "GD-05", "GD-06", "GD-07", "ENG-01")),
    SkillSpec("ENG-03", "eng-03-tools-programmer", "Tools Programmer", "07-engineering", 4, ("ART-04", "ENG-01")),
    SkillSpec("ENG-04", "eng-04-houdini-specialist", "Houdini Specialist", "07-engineering", 3, ("WLD-03", "ART-02", "GD-06")),
    SkillSpec("ENG-05", "eng-05-physics-engineer", "Physics Engineer", "07-engineering", 4, ("GD-06", "ART-02", "DIR-04")),
    SkillSpec("ENG-06", "eng-06-rendering-engineer", "Rendering Engineer", "07-engineering", 4, ("DIR-04", "ART-07", "ART-08")),
    SkillSpec("ENG-07", "eng-07-performance-engineer", "Performance Engineer", "07-engineering", 4, ("ENG-01", "ENG-02", "ENG-03", "ENG-04", "ENG-05", "ENG-06", "ART-07", "ART-09", "AI-01", "AI-02", "AI-03")),
    SkillSpec("ENG-08", "eng-08-build-engineer", "Build Engineer", "07-engineering", 4, ("ENG-01", "ENG-02", "ENG-03", "ENG-07")),
    # 08-production-quality (6 skills)
    SkillSpec("PRD-01", "prd-01-production-planner", "Production Planner", "08-production-quality", 1, ("DIR-01", "DIR-02")),
    SkillSpec("PRD-02", "prd-02-risk-manager", "Risk Manager", "08-production-quality", 1, ("DIR-02", "DIR-04", "WLD-02")),
    SkillSpec("PRD-03", "prd-03-documentation-specialist", "Documentation Specialist", "08-production-quality", 5, ("NAR-05", "WLD-01", "GD-01", "ENG-01")),
    SkillSpec("PRD-04", "prd-04-qa-architect", "QA Architect", "08-production-quality", 5, ("GD-02", "WLD-04", "ENG-02")),
    SkillSpec("PRD-05", "prd-05-test-engineer", "Test Engineer", "08-production-quality", 5, ("PRD-04", "ENG-07", "ENG-08")),
    SkillSpec("PRD-06", "prd-06-accessibility-specialist", "Accessibility Specialist", "08-production-quality", 5, ("GD-07", "GD-05", "AUD-04")),
)

SKILLS_BY_ID: dict[str, SkillSpec] = {spec.skill_id: spec for spec in CANONICAL_SKILLS}
SKILLS_BY_SLUG: dict[str, SkillSpec] = {spec.slug: spec for spec in CANONICAL_SKILLS}
