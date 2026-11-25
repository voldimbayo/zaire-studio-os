"""Spécifications et génération du Département 04-AI-SIMULATION (AI-01 à AI-04)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_MASS_BUDGET_SCRIPT = '''"""Calculateur de budget CPU ECS Mass Crowd & Hydratation pour AI-02."""

from __future__ import annotations

import argparse
import json
import sys


def evaluate_crowd_budget(
    hydrated_actors: int = 18,
    mass_lod1_count: int = 180,
    mass_lod2_count: int = 420,
    mode: str = "perf_60fps",
) -> dict:
    """Calcule le coût CPU estimé (en ms) de la simulation de foule par commune."""
    # Coûts unitaires moyens mesurés sous UE5 Mass Entity / ZoneGraph
    npc_ai_ms = round(hydrated_actors * 0.095, 3)  # Budget AI-01 max 2.5 ms (24 acteurs max)
    mass_cpu_ms = round((mass_lod1_count * 0.0045) + (mass_lod2_count * 0.0018), 3)

    max_npc_budget = 2.5 if mode == "perf_60fps" else 3.0
    max_mass_budget = 2.0 if mode == "perf_60fps" else 2.5

    within_budget = (
        hydrated_actors <= 24
        and npc_ai_ms <= max_npc_budget
        and mass_cpu_ms <= max_mass_budget
    )
    return {
        "mode": mode,
        "hydrated_actors_ai01": hydrated_actors,
        "mass_entities_total": mass_lod1_count + mass_lod2_count,
        "estimated_ai01_cpu_ms": npc_ai_ms,
        "estimated_mass_cpu_ms": mass_cpu_ms,
        "max_mass_budget_ms": max_mass_budget,
        "within_budget": within_budget,
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Vérifie le budget CPU Mass Crowd (AI-02).")
    parser.add_argument("--hydrated", type=int, default=18, help="Nombre d'acteurs hydratés ACharacter (max 24)")
    parser.add_argument("--lod1", type=int, default=180, help="Entités Mass LOD1 (25m - 80m)")
    parser.add_argument("--lod2", type=int, default=420, help="Entités Mass LOD2 (80m - 250m)")
    parser.add_argument("--file", help="Fichier JSON de configuration Mass Crowd à valider (optionnel)")
    parser.add_argument("--output", help="Chemin de sauvegarde du rapport JSON (optionnel)")
    args = parser.parse_args()

    hydrated, lod1, lod2 = args.hydrated, args.lod1, args.lod2
    mode = "perf_60fps"
    if args.file:
        from pathlib import Path
        cfg = json.loads(Path(args.file).read_text(encoding="utf-8"))
        hydrated = int(cfg.get("hydrated_actors_ai01", hydrated))
        lod1 = int(cfg.get("mass_lod1_count", lod1))
        lod2 = int(cfg.get("mass_lod2_count", lod2))
        mode = str(cfg.get("mode", mode))

    result = evaluate_crowd_budget(hydrated, lod1, lod2, mode)
    formatted = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(formatted + "\\n", encoding="utf-8")
    print(formatted)
    return 0 if result["within_budget"] else 1


if __name__ == "__main__":
    sys.exit(main())
'''

AI_SIMULATION_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="AI-01",
        description=(
            "Architecture des comportements individuels des PNJ (gardes ORG-CARTEL-FLEUVE, alliés, "
            "cibles prioritaires) sous UE5 State Trees, Environment Query System (EQS), AI Perception "
            "et Smart Objects dans un budget CPU strict <= 2.5 ms (max 24 acteurs actifs)."
        ),
        inputs=("combat-archetypes-gd-05", "level-blockouts-wld-05", "cpu-budgets-dir-04"),
        outputs=("npc-ai-architecture.md", "eqs-and-statetree-spec.md"),
        activation_triggers=(
            "Conception des boucles de patrouille, d'investigation furtive (`SYS-STEALTH`) et de combat tactique (`SYS-CMB-MELEE`) des PNJ individuels.",
            "Paramétrage des requêtes spatiales EQS (recherche de couvert `100 cm`/`200 cm`, flanquement dans les hangars de `LOC-GOMBE-PORT`) et du gestionnaire d'Attack Tokens.",
            "Optimisation du budget CPU `PERF-CPU-NPCAI` (`<= 2.5 ms` en mode 60 FPS).",
        ),
        scope_boundaries=(
            "Ne gère jamais les foules de centaines de citoyens passifs (`AI-02` Mass Crowd) ni le flux routier (`AI-03` Mass Traffic).",
            "Interdit de dépasser **24 acteurs `AI-01` actifs simultanément** dans la bulle de simulation du joueur.",
        ),
        operational_procedures=(
            "Structurer la logique décisionnelle du PNJ sous **UE5 State Trees** en 4 états racines : `Idle/SmartObject`, `Patrol/Suspicion`, `Combat/Tactical` et `Search/De-escalation`.",
            "Configurer `UAIPerceptionComponent` (Sight + Hearing) pour réagir dynamiquement aux Gameplay Tags du joueur (`State.Character.Stealth.Concealed`, `State.Character.Stealth.Disguised`, `World.Weather.TropicalStorm`).",
            "Appliquer un **Time-Slicing strict sur les requêtes EQS** (maximum 2 évaluations EQS complètes par frame sur l'ensemble de l'escouade, rafraîchissement de couvert toutes les `0.4 s`).",
            "Relier l'exécution des attaques au gestionnaire d'**Attack Tokens (`GD-05`)** et aux déclencheurs de barks (`NAR-04`).",
        ),
        decision_rules=(
            ("Mission demandant plus de 24 PNJ actifs dans la même zone", "Conserver au maximum 24 acteurs AI-01 et transférer tous les figurants/travailleurs vers AI-02 Mass Crowd avec hydratation à la demande", "Respecter le plafond absolu PERF-CPU-NPCAI <= 2.5 ms"),
            ("Requête EQS provoquant un pic > 0.5 ms sur le Game Thread", "Réduire la densité de la grille de points EQS (espacement 150 cm au lieu de 50 cm) et activer le tri préalable par distance avant les raycasts de visibilité", "Garantir la fluidité 60 FPS"),
            ("PNJ bloqué devant un obstacle dynamique ou un véhicule garé de travers", "Activer un NavModifier dynamique autour des véhicules à l'arrêt et un fallback de contournement Smart Link (escalade couvert 100 cm)", "Éliminer tout blocage NavMesh"),
        ),
        acceptance_criteria=(
            "Le coût CPU cumulé des 24 acteurs `AI-01` est `<= 2.5 ms` (60 FPS) / `<= 3.0 ms` (30 FPS).",
            "Le système d'Attack Tokens empêche formellement plus de 2 assauts de mêlée simultanés.",
            "Les seuils de détection visuelle et auditive s'adaptent aux Gameplay Tags de météo et de déguisement.",
        ),
        validation_auditors=("ENG-07", "GD-05", "WLD-05"),
        reference_filename="statetree-and-eqs-optimization.md",
        reference_content="""# Architecture UE5 State Trees, EQS & Perception (`AI-01`)

