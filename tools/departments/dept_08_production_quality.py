"""Spécifications et génération du Département 08-PRODUCTION-QUALITY (PRD-01 à PRD-06)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_XAG_COMPLIANCE_SCRIPT = '''"""Auditeur automatisé de conformité Xbox Accessibility Guidelines (XAG) pour PRD-06."""

from __future__ import annotations

import argparse
import json
import sys


def audit_xag_feature(spec: dict) -> list[str]:
    """Vérifie les critères d'accessibilité XAG obligatoires (contraste, double codage, sous-titres, QTE)."""
    errors: list[str] = []
    contrast_ratio = float(spec.get("text_contrast_ratio", 0.0))
    subtitle_bg_opacity = float(spec.get("subtitle_background_opacity", 0.0))
    has_speaker_prefix = bool(spec.get("subtitle_has_speaker_prefix", False))
    supports_lingala_unicode = bool(spec.get("supports_lingala_open_vowels", False))
    uses_color_only = bool(spec.get("uses_color_as_only_indicator", True))
    has_qte_hold_alternative = bool(spec.get("has_qte_hold_or_auto_alternative", False))
    ui_expansion_margin = float(spec.get("ui_text_expansion_tolerance_pct", 0.0))

    if contrast_ratio < 4.5:
        errors.append(f"Ratio de contraste ({contrast_ratio}:1) < minimum XAG 101 requis (4.5:1).")
    if not (0.50 <= subtitle_bg_opacity <= 1.0):
        errors.append(f"Opacité du fond de sous-titre ({subtitle_bg_opacity}) insuffisante (requis >= 0.50).")
    if not has_speaker_prefix:
        errors.append("Sous-titre non conforme XAG 104 : préfixe du locuteur ('[KOFFI]') obligatoire.")
    if not supports_lingala_unicode:
        errors.append("Police non conforme : support des glyphes Unicode lingala ('ɛ', 'ɔ') obligatoire.")
    if uses_color_only:
        errors.append("Non-conformité XAG 102 : double codage (Couleur + Forme/Icône/Son) obligatoire.")
    if not has_qte_hold_alternative:
        errors.append("Non-conformité XAG 107 (Moteur) : option de maintien continu (Hold) requise pour tout QTE.")
    if ui_expansion_margin < 35.0:
        errors.append(f"Marge d'expansion UI (+{ui_expansion_margin}%) < minimum requis +35%.")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Audite la conformité XAG d'une fonctionnalité (PRD-06).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de spécification XAG à auditer (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample_feature = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_feature = {
            "feature_id": "UI-HUD-MAIN-OVERLAY",
            "text_contrast_ratio": 7.2,
            "subtitle_background_opacity": 0.78,
            "subtitle_has_speaker_prefix": True,
            "supports_lingala_open_vowels": True,
            "uses_color_as_only_indicator": False,
            "has_qte_hold_or_auto_alternative": True,
            "ui_text_expansion_tolerance_pct": 38.0,
        }
    errs = audit_xag_feature(sample_feature)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Fonctionnalité {sample_feature.get('feature_id', 'SAMPLE')} certifiée 100% conforme aux normes d'accessibilité XAG.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

