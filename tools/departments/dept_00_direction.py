"""Spécifications et génération du Département 00-DIRECTION (DIR-01 à DIR-07)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.registry_data import CANONICAL_SKILLS
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint


def _generate_build_dag_script() -> str:
    """Génère le script build_dag_plan.py directement à partir de CANONICAL_SKILLS (zéro duplication manuelle)."""
    deps_lines = [
        f'    "{spec.skill_id}": {list(spec.upstream_ids)!r},'
        for spec in CANONICAL_SKILLS
    ]
    strata_lines = [
        f'    "{spec.skill_id}": {spec.stratum},'
        for spec in CANONICAL_SKILLS
    ]
    deps_block = "\n".join(deps_lines)
    strata_block = "\n".join(strata_lines)
    return f'''"""Planificateur topologique DAG déterministe pour DIR-01 (Studio Orchestrator).

Généré automatiquement depuis la source unique de vérité `tools/registry_data.py` (`CANONICAL_SKILLS`).
"""

from __future__ import annotations

import argparse
import json
import sys


DEFAULT_DEPENDENCIES: dict[str, list[str]] = {{
{deps_block}
}}

DEFAULT_STRATA: dict[str, int] = {{
{strata_block}
}}


def compute_waves(selected_skills: list[str], dep_map: dict[str, list[str]] | None = None) -> list[list[str]]:
    """Regroupe les skills sélectionnés en vagues d'exécution parallèles selon leurs dépendances et strates."""
    if not selected_skills:
        raise ValueError("La liste des skills sélectionnés ne peut pas être vide.")
    graph = dep_map or DEFAULT_DEPENDENCIES
    unknown = sorted(s for s in selected_skills if s not in graph)
    if unknown:
        raise ValueError(f"Skill(s) inconnu(s) du catalogue ZAÏRE STUDIO OS : {{', '.join(unknown)}}")
    active_set = set(selected_skills)
    remaining = set(active_set)
    completed: set[str] = set()
    waves: list[list[str]] = []

    while remaining:
        deps_satisfied = [
            skill
            for skill in remaining
            if all((dep not in active_set) or (dep in completed) for dep in graph[skill])
        ]
        if not deps_satisfied:
            raise ValueError(f"Cycle de dépendances détecté parmi : {{sorted(remaining)}}")
        min_stratum = min(DEFAULT_STRATA.get(s, 0) for s in deps_satisfied)
        ready = sorted(s for s in deps_satisfied if DEFAULT_STRATA.get(s, 0) == min_stratum)
        waves.append(ready)
        completed.update(ready)
        remaining -= set(ready)

    return waves


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Génère un plan d'exécution DAG en JSON.")
    parser.add_argument(
        "--skills",
        required=True,
        help="Liste d'IDs de skills séparés par des virgules (ex: WLD-02,WLD-03,GD-02,NAR-02,NAR-06)",
    )
    parser.add_argument(
        "--output",
        help="Chemin du fichier JSON de sortie (optionnel)",
    )
    args = parser.parse_args()
    skills = [s.strip().upper() for s in args.skills.split(",") if s.strip()]
    try:
        waves = compute_waves(skills)
    except ValueError as exc:
        print(f"[ERREUR] {{exc}}", file=sys.stderr)
        return 1
    payload = {{
        "orchestrator": "DIR-01",
        "requested_skills_count": len(skills),
        "waves": [{{"wave_index": idx + 1, "parallel_skills": w}} for idx, w in enumerate(waves)],
    }}
    formatted = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(formatted + "\\n", encoding="utf-8")
    print(formatted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


BUILD_DAG_SCRIPT = _generate_build_dag_script()

DIRECTION_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="DIR-01",
        description=(
            "Point d'entrée unique et orchestrateur central de ZAÏRE STUDIO OS. Analyse les requêtes "
            "utilisateurs, vérifie les entités dans knowledge/entities-registry.csv, construit le Graphe "
            "Orienté Acyclique (DAG) d'exécution en vagues parallèles, émet les Task Envelopes typées "
            "et consolide les livrables inter-départements."
        ),
        inputs=("user-request", "knowledge/entities-registry.csv", "architecture/skill-dependencies.md"),
        outputs=("execution-plan-dag.json", "task-envelopes.json", "consolidated-brief.md"),
        activation_triggers=(
            "Toute requête utilisateur transversale impliquant 2 ou plusieurs départements (ex: création d'une mission, d'un quartier de Kinshasa ou d'un système complet).",
            "Demande d'arbitrage entre contraintes techniques (DIR-04/ENG-07) et ambitions créatives ou ludiques (DIR-03/DIR-05).",
            "Détection d'une entité en statut BLOCKED ou RESEARCH_REQUIRED nécessitant un reroutage dynamique.",
        ),
        scope_boundaries=(
            "Ne rédige jamais directement le contenu métier spécialisé (pas de code C++ UE5, pas de dialogues littéraires, pas de shaders HLSL, pas de tables d'économie).",
            "N'altère pas le statut d'une entité vers CONFIRMED sans la signature conjointe de DIR-06 et DIR-07.",
        ),
        operational_procedures=(
            "Phase INTAKE : Extraire toutes les entités explicites ou implicites de la requête et consulter `knowledge/entities-registry.csv` pour vérifier leur statut (`CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`).",
            "Phase PLANNING : Sélectionner l'ensemble minimal de skills requis et exécuter `scripts/build_dag_plan.py` afin d'ordonner les tâches en vagues parallèles strictement acycliques.",
            "Phase DISPATCH : Générer pour chaque skill un ordre de mission conforme à `schemas/task-envelope.schema.json` en injectant les budgets cibles (`16.6 ms` Performance / `33.3 ms` Qualité) et les langues (`fr-CD`, `ln-CD`).",
            "Phase REVIEW & ARBITRATION : Vérifier les Handoff Packets produits par chaque vague ; en cas de conflit (ex: nombre de PNJ actifs > 24), convoquer `DIR-04` et `DIR-05`.",
            "Phase CONSOLIDATION : Assembler la synthèse finale suivant `templates/execution-plan-dag.json` et transmettre les nouvelles entités `PROPOSED` à `PRD-03` et `DIR-06`.",
        ),
        decision_rules=(
            ("Entité requise absente du registre", "Créer un ID provisoire au statut PROPOSED ou RESEARCH_REQUIRED et router vers le skill propriétaire (WLD-01, NAR-03, GD-02...)", "Refuser toute génération avec un nom libre sans ID normalisé"),
            ("Entité critique au statut BLOCKED ou DEPRECATED", "Suspendre la branche dépendante du DAG et notifier immédiatement l'utilisateur", "Convoquer le collège de direction (DIR-02, DIR-03, DIR-04)"),
            ("Dépassement de budget CPU/GPU détecté en Vague 3/4", "Ouvrir une boucle d'arbitrage DIR-04 + DIR-05 (ex: basculer le surplus de PNJ AI-01 vers AI-02 Mass Crowd)", "Marquer le livrable BLOCKED tant que P99 > 16.6 ms"),
            ("Un skill génère une section hors de son périmètre (Scope Violation)", "Tronquer la section hors périmètre et émettre une Task Envelope vers le skill légitime", "Consigner l'alerte SCOPE_GUARD dans le rapport d'orchestration"),
        ),
        acceptance_criteria=(
            "100 % des sous-tâches sont assignées à un skill unique identifié par son code (`NAR-01`..`PRD-06`).",
            "Le graphe d'exécution en vagues est un DAG strict (0 cycle vérifié par `scripts/build_dag_plan.py`).",
            "Chaque Task Envelope inclut explicitement les entités du registre et l'enveloppe frametime UE5.",
            "La synthèse finale distingue clairement les éléments `CONFIRMED`, `PROPOSED` et `RESEARCH_REQUIRED`.",
        ),
        validation_auditors=("DIR-06", "DIR-07"),
        reference_filename="orchestration-rules.md",
        reference_content="""# Règles d'Orchestration & Tri Topologique (`DIR-01`)

## 1. Protocole en 6 Phases
1. **INTAKE** : Lecture de `knowledge/entities-registry.csv`. Vérification des préfixes (`CHR-`, `FAM-`, `ORG-`, `DST-`, `LOC-`, `MSN-`, `ITM-`, `VEH-`, `SYS-`).
2. **PLANNING** : Calcul des strates 0 à 5. Aucun skill de Strate $N$ ne peut s'exécuter avant la complétion de ses dépendances amont de Strate $< N$.
3. **DISPATCH** : Envoi de la `Task Envelope` JSON.
4. **HANDOFF** : Réception du `Handoff Packet` Markdown.
5. **GATEKEEPING** : Contrôle par `NAR-06` (Continuité), `ENG-07` (Performance), `PRD-04` (QA) et `PRD-06` (Accessibilité XAG).
6. **CONSOLIDATION** : Mise à jour de `knowledge/entities-registry.csv` via `PRD-03` et validation finale `DIR-06`/`DIR-07`.

## 2. Plafonds Techniques Impératifs à Injecter dans `constraints`
- `target_frametime_ms` : `16.6` (Mode Performance 60 FPS) ou `33.3` (Mode Qualité 30 FPS).
- `max_npc_active` : `24` acteurs `AI-01` (au-delà, utiliser `AI-02` Mass Crowd jusqu'à 600+ entités).
- `min_corridor_width_cm` : `350` cm.
""",
        template_filename="execution-plan-dag.json",
        template_content="""{
  "orchestration_id": "ORC-2026-001",
  "user_intent": "Description synthétique de la requête utilisateur",
  "referenced_entities": [
    {
      "id": "DST-GOMBE",
      "status": "CONFIRMED"
    }
  ],
  "dag_waves": [
    {
      "wave_index": 1,
      "parallel_tasks": [
        {
          "task_id": "TSK-2026-001",
          "target_skill": "WLD-02",
          "objective": "Vérifier le contexte culturel et linguistique",
          "required_output_template": "cultural-brief-template.md"
        }
      ]
    }
  ],
  "arbitration_notes": [],
  "final_status": "PROPOSED"
}
""",
        example_filename="sample-orchestration-plan.md",
        example_content="""# Exemple d'Exécution `DIR-01` — Mission d'Infiltration au Port ONATRA

## 1. Requête Utilisateur
> « Concevoir une mission d'infiltration nocturne dans les entrepôts du Port ONATRA à la Gombe avec exfiltration en moto Wewa. »

## 2. Sortie Générée (`execution-plan-dag.json`)
```json
{
  "orchestration_id": "ORC-2026-042",
  "user_intent": "Conception complète de la mission MSN-MAIN-002-ONATRA (Infiltration Port de Kinshasa + Fuite Wewa)",
  "referenced_entities": [
    {"id": "DST-GOMBE", "status": "CONFIRMED"},
    {"id": "LOC-GOMBE-PORT", "status": "CONFIRMED"},
    {"id": "CHR-PROTAG-KOFFI", "status": "CONFIRMED"},
    {"id": "ORG-CARTEL-FLEUVE", "status": "CONFIRMED"},
    {"id": "VEH-MOTO-WEWA-01", "status": "CONFIRMED"},
    {"id": "SYS-STEALTH", "status": "CONFIRMED"}
  ],
  "dag_waves": [
    {
      "wave_index": 1,
      "parallel_tasks": [
        {"task_id": "TSK-2026-101", "target_skill": "WLD-02", "objective": "Documenter le jargon portuaire lingala/français kinois des dockers ONATRA"},
        {"task_id": "TSK-2026-102", "target_skill": "WLD-03", "objective": "Spécifier la morphologie des quais, grues et dépôts de conteneurs de LOC-GOMBE-PORT"},
        {"task_id": "TSK-2026-103", "target_skill": "GD-06", "objective": "Calibrer l'adhérence de VEH-MOTO-WEWA-01 sur béton portuaire humide"}
      ]
    },
    {
      "wave_index": 2,
      "parallel_tasks": [
        {"task_id": "TSK-2026-104", "target_skill": "GD-02", "objective": "Concevoir la machine à états sans soft-lock de MSN-MAIN-002-ONATRA"},
        {"task_id": "TSK-2026-105", "target_skill": "NAR-02", "objective": "Rédiger le script dramatique et la beat sheet de la mission"}
      ]
    },
    {
      "wave_index": 3,
      "parallel_tasks": [
        {"task_id": "TSK-2026-106", "target_skill": "WLD-05", "objective": "Produire le blockout métrique (allées >= 350cm, couverts conteneurs 200cm)"},
        {"task_id": "TSK-2026-107", "target_skill": "NAR-04", "objective": "Rédiger les barks d'alerte en lingala/français des gardes ORG-CARTEL-FLEUVE"},
        {"task_id": "TSK-2026-108", "target_skill": "AI-01", "objective": "Configurer le State Tree de patrouille nocturne pour 18 gardes max"}
      ]
    },
    {
      "wave_index": 4,
      "parallel_tasks": [
        {"task_id": "TSK-2026-109", "target_skill": "NAR-06", "objective": "Auditer la continuité narrative avec MSN-MAIN-001-ARRIVEE"},
        {"task_id": "TSK-2026-110", "target_skill": "PRD-04", "objective": "Établir le plan de test QA d'infiltration et d'exfiltration"}
      ]
    }
  ],
  "final_status": "PROPOSED"
}
```
""",
        scripts={"build_dag_plan.py": BUILD_DAG_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="DIR-02",
        description=(
            "Gouvernance exécutive, cadrage du périmètre (scope), arbitrage budgétaire et validation "
            "des jalons majeurs (Vertical Slice, Alpha, Beta, Gold) de ZAÏRE. Garantit l'équilibre "
            "entre ambition open-world à Kinshasa, vélocité de production et maîtrise des risques."
        ),
        inputs=("execution-plan-dag.json", "risk-register.csv", "sprint-velocity-metrics"),
        outputs=("milestone-gate-review.md", "scope-arbitration-decision.md"),
        activation_triggers=(
            "Validation d'un passage de jalon (Concept, Vertical Slice, Alpha, Beta, Certification Gold).",
            "Demande d'ajout d'une fonctionnalité majeure ou d'une nouvelle commune de Kinshasa non planifiée.",
            "Escalade par DIR-01 ou PRD-02 d'un risque critique (score >= 12/25) menaçant le chemin critique.",
        ),
        scope_boundaries=(
            "N'intervient jamais dans l'écriture du code C++ (`ENG-01`/`ENG-02`) ni dans le réglage artistique des shaders (`ART-08`).",
            "Ne sacrifie jamais la conformité d'accessibilité XAG (`PRD-06`) ou la stabilité technique (`DIR-04`) pour accélérer un jalon.",
        ),
        operational_procedures=(
            "Évaluer la proposition de fonctionnalité ou l'état du jalon par rapport à la capacité des 8 départements et au buffer de contingence de 15 %.",
            "Croiser les dépendances avec le registre des risques (`PRD-02`) et les lacunes documentaires (`research/research-gaps.md`).",
            "Classer chaque livrable du jalon en `MUST_HAVE (P0)`, `SHOULD_HAVE (P1)` ou `DEFERRED_POST_LAUNCH (P2)`.",
            "Prononcer la décision d'arbitrage (`GO`, `CONDITIONAL_GO`, `NO_GO_SCOPE_CUT`) dans `templates/milestone-gate-review.md`.",
        ),
        decision_rules=(
            ("Dérive de charge estimée > +10 % sur un jalon", "Activer le Feature Gating : déprioriser les éléments P2 ou restreindre la densité aux communes P0 (Gombe, Matonge, Kalamu, Limete)", "Marquer les entités coupées au statut DEPRECATED via DIR-06"),
            ("Commune en statut RESEARCH_REQUIRED (ex: DST-MASINA) sur le chemin critique", "Isoler la commune hors du Vertical Slice et maintenir le focus sur DST-GOMBE et DST-MATONGE", "Assigner une tâche prioritaire d'acquisition SIG à WLD-03"),
            ("Risque juridique sur licences musicales (AUD-03)", "Exiger l'activation par défaut du fallback Streamer Safe composé en interne", "Bloquer l'intégration de la piste jusqu'à validation contractuelle"),
        ),
        acceptance_criteria=(
            "Écart budgétaire et capacitaire maintenu dans l'enveloppe de tolérance de ±5 %.",
            "100 % des coupes de périmètre (Scope Cuts) identifient les IDs d'entités à passer en `DEPRECATED`.",
            "Chaque jalon dispose de critères d'entrée et de sortie mesurables validés avec `DIR-04` et `DIR-07`.",
        ),
        validation_auditors=("DIR-01", "DIR-07"),
        reference_filename="milestone-governance.md",
        reference_content="""# Gouvernance des Jalons AAA (`DIR-02`)

## 1. Grille des Jalons de Production ZAÏRE
- **Vertical Slice (VS)** : 1 quartier complet (`DST-GOMBE` -> `LOC-GOMBE-PORT` + `DST-MATONGE` -> `LOC-MATONGE-VICTOIRE`), 1 mission principale (`MSN-MAIN-001-ARRIVEE`), boucle complète combat/infiltration/conduite Wewa à 60 FPS (`<= 16.6 ms`).
- **Feature Complete (Alpha)** : 100 % des systèmes (`SYS-*`) et quêtes principales jouables de bout en bout en blockout/art intermédiaire.
- **Content Complete (Beta)** : 100 % des assets artistiques, doublages multilingues (`fr-CD`, `ln-CD`) et optimisation PSO/VRAM intégrés.
- **Gold Master** : 0 bug Sévérité A/B, conformité XAG validée par `DIR-07`.
""",
        template_filename="milestone-gate-review.md",
        template_content="""# Décision de Jalon & Arbitrage de Scope (`DIR-02`)

- **Jalon Évalué** : `Vertical Slice` | `Alpha` | `Beta` | `Gold`
- **Décision Exécutive** : `GO` | `CONDITIONAL_GO` | `NO_GO`
- **Variation Charge / Budget** : `[+X % / -Y %]`

## 1. Arbitrage du Périmètre (Scope Matrix)
| ID Entité / Système | Priorité (`P0`/`P1`/`P2`) | Décision (`MAINTAIN` / `DEFER` / `DEPRECATE`) | Justification |
| :--- | :--- | :--- | :--- |
| `DST-...` | `P0` | `MAINTAIN` | Cœur du Vertical Slice |

## 2. Risques Critiques & Conditions de Passage
- **Conditions obligatoires avant clôture** : `[Liste]`
""",
        example_filename="sample-scope-arbitration.md",
        example_content="""# Exemple d'Arbitrage `DIR-02` — Périmètre Vertical Slice Kinshasa

- **Jalon Évalué** : `Vertical Slice`
- **Décision Exécutive** : `CONDITIONAL_GO`
- **Variation Charge / Budget** : `-2.4 %` (après report de `DST-MASINA` en Alpha)

## 1. Arbitrage du Périmètre (Scope Matrix)
| ID Entité / Système | Priorité | Décision | Justification |
| :--- | :--- | :--- | :--- |
| `DST-GOMBE` | `P0` | `MAINTAIN` | Commune portuaire et financière requise pour `MSN-MAIN-001-ARRIVEE`. |
| `DST-MATONGE` | `P0` | `MAINTAIN` | Pôle culturel démontrant `SYS-CROWD-MASS` (600+ PNJ) et `ORG-RADIO-KIN`. |
| `DST-MASINA` | `P2` | `DEFER` | Actuellement en `RESEARCH_REQUIRED` (données SIG ruelles secondaires incomplètes). Reporté au jalon Alpha. |
""",
    ),
    SkillBlueprint(
        skill_id="DIR-03",
        description=(
            "Gardien des 3 piliers créatifs de ZAÏRE, de la cohérence tonale, esthétique, émotionnelle "
            "et de l'authenticité culturelle kinoise à travers la narration, le world design, la direction "
            "artistique et la direction audio."
        ),
        inputs=("creative-proposals", "knowledge/world-bible/cultural-guidelines.md", "art-and-narrative-deliverables"),
        outputs=("creative-vision-review.md", "creative-pillar-scorecard.md"),
        activation_triggers=(
            "Validation initiale ou mise à jour des Bibles (World Bible, Narrative Bible, Art Bible, Audio Bible).",
            "Revue d'alignement créatif sur une nouvelle mission principale (`MSN-MAIN-*`), un personnage majeur (`CHR-*`) ou un quartier (`DST-*`).",
            "Arbitrage en cas de dissonance ludo-narrative ou de risque de stéréotype culturel soulevé par `WLD-02`.",
        ),
        scope_boundaries=(
            "Ne modifie jamais les budgets matériels CPU/GPU/VRAM fixés par `DIR-04`.",
            "N'écrit pas les scripts de mission complets (`NAR-02`) ni les graphes de dialogue (`NAR-04`), mais valide leur tonalité et leurs enjeux.",
        ),
        operational_procedures=(
            "Évaluer le livrable soumis au regard des **3 Piliers Créatifs de ZAÏRE** définis dans `references/creative-pillars.md`.",
            "Vérifier l'ancrage culturel kinois en croisant avec `knowledge/world-bible/cultural-guidelines.md` et `knowledge/world-bible/kinshasa-districts.md`.",
            "Noter la cohérence sensorielle (contraste visuel entre la Gombe et Matonge/Kalamu, rythme musical, authenticité du code-switching français/lingala).",
            "Émettre un avis formel (`APPROVED`, `REVISION_REQUIRED`, `VETO_CREATIVE`) via `templates/creative-vision-review.md`.",
        ),
        decision_rules=(
            ("Présence d'un cliché générique ('Afrique exotisée' ou argot non kinois)", "Opposer un VETO_CREATIVE immédiat et renvoyer le livrable vers WLD-02 pour correction", "Bloquer toute promotion au statut CONFIRMED"),
            ("Mécanique de gameplay contredisant l'identité de Koffi (CHR-PROTAG-KOFFI)", "Demander à DIR-05 et GD-01/GD-02 d'intégrer une alternative d'infiltration sociale ou de négociation", "Maintenir l'alignement ludo-narratif du protagoniste"),
            ("Uniformité visuelle ou sonore entre deux communes", "Exiger de ART-01 et AUD-01 une différenciation marquée des palettes chromatiques et ambiances", "Se référer aux signatures de kinshasa-districts.md"),
        ),
        acceptance_criteria=(
            "Le livrable obtient un score >= 4/5 sur chacun des 3 piliers créatifs de ZAÏRE.",
            "Zéro stéréotype ou anachronisme culturel détecté (conformité à `cultural-guidelines.md`).",
            "Alignement explicite entre l'intention dramatique, l'espace urbain et la mécanique jouable.",
        ),
        validation_auditors=("DIR-01", "WLD-02"),
        reference_filename="creative-pillars.md",
        reference_content="""# Les 3 Piliers Créatifs de ZAÏRE (`DIR-03`)

1. **Pilier 1 — Kinshasa Vivante & Souveraine ("Mégapole Électrique")** :
   La ville n'est pas un simple décor statique mais un organisme vivant, sonore, dense et stratifié où chaque commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`) possède son propre pouls architectural, social et musical.
2. **Pilier 2 — Ingéniosité Urbaine & Vélocité ("Flux & Débrouillardise")** :
   Le joueur triomphe par sa lecture de la ville : maîtrise des réseaux humains, parkour urbain fluide, pilotage nerveux des motos Wewa (`VEH-MOTO-WEWA-01`) et utilisation tactique de la foule et de la météo équatoriale.
3. **Pilier 3 — Tension Sociale &Ancrage Humain ("Du Port aux Ngandas")** :
   Chaque conflit mêle enjeux intimes familiaux (`FAM-KABONGO` vs `FAM-MUKENDI`) et luttes d'influence économiques sur le bassin du fleuve Congo, portés par des dialogues bilingues français/lingala crédibles.
""",
        template_filename="creative-vision-review.md",
        template_content="""# Revue de Direction Créative (`DIR-03`)

- **Livrable Audité** : `[ID / Fichier]`
- **Skill Émetteur** : `[NAR-* / WLD-* / ART-* / AUD-*]`
- **Verdict Créatif** : `APPROVED` | `REVISION_REQUIRED` | `VETO_CREATIVE`

## 1. Évaluation sur les 3 Piliers Créatifs
| Pilier | Score (/5) | Commentaire & Directives |
| :--- | :--- | :--- |
| 1. Kinshasa Vivante & Souveraine | `[X/5]` | `[Analyse]` |
| 2. Ingéniosité Urbaine & Vélocité | `[X/5]` | `[Analyse]` |
| 3. Tension Sociale & Ancrage Humain | `[X/5]` | `[Analyse]` |

## 2. Conformité Culturelle & Sensorielle
- **Authenticité linguistique / sociale (`WLD-02`)** : `[OK / À corriger]`
- **Directives d'ajustement** : `[Instructions précises]`
""",
        example_filename="sample-creative-review.md",
        example_content="""# Exemple de Revue `DIR-03` — Validation de `MSN-MAIN-001-ARRIVEE`

- **Livrable Audité** : `MSN-MAIN-001-ARRIVEE (L'Accostage de l'Aube)`
- **Skill Émetteur** : `GD-02` / `NAR-02`
- **Verdict Créatif** : `APPROVED`

## 1. Évaluation sur les 3 Piliers Créatifs
| Pilier | Score (/5) | Commentaire & Directives |
| :--- | :--- | :--- |
| 1. Kinshasa Vivante & Souveraine | `5/5` | Excellent contraste entre la brume industrielle de `LOC-GOMBE-PORT` à l'aube et l'éveil des marchés de `DST-KALAMU`. |
| 2. Ingéniosité Urbaine & Vélocité | `5/5` | Le choix laissé entre l'accréditation sociale (`ITM-DOC-PASSEPORT`) et le contournement par les grues valorise l'intelligence urbaine. |
| 3. Tension Sociale & Ancrage Humain | `4/5` | Renforcer l'échange en lingala (`LEX-006 Libongo`, `LEX-008 Tɔ́kɛndɛ́`) avec le docker allié avant la poursuite en Wewa. |
""",
    ),
    SkillBlueprint(
        skill_id="DIR-04",
        description=(
            "Direction technique et architecture globale Unreal Engine 5 / SideFX Houdini / Wwise. "
            "Définit et fait respecter les budgets matériels (16.6 ms à 60 FPS, 33.3 ms à 30 FPS, "
            "VRAM, RAM), les règles de streaming World Partition et les Architecture Decision Records (ADR)."
        ),
        inputs=("technical-proposals", "knowledge/technical-specs/performance-budgets.csv", "profiling-reports-eng-07"),
        outputs=("technical-adr.md", "hardware-budget-allocation.csv"),
        activation_triggers=(
            "Définition ou modification d'une architecture moteur (World Partition, GAS, Mass Entity, ZoneGraph, Lumen, Nanite, Chaos).",
            "Demande d'arbitrage technique suite à un dépassement de frametime ou de VRAM remonté par `ENG-07`.",
            "Validation de faisabilité technique d'un nouveau système de gameplay (`GD-01`..`GD-06`) ou pipeline procédural (`ENG-04`).",
        ),
        scope_boundaries=(
            "Ne modifie pas l'écriture dramatique (`NAR-02`) tant qu'elle respecte les budgets d'acteurs et de streaming.",
            "N'autorise aucune dérogation à la règle Zero Synchronous Loading sur le Game Thread.",
        ),
        operational_procedures=(
            "Vérifier la conformité de la proposition avec les plafonds de `knowledge/technical-specs/performance-budgets.csv`.",
            "Contrôler l'absence de goulots d'étranglement connus sous UE5 (explosion de permutations PSO, WPO excessif sur Nanite, requêtes EQS synchrones, chargements bloquants).",
            "Rédiger un Architecture Decision Record (ADR) normé via `templates/technical-adr.md`.",
            "Fixer les seuils d'alerte automatisés pour `ENG-07` (Performance Engineer) et `PRD-05` (Test Engineer / Gauntlet).",
        ),
        decision_rules=(
            ("Système dépassant son budget CPU/GPU alloué dans performance-budgets.csv", "Opposer un VETO_TECHNIQUE et imposer une architecture orientée données (Mass Entity) ou du time-slicing", "Marquer le système BLOCKED jusqu'à retour sous le seuil P99"),
            ("Utilisation de LoadSynchronous() ou de Static Switches abusifs dans un Master Material", "Rejeter l'implémentation et imposer FStreamableManager / Custom Primitive Data", "Ajouter une règle bloquante dans le validateur pré-commit ENG-03"),
            ("Densité de foule demandée > 24 acteurs dans un marché (ex: DST-MATONGE)", "Imposer le découpage : max 24 ACharacter complets (AI-01) + jusqu'à 600 entités Mass Crowd (AI-02) avec hydratation à 25m", "Valider l'enveloppe CPU Mass <= 2.0 ms"),
        ),
        acceptance_criteria=(
            "Le budget frametime cumulé des sous-systèmes reste `<= 16.6 ms` (Performance) et `<= 33.3 ms` (Qualité).",
            "Le budget VRAM total est maintenu `<= 6144 MB` (Performance) / `<= 8192 MB` (Qualité).",
            "Chaque ADR technique définit une métrique de vérification automatisable dans Unreal Insights / Gauntlet.",
        ),
        validation_auditors=("ENG-07", "DIR-07"),
        reference_filename="ue5-technical-guardrails.md",
        reference_content="""# Garde-Fous Techniques Unreal Engine 5 (`DIR-04`)

## 1. Enveloppes Budgétaires Incompressibles (Kinshasa Open World)
- **Frametime Total P99** : `16.6 ms` (60 FPS) / `33.3 ms` (30 FPS).
- **Game Thread** : `<= 6.5 ms` (`AI-01` <= 2.5 ms, `AI-02/03` Mass <= 2.0 ms, `ENG-05` Chaos <= 1.5 ms).
- **GPU Passes** : `ART-07` Lumen GI + Reflections `<= 4.5 ms`, `ART-04` Nanite `<= 2.5 ms`, `ART-09` Niagara `<= 1.5 ms`.
- **VRAM** : `<= 6144 MB` en cible standard (pools stricts : Virtual Textures, Render Targets Lumen/VSM, Meshes Nanite).

## 2. Règles d'Architecture Obligatoires
1. **World Partition & Data Layers (`ENG-01`)** : Taille de cellule `12800 cm` (128 m), rayon de chargement adapté à la vitesse maximale des motos Wewa (`VEH-MOTO-WEWA-01`).
2. **Zéro Chargement Synchrone** : Usage exclusif de `FStreamableManager::RequestAsyncLoad` et `TSoftObjectPtr<T>`.
3. **PSO Precache** : Collecte obligatoire des Pipeline State Objects sur chaque build nocturne (`ENG-08`).
""",
        template_filename="technical-adr.md",
        template_content="""# ADR-TECH-NNN : [Titre de la Décision d'Architecture UE5]

- **Statut** : `PROPOSED` | `CONFIRMED`
- **Autorité** : `DIR-04 (Technical Director)`
- **Sous-systèmes Impactés** : `[PERF-CPU-* / PERF-GPU-* / SYS-*]`

## 1. Problématique & Contrainte Budgétaire
`[Description de la contrainte technique et de l'enveloppe ms/MB]`

## 2. Architecture Retenue
`[Spécification précise UE5 / Houdini / Wwise]`

## 3. Seuils de Validation (`ENG-07` / `PRD-05`)
- **Budget CPU max** : `[X.X ms]`
- **Budget GPU max** : `[Y.Y ms]`
- **Budget VRAM max** : `[Z MB]`
""",
        example_filename="sample-technical-adr.md",
        example_content="""# ADR-TECH-004 : Architecture Hybride des Foules de Matonge (`AI-01` + `AI-02`)

- **Statut** : `CONFIRMED`
- **Autorité** : `DIR-04 (Technical Director)`
- **Sous-systèmes Impactés** : `PERF-CPU-NPCAI`, `PERF-CPU-MASS`, `SYS-CROWD-MASS`, `DST-MATONGE`

## 1. Problématique & Contrainte Budgétaire
Le Rond-Point Victoire (`LOC-MATONGE-VICTOIRE`) requiert plus de 500 citoyens visibles simultanément pour être crédible, alors que 500 `ACharacter` dotés de `UCharacterMovementComponent` et de Behavior Trees consommeraient > 18 ms sur le Game Thread.

## 2. Architecture Retenue
- **Couche Proche (0 à 25 m du joueur)** : Plafond strict de **24 `ACharacter`** gérés par `AI-01` (State Trees + Smart Objects + ragdoll Chaos complet).
- **Couche Médiane et Lointaine (25 m à 250 m)** : Jusqu'à **600 entités ECS `MassEntity`** (`AI-02`) circulant sur `ZoneGraph` avec animations partagées par Vertex Animation Textures (VAT) et instanciation Nanite/HISM.
- **Hydratation Dynamique** : Conversion asynchrone sans hitch entre représentation Mass LOD et `ACharacter` lorsque le joueur interagit ou déclenche un combat.

## 3. Seuils de Validation (`ENG-07` / `PRD-05`)
- **Budget CPU `AI-01` (24 acteurs)** : `<= 2.5 ms`
- **Budget CPU `AI-02` (600 entités Mass)** : `<= 2.0 ms`
- **Budget VRAM Kits Modulaires PNJ (`ART-03`)** : `<= 768 MB`
""",
    ),
    SkillBlueprint(
        skill_id="DIR-05",
        description=(
            "Direction du Game Design de ZAÏRE. Garantit la cohérence systémique entre les boucles "
            "de gameplay (Core Loops), le combat, la conduite des véhicules kinois, l'économie, la "
            "progression, les missions et le respect des métriques spatiales."
        ),
        inputs=("game-design-specs-gd-01-to-07", "level-blockouts-wld-05", "knowledge/technical-specs/spatial-metrics.md"),
        outputs=("gameplay-coherence-review.md", "systemic-balance-directive.md"),
        activation_triggers=(
            "Validation de tout nouveau système de jeu (`SYS-*`), mission (`MSN-*`), véhicule (`VEH-*`) ou archétype de combat.",
            "Arbitrage d'équilibrage entre économie (`GD-03`), progression (`GD-04`) et difficulté de combat (`GD-05`).",
            "Validation du playtest d'un blockout Level Design (`WLD-05`) avant autorisation du passage à l'Environment Art (`WLD-06`/`ART-02`).",
        ),
        scope_boundaries=(
            "N'écrit pas le code C++ des GameplayAbilities (`ENG-02`).",
            "N'autorise jamais la mise en production artistique d'un niveau dont le blockout (`WLD-05`) viole `spatial-metrics.md`.",
        ),
        operational_procedures=(
            "Vérifier l'intégration du système ou de la mission dans les Core Loops de ZAÏRE (Observer -> S'infiltrer/Négocier/Combattre -> Traverser Kinshasa -> Réinvestir dans le réseau local).",
            "Contrôler l'interopérabilité via la taxonomie officielle `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.",
            "Auditer la conformité aux métriques spatiales (`knowledge/technical-specs/spatial-metrics.md` : couloirs `>= 350 cm`, couverts `100 cm`/`200 cm`, voies routières `350-400 cm`).",
            "Émettre la directive de validation ou de rééquilibrage dans `templates/gameplay-coherence-review.md`.",
        ),
        decision_rules=(
            ("Blockout WLD-05 comportant un couloir jouable < 350 cm ou une impasse non intentionnelle", "Rejeter le handoff vers WLD-06/ART-02 et exiger une reprise géométrique du blockout", "Appliquer strictement la règle Blockout First"),
            ("Mission GD-02 n'offrant qu'une seule approche linéaire ou vulnérable au soft-lock", "Exiger au moins 2 approches distinctes (ex: infiltration sociale ITM-DOC-PASSEPORT + parcours parkour/mêlée) et une gestion de fuite", "Bloquer le passage en CONFIRMED"),
            ("Mécanique introduisant un tag absent de gameplay-tags-taxonomy.csv", "Valider la pertinence systémique du tag et ordonner son ajout normalisé dans la taxonomie", "Interdire les variables booléennes ad-hoc non composables"),
        ),
        acceptance_criteria=(
            "100 % des interactions inter-systèmes passent par des `FGameplayTag` répertoriés.",
            "100 % des espaces de mission respectent les gabarits de caméra, de couvert et de circulation véhicule.",
            "L'équilibrage numérique évite à la fois l'inflation monétaire (`GD-03`) et la trivialisation du combat (`GD-05`).",
        ),
        validation_auditors=("DIR-03", "DIR-07"),
        reference_filename="core-loops-and-metrics.md",
        reference_content="""# Boucles de Gameplay & Règles d'Arbitrage Ludique (`DIR-05`)

## 1. Boucle Principale (Core Loop) de ZAÏRE
1. **Reconnaissance Urbaine (Minute-to-Minute)** : Explorer Kinshasa sans mini-carte invasive grâce aux landmarks (`SYS-WLD-LANDMARKS`), écouter les rumeurs dans les ngandas (`DST-MATONGE`) et observer les routines PNJ (`AI-04`).
2. **Action & Approche Tactique** : Aborder chaque objectif (`MSN-*`) via un spectre fluide entre **Infiltration Sociale/Urbaine** (`SYS-STEALTH`), **Combat Corps-à-Corps Nerveux** (`SYS-CMB-MELEE`) et **Exfiltration Véhiculaire** (`VEH-MOTO-WEWA-01`).
3. **Impact & Réputation Locale (Hour-to-Hour)** : Faire évoluer la réputation par commune (`SYS-WLD-REPUTATION`), débloquer des raccourcis, des informateurs et des améliorations mécaniques (`GD-03`/`GD-04`).

## 2. Règles Non-Négociables de Playtest Blockout
- **Latence d'input combat** : `< 100 ms`.
- **Attack Tokens (`GD-05`)** : Maximum 2 assaillants au corps-à-corps simultanés contre Koffi en difficulté standard.
- **Règle des 40 secondes (`WLD-04`)** : Un point d'intérêt ou micro-événement systémique toutes les 40 secondes de déplacement à pied.
""",
        template_filename="gameplay-coherence-review.md",
        template_content="""# Revue de Cohérence Ludique & Systémique (`DIR-05`)

- **Livrable Évalué** : `[SYS-* / MSN-* / BLK-* / VEH-*]`
- **Skill Émetteur** : `[GD-* / WLD-* / AI-*]`
- **Décision Lead Game Designer** : `APPROVED_FOR_PRODUCTION` | `REBALANCE_REQUIRED` | `BLOCKOUT_REJECTED`

## 1. Contrôle des Métriques & Gameplay Tags
- **Conformité `spatial-metrics.md`** : `[Conforme / Non conforme]`
- **Gameplay Tags utilisés** : `[Liste des tags]`
- **Approches tactiques supportées** : `[Infiltration / Combat / Véhicule / Social]`

## 2. Directives d'Équilibrage
`[Ajustements numériques ou spatiaux exigés]`
""",
        example_filename="sample-gameplay-review.md",
        example_content="""# Exemple de Revue `DIR-05` — Approbation du Blockout `LOC-GOMBE-PORT`

- **Livrable Évalué** : `BLK-GOMBE-PORT-01 (Entrepôt & Quais ONATRA)`
- **Skill Émetteur** : `WLD-05 (Level Designer)`
- **Décision Lead Game Designer** : `APPROVED_FOR_PRODUCTION`

## 1. Contrôle des Métriques & Gameplay Tags
- **Conformité `spatial-metrics.md`** : Conforme. Allées entre conteneurs élargies à `400 cm` (minimum requis `350 cm`), couverts bas à `100 cm`, grues d'accroche parkour à `280 cm`.
- **Gameplay Tags utilisés** : `State.Character.Stealth.Concealed`, `State.Character.Stealth.Disguised`, `Ability.Movement.Vault`, `Vehicle.Type.MotoWewa`.
- **Approches tactiques supportées** :
  1. Accès social par le poste de garde principal avec `ITM-DOC-PASSEPORT`.
  2. Infiltration verticale par les portiques de conteneurs.
  3. Exfiltration rapide sur les quais via `VEH-MOTO-WEWA-01` (couloir d'inter-file `>= 150 cm`).
""",
    ),
    SkillBlueprint(
        skill_id="DIR-06",
        description=(
            "Autorité de gouvernance documentaire et gardien de la Single Source of Truth (knowledge/). "
            "Contrôle l'unicité des identifiants, l'intégrité référentielle, la traçabilité des sources "
            "et valide la transition des entités du statut PROPOSED vers CONFIRMED ou DEPRECATED."
        ),
        inputs=("handoff-packets", "knowledge/entities-registry.csv", "knowledge/status-audit-log.csv", "continuity-audits-nar-06"),
        outputs=("registry-promotion-decision.md", "updated-status-audit-entry.csv"),
        activation_triggers=(
            "Fin de chaque cycle d'orchestration (Phase 6 CONSOLIDATION) lorsqu'un skill propose de nouvelles entités (`PROPOSED`).",
            "Demande de promotion d'un livrable ou d'une entité au statut `CONFIRMED`.",
            "Retrait d'une entité suite à un arbitrage de scope (`DIR-02`) nécessitant son passage en `DEPRECATED`.",
        ),
        scope_boundaries=(
            "Ne rédige pas le contenu métier initial à la place des spécialistes ; juge exclusivement la conformité structurelle, documentaire et référentielle.",
            "Ne supprime jamais physiquement une ligne de `knowledge/entities-registry.csv` (utiliser le statut `DEPRECATED` pour préserver l'historique).",
        ),
        operational_procedures=(
            "Exécuter `python tools/validate_registry.py` pour vérifier la syntaxe des IDs, l'absence de doublons et la validité de toutes les dépendances.",
            "Vérifier que toute donnée incertaine (SIG secondaire, point historique ou technique non sourcé) est isolée avec le statut `RESEARCH_REQUIRED`.",
            "Vérifier la présence du rapport d'audit de continuité (`NAR-06`) pour les entités narratives/missions et de `PRD-03` pour le formatage Docs-as-Code.",
            "Enregistrer toute transition de statut dans `knowledge/status-audit-log.csv` avec horodatage ISO-8601 et justification.",
        ),
        decision_rules=(
            ("Entité proposée référençant un ID parent ou une dépendance inexistante (Référence Fantôme)", "Rejeter immédiatement la promotion et renvoyer le Handoff Packet au skill émetteur", "Maintenir le statut PROPOSED ou passer en BLOCKED"),
            ("Donnée factuelle sur Kinshasa affirmée sans source vérifiée ni validation WLD-02/WLD-03", "Forcer le statut de l'entité à RESEARCH_REQUIRED", "Déclencher une tâche de vérification documentaire via DIR-01"),
            ("Tous les contrôles DoD, NAR-06, PRD-03 et DIR-07 sont au vert", "Promouvoir l'entité au statut CONFIRMED et inscrire la transition dans status-audit-log.csv", "Publier la mise à jour à l'ensemble des départements"),
        ),
        acceptance_criteria=(
            "`python tools/validate_registry.py` retourne un code de sortie `0` (zéro erreur).",
            "100 % des changements de statuts sont tracés dans `knowledge/status-audit-log.csv`.",
            "Aucun ID déprécié (`DEPRECATED`) n'est réutilisé ou référencé comme dépendance active d'une entité `CONFIRMED`.",
        ),
        validation_auditors=("DIR-01", "DIR-07"),
        reference_filename="knowledge-governance-rules.md",
        reference_content="""# Règles de Gouvernance du Registre Maître (`DIR-06`)

## 1. Convention Stricte des 9 Préfixes d'Identifiants
- `CHR-[ROLE]-[SLUG]` : Personnages (`CATEGORY = CHARACTER`, Owner `NAR-03`)
- `FAM-[NOM]` : Familles (`CATEGORY = FAMILY`, Owner `NAR-03`)
- `ORG-[TYPE]-[SLUG]` : Organisations (`CATEGORY = ORGANIZATION`, Owner `NAR-05`)
- `DST-[COMMUNE]` : Quartiers / Communes (`CATEGORY = DISTRICT`, Owner `WLD-01`)
- `LOC-[DST]-[SLUG]` : Lieux / POI (`CATEGORY = LOCATION`, Owner `WLD-04`)
- `MSN-[TYPE]-[NUM]-[SLUG]` : Missions / Quêtes (`CATEGORY = MISSION`, Owner `GD-02`)
- `ITM-[CAT]-[SLUG]` : Objets / Équipements (`CATEGORY = ITEM`, Owner `GD-01`/`GD-03`/`GD-05`)
- `VEH-[CAT]-[SLUG]` : Véhicules (`CATEGORY = VEHICLE`, Owner `GD-06`)
- `SYS-[DOMAINE]-[SLUG]` : Systèmes de Gameplay (`CATEGORY = SYSTEM`, Owner `GD-01`/`ENG-01`/`AI-*`)

## 2. Matrice d'Autorisation des Transitions de Statuts
- `RESEARCH_REQUIRED -> PROPOSED` : Skill propriétaire après fourniture de la recherche `WLD-02`/`WLD-03`/`ENG-*`.
- `PROPOSED -> CONFIRMED` : Signature conjointe obligatoire de `DIR-06` + `DIR-07` (+ Directeur de pôle concerné).
- `* -> BLOCKED` : `DIR-04`, `DIR-07`, `NAR-06`, `ENG-07`, `PRD-04`.
- `* -> DEPRECATED` : `DIR-02`, `DIR-03`, `DIR-06`.
""",
        template_filename="registry-promotion-decision.md",
        template_content="""# Décision de Gouvernance Documentaire (`DIR-06`)

- **Date d'Audit** : `YYYY-MM-DD`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)` | `FAIL`

## 1. Transitions de Statuts Décidées
| ID Entité | Ancien Statut | Nouveau Statut | Valideurs | Justification & Sources (`SRC-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `LOC-...` | `PROPOSED` | `CONFIRMED` | `DIR-03, DIR-06, DIR-07` | `[Justification]` |

## 2. Anomalies Référentielles Rejetées
- `[Aucune / Liste des IDs fantômes ou mal formés]`
""",
        example_filename="sample-registry-promotion.md",
        example_content="""# Exemple de Décision `DIR-06` — Promotion de `LOC-LIMETE-ECHANGEUR`

- **Date d'Audit** : `2026-11-25`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`

## 1. Transitions de Statuts Décidées
| ID Entité | Ancien Statut | Nouveau Statut | Valideurs | Justification & Sources (`SRC-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `LOC-LIMETE-ECHANGEUR` | `PROPOSED` | `CONFIRMED` | `DIR-03, DIR-06, DIR-07` | Landmark majeur de `DST-LIMETE` vérifié (`SRC-019`), dépendances `DST-LIMETE` et `SYS-WLD-LANDMARKS` confirmées. |
| `DST-MASINA` | `PROPOSED` | `RESEARCH_REQUIRED` | `DIR-06` | Maintenu en `RESEARCH_REQUIRED` tant que le réseau de voirie secondaire OSM n'est pas complété par `WLD-03`. |
""",
    ),
    SkillBlueprint(
        skill_id="DIR-07",
        description=(
            "Autorité suprême d'Assurance Qualité, de conformité d'accessibilité (Xbox Accessibility "
            "Guidelines - XAG) et de certification finale de ZAÏRE STUDIO OS. Contrôle les 6 critères "
            "de la Definition of Done (DoD) et détient le droit de blocage (BLOCKED) sur toute livraison."
        ),
        inputs=("qa-test-plans-prd-04", "gauntlet-reports-prd-05", "xag-audits-prd-06", "perf-reports-eng-07"),
        outputs=("quality-gate-verdict.md", "certification-checklist-report.md"),
        activation_triggers=(
            "Évaluation finale d'un livrable ou d'un lot de production avant son passage au statut `CONFIRMED`.",
            "Validation de la conformité d'accessibilité XAG sur toute fonctionnalité UI/UX (`GD-07`), combat (`GD-05`), véhicule (`GD-06`) ou sous-titrage (`AUD-04`).",
            "Revue des résultats de tests automatisés nocturnes Gauntlet (`PRD-05`) et des métriques de performance (`ENG-07`).",
        ),
        scope_boundaries=(
            "Ne planifie pas les sprints quotidiens (`PRD-01`) et ne corrige pas directement le code source (`ENG-02`).",
            "N'accorde jamais de validation `CONFIRMED` si l'un des 6 critères de la Definition of Done (`architecture/quality-standards.md`) est en échec.",
        ),
        operational_procedures=(
            "Vérifier les **6 critères obligatoires de la Definition of Done (DoD)** sur le Handoff Packet soumis.",
            "Contrôler les indicateurs quantitatifs : frametime P99 (`<= 16.6 ms` / `<= 33.3 ms`), reproductibilité des rapports QA (`>= 90 %`), couverture de tests automatisés sur les systèmes critiques (`>= 80 %`).",
            "Vérifier l'audit d'accessibilité XAG produit par `PRD-06` (double codage visuel/sonore, sous-titres enrichis avec locuteur `[KOFFI]` et glyphes lingala `ɛ`/`ɔ`, alternative aux QTE).",
            "Prononcer le verdict final (`CONFIRMED_RELEASE_READY` ou `BLOCKED_QUALITY_GATE`) via `templates/quality-gate-verdict.md`.",
        ),
        decision_rules=(
            ("Présence d'un bug de Sévérité A (Crash, Soft-Lock narratif, corruption de sauvegarde, dépassement VRAM OOM)", "Placer immédiatement l'entité ou le build au statut BLOCKED", "Ouvrir un ticket critique prioritaire via DIR-01 vers ENG-01/ENG-07/GD-02"),
            ("Interface UI ou mécanique de jeu dépourvue de double codage daltonisme ou de support d'expansion texte +35 %", "Refuser la validation qualité pour non-conformité XAG", "Renvoyer vers GD-07, AUD-04 et PRD-06"),
            ("100 % des 6 critères DoD validés et tests Gauntlet/XAG/Continuité réussis", "Cosigner avec DIR-06 la promotion de l'entité au statut CONFIRMED", "Archiver le certificat qualité du jalon"),
        ),
        acceptance_criteria=(
            "Les 6 critères de la Definition of Done universelle sont explicitement cochés et justifiés.",
            "0 anomalie bloquante (Sévérité A) ouverte sur le périmètre audité.",
            "Conformité XAG vérifiée (visuelle, auditive, motrice, cognitive).",
        ),
        validation_auditors=("DIR-01", "DIR-06"),
        reference_filename="quality-dod-and-xag.md",
        reference_content="""# Definition of Done (DoD) & Seuils Qualité Studio (`DIR-07`)

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
""",
        template_filename="quality-gate-verdict.md",
        template_content="""# Verdict Quality Gate & Certification (`DIR-07`)

- **Cible Auditée** : `[ID Entité / Jalon / Livrable]`
- **Verdict Final** : `CONFIRMED_RELEASE_READY` | `BLOCKED_QUALITY_GATE`
- **Cosignature Documentaire** : `DIR-06`

## 1. Contrôle des 6 Critères Definition of Done (DoD)
| # | Critère DoD | Statut (`PASS`/`FAIL`) | Preuve / Référence Audit |
| :--- | :--- | :--- | :--- |
| 1 | Format & Gabarit Officiel | `PASS` | `[Template vérifié]` |
| 2 | Intégrité des IDs Registre | `PASS` | `[validate_registry.py OK]` |
| 3 | Traçabilité & `RESEARCH_REQUIRED` | `PASS` | `[Sources SRC-* citées]` |
| 4 | Respect Strict du Périmètre | `PASS` | `[Aucun overlap]` |
| 5 | Budgets UE5 & Métriques Spatiales | `PASS` | `[ENG-07 / WLD-05 OK]` |
| 6 | Validation Croisée & Accessibilité XAG | `PASS` | `[NAR-06 / PRD-04 / PRD-06 OK]` |

## 2. Motifs de Blocage ou Actions Correctives
- `[Aucun / Liste des points bloquants]`
""",
        example_filename="sample-quality-verdict.md",
        example_content="""# Exemple de Verdict `DIR-07` — Certification de `MSN-MAIN-001-ARRIVEE`

- **Cible Auditée** : `MSN-MAIN-001-ARRIVEE (L'Accostage de l'Aube — Vertical Slice)`
- **Verdict Final** : `CONFIRMED_RELEASE_READY`
- **Cosignature Documentaire** : `DIR-06`

## 1. Contrôle des 6 Critères Definition of Done (DoD)
| # | Critère DoD | Statut | Preuve / Référence Audit |
| :--- | :--- | :--- | :--- |
| 1 | Format & Gabarit Officiel | `PASS` | Conforme à `mission-design-template.md`. |
| 2 | Intégrité des IDs Registre | `PASS` | `LOC-GOMBE-PORT`, `CHR-PROTAG-KOFFI`, `VEH-MOTO-WEWA-01` validés. |
| 3 | Traçabilité & `RESEARCH_REQUIRED` | `PASS` | Références `SRC-001`, `SRC-002`, `SRC-019` vérifiées. |
| 4 | Respect Strict du Périmètre | `PASS` | Séparation respectée entre `GD-02`, `NAR-02`, `WLD-05` et `ENG-02`. |
| 5 | Budgets UE5 & Métriques Spatiales | `PASS` | P99 mesuré à `15.8 ms` (60 FPS), couloirs entrepôt `>= 400 cm`. |
| 6 | Validation Croisée & Accessibilité XAG | `PASS` | Audit `NAR-06` (0 conflit), `PRD-06` (XAG sous-titres `[KOFFI]` + glyphes `ɛ`/`ɔ` + maintien QTE validés). |
""",
    ),
)


def build_department_00(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 7 skills du département 00-direction."""
    created: list[Path] = []
    for bp in DIRECTION_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_00(WORKSPACE_ROOT)
    print(f"[OK] Département 00-direction généré ({len(paths)} skills).")