## 1. Budget & Plafonds d'Exécution (`PERF-CPU-NPCAI`)
- **Enveloppe CPU Max** : `2.5 ms` sur Game Thread / Worker Threads (`<= 24` acteurs `ACharacter` actifs).
- **Fréquence de Tick Perception** : `10 Hz` (`0.1 s`) pour les ennemis à `< 20 m` ; `4 Hz` (`0.25 s`) entre `20 m` et `60 m`.
- **Budget EQS** : Time-slicing réglé à `0.35 ms/frame` max pour l'évaluation des points de couverture.

## 2. Modulation Sensorielle par Gameplay Tags
| Gameplay Tag Actif | Multiplicateur Cône Visuel | Multiplicateur Rayon Auditif | Comportement Garde |
| :--- | :--- | :--- | :--- |
| `State.Character.Stealth.Concealed` | `0.25x` | `1.00x` | Ignore le joueur sauf à distance `< 300 cm` en plein axe. |
| `State.Character.Stealth.Disguised` | `0.15x` (zone autorisée) | `1.00x` | Salue ou contrôle verbalement (`BRK-PORT-01`) sans alerte immédiate. |
| `World.Weather.TropicalStorm` | `0.70x` (pluie dense) | `0.60x` (masquage pluie) | Cherche un abri Smart Object sous les auvents si non alerté. |
""",
        template_filename="npc-ai-architecture.md",
        template_content="""# Spécification d'Architecture IA PNJ (`AI-01`)