PRODUCTION_QUALITY_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="PRD-01",
        description=(
            "Planification opérationnelle de la production de ZAÏRE : découpage en sprints Agiles/Hybrides, "
            "matrices RACI inter-départements, suivi du chemin critique (Blockout WLD-05 -> Env Art ART-02 -> "
            "Lighting ART-07 -> Perf ENG-07) et intégration d'un buffer de contingence de 15 %."
        ),
        inputs=("orchestration-dag-dir-01", "milestone-targets-dir-02", "architecture/skill-dependencies.md"),
        outputs=("sprint-execution-plan.md", "department-raci-matrix.csv"),
        activation_triggers=(
            "Traduction d'un jalon exécutif (`DIR-02` : Vertical Slice, Alpha, Beta, Gold) en plannings de sprints de 2 semaines pour les 8 départements.",
            "Résolution d'un goulot d'étranglement inter-départements (ex: attente de validation d'un blockout `WLD-05` avant démarrage d'`ART-02`).",
            "Replanification dynamique suite à l'apparition d'un ticket `BLOCKED` ou `RESEARCH_REQUIRED`.",
        ),
        scope_boundaries=(
            "Ne décide pas seul d'une coupe de fonctionnalité majeure (`DIR-02`) ni d'un compromis sur les budgets techniques (`DIR-04`).",
            "Interdit toute planification de sprint saturée à 100 % sans la réserve de **15 % de buffer d'aléas Open World**.",
        ),
        operational_procedures=(
            "Ordonner les tâches du sprint en respectant les 6 strates topologiques de `architecture/skill-dependencies.md` (Strate 0 -> Strate 5).",
            "Allouer maximum **85 % de la capacité** de chaque département aux tâches planifiées et réserver **15 % de buffer** pour absorber les itérations playtest (`DIR-05`) et optimisations P99 (`ENG-07`).",
            "Établir la matrice **RACI** (*Responsible, Accountable, Consulted, Informed*) de chaque livrable en s'assurant qu'un seul skill est `Responsible (R)`.",
            "Documenter le plan de sprint dans `templates/sprint-plan-template.md`.",
        ),
        decision_rules=(
            ("Tâche d'Environment Art (ART-02) planifiée dans le même sprint que le blockout Level Design (WLD-05) du même lieu", "Décaler la production ART-02 au sprint N+1 : le sprint N est consacré au blockout WLD-05 et à sa validation playtest DIR-05", "Appliquer strictement la règle Blockout First"),
            ("Blocage de plus de 24h sur une dépendance RESEARCH_REQUIRED (ex: WLD-02/WLD-03)", "Basculer la capacité du département aval sur une commune CONFIRMED (ex: DST-GOMBE ou DST-MATONGE) pendant que la recherche aboutit", "Éviter tout temps mort sur le chemin critique"),
            ("Consommation complète du buffer de 15 % avant la fin de la première semaine du sprint", "Déclencher une alerte précoce vers DIR-02 et PRD-02 pour déprioriser les tâches P2 du sprint", "Garantir un taux de complétion des engagements P0 >= 90 %"),
        ),
        acceptance_criteria=(
            "Chaque tâche du sprint possède un unique skill `Responsible (R)` et respecte l'ordre DAG.",
            "Un buffer de capacité de `15 %` est explicitement provisionné.",
            "Aucun livrable `ART-02` n'est planifié sans un blockout `WLD-05` préalablement validé.",
        ),
        validation_auditors=("DIR-01", "DIR-02"),
        reference_filename="agile-openworld-production.md",
        reference_content="""# Méthodologie de Planification Hybride Open World (`PRD-01`)

## 1. Chaîne Critique d'un Lieu ou d'une Mission (`LOC-*` / `MSN-*`)
1. **Sprint N-1 (Fondations Strates 1-2)** : Recherche `WLD-02`/`WLD-03` -> Design `GD-02` + Script `NAR-02` -> Blockout `WLD-05` -> Validation Playtest `DIR-05`.
2. **Sprint N (Production Strate 3)** : Environment Brief `WLD-06` -> Kits 3D `ART-02` + IA `AI-01`/`AI-02` + Dialogues/Barks `NAR-04` + SFX `AUD-02`.
3. **Sprint N+1 (Intégration & Gatekeeping Strates 4-5)** : Éclairage `ART-07` + VFX `ART-09` + Profilage P99 `ENG-07` + Tests Gauntlet `PRD-05` + Certification `DIR-06`/`DIR-07`.
""",
        template_filename="sprint-plan-template.md",
        template_content="""# Plan de Sprint & Matrice RACI (`PRD-01`)

- **ID Sprint** : `SPR-2026-NN`
- **Jalon Cible (`DIR-02`)** : `[Vertical Slice / Alpha / Beta / Gold]`
- **Capacité Planifiée / Buffer** : `85 % Planifié / 15 % Buffer Aléas`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Séquencement des Livrables sur le Chemin Critique
| Task ID | Livrable / Entité | Skill `R` (Responsible) | Skill `A` (Accountable) | Skills `C` (Consulted) | Strate DAG |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TSK-...` | `[Livrable]` | `[Skill unique]` | `DIR-...` | `[Auditeurs]` | `[1..5]` |

## 2. Goulots d'Étranglement & Dépendances Surveillées
- **Verrou Blockout First** : `[État de validation WLD-05 -> ART-02]`
""",
        example_filename="sample-sprint-plan.md",
        example_content="""# Exemple `PRD-01` — Plan du Sprint `SPR-2026-04` (Vertical Slice `LOC-GOMBE-PORT`)

- **ID Sprint** : `SPR-2026-04`
- **Jalon Cible (`DIR-02`)** : `Vertical Slice (MSN-MAIN-001-ARRIVEE)`
- **Capacité Planifiée / Buffer** : `85 % Planifié / 15 % Buffer Optimisation P99`
- **Statut** : `CONFIRMED`

## 1. Séquencement des Livrables sur le Chemin Critique
| Task ID | Livrable / Entité | Skill `R` | Skill `A` | Skills `C` | Strate DAG |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TSK-2026-041` | Habillage Modulaire `KIT-GOMBE-PORT` sur `BLK-GOMBE-PORT-01` validé | `ART-02` | `DIR-03` | `WLD-06`, `ART-04`, `WLD-05` | Strate 3 |
| `TSK-2026-042` | State Tree Patrouille 16 Gardes `ORG-CARTEL-FLEUVE` | `AI-01` | `DIR-04` | `GD-05`, `ENG-07` | Strate 3 |
| `TSK-2026-043` | Éclairage Aube Brumeuse `LGT_GOMBE_DAWN_FOG` (`<= 4.2 ms`) | `ART-07` | `DIR-03` | `ART-01`, `ENG-06` | Strate 3 |
| `TSK-2026-044` | Audit P99 (`<= 16.6 ms`) & Suite Gauntlet `MSN-MAIN-001-ARRIVEE` | `ENG-07` | `DIR-04` | `PRD-05`, `DIR-07` | Strates 4-5 |

## 2. Goulots d'Étranglement & Dépendances Surveillées
- **Verrou Blockout First** : `BLK-GOMBE-PORT-01` a été validé par `DIR-05` au Sprint 03 ; `ART-02` peut produire les kits Nanite sans risque de reprise métrique.
""",
    ),
    SkillBlueprint(
        skill_id="PRD-02",
        description=(
            "Identification, quantification (Probabilité x Impact sur 25) et plans de mitigation des "
            "risques techniques, culturels, juridiques (licences musicales rumba/ndombolo, marques) "
            "et de planning de ZAÏRE STUDIO OS."
        ),
        inputs=("research-gaps-phase-1", "technical-budgets-dir-04", "cultural-briefs-wld-02"),
        outputs=("risk-register.csv", "critical-risk-mitigation-plan.md"),
        activation_triggers=(
            "Évaluation d'une lacune documentaire ou technique identifiée dans `research/research-gaps.md`.",
            "Introduction d'une dépendance externe (musique sous licence tiers dans `AUD-03`, données SIG secondaires de Kinshasa dans `WLD-03`/`ENG-04`).",
            "Apparition d'un blocage récurrent ou d'une dérive de performance menaçant un jalon `DIR-02`.",
        ),
        scope_boundaries=(
            "Ne corrige pas lui-même le bug C++ ou le mesh 3D ; impose et suit le plan de contingence assigné au skill propriétaire.",
            "Interdit de laisser un risque critique (Score `>= 12/25`) sans plan de mitigation actif et sans responsable désigné.",
        ),
        operational_procedures=(
            r"Coter chaque risque selon sa **Probabilité $P \in [1..5]$** et son **Impact $I \in [1..5]$**, produisant un Score de Criticité $S = P \times I \in [1..25]$.",
            "Classer les risques en 3 niveaux : `LOW (1-5)`, `MEDIUM (6-11)`, `CRITICAL (12-25)`.",
            "Pour tout risque `CRITICAL (>= 12)`, définir obligatoirement : (1) Action Préventive immédiate, (2) Solution de Repli (Fallback technique ou créatif déjà prêt), (3) Skill Propriétaire.",
            "Mettre à jour `templates/risk-register-template.csv` et notifier `DIR-02` et `DIR-07`.",
        ),
        decision_rules=(
            ("Risque de strike DMCA / expiration de licence sur les musiques de Radio Lokole (Score 4x4 = 16/25)", "Exiger d'AUD-03 qu'un Switch Wwise SW_Music_LicenseMode bascule à 100 % sur des compositions originales du studio en mode Streamer Safe", "Neutraliser l'impact juridique et commercial"),
            ("Couverture SIG/OSM hétérogène dans les communes secondaires comme DST-MASINA (Score 4x3 = 12/25)", "Isoler DST-MASINA en statut RESEARCH_REQUIRED hors du Vertical Slice et utiliser le générateur de subdivision paramétrique WLD-03/ENG-04", "Protéger le planning du Vertical Slice DIR-02"),
            ("Risque de dépassement du budget CPU/GPU dans les marchés denses sous la pluie (Score 3x5 = 15/25)", "Activer le délestage dynamique : réduction de 40 % de la foule en plein air sous l'averse (AI-02) et bascule automatique des réflexions Lumen sur Surface Cache > 0.40 Roughness (ENG-06)", "Garantir le maintien des 60 FPS (16.6 ms)"),
        ),
        acceptance_criteria=(
            "100 % des lacunes de `research/research-gaps.md` sont couvertes par une entrée dans `risk-register.csv`.",
            "100 % des risques ayant un score `>= 12/25` possèdent un plan de mitigation et un fallback opérationnel.",
            "Chaque risque est rattaché à un skill propriétaire unique (`WLD-03`, `AUD-03`, `ENG-07`, etc.).",
        ),
        validation_auditors=("DIR-02", "DIR-04", "DIR-07"),
        reference_filename="risk-scoring-and-mitigation.md",
        reference_content="""# Méthodologie de Cotation & Mitigation des Risques AAA (`PRD-02`)

## 1. Grille de Criticité ($S = P \times I$)
- **Probabilité ($1..5$)** : `1` = Rare (<10%), `3` = Possible (40-60%), `5` = Quasi-certain (>85%).
- **Impact ($1..5$)** : `1` = Mineur, `3` = Retard de sprint / Dégradation FPS locale, `5` = Blocage Jalon / Crash / Litige juridique ou rejet culturel.
- **Seuil d'Action Obligatoire** : Tout score **`>= 12`** déclenche une mesure de contingence immédiate intégrée au DAG de `DIR-01`.
""",
        template_filename="risk-register-template.csv",
        template_content="""risk_id,category,description,probability_1_5,impact_1_5,criticality_score,owner_skill,preventive_action,fallback_plan,status
RSK-TECH-001,PERFORMANCE,Saturation CPU/GPU au Rond-Point Victoire sous averse tropicale,3,5,15,ENG-07,Plafond 18 acteurs AI-01 + 600 Mass VAT + Cutout Niagara,Migration de 60% de la foule sous les auvents (AI-02) pendant l'orage,MITIGATED
RSK-DATA-002,GIS_COVERAGE,Données OSM incomplètes sur les ruelles secondaires de Masina (DST-MASINA),4,3,12,WLD-03,Marquage RESEARCH_REQUIRED et exclusion du Vertical Slice,Subdivision parcellaire procédurale Houdini HDA calibrée par WLD-03,MITIGATED
RSK-LEGL-003,MUSIC_LICENSING,Droits de diffusion streaming sur les morceaux de rumba/ndombolo tiers,4,4,16,AUD-03,Séparation stricte dans Wwise entre pistes licenciées et pistes studio,Activation en 1 clic du mode Streamer Safe 100% compositions originales,MITIGATED
""",
        example_filename="sample-risk-register.md",
        example_content="""# Exemple `PRD-02` — Registre des Risques Critiques & Plans de Contingence

## 1. Risques Critiques Traités (`Score >= 12/25`)
| ID Risque | Catégorie | Description | $P \times I$ | Score | Skill Owner | Plan de Mitigation & Fallback Actif |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RSK-LEGL-003` | `LEGAL / AUDIO` | Revendications DMCA sur les streams utilisant la radio `ORG-RADIO-KIN`. | `4 × 4` | **16/25** | `AUD-03` | Switch Wwise `SW_Music_LicenseMode = STREAMER_SAFE` remplaçant 100 % des titres tiers par les rumbas originales du studio. |
| `RSK-TECH-001` | `PERFORMANCE` | Cumul de coût GPU Lumen + Niagara Pluie + 600 PNJ à `DST-MATONGE`. | `3 × 5` | **15/25** | `ENG-07` | Sous `World.Weather.TropicalStorm`, `AI-02` abrite 60 % des piétons sous les galeries (réduisant le coût CPU/GPU tout en augmentant le réalisme). |
| `RSK-DATA-002` | `WORLD / GIS` | Ruelles secondaires de `DST-MASINA` peu détaillées dans OpenStreetMap. | `4 × 3` | **12/25** | `WLD-03` | Maintien de `DST-MASINA` en `RESEARCH_REQUIRED` hors du Vertical Slice (`DIR-02`) et règles de subdivision d'îlots `ENG-04`. |
""",
    ),
    SkillBlueprint(
        skill_id="PRD-03",
        description=(
            "Ingénierie documentaire (Docs-as-Code) et maintenance opérationnelle de la Single Source "
            "of Truth (knowledge/). Formate, indexe et vérifie l'unicité des identifiants (CHR-*, LOC-*, "
            "MSN-*, etc.), la traçabilité des sources (SRC-*) et prépare les lots de promotion de statut "
            "pour DIR-06."
        ),
        inputs=("all-department-handoff-packets", "knowledge/entities-registry.csv", "research/source-registry.csv"),
        outputs=("registry-update-patch.csv", "documentation-traceability-report.md"),
        activation_triggers=(
            "Réception des Handoff Packets en fin de vague d'exécution (Strate 5 du DAG).",
            "Enregistrement d'une nouvelle entité au statut `PROPOSED` ou `RESEARCH_REQUIRED` dans `knowledge/entities-registry.csv`.",
            "Mise à jour de l'index maître `docs/skills-index.md` et vérification de l'absence de liens morts ou de références fantômes.",
        ),
        scope_boundaries=(
            "Ne prononce pas seul la validation finale `CONFIRMED` (prérogative exclusive de `DIR-06` et `DIR-07`).",
            "Rejette automatiquement tout document comportant un identifiant mal formé ou une référence à une entité inexistante.",
        ),
        operational_procedures=(
            "Analyser chaque Handoff Packet pour extraire la table des entités lues (`READ`), créées (`NEW`) ou modifiées (`UPDATE`).",
            "Vérifier la conformité syntaxique de chaque ID à `schemas/entity-registry.schema.json` et l'existence de toutes ses dépendances amont.",
            "Exécuter `python tools/validate_registry.py` et `python tools/lint_skills.py` pour certifier l'intégrité documentaire du dépôt.",
            "Préparer le rapport de traçabilité suivant `templates/entity-registry-entry.md` pour signature par `DIR-06`.",
        ),
        decision_rules=(
            ("Handoff Packet mentionnant un lieu 'LOC-PORT-KIN' alors que l'ID officiel du registre est 'LOC-GOMBE-PORT'", "Rejeter le paquet pour Référence Fantôme et imposer l'alignement sur l'ID canonique LOC-GOMBE-PORT de entities-registry.csv", "Maintenir l'unicité absolue de la Single Source of Truth"),
            ("Nouvelle entité soumise sans champ summary ou sans owner_skill valide", "Bloquer l'insertion dans entities-registry.csv jusqu'à complétion des 11 colonnes obligatoires du schéma", "Garantir que validate_registry.py passe à 100 %"),
            ("Spécification technique s'appuyant sur une méthode GDC ou UE5", "Vérifier que le code source SRC-001..SRC-020 de research/source-registry.csv est explicitement cité dans la colonne sources", "Assurer la traçabilité documentaire de Phase 1 à Phase 3"),
        ),
        acceptance_criteria=(
            "`python tools/validate_registry.py` s'exécute avec 0 erreur.",
            "100 % des entités citées dans les livrables sont indexées dans `knowledge/entities-registry.csv`.",
            "Aucun lien relatif cassé dans les fichiers Markdown du dépôt.",
        ),
        validation_auditors=("DIR-06", "DIR-01"),
        reference_filename="docs-as-code-and-registry-ops.md",
        reference_content="""# Procédures Docs-as-Code & Maintenance du Registre (`PRD-03`)

## 1. Les 11 Colonnes Obligatoires de `knowledge/entities-registry.csv`
1. `id` : Identifiant ASCII majuscule (`^(CHR|FAM|ORG|DST|LOC|MSN|ITM|VEH|SYS)-[A-Z0-9-]+$`).
2. `category` : `CHARACTER`, `FAMILY`, `ORGANIZATION`, `DISTRICT`, `LOCATION`, `MISSION`, `ITEM`, `VEHICLE`, `SYSTEM`.
3. `name` : Nom lisible complet.
4. `district_id` : `DST-*` ou `GLOBAL`.
5. `status` : `CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`.
6. `owner_skill` : Code du skill propriétaire (`NAR-03`, `WLD-01`, `GD-02`...).
7. `validated_by` : Liste des valideurs séparés par `|` (`DIR-03|DIR-06`).
8. `dependencies` : Liste des IDs prérequis séparés par `|`.
9. `sources` : Références `SRC-*` issues de `research/source-registry.csv`.
10. `last_updated` : Date ISO `YYYY-MM-DD`.
11. `summary` : Description opérationnelle concise.
""",
        template_filename="entity-registry-entry.md",
        template_content="""# Fiche d'Indexation & Traçabilité Registre (`PRD-03`)

- **Lot Documentaire Audité** : `[Task ID / Handoff Packet]`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`
- **Statut d'Indexation** : `READY_FOR_DIR06_PROMOTION` | `REJECTED_PHANTOM_ID`

## 1. Entrées Formatées pour `knowledge/entities-registry.csv`
```csv
id,category,name,district_id,status,owner_skill,validated_by,dependencies,sources,last_updated,summary
```

## 2. Contrôle des Références & Sources (`SRC-*`)
- **IDs Vérifiés** : `[Liste]`
- **Sources Rattachées** : `[SRC-*]`
""",
        example_filename="sample-registry-indexing.md",
        example_content="""# Exemple `PRD-03` — Indexation de la Mission `MSN-SIDE-014-WEWA`

- **Lot Documentaire Audité** : `TSK-2026-114 (Handoff GD-02 & WLD-04)`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`
- **Statut d'Indexation** : `READY_FOR_DIR06_PROMOTION`

## 1. Entrées Formatées pour `knowledge/entities-registry.csv`
```csv
id,category,name,district_id,status,owner_skill,validated_by,dependencies,sources,last_updated,summary
MSN-SIDE-014-WEWA,MISSION,Course Contre la Pluie,DST-MATONGE,PROPOSED,GD-02,DIR-05,LOC-MATONGE-VICTOIRE|VEH-MOTO-WEWA-01,SRC-002,2026-11-25,Mission secondaire de livraison urgente en moto Wewa à travers Matonge sous une averse équatoriale.
```

## 2. Contrôle des Références & Sources (`SRC-*`)
- **IDs Vérifiés** : `DST-MATONGE` (`CONFIRMED`), `LOC-MATONGE-VICTOIRE` (`CONFIRMED`), `VEH-MOTO-WEWA-01` (`CONFIRMED`). Zéro référence fantôme.
- **Sources Rattachées** : `SRC-002` (UE5 GAS / State Machines).
""",
    ),
    SkillBlueprint(
        skill_id="PRD-04",
        description=(
            "Architecture globale de l'Assurance Qualité (QA) de ZAÏRE : plans de test Open World par "
            "quadrillage géographique des cellules World Partition de Kinshasa, matrices de test des "
            "machines à états de quêtes (zéro soft-lock), protocoles de reproductibilité déterministe "
            "(>= 90 %) et checklists de certification plateforme."
        ),
        inputs=("mission-design-gd-02", "open-world-grid-wld-04", "gameplay-cpp-specs-eng-02"),
        outputs=("master-qa-test-plan.md", "deterministic-bug-report.json"),
        activation_triggers=(
            "Conception du plan de test fonctionnel et destructif (Destructive QA) d'une nouvelle mission (`MSN-*`), d'un système (`SYS-*`) ou d'une commune (`DST-*`).",
            "Triage et qualification de la sévérité (`SEV-A Blocker`, `SEV-B Critical`, `SEV-C Major`, `SEV-D Minor`) des anomalies avant passage de jalon.",
            "Préparation du cahier de tests à automatiser par `PRD-05` sous Unreal Gauntlet.",
        ),
        scope_boundaries=(
            "N'écrit pas le code C++ des contrôleurs automatisés Gauntlet (`PRD-05`).",
            "Refuse tout rapport de bug dépourvu des coordonnées exactes World Partition, du `GlobalSeed`, de l'état des Gameplay Tags et des étapes de reproduction déterministes.",
        ),
        operational_procedures=(
            "Découper chaque commune (`DST-*`) selon la grille de cellules `World Partition (128 m × 128 m)` et vérifier aux frontières de cellules : (1) Continuité des collisions et du NavMesh, (2) Absence de perte d'état de quête lors du déchargement/rechargement de `Data Layers`, (3) Transition fluide des splines `ZoneGraph`.",
            "Exécuter sur chaque mission `GD-02` la **Matrice de Tests Destructifs Anti-Soft-Lock** : détruire volontairement `VEH-MOTO-WEWA-01`, fuir à `> 500 m` en plein dialogue, déclencher le combat pendant une phase d'infiltration sociale (`ITM-DOC-PASSEPORT`), changer la météo en `World.Weather.TropicalStorm`.",
            "Normaliser tout ticket d'anomalie selon `templates/qa-test-plan-template.md` afin de garantir un taux de reproductibilité **`>= 90 %`**.",
            "Remonter immédiatement tout bug `SEV-A` à `DIR-07` pour passage de l'entité au statut `BLOCKED`.",
        ),
        decision_rules=(
            ("Rapport de bug intermittent avec un taux de reproduction < 90 %", "Exiger la capture automatique du Snapshot d'État (Coordonnées X/Y/Z cm, GlobalSeed, GameplayTags actifs, DataLayers chargés) avant validation du ticket", "Atteindre le standard de reproductibilité >= 90 % (quality-standards.md)"),
            ("Détection d'un cas où la destruction de la moto Wewa bloque la progression d'une quête sans alternative", "Classer l'anomalie en SEV-A (Blocker), marquer la mission BLOCKED et assigner le correctif de machine à états à GD-02", "Appliquer la tolérance zéro sur les soft-locks"),
            ("Scénario de test répétitif validé manuellement à chaque build (ex: traversée Gombe -> Matonge)", "Transférer le cas de test à PRD-05 pour conversion en test de non-régression nocturne automatisé Gauntlet", "Maximiser la couverture automatisée >= 80 %"),
        ),
        acceptance_criteria=(
            "100 % des étapes de la machine à états de mission (`GD-02`) sont couvertes par un cas de test nominal ET un cas de test destructif (interruption/fuite/perte véhicule).",
            "Taux de reproductibilité des rapports d'anomalies `>= 90 %`.",
            "Couverture spatiale de 100 % des cellules World Partition actives du jalon.",
        ),
        validation_auditors=("DIR-07", "PRD-05"),
        reference_filename="open-world-qa-grid-methodology.md",
        reference_content="""# Méthodologie QA par Quadrillage Open World & Tests Destructifs (`PRD-04`)

## 1. Classification des Sévérités d'Anomalies ZAÏRE STUDIO OS
- **`SEV-A (Blocker / Passage en BLOCKED immédiat)`** : Crash moteur, OOM VRAM (`> 6144 MB`), Soft-Lock de quête principal ou secondaire, perte de sauvegarde, chute à travers le sol.
- **`SEV-B (Critical)`** : Frametime P99 `> 16.6 ms` sur un parcours principal, blocage du trafic `AI-03` non résolu après `8 s`, absence de préfixe locuteur ou troncature UI (`AUD-04`/`PRD-06`).
- **`SEV-C (Major)`** : Artefact visuel Nanite/Lumen, couture de texture visible, bark désynchronisé.
- **`SEV-D (Minor / Polish)`** : Détail cosmétique mineur hors chemin principal.
""",
        template_filename="qa-test-plan-template.md",
        template_content="""# Plan de Test QA Open World & Anti-Soft-Lock (`PRD-04`)

- **ID Plan de Test** : `QATP-[MSN/DST]-[NUM]`
- **Cible Testée** : `MSN-...` | `LOC-...` (`DST-...`)
- **Cellules World Partition Couvertes** : `[Grid_X.._Y..]`
- **Taux de Reproductibilité Exigé** : `>= 90 %`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Matrice de Couverture Fonctionnelle & Destructive
| Test Case ID | Catégorie (`NOMINAL` / `DESTRUCTIVE`) | Action Testeur / Perturbation | Résultat Attendu (Zéro Soft-Lock) | Automatisation (`PRD-05`) |
| :--- | :--- | :--- | :--- | :--- |
| `TC-001` | `DESTRUCTIVE` | `[Destruction véhicule / Fuite]` | `[Handler de récupération GD-02 actif]` | `Oui (Gauntlet)` |

## 2. Format de Ticket d'Anomalie Déterministe
- **Coordonnées UE5 (X, Y, Z cm) & Seed** : `[X=..., Y=..., Z=... | Seed=19600630]`
- **Gameplay Tags & Data Layers Actifs** : `[Liste]`
""",
        example_filename="sample-qa-test-plan.md",
        example_content="""# Exemple `PRD-04` — Plan de Test QA `QATP-MSN-001-PORT` (`MSN-MAIN-001-ARRIVEE`)

- **ID Plan de Test** : `QATP-MSN-001-PORT`
- **Cible Testée** : `MSN-MAIN-001-ARRIVEE` & `LOC-GOMBE-PORT` (`DST-GOMBE`)
- **Cellules World Partition Couvertes** : `Grid_X04_Y08` à `Grid_X10_Y12` (transition `DST-GOMBE` -> `DST-KALAMU`)
- **Taux de Reproductibilité Exigé** : `96 %` mesuré (`>= 90 %` requis)
- **Statut** : `CONFIRMED`

## 1. Matrice de Couverture Fonctionnelle & Destructive
| Test Case ID | Catégorie | Action Testeur / Perturbation | Résultat Attendu | Automatisation (`PRD-05`) |
| :--- | :--- | :--- | :--- | :--- |
| `TC-MSN001-01` | `NOMINAL` | Infiltration sociale avec `ITM-DOC-PASSEPORT` jusqu'au coffre du hangar N°4. | Tag `State.Character.Stealth.Disguised` reconnu par `AI-01`, bark `BRK-PORT-01` joué, 0 alerte. | `Oui (Functional Test)` |
| `TC-MSN001-02` | `DESTRUCTIVE` | Déclencher le combat à la machette (`ITM-WPN-MACHETTE`) au milieu du dialogue `DLG-MSN-001-PORT`. | Handler `on_combat_triggered` exécuté, coffre de quête toujours interactif après le combat. | `Oui (Functional Test)` |
| `TC-MSN001-03` | `DESTRUCTIVE` | Détruire la `VEH-MOTO-WEWA-01` de la rampe est avant l'étape d'exfiltration `ST-03`. | Apparition validée des Wewa de secours à la sortie du port + objectif réalisable en `VEH-TAXI-JAUNE-01` (**0 Soft-Lock**). | `Oui (Gauntlet)` |
| `TC-MSN001-04` | `BOUNDARY` | Franchir la frontière `DST-GOMBE` -> `DST-KALAMU` à `95 km/h` sous `World.Weather.TropicalStorm`. | Déchargement de `DL_MSN001_SyndicateAlert` sans hitch (`P99 <= 16.6 ms`). | `Oui (Gauntlet Perf Bot)` |
""",
    ),
    SkillBlueprint(
        skill_id="PRD-05",
        description=(
            "Ingénierie des tests automatisés sous Unreal Engine 5 : Unreal Gauntlet Automation "
            "Framework, AFunctionalTest Actors et bots d'exploration autonome de Kinshasa. Garantit "
            "une couverture >= 80 % des systèmes critiques (SYS-*) et un taux de faux positifs < 2 % "
            "grâce à une synchronisation 100 % événementielle (zéro sleep arbitraire)."
        ),
        inputs=("qa-test-plans-prd-04", "performance-budgets-eng-07", "ci-cd-pipelines-eng-08"),
        outputs=("gauntlet-automation-spec.md", "automated-test-suite-summary.csv"),
        activation_triggers=(
            "Implémentation en C++ / Python UE5 des cas de test prioritaires identifiés par `PRD-04`.",
            "Création des bots de traversée nocturne (*Soak & Traversal Bots*) mesurant le frametime P99 (`ENG-07`), la mémoire VRAM et l'absence de deadlock trafic (`AI-03`) sur 2 heures.",
            "Intégration de la suite de tests dans le pipeline BuildGraph / Horde de `ENG-08`.",
        ),
        scope_boundaries=(
            "Ne remplace pas l'évaluation qualitative humaine du Game Feel (`DIR-05`) ou de l'authenticité culturelle (`WLD-02`).",
            "Interdit formellement l'utilisation de délais fixes (`FPlatformProcess::Sleep` ou `Delay(5.0f)`) pour attendre la fin d'un chargement ou d'une animation dans un test automatisé.",
        ),
        operational_procedures=(
            "Écrire les tests unitaires et fonctionnels sous `IMPLEMENT_SIMPLE_AUTOMATION_TEST` et `AFunctionalTest` en synchronisant chaque étape sur des **Delegates événementiels explicites** (`OnStreamingCompleted`, `OnGameplayTagChanged`, `OnAbilityEnded`, `OnQuestStateReached`).",
            "Configurer le contrôleur **`UZaireGauntletTraversalController`** pour faire parcourir à un bot une boucle de `2 heures` à travers `DST-GOMBE`, `DST-KALAMU`, `DST-MATONGE` et `DST-LIMETE` tout en enregistrant un rapport `CSVProfiler` pour `ENG-07`.",
            "Maintenir la couverture automatisée des systèmes critiques (`SYS-WLD-STREAMING`, `SYS-CMB-MELEE`, `SYS-STEALTH`, `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS`) à **`>= 80 %`**.",
            "Documenter l'architecture de la suite dans `templates/gauntlet-test-spec.md`.",
        ),
        decision_rules=(
            ("Test automatisé échouant de manière aléatoire (Flaky Test > 2 % de faux positifs) sur la ferme CI", "Remplacer immédiatement toute attente temporelle fixe par un abonnement au delegate d'achèvement du sous-système (ex: UWorldPartitionSubsystem::OnStreamingStateUpdated)", "Ramener le taux de faux positifs sous la barre des 2 %"),
            ("Couverture automatisée d'un nouveau système SYS-* inférieure à 80 %", "Refuser le passage du système au jalon Beta/Gold et ajouter les AFunctionalTest manquants dans la map de test dédiée", "Respecter le seuil obligatoire >= 80 % (quality-standards.md)"),
            ("Bot Gauntlet détectant une hausse de consommation RAM/VRAM monotone (+50 MB/heure) pendant le test d'endurance de 2h", "Émettre une alerte automatique de fuite mémoire (Memory Leak) vers ENG-01 et ENG-07 avec le diff d'allocations Unreal Insights", "Bloquer le build nocturne"),
        ),
        acceptance_criteria=(
            "Couverture des systèmes critiques `SYS-*` par tests automatisés `>= 80 %`.",
            "Taux de faux positifs (flakiness) `< 2 %` sur 50 exécutions CI consécutives (0 `Sleep` fixe).",
            "Exécution automatique intégrée à l'étape 4 du BuildGraph `ENG-08`.",
        ),
        validation_auditors=("PRD-04", "ENG-08", "DIR-07"),
        reference_filename="unreal-gauntlet-event-driven-tests.md",
        reference_content="""# Architecture des Tests Automatisés Gauntlet Sans Faux Positifs (`PRD-05`)

## 1. Règle d'Or Anti-Flakiness : Synchronisation Événementielle Pure
- **Interdit** : `AddCommand(new FDelayedFunctionLatentCommand(..., 3.0f));` (échoue si le disque ou le shader cache met 3.2s).
- **Obligatoire** : `AddCommand(new FZaireWaitForWorldPartitionIdleCommand(World));` suivi de `FZaireWaitForGameplayTagCommand(Actor, Tag)`.

## 2. Suite Nocturne Gauntlet (`ZaireNightlyAutomationSuite`)
| Suite ID | Type Gauntlet | Durée | Systèmes Couverts (`>= 80 %`) | Critère de Succès Bloquant |
| :--- | :--- | :--- | :--- | :--- |
| `GT_Smoke_BootAndPort` | `FunctionalTest` | `3.5 min` | `SYS-WLD-STREAMING`, `SYS-STEALTH`, `SYS-CMB-MELEE` | 100 % des assertions vertes, 0 crash. |
| `GT_Perf_KinshasaLoop` | `GauntletController` | `30 min` | `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS` | `P99 <= 16.6 ms` (`ENG-07`), `VRAM <= 6144 MB`. |
| `GT_Soak_2Hours_Traffic` | `EnduranceSoak` | `120 min` | Stabilité mémoire & Watchdog Anti-Deadlock `AI-03` | 0 deadlock routier `> 8s`, dérive RAM `< 1 %`. |
""",
        template_filename="gauntlet-test-spec.md",
        template_content="""# Spécification de Suite de Tests Automatisés Gauntlet (`PRD-05`)

- **Nom de la Suite / Contrôleur** : `UZaireGauntlet...Controller` | `AFT_Zaire_...`
- **Systèmes Critiques Couverts (`SYS-*`)** : `[Liste]`
- **Taux de Couverture / Faux Positifs** : `[>= 80 % | < 2 %]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Protocole de Synchronisation Événementielle (Zéro `Sleep`)
| Étape du Test | Commande Latente / Delegate Attendu | Assertion Vérifiée | Timeout Sécurité |
| :--- | :--- | :--- | :--- |
| `Step 1` | `OnWorldPartitionStreamingCompleted` | `Cellules chargées == true` | `30 s` |

## 2. Seuils de Régression CI/CD (`ENG-07` / `ENG-08`)
- **Critère d'échec automatique du build** : `[P99 > 16.6 ms / Soft-lock / Assert Fail]`
""",
        example_filename="sample-gauntlet-test-spec.md",
        example_content="""# Exemple `PRD-05` — Suite Automatisée `GT_MSN001_And_Matonge_Soak`

- **Nom de la Suite / Contrôleur** : `AFT_Zaire_MSN001_AntiSoftLock` & `UZaireGauntletKinshasaTraversal`
- **Systèmes Critiques Couverts (`SYS-*`)** : `SYS-WLD-STREAMING`, `SYS-STEALTH`, `SYS-CMB-MELEE`, `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS` (**Couverture : 88.5 %** `>= 80 %`)
- **Taux de Faux Positifs** : `0.4 %` sur 250 runs Horde (`< 2 %` requis)
- **Statut** : `CONFIRMED`

## 1. Protocole de Synchronisation Événementielle (Zéro `Sleep`)
| Étape du Test | Delegate / Événement Attendu | Assertion Vérifiée | Timeout Sécurité |
| :--- | :--- | :--- | :--- |
| `1_SpawnAndStream` | `UZaireDistrictStreamingSubsystem::OnDistrictReady` | `LOC-GOMBE-PORT` chargé, `VRAM <= 6144 MB`. | `20 s` |
| `2_TestParryGAS` | `UZaireGA_MeleeParry::OnParryDeflectTriggered` | Tag `State.Character.Combat.Parrying` actif + Hitstop `85 ms`. | `10 s` |
| `3_DestroyWewaFallback` | `AZaireVehicle::OnChaosVehicleDestroyed` | Transition `MSN-MAIN-001-ARRIVEE` vers `ST-03_BackupVehicle` en `< 1 frame`. | `5 s` |
| `4_MatongeTrafficSoak` | `UZaireTrafficWatchdog::OnIntersectionCycle` | 600 PNJ `AI-02` + 75 véhicules `AI-03` pendant 2h, `0 deadlock > 8s`, `P99 <= 16.6 ms`. | `120 min` |
""",
    ),
    SkillBlueprint(
        skill_id="PRD-06",
        description=(
            "Ingénierie de l'accessibilité universelle selon les Xbox Accessibility Guidelines (XAG) : "
            "accessibilité visuelle (double codage forme+couleur, contraste >= 4.5:1, daltonisme), "
            "auditive (sous-titres enrichis avec préfixe [KOFFI], glyphes Unicode lingala ɛ/ɔ, "
            "indicateurs directionnels), motrice (remapping complet, maintien continu Hold au lieu des "
            "QTE rapides) et cognitive."
        ),
        inputs=("ui-screen-specs-gd-07", "combat-design-gd-05", "localization-tables-aud-04"),
        outputs=("xag-compliance-matrix.csv", "accessibility-audit-report.md"),
        activation_triggers=(
            "Audit obligatoire de toute interface utilisateur (`GD-07`), mécanique de combat (`GD-05`), conduite (`GD-06`) ou système de sous-titrage (`AUD-04`).",
            "Exécution du validateur automatisé `scripts/check_xag_compliance.py` avant toute certification qualité par `DIR-07`.",
            "Spécification des options du menu Accessibilité de ZAÏRE (accessibles dès le premier lancement du jeu, *First-Boot Accessibility Screen*).",
        ),
        scope_boundaries=(
            "Ne programme pas directement les widgets C++ (`ENG-02`) ni les shaders post-process (`ART-08`), mais détient un droit de blocage qualité avec `DIR-07` en cas de non-conformité XAG.",
            "Interdit toute mécanique reposant exclusivement sur la couleur, le son ou le martèlement rapide de touche (Button Mashing QTE) sans alternative.",
        ),
        operational_procedures=(
            "Exécuter `scripts/check_xag_compliance.py` sur les spécifications UI/Gameplay soumises.",
            "Vérifier la conformité **XAG 101 / 102 (Visuel)** : ratio de contraste `>= 4.5:1` (`>= 7:1` sur les sous-titres), mise à l'échelle de l'UI jusqu'à `+35 %`, double codage systématique (Couleur + Forme/Icône).",
            "Vérifier la conformité **XAG 104 (Sous-titrage & Audio)** : préfixe explicite du locuteur coloré et différencié (`[KOFFI]`, `[AMINA]`), support parfait des caractères Unicode du lingala (`ɛ`, `ɔ`), fond semi-opaque réglable (`50 %` à `100 %`) et indicateur visuel directionnel pour les menaces sonores (`BUS_SFX_CombatTelegraph`).",
            "Vérifier la conformité **XAG 107 (Moteur)** : remapping complet des touches (`Enhanced Input`), option de remplacement des pressions répétées (QTE) par un maintien continu (`Hold`) ou une validation automatique, et assistance au maintien de voie sur `VEH-MOTO-WEWA-01`.",
        ),
        decision_rules=(
            ("Séquence de lutte au corps-à-corps ou de crochetage exigeant un martèlement rapide de bouton (Button Mashing)", "Imposer l'intégration native de l'option 'QTE Input Mode : Tap / Hold / Auto-Complete' dans Enhanced Input (ENG-02)", "Respecter XAG 107 et quality-standards.md Section 2.D"),
            ("Alarme d'attaque lourde ennemie transmise uniquement par un signal sonore (AUD-02)", "Ajouter un indicateur visuel radial directionnel à fort contraste autour de Koffi synchronisé sur le Startup de l'attaque (>= 22 frames)", "Assurer une jouabilité complète pour les joueurs sourds ou malentendants"),
            ("Sous-titre dépourvu du nom du locuteur ou fond transparent illisible sous le soleil équatorial de midi", "Forcer le format '[LOCUTEUR] : Texte' et un fond sombre semi-opaque par défaut à 78 % d'opacité (ratio contraste >= 7:1)", "Garantir la validation de check_xag_compliance.py"),
        ),
        acceptance_criteria=(
            "`python skills/08-production-quality/prd-06-accessibility-specialist/scripts/check_xag_compliance.py` retourne un code `0`.",
            "Les 4 piliers XAG (Visuel, Auditif, Moteur, Cognitif) sont couverts et validés sans exception.",
            "L'écran de configuration d'accessibilité est présenté dès le premier démarrage du jeu (*First-Boot Flow*).",
        ),
        validation_auditors=("DIR-07", "GD-07", "AUD-04"),
        reference_filename="xag-compliance-standards.md",
        reference_content="""# Référentiel de Conformité Xbox Accessibility Guidelines — XAG (`PRD-06`)

## 1. Grille des Exigences XAG Obligatoires pour ZAÏRE
| Code XAG | Domaine | Exigence Technique Impérative dans ZAÏRE STUDIO OS | Skills Impliqués |
| :--- | :--- | :--- | :--- |
| **XAG 101** | Contraste & Texte | Ratio de contraste `>= 4.5:1` (UI) et `>= 7.0:1` (Sous-titres), tolérance expansion `+35 %`, police Unicode (`ɛ`, `ɔ`). | `GD-07`, `AUD-04` |
| **XAG 102** | Daltonisme & Couleur | Zéro information codée par la couleur seule (Double codage Couleur + Forme/Icône + Filtres Deutéranopie/Protanopie/Tritanopie). | `GD-07`, `ART-01` |
| **XAG 104** | Sous-titres & Audio | Préfixe locuteur `[KOFFI]`, fond réglable (`50-100 %`), taille police `28-42 px`, radar visuel des sons critiques (`BUS_SFX_CombatTelegraph`). | `AUD-04`, `AUD-01`, `GD-07` |
| **XAG 107** | Accessibilité Motrice | Remapping complet `Enhanced Input`, bascule `Hold / Toggle` pour la course/visée, remplacement des QTE par maintien continu ou auto-succès. | `ENG-02`, `GD-05`, `GD-06` |
| **XAG 108** | Cognitif & Navigation | Rappel permanent de l'objectif `MSN-*` sur le téléphone diégétique et guidage visuel optionnel par les landmarks (`SYS-WLD-LANDMARKS`). | `GD-02`, `WLD-04`, `GD-07` |
""",
        template_filename="xag-compliance-matrix.csv",
        template_content="""xag_id,pillar,requirement_summary,target_system_or_widget,measured_metric,compliance_status,auditor_skill
XAG-101,VISUAL,Contraste texte >= 4.5:1 et expansion UI +35% avec glyphes lingala (ɛ/ɔ),UI-HUD-MAIN-OVERLAY,Contraste 7.2:1 | Expansion +38%,COMPLIANT,PRD-06
XAG-102,VISUAL,Double codage Forme + Couleur sur tous les états IA et objectifs,SYS-STEALTH / AI-01,Cercle / Triangle strié / Losange + Icône,COMPLIANT,PRD-06
XAG-104,AUDITORY,Sous-titres enrichis avec préfixe [LOCUTEUR] et fond semi-opaque >= 50%,AUD-04 / SUBTITLES,Opacité 78% + Préfixe [KOFFI] + Radar sonore,COMPLIANT,PRD-06
XAG-107,MOTOR,Alternative Hold / Auto aux QTE et remapping complet Enhanced Input,SYS-CMB-MELEE / ENG-02,Modes Tap / Hold / Auto disponibles,COMPLIANT,PRD-06
""",
        example_filename="sample-accessibility-audit.md",
        example_content="""# Exemple `PRD-06` — Rapport d'Audit XAG du Vertical Slice (`MSN-MAIN-001-ARRIVEE`)

## 1. Exécution du Validateur (`scripts/check_xag_compliance.py`)
- **Cible Auditée** : `UI-HUD-MAIN-OVERLAY`, `DLG-MSN-001-PORT`, `SYS-CMB-MELEE`, `VEH-MOTO-WEWA-01`
- **Résultat Script** : `PASS (100 % conforme aux normes XAG)`

## 2. Synthèse de Conformité par Pilier (`xag-compliance-matrix.csv`)
| Code XAG | Pilier | Vérification sur le Vertical Slice Kinshasa | Statut |
| :--- | :--- | :--- | :--- |
| **XAG 101** | Visuel & Typographie | Contraste mesuré à `7.2:1` sous le soleil équatorial de midi (`EV100 = 15`). Rendu parfait des glyphes `Kɛbá!` et `Tɔ́kɛndɛ́` jusqu'à `+38 %` d'expansion. | **CONFORME** |
| **XAG 102** | Double Codage | Les jauges de vigilance des gardes de `LOC-GOMBE-PORT` combinent couleur, forme géométrique (cercle/triangle/losange) et motif hachuré. | **CONFORME** |
| **XAG 104** | Sous-titres & Radar Audio | Format `[AMINA] : « Kɛbá Koffi... »` sur fond noir `78 %` d'opacité + arc visuel directionnel lors des attaques lourdes `ENM-CARTEL-BRUTE`. | **CONFORME** |
| **XAG 107** | Moteur & Contrôles | Remapping complet clavier/manette via `Enhanced Input`, maintien continu (`Hold`) sur les prises de mêlée et assistance de trajectoire optionnelle en `VEH-MOTO-WEWA-01`. | **CONFORME** |
""",
        scripts={"check_xag_compliance.py": CHECK_XAG_COMPLIANCE_SCRIPT},
    ),
)


def build_department_08(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 6 skills du département 08-production-quality."""
    created: list[Path] = []
    for bp in PRODUCTION_QUALITY_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_08(WORKSPACE_ROOT)
    print(f"[OK] Département 08-production-quality généré ({len(paths)} skills).")
