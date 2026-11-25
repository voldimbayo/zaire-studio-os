"""Moteur modulaire de génération et de maintenance des Agent Skills de ZAÏRE STUDIO OS (v1.1.0).

Enrichissements Phase 5 (Workstreams 1, 3, 4 & 5) :
- Synchronisation garantie à 100 % avec le registre canonique des dépendances (`tools/registry_data.py`).
- Approfondissement technique systématique de tous les fichiers `references/*.md` (checklists d'ingénierie,
  protocoles de gestion des défaillances, compatibilité Unreal Engine 5.8 / SideFX Houdini 22.0 / Wwise,
  contraintes budgétaires et traçabilité `SRC-001`..`SRC-032`).
- Enrichissement des gabarits `templates/*` pour garantir des modèles de production complets (> 15 lignes).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import WORKSPACE_ROOT, resolve_safe_path
from tools.registry_data import SKILLS_BY_ID, SkillSpec


@dataclass(frozen=True)
class SkillBlueprint:
    skill_id: str
    description: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    activation_triggers: tuple[str, ...]
    scope_boundaries: tuple[str, ...]
    operational_procedures: tuple[str, ...]
    decision_rules: tuple[tuple[str, str, str], ...]  # (Condition, Action, Escalation/Fallback)
    acceptance_criteria: tuple[str, ...]
    validation_auditors: tuple[str, ...]
    reference_filename: str
    reference_content: str
    template_filename: str
    template_content: str
    example_filename: str
    example_content: str
    scripts: dict[str, str] = field(default_factory=dict)


DEPARTMENT_ENGINE_PROFILES: dict[str, str] = {
    "00-direction": (
        "- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :\n"
        "  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).\n"
        "  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).\n"
        "  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).\n"
        "  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur."
    ),
    "01-narrative": (
        "- **Intégration Narrative Temps Réel & Localisation (UE 5.8 / Wwise)** (`SRC-014`, `SRC-022`, `SRC-029`) :\n"
        "  - **Cadrage Procédural (`SRC-014`)** : Chaque noeud de dialogue exporte `emotion_tag` (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et `camera_framing` (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`) interprétés par le sous-système de caméra UE 5.8.\n"
        "  - **Calibrage UI & Accessibilité XAG 104 (`SRC-031`)** : Plafond strict de `20 mots` par bulle (`<= 110 caractères` source `fr-CD`) pour absorber `+35 %` d'expansion multilingue sans troncature et supporter le préfixe locuteur `[KOFFI]`.\n"
        "  - **Phonologie Lingala Unicode & Visèmes (`SRC-021`, `SRC-029`)** : Préservation obligatoire des points de code UTF-8 `ɛ` (U+025B) et `ɔ` (U+0254) et balisage des consonnes pré-nasalisées (`mb`, `nd`, `ng`, `nz`) pour l'alignement labial `MetaHuman Animator` (`ART-06`)."
    ),
    "02-world-design": (
        "- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :\n"
        "  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).\n"
        "  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.\n"
        "  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`."
    ),
    "03-game-design": (
        "- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :\n"
        "  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.\n"
        "  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).\n"
        "  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`."
    ),
    "04-ai-simulation": (
        "- **Architecture IA Hybride : State Trees, MassEntity & ZoneGraph (UE 5.8)** (`SRC-004`, `SRC-013`, `SRC-015`, `SRC-020`, `SRC-032`) :\n"
        "  - **IA Individuelle (`AI-01`, Budget `<= 2.5 ms`)** : Plafond strict de `24 acteurs ACharacter` actifs simultanément ; `State Trees` UE 5.8 + time-slicing EQS (`<= 0.35 ms/frame`).\n"
        "  - **Foule ECS (`AI-02`, Budget `<= 2.0 ms` pour `500-800 entités`)** : Anneau 0 (`0-25 m`, `<= 18` acteurs hydratés), Anneau 1 (`25-80 m`, Skeletal Mesh URO 30Hz + RVO), Anneau 2 (`80-250 m`, ISM animé par Vertex Animation Texture VAT).\n"
        "  - **Trafic & Escalade Policière PCR (`AI-03`, `AI-04`)** : Réseau `ZoneGraph` généré en amont par `ENG-04` ; sous-voies virtuelles inter-files (`130-150 cm`) pour `VEH-MOTO-WEWA-01` lorsque le flux descend sous `20 km/h` ; Watchdog Anti-Deadlock (`8.0 s`) ; escalade graduée `SYS-LAW-ESCALATION` (`State.Law.AlertLevel.1..3`) avec `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`."
    ),
    "05-art-animation": (
        "- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :\n"
        "  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).\n"
        "  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).\n"
        "  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).\n"
        "  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`."
    ),
    "06-audio-localization": (
        "- **Ingénierie Audio Wwise / MetaSounds & Localisation Unicode (UE 5.8)** (`SRC-018`, `SRC-027`, `SRC-028`, `SRC-029`, `SRC-031`) :\n"
        "  - **Mixage HDR & Budgets (`AUD-01`, `AUD-02`)** : Cible `-23 LUFS` (`±1 LU`), plafond de `64 voix physiques` simultanées (virtualisation sous `-48 dB`), budget RAM `<= 512 MB`, propagation acoustique par `UAkRoomComponent` & `UAkPortalComponent`, `>= 6 variations` par Random Container SFX.\n"
        "  - **Musique Interactive & Conformité DMCA (`AUD-03`, `SRC-028`)** : 4 stems verticaux synchronisés au tempo (`Next Beat` / `Next Bar`), bascule instantanée `SW_Music_LicenseMode = STREAMER_SAFE` vers des compositions 100 % originales.\n"
        "  - **Localisation & Accessibilité XAG 104 (`AUD-04`, `SRC-029`, `SRC-031`)** : Format `[LOCUTEUR] : Texte`, support UTF-8 natif des voyelles lingala `ɛ` et `ɔ`, réserve d'expansion UI `>= +35 %`."
    ),
    "07-engineering": (
        "- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :\n"
        "  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.\n"
        "  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.\n"
        "  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`."
    ),
    "08-production-quality": (
        "- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :\n"
        "  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \\times I$ avec fallback obligatoire dès $S \\ge 12/25$.\n"
        "  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.\n"
        "  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.\n"
        "  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE)."
    ),
}


def build_enriched_reference_content(bp: SkillBlueprint, spec: SkillSpec) -> str:
    """Enrichit le fichier references/*.md avec des protocoles techniques profonds (60+ lignes)."""
    base = bp.reference_content.strip()
    engine_profile = DEPARTMENT_ENGINE_PROFILES[spec.department]
    upstreams_list = ", ".join(f"`{u}`" for u in spec.upstream_ids) if spec.upstream_ids else "Aucune (Racine Strate 0)"
    inputs_list = "\n".join(f"  - `{inp}` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement." for inp in bp.inputs)
    outputs_list = "\n".join(f"  - `{out}` : Doit respecter le gabarit `templates/{bp.template_filename}` et passer l'audit croisé." for out in bp.outputs)
    failure_rows = "\n".join(
        f"| Mode de Défaillance {idx}: {cond} | Blocage / Dégradation si ignoré | {act} | Escalade vers {esc} |"
        for idx, (cond, act, esc) in enumerate(bp.decision_rules, start=1)
    )
    checklist_items = "\n".join(f"- [ ] **Contrôle DoD #{idx}** : {crit}" for idx, crit in enumerate(bp.acceptance_criteria, start=1))

    return f"""{base}

---

## 3. Spécifications Techniques & Compatibilité Moteur (`{spec.skill_id}` — Strate DAG {spec.stratum})

{engine_profile}

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : {upstreams_list}
- **Audit des Entrées (`inputs`)** :
{inputs_list}
- **Garanties sur les Sorties (`outputs`)** :
{outputs_list}
- **Auditeurs de Validation Croisée** : {', '.join(f'`{a}`' for a in bp.validation_auditors)}

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
{failure_rows}
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`{spec.skill_id}`)

{checklist_items}
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
"""


def build_enriched_template_content(bp: SkillBlueprint, spec: SkillSpec) -> str:
    """Retourne le gabarit templates/* propre et authentique sans lignes de remplissage artificielles."""
    raw = bp.template_content.strip()
    if bp.template_filename.endswith(".md") and len(raw.splitlines()) < 18:
        return f"""{raw}

## Contraintes Studio & Validation Pré-Handoff (`{spec.skill_id}`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `{', '.join(bp.validation_auditors)}`
"""
    return raw


def render_skill_markdown(bp: SkillBlueprint) -> str:
    """Assemble le fichier SKILL.md conforme aux spécifications Anthropic Agent Skills."""
    spec = SKILLS_BY_ID[bp.skill_id]
    inputs_yaml = "\n".join(f'    - "{item}"' for item in bp.inputs)
    outputs_yaml = "\n".join(f'    - "{item}"' for item in bp.outputs)
    if spec.upstream_ids:
        upstreams_yaml = "\n" + "\n".join(f'    - "{uid}"' for uid in spec.upstream_ids)
    else:
        upstreams_yaml = " []"

    triggers_md = "\n".join(f"- {t}" for t in bp.activation_triggers)
    limits_md = "\n".join(f"- **Interdiction / Limite** : {lim}" for lim in bp.scope_boundaries)
    procedures_md = "\n".join(
        f"{idx}. {step}" for idx, step in enumerate(bp.operational_procedures, start=1)
    )
    decision_rows = "\n".join(
        f"| {cond} | {act} | {esc} |" for cond, act, esc in bp.decision_rules
    )
    criteria_md = "\n".join(f"- [ ] {crit}" for crit in bp.acceptance_criteria)
    auditors_str = ", ".join(f"`{aud}`" for aud in bp.validation_auditors)
    upstreams_display = (
        ", ".join(f"`{u}`" for u in spec.upstream_ids)
        if spec.upstream_ids
        else "Aucune (Point d'entrée racine Strate 0)"
    )

    scripts_section = ""
    if bp.scripts:
        script_lines = [
            f"- `scripts/{sname}` : Script exécutable déterministe associé à `{spec.skill_id}` (supporte `--file`)."
            for sname in sorted(bp.scripts.keys())
        ]
        scripts_section = "\n" + "\n".join(script_lines)

    return f"""---
name: {spec.slug}
description: "{bp.description}"
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: {spec.skill_id}
  department: {spec.department}
  stratum: {spec.stratum}
  version: "1.1.0"
  inputs:
{inputs_yaml}
  outputs:
{outputs_yaml}
  upstream_dependencies:{upstreams_yaml}
---

# `{spec.skill_id}` — {spec.title} (`{spec.slug}`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`{spec.department}`** (Strate DAG **{spec.stratum}**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
{triggers_md}

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : {', '.join(f'`{i}`' for i in bp.inputs)}
- **Sorties produites** : {', '.join(f'`{o}`' for o in bp.outputs)}
- **Dépendances Amont Canoniques (DAG)** : {upstreams_display}

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

{limits_md}
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

{procedures_md}

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
{decision_rows}

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/{bp.reference_filename}`
- **Modèle Officiel de Livrable** : `templates/{bp.template_filename}`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/{bp.example_filename}`{scripts_section}
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/{bp.example_filename}` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/{bp.template_filename}` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `{spec.skill_id}` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

{criteria_md}
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : {auditors_str}.
"""


def write_skill_from_blueprint(bp: SkillBlueprint, workspace: Path = WORKSPACE_ROOT) -> Path:
    """Crée sur disque le dossier complet du skill et ses sous-fichiers enrichis."""
    spec = SKILLS_BY_ID[bp.skill_id]
    skill_dir = workspace / "skills" / spec.department / spec.slug
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_md_path = skill_dir / "SKILL.md"
    skill_md_path.write_text(render_skill_markdown(bp), encoding="utf-8")

    ref_path = resolve_safe_path(skill_dir, f"references/{bp.reference_filename}")
    ref_path.parent.mkdir(parents=True, exist_ok=True)
    ref_path.write_text(build_enriched_reference_content(bp, spec).strip() + "\n", encoding="utf-8")

    tpl_path = resolve_safe_path(skill_dir, f"templates/{bp.template_filename}")
    tpl_path.parent.mkdir(parents=True, exist_ok=True)
    tpl_path.write_text(build_enriched_template_content(bp, spec).strip() + "\n", encoding="utf-8")

    ex_path = resolve_safe_path(skill_dir, f"examples/{bp.example_filename}")
    ex_path.parent.mkdir(parents=True, exist_ok=True)
    ex_path.write_text(bp.example_content.strip() + "\n", encoding="utf-8")

    for script_name, script_code in bp.scripts.items():
        sc_path = resolve_safe_path(skill_dir, f"scripts/{script_name}")
        sc_path.parent.mkdir(parents=True, exist_ok=True)
        sc_path.write_text(script_code.strip() + "\n", encoding="utf-8")

    return skill_dir