- **ID Profil IA** : `AI-PRF-[SLUG]`
- **Archétypes Associés (`GD-05`)** : `[ENM-* / CHR-*]`
- **Plafond Acteurs Simultanés** : `[<= 24]`
- **Budget CPU Alloué** : `<= 2.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Hiérarchie UE5 State Tree
| État State Tree | Condition d'Entrée (Tags / Perception) | Tâches & Smart Objects | Bark Associé (`NAR-04`) |
| :--- | :--- | :--- | :--- |
| `ST_Patrol` | `[Condition]` | `[Action]` | `BRK-...` |

## 2. Configuration des Requêtes EQS & Attack Tokens
- **Requête EQS Couverture / Flanquement** : `[Générateur, espacement cm, tests]`
- **Gestion des Attack Tokens (`GD-05`)** : `[Règle d'acquisition et de relâchement]`
""",
        example_filename="sample-npc-ai-spec.md",
        example_content="""# Exemple `AI-01` — Architecture IA des Gardes Portuaires (`ORG-CARTEL-FLEUVE`)

- **ID Profil IA** : `AI-PRF-PORT-GUARD`
- **Archétypes Associés (`GD-05`)** : `ENM-PORT-VIGILE` (1 jeton), `ENM-CARTEL-BRUTE` (2 jetons)
- **Plafond Acteurs Simultanés** : `16 gardes` dans `LOC-GOMBE-PORT`
- **Budget CPU Alloué** : `1.65 ms` mesuré (`<= 2.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Hiérarchie UE5 State Tree
| État State Tree | Condition d'Entrée | Tâches & Smart Objects | Bark Associé (`NAR-04`) |
| :--- | :--- | :--- | :--- |
| `ST_Dock_Duty` | Alerte = 0 | Inspecte les caisses `KIT-CARGO-CRATE-100`, s'abrite sous le hangar si `World.Weather.TropicalStorm`. | `BRK-PORT-01` |
| `ST_Verify_Pass` | Voit Koffi avec `State.Character.Stealth.Disguised` à `< 500 cm` | Interpelle le joueur pendant `3.0 s` sans dégainer. | `BRK-PORT-01` |
| `ST_Combat_Engage` | Tag `State.Character.Combat.Engaged` | Demande un Attack Token ; si accordé, engage au corps-à-corps ; sinon encercle à `450 cm`. | `BRK-PORT-02` |

## 2. Configuration des Requêtes EQS & Attack Tokens
- **Requête EQS (`EQS_FindPortCover`)** : Grille `1600 cm × 1600 cm`, pas de `150 cm`, filtre par distance d'abord puis test de ligne de vue vers `CHR-PROTAG-KOFFI` sur les conteneurs (`240 cm`) et caisses (`100 cm`).
- **Gestion des Attack Tokens (`GD-05`)** : Jeton relâché immédiatement dès l'entrée en phase `Recovery` de l'attaque ou sur parade réussie (`State.Character.Combat.Parrying`).
""",
    ),
    SkillBlueprint(
        skill_id="AI-02",
        description=(
            "Simulation de foules urbaines denses (marchés de Kinshasa, Rond-Point Victoire, boulevards) "
            "sous UE5 Mass Entity / Mass Crowd et ZoneGraph. Gère 500 à 800+ citoyens simultanés dans un "
            "budget CPU <= 2.0 ms avec évitement RVO et hydratation dynamique sans hitch en acteurs complets."
        ),
        inputs=("open-world-density-wld-04", "modular-npc-kits-art-03", "cpu-budgets-dir-04"),
        outputs=("mass-crowd-architecture.md", "district-crowd-density.csv"),
        activation_triggers=(
            "Configuration de la densité piétonne d'une commune (`DST-MATONGE`, `DST-GOMBE`, `DST-KALAMU`, `DST-LIMETE`) selon l'heure et la météo.",
            "Conception des Fragments et Processors ECS (`UMassProcessor`) et des règles d'hydratation (`MassRepresentation` -> `ACharacter` `AI-01`).",
            "Vérification du budget CPU `PERF-CPU-MASS` (`<= 2.0 ms` à 60 FPS) via `scripts/check_mass_budget.py`.",
        ),
        scope_boundaries=(
            "Ne sculpte pas les vêtements modulaires 3D des passants (`ART-03`) et ne gère pas la logique de combat individuel (`AI-01`).",
            "Interdit toute instanciation de `UCharacterMovementComponent` sur les entités Mass de niveau LOD 1 et LOD 2 (usage exclusif de `ZoneGraph` + Vertex Animation Textures).",
        ),
        operational_procedures=(
            "Définir l'archétype ECS `MassCrowd` avec ses Fragments minimaux (`FTransformFragment`, `FMassZoneGraphLaneLocationFragment`, `FMassLookAtFragment`, `FZaireDistrictCultureFragment`).",
            "Configurer les **3 Anneaux de Représentation LOD** : Anneau 0 (`0 - 25 m` : jusqu'à 18 acteurs hydratés interactifs), Anneau 1 (`25 - 80 m` : Skeletal Mesh simplifié avec URO), Anneau 2 (`80 - 250 m` : Instanced Static Mesh animé par VAT).",
            "Programmer la réaction collective aux événements systémiques (`World.Weather.TropicalStorm` -> repli sous les auvents de `DST-MATONGE` ; combat ou coup de feu -> onde de panique directionnelle).",
            "Valider l'enveloppe CPU en exécutant `scripts/check_mass_budget.py`.",
        ),
        decision_rules=(
            ("Budget CPU Mass estimé > 2.0 ms par check_mass_budget.py", "Réduire le rayon d'hydratation de l'Anneau 0 de 25m à 18m et basculer 30 % des entités LOD1 vers la représentation VAT Instanced Static Mesh (LOD2)", "Maintenir le frametime global sous 16.6 ms"),
            ("Averse équatoriale déclenchée (World.Weather.TropicalStorm)", "Basculer la vitesse de déplacement des piétons sur ZoneGraph à 1.6x vers les tags d'abris (auvents de 180 cm de WLD-03) et réduire la densité de spawn en plein air de 60 %", "Simuler un comportement urbain kinois crédible"),
            ("Collision entre une moto Wewa du joueur et un piéton Mass LOD1", "Hydrater instantanément l'entité touchée en acteur physique Chaos ragdoll/esquive et déclencher le bark BRK-CROWD-01", "Assurer une continuité physique sans pop visuel"),
        ),
        acceptance_criteria=(
            "`python skills/04-ai-simulation/ai-02-crowd-simulation-specialist/scripts/check_mass_budget.py` retourne un code `0` (`within_budget: true`).",
            "500+ entités sont simulées simultanément à `DST-MATONGE` pour un coût CPU `<= 2.0 ms`.",
            "L'hydratation/déshydratation entre `MassEntity` et `ACharacter` utilise un pool pré-alloué garantissant 0 hitch d'allocation mémoire.",
        ),
        validation_auditors=("ENG-07", "PRD-05", "DIR-04"),
        reference_filename="ue5-mass-crowd-ecs.md",
        reference_content="""# Architecture ECS UE5 Mass Crowd — Marchés de Kinshasa (`AI-02`)

## 1. Anneaux de Level of Detail (MassRepresentation)
| Anneau LOD | Distance Caméra | Représentation Visuelle (`ART-03`/`ART-05`) | Physique & Navigation | Coût CPU Unitaire |
| :--- | :--- | :--- | :--- | :--- |
| **LOD 0 (Hydraté)** | `0 à 25 m` | `ACharacter` complet + Barks `NAR-04` | Capsule Chaos + Smart Objects | `~0.095 ms` (Pool max 18-24) |
| **LOD 1 (Médian)** | `25 à 80 m` | `USkeletalMeshComponent` partagé (URO 30Hz) | `ZoneGraph` + Évitement RVO | `~0.0045 ms` |
| **LOD 2 (Lointain)** | `80 à 250 m` | `UInstancedStaticMesh` + Vertex Anim Texture (VAT) | `ZoneGraph` cinématique pur | `~0.0018 ms` |
| **LOD 3 (Offscreen)** | `> 250 m` | Culled (0 draw call) | Progression statistique basse fréq. | `< 0.0003 ms` |
""",
        template_filename="mass-crowd-spec.md",
        template_content="""# Spécification Simulation de Foule Mass Entity (`AI-02`)

- **Système** : `SYS-CROWD-MASS`
- **Commune Cible** : `DST-...`
- **Budget CPU Max (`PERF-CPU-MASS`)** : `<= 2.0 ms` (60 FPS)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Distribution par Anneau LOD & Validation Budget
- **Acteurs Hydratés (LOD 0, `< 25 m`)** : `[<= 18]`
- **Entités Mass LOD 1 (`25 - 80 m`)** : `[XXX]`
- **Entités Mass LOD 2 VAT (`80 - 250 m`)** : `[XXX]`
- **Coût CPU Estimé (`check_mass_budget.py`)** : `[X.XX ms]`

## 2. Courbes de Densité Horaire & Réactivité Météo
| Créneau Horaire / Événement | Densité Active (%) | Profils PNJ Dominants (`ART-03`) | Comportement ZoneGraph |
| :--- | :--- | :--- | :--- |
| `Journée (08h-18h)` | `100 %` | `[Profils]` | `[Comportement]` |
""",
        example_filename="sample-mass-crowd-spec.md",
        example_content="""# Exemple `AI-02` — Simulation de Foule de `DST-MATONGE` (`LOC-MATONGE-VICTOIRE`)

- **Système** : `SYS-CROWD-MASS`
- **Commune Cible** : `DST-MATONGE`
- **Budget CPU Max (`PERF-CPU-MASS`)** : `<= 2.0 ms` (60 FPS)
- **Statut** : `CONFIRMED`

## 1. Distribution par Anneau LOD & Validation Budget
- **Acteurs Hydratés (LOD 0, `< 25 m`)** : `18 acteurs` (commerçants, passants proches, ambianceurs).
- **Entités Mass LOD 1 (`25 - 80 m`)** : `180 entités` sur les trottoirs de `500 cm` du Rond-Point Victoire.
- **Entités Mass LOD 2 VAT (`80 - 250 m`)** : `420 entités` sur les avenues radiales.
- **Coût CPU Estimé (`check_mass_budget.py`)** : **`1.566 ms`** (600 entités Mass + 18 acteurs hydratés -> **CONFORME `< 2.0 ms`**).

## 2. Courbes de Densité Horaire & Réactivité Météo
| Créneau Horaire / Événement | Densité Active (%) | Profils PNJ Dominants (`ART-03`) | Comportement ZoneGraph |
| :--- | :--- | :--- | :--- |
| `Marché Matinal (07h-12h)` | `90 % (540 PNJ)` | Commerçants, livreurs, étudiants | Flux continu le long des étals et arrêts bus `ORG-TRANSCO`. |
| `Soirée Musicale (18h-23h)` | `100 % (600 PNJ)` | Citoyens, Sapeurs, clients de ngandas | Regroupement en grappes statiques autour des terrasses diffusant `ORG-RADIO-KIN`. |
| `Averse (World.Weather.TropicalStorm)` | `40 % en rue / 60 % sous auvents` | Tous profils | Migration rapide (`1.6x`) vers les galeries couvertes (`180 cm` de porte-à-faux). |
""",
        scripts={"check_mass_budget.py": CHECK_MASS_BUDGET_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="AI-03",
        description=(
            "Simulation du trafic routier et fluvial de Kinshasa (SYS-TRAFFIC-ZONE) sous UE5 ZoneGraph "
            "et Mass Traffic. Gère les priorités aux grands ronds-points (Rond-Point Victoire, Échangeur), "
            "le slalom inter-file des motos Wewa (VEH-MOTO-WEWA-01), les arrêts des taxis jaunes et "
            "l'algorithme anti-deadlock."
        ),
        inputs=("urban-road-specs-wld-03", "vehicle-profiles-gd-06", "houdini-zonegraph-splines-eng-04"),
        outputs=("traffic-rules-specification.md", "intersection-priority-matrix.csv"),
        activation_triggers=(
            "Configuration des règles de circulation `MassTraffic` sur les voies `ZoneGraph` générées par Houdini (`ENG-04`).",
            "Modélisation des comportements typiques du trafic kinois (slalom des motos Wewa dans les espaces `>= 130 cm`, arrêts opportuns des taxis `VEH-TAXI-JAUNE-01`, inertie des bus `VEH-BUS-TRANSCO-01`).",
            "Prévention et résolution automatique des embouteillages bloquants (deadlocks) aux intersections complexes.",
        ),
        scope_boundaries=(
            "Ne règle pas les courbes de couple ou de suspension du véhicule contrôlé par le joueur (`GD-06`/`ENG-05`).",
            "N'active jamais la simulation physique complète Chaos sur les véhicules IA situés à plus de `45 mètres` du joueur (suivi cinématique léger sur spline `ZoneGraph`).",
        ),
        operational_procedures=(
            "Tagger chaque voie `ZoneGraph` avec ses types de véhicules autorisés (`Vehicle.Type.MotoWewa`, `Vehicle.Type.HeavyBus`, `StandardCar`) et sa vitesse cible en fonction de `WLD-03`.",
            "Implémenter la règle de **Sub-Lane Splitting (Slalom Wewa)** : lorsqu'une file de voitures roule à `< 20 km/h` et que l'écart inter-file est `>= 130 cm`, autoriser les entités `VEH-MOTO-WEWA-01` à emprunter la sous-voie virtuelle inter-file à `30-40 km/h`.",
            "Configurer le **Watchdog Anti-Deadlock aux Carrefours** : si une intersection a une vitesse moyenne `< 2 km/h` pendant plus de `8 secondes`, forcer la libération prioritaire de l'anneau intérieur du rond-point etrecycler hors-champ (`> 120 m` hors frustum caméra) les véhicules bloquants.",
            "Documenter les règles dans `templates/traffic-rules-spec.md`.",
        ),
        decision_rules=(
            ("Collision ou proximité immédiate (< 15 m) entre le joueur et un véhicule MassTraffic", "Promouvoir instantanément l'entité MassTraffic de sa spline cinématique vers un acteur Chaos Vehicle physique complet (ENG-05)", "Garantir des réactions de choc et d'évitement réalistes"),
            ("Saturation d'un rond-point (ex: LOC-MATONGE-VICTOIRE) menaçant de bloquer une mission de course Wewa", "Déclencher le protocole Anti-Deadlock après 8s d'immobilisation et maintenir en permanence un couloir inter-file de 150 cm franchissable à moto", "Éviter tout soft-lock routier sur MSN-SIDE-014-WEWA"),
            ("Dépassement du budget CPU combiné Mass Crowd + Mass Traffic (> 2.0 ms)", "Réduire le plafond de véhicules simulés de 120 à 85 en privilégiant la densité dans le cône de vision avant du joueur", "Respecter PERF-CPU-MASS"),
        ),
        acceptance_criteria=(
            "Le trafic soutient un test d'endurance de 2 heures (`PRD-05`) sur `LOC-MATONGE-VICTOIRE` et `LOC-GOMBE-BD30JUIN` avec 0 deadlock permanent.",
            "Les motos IA `VEH-MOTO-WEWA-01` utilisent les couloirs inter-files `>= 130 cm` sans collision fantôme.",
            "Aucune apparition ou disparition (pop-in/out) de véhicule n'est visible dans le frustum caméra du joueur.",
        ),
        validation_auditors=("PRD-05", "ENG-07", "GD-06"),
        reference_filename="zonegraph-kinshasa-traffic.md",
        reference_content="""# Simulation de Trafic Urbain sous UE5 ZoneGraph & MassTraffic (`AI-03`)

## 1. Comportements Spécifiques Kinois Modélisés
1. **Slalom Inter-File (`VEH-MOTO-WEWA-01`)** : Sous-voies virtuelles générées entre les voies principales de `350-400 cm`, offrant un couloir libre de `130-150 cm`.
2. **Arrêts Collectifs (`VEH-TAXI-JAUNE-01`)** : Déboîtement sur la bande d'arrêt latérale (`220 cm`) près des marchés pendant `6 à 12 secondes` pour déposer des passants `AI-02`.
3. **Priorité Anneau Circulaire (`LOC-MATONGE-VICTOIRE`)** : Priorité accordée aux véhicules engagés sur l'anneau intérieur pour évacuer le carrefour, avec cessions de passage dynamiques aux bus `VEH-BUS-TRANSCO-01`.
""",
        template_filename="traffic-rules-spec.md",
        template_content="""# Spécification Trafic ZoneGraph & Anti-Deadlock (`AI-03`)

- **Système** : `SYS-TRAFFIC-ZONE`
- **Axe / Carrefour** : `LOC-...` (`DST-...`)
- **Plafond Véhicules Actifs** : `[XX véhicules MassTraffic]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Répartition de la Flotte & Règles de Voies
| ID Véhicule | Proportion (%) | Voies Autorisées | Comportement Spécifique ZoneGraph |
| :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `[XX %]` | `[Principales + Inter-file >= 130cm]` | `[Règle]` |

## 2. Algorithme de Résolution d'Interblocage (Deadlock Watchdog)
- **Seuil de détection immobilisation** : `[X secondes à < Y km/h]`
- **Action de déblocage prioritaire** : `[Protocole]`
- **Rayon de bascule Cinématique -> Chaos Physics (`ENG-05`)** : `[XX mètres]`
""",
        example_filename="sample-traffic-spec.md",
        example_content="""# Exemple `AI-03` — Trafic du Rond-Point Victoire (`LOC-MATONGE-VICTOIRE`)

- **Système** : `SYS-TRAFFIC-ZONE`
- **Axe / Carrefour** : `LOC-MATONGE-VICTOIRE` (`DST-MATONGE`)
- **Plafond Véhicules Actifs** : `75 véhicules MassTraffic` (coût CPU inclus dans l'enveloppe `PERF-CPU-MASS <= 2.0 ms`)
- **Statut** : `CONFIRMED`

## 1. Répartition de la Flotte & Règles de Voies
| ID Véhicule | Proportion (%) | Voies Autorisées | Comportement Spécifique ZoneGraph |
| :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `45 %` | Toutes voies + sous-voies inter-files (`150 cm`) | Slalom actif dès que le flux principal descend sous `20 km/h`. |
| `VEH-TAXI-JAUNE-01` | `40 %` | Voies moyennes et extérieures (`380 cm`) | Arrêts de `8 s` sur les encoches de dépose-minute devant les galeries. |
| `VEH-BUS-TRANSCO-01` | `15 %` | Voie centrale prioritaire (`380-400 cm`) | Allure régulière, priorité forcée à l'insertion dans le rond-point. |

## 2. Algorithme de Résolution d'Interblocage (Deadlock Watchdog)
- **Seuil de détection immobilisation** : `8.0 secondes` avec vitesse moyenne du noeud d'intersection `< 2.0 km/h`.
- **Action de déblocage prioritaire** : Gel temporaire (`4.0 s`) des feux/entrées radiales, dégagement forcé de l'anneau intérieur et recyclage discret des véhicules bloqués hors du cône de caméra à `> 110 m`.
- **Rayon de bascule Cinématique -> Chaos Physics (`ENG-05`)** : `35 mètres` autour de Koffi (ou instantané en cas d'impact projectile/véhicule).
""",
    ),
    SkillBlueprint(
        skill_id="AI-04",
        description=(
            "Conception des systèmes de décision de haut niveau (Utility AI), des routines quotidiennes "
            "des habitants de Kinshasa et du générateur d'événements systémiques émergents (micro-scènes "
            "de rue, pannes mécaniques, contrôles du Syndicat, musiciens de rue) réagissant à la "
            "réputation du joueur (SYS-WLD-REPUTATION), à l'heure et à la météo."
        ),
        inputs=("world-bible-wld-01", "reputation-system-gd-01", "barks-catalog-nar-04"),
        outputs=("utility-ai-decision-matrix.csv", "systemic-events-catalog.md"),
        activation_triggers=(
            "Conception des micro-événements non scriptés qui animent Kinshasa entre deux points d'intérêt (règle des 40 secondes `WLD-04`).",
            "Modélisation des courbes d'utilité (Utility AI) gouvernant le choix d'activité des citoyens selon le cycle jour/nuit, la pluie (`World.Weather.TropicalStorm`) et la réputation de Koffi.",
            "Rattachement des événements émergents aux banques de barks (`NAR-04`) et aux gains de réputation (`GD-04`).",
        ),
        scope_boundaries=(
            "Ne programme pas les arbres de recherche de chemin bas niveau (`AI-01`) ni les processeurs vectorisés C++ (`AI-02`).",
            "Interdit de déclencher un événement systémique à moins de `80 mètres` d'une mission principale active (`MSN-MAIN-*`) pour ne pas parasiter la mise en scène de `GD-02`/`NAR-02`.",
        ),
        operational_procedures=(
            r"Calculer le score d'utilité $U \in [0.0, 1.0]$ de chaque événement candidat à partir de 4 variables normalisées : (1) Tag de Commune (`World.District.*`), (2) Heure du jour, (3) Météo (`World.Weather.*`), (4) Niveau de Réputation (`SYS-WLD-REPUTATION`).",
            "Imposer un **Temps de Recharge (Cooldown)** de `15 minutes` réelles par catégorie de micro-événement pour éliminer toute sensation de répétition mécanique.",
            "Limiter l'empreinte technique de chaque événement systémique à **`<= 4 acteurs AI-01` hydratés** maximum.",
            "Documenter le catalogue et les formules de pondération dans `templates/systemic-events-catalog.md`.",
        ),
        decision_rules=(
            ("Mission principale MSN-MAIN-* en cours d'exécution à proximité (< 80 m)", "Forcer le multiplicateur d'utilité des événements systémiques aléatoires à 0.0 dans un rayon de 80 m autour de l'objectif de quête", "Éviter toute interférence avec le script de mission GD-02"),
            ("Même événement systémique tiré deux fois dans le même quartier en moins de 15 minutes", "Appliquer une pénalité de fraîcheur (Decay Factor = 0.05) sur le score d'utilité de cet événement", "Garantir la variété de l'exploration open world"),
            ("Réputation de Koffi au palier 'Enfant du Quartier' (>= 600 points) dans la commune", "Activer les événements d'entraide citoyenne (avertissement de patrouille, diversion spontanée de foule, prêt de Wewa)", "Récompenser concrètement l'investissement social du joueur"),
        ),
        acceptance_criteria=(
            "Chaque événement du catalogue spécifie sa formule de score Utility AI, son cooldown, ses tags requis et son plafond d'acteurs (`<= 4`).",
            "Exclusion mutuelle garantie avec les arènes de missions principales actives.",
            "Tous les dialogues courts de l'événement proviennent des tables de barks validées par `NAR-04`.",
        ),
        validation_auditors=("DIR-05", "NAR-06", "WLD-04"),
        reference_filename="utility-ai-and-systemic-world.md",
        reference_content=r"""# Modèle Utility AI & Événements Systémiques Urbains (`AI-04`)

## 1. Équation de Sélection d'Événement Systémique
Le directeur systémique évalue toutes les 10 secondes les ancres disponibles (`SmartObject` de trottoir à `40 - 90 m` en avant du joueur) selon :
$$U(E) = W_{\text{district}} \cdot W_{\text{time}} \cdot W_{\text{weather}} \cdot W_{\text{cooldown}}$$
L'événement ayant le score $U(E) > 0.65$ le plus élevé est instancié en hydratant 2 à 4 entités `AI-02` vers `AI-01`.
""",
        template_filename="systemic-events-catalog.md",
        template_content="""# Catalogue d'Événements Systémiques & Utility AI (`AI-04`)

- **Commune Cible** : `DST-...`
- **Rayon d'Exclusion Mission Principale** : `80 mètres`
- **Plafond Acteurs Hydratés par Événement** : `<= 4 acteurs AI-01`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Table de Pondération Utility AI
| ID Événement | Commune (`World.District.*`) | Fenêtre Horaire | Météo Compatible | Cooldown (min) | Acteurs Hydratés |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EVT-SYS-...` | `World.District...` | `[HH:MM-HH:MM]` | `[Sec / Pluie]` | `15 min` | `[2-4]` |

## 2. Déroulé Systémique & Récompense Émergente
- **Mise en situation** : `[Description]`
- **Interaction Joueur Optionnelle** : `[Action possible]`
- **Impact `SYS-WLD-REPUTATION` / Économie (`GD-03`)** : `[Gain]`
""",
        example_filename="sample-systemic-events.md",
        example_content="""# Exemple `AI-04` — Événements Systémiques de `DST-MATONGE` & `DST-KALAMU`

- **Commune Cible** : `DST-MATONGE` & `DST-KALAMU`
- **Rayon d'Exclusion Mission Principale** : `80 mètres`
- **Plafond Acteurs Hydratés par Événement** : `<= 4 acteurs AI-01`
- **Statut** : `CONFIRMED`

## 1. Table de Pondération Utility AI
| ID Événement | Commune | Fenêtre Horaire | Météo Compatible | Cooldown (min) | Acteurs Hydratés |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EVT-SYS-WEWA-BREAKDOWN` | `World.District.Kalamu` | `06h00 - 20h00` | Sec uniquement | `15 min` | `2` (Chauffeur Wewa + Passager) |
| `EVT-SYS-CARTEL-SHAKEDOWN` | `World.District.Matonge` | `18h00 - 02h00` | Toutes météos | `20 min` | `3` (2 Vigiles `ORG-CARTEL-FLEUVE` + 1 Commerçant) |
| `EVT-SYS-RADIO-CROWD` | `World.District.Matonge` | `17h00 - 23h00` | Sec uniquement | `15 min` | `4` (Auditeurs + Vendeur autour d'un poste `ORG-RADIO-KIN`) |

## 2. Déroulé Systémique & Récompense Émergente (`EVT-SYS-CARTEL-SHAKEDOWN`)
- **Mise en situation** : Deux collecteurs de `ORG-CARTEL-FLEUVE` tentent de saisir la recette du soir d'un disquaire près de `LOC-MATONGE-VICTOIRE`.
- **Interaction Joueur Optionnelle** : Koffi peut intervenir par intimidation sociale (si réputation Matonge `>= 250`), payer la dette (`1 500 FC`) ou repousser les vigiles en mêlée (`SYS-CMB-MELEE`).
- **Impact `SYS-WLD-REPUTATION` / Économie (`GD-03`)** : `+40 points` de réputation à `DST-MATONGE` et déblocage d'un indice oral sur les rondes portuaires de `LOC-GOMBE-PORT`.
""",
    ),
)


def build_department_04(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 4 skills du département 04-ai-simulation."""
    created: list[Path] = []
    for bp in AI_SIMULATION_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_04(WORKSPACE_ROOT)
    print(f"[OK] Département 04-ai-simulation généré ({len(paths)} skills).")
