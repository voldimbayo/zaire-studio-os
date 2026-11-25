"""Spécifications et génération du Département 03-GAME-DESIGN (GD-01 à GD-07)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

SIMULATE_ECONOMY_SCRIPT = '''"""Simulateur d'équilibrage Sources & Puits (Faucets & Sinks) pour GD-03 (Economy Designer)."""

from __future__ import annotations

import argparse
import json
import sys


def simulate_player_economy(hours: int = 40) -> dict:
    """Simule l'évolution des revenus, dépenses et inflation sur N heures de jeu dans ZAÏRE."""
    balance = 5000  # Fonds de départ en Francs Congolais (FC) / Crédits locaux
    history: list[dict] = []

    for h in range(1, hours + 1):
        # Faucets : Missions principales, livraisons Wewa, contrats de quartier
        faucet = int(12000 + (h * 2500))
        # Sinks : Maintenance moto Wewa, carburant, équipement, informateurs, améliorations atelier
        sink = int(9500 + (h * 2150))
        balance += faucet - sink
        sink_ratio = round(sink / faucet, 3)
        history.append(
            {
                "hour": h,
                "faucet": faucet,
                "sink": sink,
                "sink_to_faucet_ratio": sink_ratio,
                "net_balance": balance,
            }
        )

    avg_ratio = round(sum(x["sink_to_faucet_ratio"] for x in history) / len(history), 3)
    healthy = 0.75 <= avg_ratio <= 0.92 and all(x["net_balance"] > 0 for x in history)
    return {
        "simulated_hours": hours,
        "average_sink_to_faucet_ratio": avg_ratio,
        "final_net_balance": balance,
        "economy_healthy": healthy,
        "checkpoints": [history[0], history[hours // 2 - 1], history[-1]],
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Simule l'économie Sources/Puits sur 40h (GD-03).")
    parser.add_argument("--hours", type=int, default=40, help="Durée de la campagne simulée en heures")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de paramètres économiques à valider (optionnel)")
    parser.add_argument("--output", help="Chemin de sauvegarde du rapport JSON (optionnel)")
    args = parser.parse_args()
    hours = args.hours
    if args.file:
        from pathlib import Path
        cfg = json.loads(Path(args.file).read_text(encoding="utf-8"))
        hours = int(cfg.get("simulated_hours", hours))
    report = simulate_player_economy(hours)
    formatted = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        from pathlib import Path
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(formatted + "\\n", encoding="utf-8")
    print(formatted)
    return 0 if report["economy_healthy"] else 1


if __name__ == "__main__":
    sys.exit(main())
'''

GAME_DESIGN_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="GD-01",
        description=(
            "Conception des boucles de gameplay fondamentales (Core Loops) et des systèmes transversaux "
            "(SYS-* : infiltration urbaine/sociale, réputation par commune, interactions systémiques) "
            "mappés sur l'architecture UE5 Gameplay Ability System (GAS) et les Gameplay Tags."
        ),
        inputs=("creative-pillars-dir-03", "lead-gd-directives-dir-05", "open-world-structure-wld-04"),
        outputs=("system-design-document.md", "gameplay-tags-mapping.csv"),
        activation_triggers=(
            "Création ou mise à jour d'un système de jeu transversal (`SYS-STEALTH`, `SYS-WLD-REPUTATION`, inventaire, interactions PNJ).",
            "Définition des contrats d'interaction émergente entre deux systèmes via `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.",
            "Cadrage fonctionnel d'une mécanique avant son implémentation C++ GAS par `ENG-02`.",
        ),
        scope_boundaries=(
            "Ne conçoit pas le déroulé spécifique d'une mission (`GD-02`) ni le code C++ des `UGameplayAbility` (`ENG-02`).",
            "N'introduit aucun état booléen isolé hors de la taxonomie des `FGameplayTag`.",
        ),
        operational_procedures=(
            "Enregistrer le système sous un identifiant `SYS-[DOMAINE]-[SLUG]` dans `knowledge/entities-registry.csv`.",
            "Décomposer le système en Entrées Joueur (Enhanced Input), États (`FGameplayTag`), Attributs (`UAttributeSet`) et Effets (`UGameplayEffect`).",
            "Définir la matrice d'interactions émergentes avec la météo (`World.Weather.TropicalStorm`), la foule (`AI-02`) et la réputation de quartier (`World.District.*`).",
            "Rédiger la spécification complète suivant `templates/system-design-doc-template.md`.",
        ),
        decision_rules=(
            ("Deux systèmes doivent communiquer (ex: météo pluie -> bruit de pas infiltration)", "Interdire le couplage direct entre classes et passer exclusivement par un Gameplay Tag partagé (World.Weather.TropicalStorm)", "Maintenir la modularité GAS validée avec ENG-02"),
            ("Mécanique complexe nécessitant plus de 3 minutes de tutoriel texte", "Simplifier la règle d'activation contextuelle à un seul input et enseigner par l'affordance spatiale en jeu (WLD-05)", "Appliquer le standard d'onboarding DIR-05"),
            ("Système impactant le budget CPU par un polling frame-by-frame", "Remplacer le polling par des callbacks événementiels sur changement de Gameplay Tag", "Respecter l'enveloppe Game Thread <= 6.5 ms"),
        ),
        acceptance_criteria=(
            "100 % des états et déclencheurs du système sont mappés sur des Gameplay Tags enregistrés.",
            "Le document définit clairement les règles d'activation, d'annulation (Cancel Tags) et de blocage (Block Tags) sous UE5 GAS.",
            "Les cas limites (interruption par combat, entrée dans un véhicule, transition de quartier) sont couverts.",
        ),
        validation_auditors=("DIR-05", "ENG-02"),
        reference_filename="gas-systemic-design.md",
        reference_content="""# Conception Systémique Orientée UE5 GAS (`GD-01`)

## 1. Mapping Standard vers Gameplay Ability System
- **Activation Owned Tags** : Tags octroyés à l'acteur pendant que le système est actif (ex: `State.Character.Stealth.Disguised`).
- **Activation Blocked Tags** : Tags interdisant l'activation (ex: `State.Character.Combat.Engaged` bloque immédiatement l'accréditation sociale `ITM-DOC-PASSEPORT`).
- **Émergence Systémique** : L'averse équatoriale (`World.Weather.TropicalStorm`) atténue de `-40 %` le rayon de perception auditive des gardes (`AI-01`) tout en dispersant la foule civile (`AI-02`).
""",
        template_filename="system-design-doc-template.md",
        template_content="""# Spécification de Système de Gameplay (`GD-01`)

- **ID Système** : `SYS-[DOMAINE]-[SLUG]`
- **Nom du Système** : `[Nom]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Boucle Fonctionnelle & Règles Métier
- **Objectif Joueur** : `[Intention]`
- **Règles de Fonctionnement** : `[Mécanique déterministe]`

## 2. Architecture UE5 GAS & Gameplay Tags (`ENG-02`)
| Tag / Attribut | Rôle GAS (`Owned` / `Required` / `Blocked`) | Effet Systémique |
| :--- | :--- | :--- |
| `State.Character...` | `Owned` | `[Effet]` |

## 3. Matrice d'Interactions Émergentes
- **Interaction avec Météo (`ART-07`)** : `[Impact]`
- **Interaction avec IA / Foule (`AI-01`/`AI-02`)** : `[Impact]`
""",
        example_filename="sample-system-design.md",
        example_content="""# Exemple `GD-01` — Spécification de `SYS-STEALTH` (Infiltration Urbaine & Sociale)

- **ID Système** : `SYS-STEALTH`
- **Nom du Système** : Infiltration Urbaine & Sociale
- **Statut** : `CONFIRMED`

## 1. Boucle Fonctionnelle & Règles Métier
- **Objectif Joueur** : Traverser ou saboter les zones contrôlées par `ORG-CARTEL-FLEUVE` (comme `LOC-GOMBE-PORT`) sans déclencher d'alarme générale.
- **Règles de Fonctionnement** : Combine 3 vecteurs : (1) Dissimulation géométrique derrière couverts (`100 cm`/`200 cm`), (2) Dissimulation sociale par document ou tenue (`ITM-DOC-PASSEPORT`), (3) Masquage acoustique par l'environnement kinois (pluie tropicale, groupes électrogènes, passage de barges).

## 2. Architecture UE5 GAS & Gameplay Tags (`ENG-02`)
| Tag / Attribut | Rôle GAS | Effet Systémique |
| :--- | :--- | :--- |
| `State.Character.Stealth.Concealed` | `Owned` (en couvert/ombre) | Réduit le multiplicateur de détection visuelle `AI-01` à `0.25x`. |
| `State.Character.Stealth.Disguised` | `Owned` (avec `ITM-DOC-PASSEPORT`) | Autorise la marche normale devant les vigiles à distance `> 400 cm`. |
| `State.Character.Combat.Engaged` | `Blocked` / `Cancel` | Annule immédiatement l'état furtif et active l'alerte d'escouade. |

## 3. Matrice d'Interactions Émergentes
- **Interaction avec Météo (`World.Weather.TropicalStorm`)** : Le bruit de la pluie sur les toits en tôle masque les bruits de course et d'élimination silencieuse.
- **Interaction avec Foule (`SYS-CROWD-MASS`)** : Se fondre dans un groupe d'au moins 6 dockers ou passants octroie un camouflage social temporaire.
""",
    ),
    SkillBlueprint(
        skill_id="GD-02",
        description=(
            "Conception ludique détaillée des missions principales et secondaires (MSN-*). Définit "
            "les objectifs, les approches tactiques multiples (infiltration/social/combat/véhicule), "
            "les checkpoints atomiques et les machines à états garantissant zéro soft-lock."
        ),
        inputs=("narrative-architecture-nar-01", "poi-specs-wld-04", "game-systems-gd-01"),
        outputs=("mission-design-document.md", "quest-state-machine.json"),
        activation_triggers=(
            "Création ou révision d'une mission principale (`MSN-MAIN-*`) ou secondaire (`MSN-SIDE-*`).",
            "Définition des règles de récupération d'erreur (destruction de véhicule, fuite hors zone, mort d'un PNJ secondaire) pour éviter tout blocage.",
            "Coordination des besoins d'arène avec `WLD-05` (Level Designer) et `NAR-02` (Screenwriter).",
        ),
        scope_boundaries=(
            "N'écrit pas les dialogues littéraires finaux (`NAR-02`/`NAR-04`) et ne sculpte pas les assets 3D (`ART-02`).",
            "Ne livre jamais une mission linéaire dépourvue d'au moins 2 approches sur les objectifs majeurs.",
        ),
        operational_procedures=(
            "Enregistrer la mission sous un ID `MSN-[TYPE]-[NUM]-[SLUG]` dans `knowledge/entities-registry.csv`.",
            "Construire la **Machine à États de Quête (`quest-state-machine.json`)** en prévoyant pour chaque étape : Condition de Succès, Approches Supportées (A/B/C), Gestion d'Interruption (`ON_VEHICLE_DESTROYED`, `ON_PLAYER_FLEE`, `ON_COMBAT_ESCALATION`) et Checkpoint de Restauration.",
            "Spécifier le plafond exact de PNJ `AI-01` actifs simultanément (strictement `<= 24` selon `DIR-04`).",
            "Rédiger le document complet suivant `templates/mission-design-template.md`.",
        ),
        decision_rules=(
            ("Véhicule de mission (ex: VEH-MOTO-WEWA-01) détruit ou coincé pendant une poursuite", "Ne jamais afficher un Game Over brutal s'il existe un repli : faire apparaître une Wewa de secours ou basculer l'objectif en fuite à pied/parkour", "Garantir la règle Zéro Soft-Lock (quality-standards.md)"),
            ("Nombre de gardes demandé > 24 dans l'arène de mission", "Plafonner les gardes AI-01 à 20-24 et compléter l'ambiance par des travailleurs civils AI-02 Mass Crowd", "Respecter le budget CPU AI-01 <= 2.5 ms"),
            ("Joueur quitte le périmètre de la mission en plein dialogue", "Sauvegarder le dernier checkpoint atomique et déclencher le handler ON_INTERRUPT_LEAVE de NAR-04", "Permettre la reprise fluide de la quête ultérieurement"),
        ),
        acceptance_criteria=(
            "Chaque étape de la machine à états possède un handler explicite contre les soft-locks (fuite, destruction véhicule, alerte).",
            "Au moins 2 approches tactiques distinctes sont documentées et reliées aux systèmes `GD-01`/`GD-05`/`GD-06`.",
            "Le nombre maximal de PNJ `AI-01` simultanés est `<= 24`.",
        ),
        validation_auditors=("NAR-06", "AI-01", "PRD-04", "DIR-05"),
        reference_filename="mission-state-machine-rules.md",
        reference_content="""# Architecture de Quêtes Tolérantes aux Interruptions (`GD-02`)

## 1. Protocole Anti-Soft-Lock en Monde Ouvert
Dans un monde ouvert systémique comme Kinshasa, toute étape de mission doit survivre à 4 événements imprévus :
1. `EVENT_VEHICLE_LOST` : Destruction ou perte de `VEH-MOTO-WEWA-01` -> activation d'un point de récupération secondaire ou continuation en parkour.
2. `EVENT_STEALTH_BROKEN` : Échec de l'infiltration `SYS-STEALTH` -> transition dynamique de l'objectif "Infiltrer sans alerte" vers "Arracher les registres sous le feu et s'exfiltrer" (pas d'écran d'échec punitif).
3. `EVENT_AREA_ABANDONED` : Sortie du rayon de `300 m` -> suspension propre de la mission au dernier checkpoint atomique.
4. `EVENT_WEATHER_SHIFT` : Déclenchement de `World.Weather.TropicalStorm` -> adaptation des cônes de détection `AI-01` et de l'adhérence `GD-06`.
""",
        template_filename="mission-design-template.md",
        template_content="""# Mission Design Document (`GD-02`)

- **ID Mission** : `MSN-[MAIN/SIDE]-[NUM]-[SLUG]`
- **Titre** : `[Titre de la Mission]`
- **Lieu & Commune** : `LOC-...` (`DST-...`)
- **Plafond PNJ `AI-01` Actifs** : `[<= 24]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Approches Tactiques Multiples
- **Approche A (Infiltration / Social `SYS-STEALTH`)** : `[Mécanique]`
- **Approche B (Mêlée / Action `SYS-CMB-MELEE`)** : `[Mécanique]`
- **Approche C (Mobilité / Exfiltration `VEH-*`)** : `[Mécanique]`

## 2. Machine à États & Protection Anti-Soft-Lock
| Étape ID | Objectif Joueur | Condition Transition Succès | Handler Anti-Soft-Lock (Véhicule détruit / Fuite / Alerte) |
| :--- | :--- | :--- | :--- |
| `ST-01` | `[Objectif]` | `[Condition]` | `[Action de récupération sans blocage]` |
""",
        example_filename="sample-mission-design.md",
        example_content="""# Exemple `GD-02` — Mission Design de `MSN-MAIN-001-ARRIVEE` (L'Accostage de l'Aube)

- **ID Mission** : `MSN-MAIN-001-ARRIVEE`
- **Titre** : L'Accostage de l'Aube
- **Lieu & Commune** : `LOC-GOMBE-PORT` (`DST-GOMBE`) -> `DST-KALAMU`
- **Plafond PNJ `AI-01` Actifs** : `16 gardes ORG-CARTEL-FLEUVE` (+ 40 dockers `AI-02` Mass Crowd)
- **Statut** : `CONFIRMED`

## 1. Approches Tactiques Multiples
- **Approche A (Social & Furtivité `SYS-STEALTH`)** : Présenter `ITM-DOC-PASSEPORT` au poste sud (`State.Character.Stealth.Disguised`), traverser le hangar N°4 en évitant les chefs d'équipe et récupérer le manifeste de saisie de `FAM-KABONGO`.
- **Approche B (Verticalité & Mêlée `SYS-CMB-MELEE`)** : Escalader la grue ouest (`+400 cm`), neutraliser les 2 guetteurs à la machette (`ITM-WPN-MACHETTE`) et descendre par la verrière du bureau.
- **Approche C (Exfiltration Véhiculaire `VEH-MOTO-WEWA-01`)** : Rejoindre la moto Wewa sur la rampe est et semer les patrouilles sur le Boulevard du 30 Juin (`LOC-GOMBE-BD30JUIN`) jusqu'à Kalamu.

## 2. Machine à États & Protection Anti-Soft-Lock
| Étape ID | Objectif Joueur | Condition Transition Succès | Handler Anti-Soft-Lock |
| :--- | :--- | :--- | :--- |
| `ST-01` | Pénétrer dans le hangar N°4 de `LOC-GOMBE-PORT` | Entrée dans le volume `VOL_Hangar4_Interior` | Si `ITM-DOC-PASSEPORT` est compromis, bascule automatique sur l'objectif d'accès par la grue ouest ou brèche latérale. |
| `ST-02` | Récupérer le registre de saisie `FAM-KABONGO` | Interaction avec le coffre `OBJ_Manifest_Safe` | Si combat engagé (`State.Character.Combat.Engaged`), le coffre reste ouvrable après neutralisation des 3 gardes proches. |
| `ST-03` | S'exfiltrer vers l'atelier de `DST-KALAMU` | Atteindre `DST-KALAMU` hors état d'alerte | Si la `VEH-MOTO-WEWA-01` initiale est détruite, 2 motos coursiers supplémentaires circulent à la sortie du port + possibilité de monter dans un taxi `VEH-TAXI-JAUNE-01`. |
""",
    ),
    SkillBlueprint(
        skill_id="GD-03",
        description=(
            "Modélisation mathématique et équilibrage de l'économie virtuelle de ZAÏRE (Sources & Puits / "
            "Faucets & Sinks). Définit les récompenses de missions, le coût des équipements (ITM-*), la "
            "maintenance des véhicules (VEH-*) et prévient l'hyper-inflation sur 40+ heures de jeu."
        ),
        inputs=("game-systems-gd-01", "missions-list-gd-02", "items-and-vehicles-registry"),
        outputs=("economy-balance-sheet.csv", "faucets-sinks-simulation.json"),
        activation_triggers=(
            "Création ou tarification d'un nouvel objet (`ITM-*`), véhicule (`VEH-*`) ou service urbain (atelier mécanique, informateur, transport).",
            "Calibrage des récompenses monétaires (`LEX-010 Mosolo`) des missions principales et secondaires (`MSN-*`).",
            "Vérification de la stabilité économique long-terme via `scripts/simulate_economy.py`.",
        ),
        scope_boundaries=(
            "Ne conçoit pas les paliers de points d'expérience ou de compétences (`GD-04`) ni les écrans UI de boutique (`GD-07`).",
            "N'autorise aucune source de revenu infinie non plafonnée (exploit farming) sans temps de recharge ou coût d'opportunité.",
        ),
        operational_procedures=(
            "Inventorier toutes les Sources de revenus (**Faucets** : missions `MSN-*`, livraisons Wewa, revente de cargaisons `LEX-012 Bilɔkɔ`) et tous les Puits de dépense (**Sinks** : réparation/customisation `VEH-MOTO-WEWA-01`, équipement `ITM-*`, frais d'informateurs, soutien au réseau citoyen).",
            "Lier les multiplicateurs de prix des commerçants de chaque commune (`DST-*`) au niveau de `SYS-WLD-REPUTATION` (`-15 %` en réputation alliée, `+25 %` en zone tendue).",
            "Exécuter `scripts/simulate_economy.py` pour vérifier que le ratio moyen `Sink / Faucet` reste compris entre **`0.75` et `0.92`** sur 40 heures de jeu.",
            "Exporter la table de prix normalisée dans `templates/economy-balance-sheet.csv`.",
        ),
        decision_rules=(
            ("Ratio Sink / Faucet < 0.75 détecté par simulate_economy.py (excès de liquidités / inflation)", "Augmenter le coût des améliorations de palier 2/3 à l'atelier mécanique ou introduire des puits de prestige (tenues Sapeurs, améliorations radio)", "Maintenir la valeur perçue du Mosolo jusqu'à l'Acte III"),
            ("Ratio Sink / Faucet > 0.92 ou solde négatif sur le chemin critique", "Réduire de 30 % les coûts de réparation obligatoire des véhicules et augmenter la prime des missions principales MSN-MAIN-*", "Garantir zéro blocage financier sur la quête principale"),
            ("Activité secondaire répétable générant plus de revenus/minute qu'une mission principale", "Appliquer un rendement décroissant (diminishing returns) après 3 exécutions dans la même journée in-game", "Protéger le rythme de progression GD-04"),
        ),
        acceptance_criteria=(
            "`python skills/03-game-design/gd-03-economy-designer/scripts/simulate_economy.py` retourne un code `0` (`economy_healthy: true`).",
            "Aucun achat obligatoire de la quête principale ne bloque la progression du joueur.",
            "100 % des items tarifés utilisent des identifiants `ITM-*` ou `VEH-*` valides.",
        ),
        validation_auditors=("DIR-05", "GD-04"),
        reference_filename="faucets-and-sinks-math.md",
        reference_content=r"""# Modèle Mathématique Sources & Puits (`GD-03`)

## 1. Équation d'Équilibre Monétaire (`Mosolo`)
Pour chaque heure de jeu $t \in [1, 40]$, le flux net $\Delta M(t) = F(t) - S(t)$ doit vérifier :
$$0.75 \le \frac{S(t)}{F(t)} \le 0.92$$
- **Faucets $F(t)$** : $12\,000 + 2\,500 \cdot t$ (Missions principales, courses urgentes `MSN-SIDE-014-WEWA`, contrats d'atelier).
- **Sinks $S(t)$** : $9\,500 + 2\,150 \cdot t$ (Pièces moteur Wewa, outils d'infiltration, corruption/accréditations portuaires, équipement de mêlée).
""",
        template_filename="economy-balance-sheet.csv",
        template_content="""item_or_mission_id,entity_type,flow_direction,base_value_fc,reputation_modifier_min,reputation_modifier_max,act_unlock,notes
MSN-MAIN-001-ARRIVEE,MISSION,FAUCET,15000,1.0,1.0,ACT_1,Prime de récupération du manifeste portuaire
ITM-WPN-MACHETTE,ITEM,SINK,8500,0.85,1.25,ACT_1,Achat ou renforcement à l'atelier de Kalamu
VEH-MOTO-WEWA-01,VEHICLE,SINK,4500,0.85,1.15,ACT_1,Révision complète suspension et pneus pluie
""",
        example_filename="sample-economy-model.md",
        example_content="""# Exemple `GD-03` — Modèle Économique de l'Acte I & Simulation 40h

## 1. Résultat de `scripts/simulate_economy.py`
- **Durée simulée** : `40 heures`
- **Ratio Moyen `Sink / Faucet`** : `0.844` (Cible `[0.75, 0.92]` -> **CONFORME**)
- **Solde Net Final (Heure 40)** : `395 000 FC` (`economy_healthy: true`)

## 2. Extrait de la Table d'Équilibrage (`economy-balance-sheet.csv`)
| ID Entité | Type | Flux | Valeur de Base (FC) | Modificateur Réputation (`SYS-WLD-REPUTATION`) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `MSN-MAIN-001-ARRIVEE` | `MISSION` | `FAUCET` | `15 000 FC` | Fixe (`1.0x`) | Capital initial débloquant l'atelier `FAM-KABONGO`. |
| `MSN-SIDE-014-WEWA` | `MISSION` | `FAUCET` | `6 500 FC` | `+20 %` si livraison sans collision | Course express à `DST-MATONGE`. |
| `ITM-WPN-MACHETTE` | `ITEM` | `SINK` | `8 500 FC` | `0.85x` à Kalamu (allié) | Forge et équilibrage lame renforcée. |
| `ITM-DOC-PASSEPORT` | `ITEM` | `SINK` | `5 000 FC` | `1.25x` à la Gombe | Renouvellement falsifié du laissez-passer ONATRA. |
""",
        scripts={"simulate_economy.py": SIMULATE_ECONOMY_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="GD-04",
        description=(
            "Conception des systèmes de progression de Koffi (CHR-PROTAG-KOFFI) : courbes d'expérience, "
            "arbres de compétences (Combat Urbain, Ingénierie & Wewa, Réseau & Infiltration Sociale) "
            "et paliers de réputation par commune (SYS-WLD-REPUTATION)."
        ),
        inputs=("game-systems-gd-01", "combat-design-gd-05", "narrative-architecture-nar-01"),
        outputs=("progression-curve.csv", "skill-tree-specification.md"),
        activation_triggers=(
            "Définition des paliers de montée en niveau et des coûts de déblocage des capacités UE5 GAS (`Ability.*`).",
            "Calibrage des récompenses systémiques octroyées par la réputation dans chaque quartier (`DST-GOMBE`, `DST-MATONGE`, `DST-KALAMU`, `DST-LIMETE`).",
            "Équilibrage du rythme d'acquisition des compétences entre le début de l'Acte I et la fin de l'Acte III.",
        ),
        scope_boundaries=(
            "Ne fixe pas les prix monétaires en boutique (`GD-03`) et n'implémente pas les classes C++ GAS (`ENG-02`).",
            "N'accorde aucun bonus purement passif invisible (+1 % dégât) : chaque noeud majeur doit enrichir les options tactiques du joueur.",
        ),
        operational_procedures=(
            "Structurer la progression autour de **3 Branches de Compétences** alignées sur les piliers créatifs (`DIR-03`) : (1) *Mêlée & Agilité Urbaine* (`GD-05`), (2) *Mécanique & Maîtrise Wewa* (`GD-06`), (3) *Voix de Kinshasa & Infiltration* (`GD-01`).",
            "Modéliser la courbe d'XP selon une fonction polynomiale contrôlée afin de garantir un nouveau déblocage toutes les 45 à 60 minutes de jeu actif.",
            "Définir les 4 paliers de `SYS-WLD-REPUTATION` par commune (*Inconnu -> Respecté -> Enfant du Quartier -> Pilier de Kinshasa*) et leurs avantages concrets en jeu.",
            "Rédiger la spécification dans `templates/skill-tree-spec.md`.",
        ),
        decision_rules=(
            ("Compétence indispensable au franchissement d'un blockout principal (ex: Ability.Movement.Vault)", "L'inclure dans le kit de base de Koffi dès MSN-MAIN-001-ARRIVEE (ne jamais verrouiller une métrique spatiale de base derrière un arbre d'XP)", "Garantir la cohérence avec WLD-05"),
            ("Branche de compétences choisie par moins de 15 % des profils de jeu simulés", "Ajouter une synergie transversale (ex: l'arbre Réseau débloque aussi des raccourcis de livraison Wewa et des diversions de foule AI-02)", "Équilibrer l'attractivité des 3 approches"),
            ("Gain de puissance en fin d'Acte II rendant les affrontements de l'Acte III triviaux", "Plafonner les multiplicateurs de santé/dégâts à +35 % sur l'ensemble du jeu et concentrer la progression sur la variété tactique", "Synchroniser avec GD-05"),
        ),
        acceptance_criteria=(
            "Chaque compétence débloquée correspond à une `UGameplayAbility` ou un `UGameplayEffect` identifié par un `FGameplayTag`.",
            "Les 4 paliers de réputation locale (`SYS-WLD-REPUTATION`) produisent des effets visibles sur les PNJ, le trafic et les commerçants.",
            "Aucune capacité obligatoire pour le chemin critique n'est verrouillée derrière un choix optionnel.",
        ),
        validation_auditors=("DIR-05", "GD-03", "GD-05"),
        reference_filename="progression-and-reputation-math.md",
        reference_content=r"""# Formules de Progression & Réputation par Quartier (`GD-04`)

## 1. Courbe d'Expérience (Niveaux 1 à 20)
$$XP_{\text{requis}}(L) = 500 \cdot L^2 + 1500 \cdot L$$
- **Niveau 1 -> 5 (Acte I)** : Maîtrise des fondamentaux (contre-attaque machette, slalom Wewa, laissez-passer).
- **Niveau 6 -> 14 (Acte II)** : Synergies urbaines (appel d'attroupement via `ORG-RADIO-KIN`, sabotage de grues/transformateurs).
- **Niveau 15 -> 20 (Acte III)** : Maîtrise complète des 3 branches.
""",
        template_filename="skill-tree-spec.md",
        template_content="""# Spécification d'Arbre de Progression & Réputation (`GD-04`)

- **Système Lié** : `SYS-WLD-REPUTATION` & Progression `CHR-PROTAG-KOFFI`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Matrice des Compétences Déblocables (Mapping GAS)
| Skill Node ID | Branche | Gameplay Tag Associé | Prérequis | Effet Tactique Concret |
| :--- | :--- | :--- | :--- | :--- |
| `SKL-...` | `[Mêlée / Wewa / Réseau]` | `Ability....` | `[Niveau / Node]` | `[Description]` |

## 2. Paliers de Réputation par Commune (`DST-*`)
| Palier | Seuil Points | Effet sur la Foule (`AI-02`) & Commerces (`GD-03`) |
| :--- | :--- | :--- |
| 1. Inconnu | `0 - 249` | Comportement neutre, prix standards (`1.0x`). |
""",
        example_filename="sample-progression-spec.md",
        example_content="""# Exemple `GD-04` — Arbre de Progression de Koffi & Réputation `DST-MATONGE`

- **Système Lié** : `SYS-WLD-REPUTATION` & Progression `CHR-PROTAG-KOFFI`
- **Statut** : `CONFIRMED`

## 1. Matrice des Compétences Déblocables (Mapping GAS)
| Skill Node ID | Branche | Gameplay Tag Associé | Prérequis | Effet Tactique Concret |
| :--- | :--- | :--- | :--- | :--- |
| `SKL-CMB-01` | Mêlée & Agilité | `State.Character.Combat.Parrying` | Niveau 2 | Élargit la fenêtre de parade parfaite de `+50 ms` avec `ITM-WPN-MACHETTE` et désarme l'assaillant. |
| `SKL-VEH-01` | Mécanique & Wewa | `Vehicle.Type.MotoWewa` | Niveau 3 | Amortissement amélioré après un saut de rampe et maintien de l'adhérence sous `World.Weather.TropicalStorm`. |
| `SKL-NET-01` | Voix de Kinshasa | `State.Character.Stealth.Disguised` | Niveau 4 | Permet d'interpeller les citoyens en lingala (`LEX-001 Mbote`) pour créer une diversion sonore devant les gardes `AI-01`. |

## 2. Paliers de Réputation à `DST-MATONGE`
| Palier | Seuil Points | Effet sur la Foule (`AI-02`) & Commerces (`GD-03`) |
| :--- | :--- | :--- |
| 1. Inconnu | `0 - 249` | Foule neutre, tarifs standards (`1.0x`). |
| 2. Respecté | `250 - 599` | Salutations positives en barks (`NAR-04`), remise `-10 %` chez les mécaniciens. |
| 3. Enfant du Quartier | `600 - 999` | Les chauffeurs de `VEH-MOTO-WEWA-01` cèdent immédiatement leur guidon en cas d'urgence ; remise `-15 %`. |
""",
    ),
    SkillBlueprint(
        skill_id="GD-05",
        description=(
            "Conception du système de combat urbain de ZAÏRE (SYS-CMB-MELEE) : affrontements à mains nues "
            "et à l'arme blanche (ITM-WPN-MACHETTE), timing image par image (Startup/Active/Recovery), "
            "hitstop, archétypes ennemis et régulation des assauts par Attack Tokens."
        ),
        inputs=("game-systems-gd-01", "lead-gd-directives-dir-05", "animation-metrics-art-05"),
        outputs=("combat-design-bible.md", "weapon-and-archetype-matrix.csv"),
        activation_triggers=(
            "Calibrage des coups, parades, esquives et sensations d'impact (Game Feel) de `CHR-PROTAG-KOFFI`.",
            "Conception d'un nouvel archétype d'ennemi (vigile portuaire, homme de main de `ORG-CARTEL-FLEUVE`, élite) pour `AI-01`.",
            "Réglage du système d'Attack Tokens et du comportement caméra dans les espaces urbains de Kinshasa.",
        ),
        scope_boundaries=(
            "Ne produit pas les fichiers d'animation `.fbx` (`ART-05`/`ART-06`) ni les systèmes de particules Niagara d'impact (`ART-09`).",
            "Interdit que plus de **2 ennemis au corps-à-corps** n'attaquent simultanément Koffi hors champ caméra (règle Attack Tokens).",
        ),
        operational_procedures=(
            "Définir chaque attaque à 60 FPS en 3 phases exactes : **Startup (Anticipation lisible)**, **Active (Frames de collision hitbox)** et **Recovery (Fenêtre de punition/annulation)**.",
            "Spécifier les paramètres de **Game Feel** : durée de Hitstop (`40 ms` sur coup léger, `85 ms` sur parade parfaite ou coup lourd), amplitude du Camera Shake et déclencheur `FGameplayTag`.",
            "Configurer le budget d'**Attack Tokens** par archétype ennemi (`1 jeton` pour assaillant standard, `2 jetons` pour élite lourd, plafond global de l'escouade = `2 jetons` actifs simultanément).",
            "Documenter la matrice complète dans `templates/combat-archetype-template.md`.",
        ),
        decision_rules=(
            ("Attaque ennemie avec un Startup < 18 frames (300 ms à 60 FPS)", "Allonger l'animation d'anticipation à >= 22 frames (366 ms) avec un indice sonore clair (AUD-02) et visuel", "Garantir une réaction humaine équitable et conforme à l'accessibilité PRD-06"),
            ("Combat déclenché dans un espace de largeur < 500 cm", "Restreindre dynamiquement le plafond d'Attack Tokens à 1 seul assaillant actif et activer les animations de combat rapproché mural", "Prévenir toute désorientation caméra"),
            ("Latence mesurée entre l'input joueur et la première frame d'esquive/parade > 100 ms", "Autoriser l'annulation (Animation Cancel) des 6 dernières frames de Recovery des attaques légères par la parade ou l'esquive", "Maintenir la réactivité nerveuse exigée par DIR-05"),
        ),
        acceptance_criteria=(
            "Toutes les attaques spécifient leurs frames Startup / Active / Recovery à 60 FPS et leur durée de Hitstop en ms.",
            "La règle des Attack Tokens (max 2 jetons simultanés) est explicitement paramétrée pour `AI-01`.",
            "Chaque arme ou capacité est reliée à un identifiant `ITM-*` et un tag `Ability.Melee.*` ou `State.Character.Combat.*`.",
        ),
        validation_auditors=("DIR-05", "ENG-02", "AI-01", "ART-05"),
        reference_filename="frame-data-and-attack-tokens.md",
        reference_content="""# Frame Data (60 FPS) & Régulation par Attack Tokens (`GD-05`)

## 1. Standards de Frame Data à 60 FPS (`1 frame = 16.66 ms`)
| Action (`FGameplayTag`) | Startup (Frames) | Active (Frames) | Recovery (Frames) | Hitstop (ms) | Cancel Window |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Ability.Melee.LightAttack` (Mains nues) | `9 f (150 ms)` | `4 f (66 ms)` | `11 f (183 ms)` | `40 ms` | Frame 16 -> Parade/Esquive |
| `Ability.Melee.LightAttack` (`ITM-WPN-MACHETTE`) | `12 f (200 ms)` | `5 f (83 ms)` | `14 f (233 ms)` | `55 ms` | Frame 20 -> Parade/Esquive |
| `Ability.Melee.HeavyAttack` (`ITM-WPN-MACHETTE`) | `24 f (400 ms)` | `6 f (100 ms)` | `20 f (333 ms)` | `90 ms` | Non annulable pendant Active |
| `State.Character.Combat.Parrying` | `3 f (50 ms)` | `12 f (200 ms)` | `10 f (166 ms)` | `85 ms` | Contre-attaque immédiate sur succès |
""",
        template_filename="combat-archetype-template.md",
        template_content="""# Spécification Combat & Archétypes Ennemis (`GD-05`)

- **Système** : `SYS-CMB-MELEE`
- **Arme / Capacité Évaluée** : `ITM-...` (`Ability.Melee...`)
- **Plafond Attack Tokens Escouade** : `2 jetons simultanés max`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Table Frame Data (Base 60 FPS)
| Mouvement | Gameplay Tag | Startup (f) | Active (f) | Recovery (f) | Dégâts | Hitstop (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[Nom coup]` | `Ability.Melee...` | `[XX]` | `[XX]` | `[XX]` | `[XX]` | `[XX ms]` |

## 2. Archétypes Ennemis & Comportement IA (`AI-01`)
| ID Archétype | Coût Attack Token | Santé (HP) | Pattern d'Attaque & Télégraphe | Contre Tactique Joueur |
| :--- | :--- | :--- | :--- | :--- |
| `ENM-...` | `1` | `[HP]` | `[Startup >= 22f + signal]` | `[Parade / Esquive]` |
""",
        example_filename="sample-combat-spec.md",
        example_content="""# Exemple `GD-05` — Spécification Combat `ITM-WPN-MACHETTE` & Vigiles `ORG-CARTEL-FLEUVE`

- **Système** : `SYS-CMB-MELEE`
- **Arme / Capacité Évaluée** : `ITM-WPN-MACHETTE` (`Ability.Melee.LightAttack`, `Ability.Melee.HeavyAttack`, `State.Character.Combat.Parrying`)
- **Plafond Attack Tokens Escouade** : `2 jetons simultanés max` (1 jeton en couloir `< 500 cm`)
- **Statut** : `CONFIRMED`

## 1. Table Frame Data (Base 60 FPS)
| Mouvement | Gameplay Tag | Startup (f) | Active (f) | Recovery (f) | Dégâts | Hitstop (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Taille Rapide Machette | `Ability.Melee.LightAttack` | `12 f` | `5 f` | `14 f` | `25` | `55 ms` |
| Fente Brise-Garde | `Ability.Melee.HeavyAttack` | `24 f` | `6 f` | `20 f` | `55` | `90 ms` |
| Parade Renforcée | `State.Character.Combat.Parrying` | `3 f` | `12 f` | `10 f` | `0 (+Stagger)` | `85 ms` |

## 2. Archétypes Ennemis & Comportement IA (`AI-01`)
| ID Archétype | Coût Attack Token | Santé (HP) | Pattern d'Attaque & Télégraphe | Contre Tactique Joueur |
| :--- | :--- | :--- | :--- | :--- |
| `ENM-PORT-VIGILE` | `1 jeton` | `100 HP` | Coup de matraque télégraphié (`24 frames / 400 ms` + bark `BRK-PORT-02`). | Parade `State.Character.Combat.Parrying` suivie d'une Taille Rapide. |
| `ENM-CARTEL-BRUTE` | `2 jetons` | `220 HP` | Charge lourde imblocable (`36 frames / 600 ms` + son métallique lourd `AUD-02`). | Esquive latérale obligatoire puis punition par `Ability.Melee.HeavyAttack`. |
""",
    ),
    SkillBlueprint(
        skill_id="GD-06",
        description=(
            "Conception ludique et tuning de conduite des véhicules de Kinshasa (VEH-MOTO-WEWA-01, "
            "VEH-TAXI-JAUNE-01, VEH-BUS-TRANSCO-01) sous UE5 Chaos Vehicles. Calibre les courbes "
            "de couple, la maniabilité simcade, la stabilisation deux-roues et l'adhérence par surface "
            "(asphalte, latérite sèche, boue d'averse équatoriale)."
        ),
        inputs=("urban-typology-wld-03", "game-systems-gd-01", "lead-gd-directives-dir-05"),
        outputs=("vehicle-handling-spec.md", "surface-friction-matrix.csv"),
        activation_triggers=(
            "Création ou réglage d'un véhicule jouable ou IA (`VEH-*`).",
            "Équilibrage de l'impact de la météo (`World.Weather.TropicalStorm`) et de la nature des sols kinois (béton portuaire, asphalte du Boulevard du 30 Juin, latérite de Kalamu) sur le freinage et la dérive.",
            "Paramétrage du comportement d'inter-file (slalom trafic `130 cm`) de la moto `VEH-MOTO-WEWA-01`.",
        ),
        scope_boundaries=(
            "Ne modélise pas le maillage 3D ni le rig squelettique du véhicule (`ART-02`/`ART-08`).",
            "Ne programme pas le solveur bas niveau C++ Chaos (`ENG-05`), mais fournit les valeurs cibles exactes de suspension, masse, centre de gravité et friction.",
        ),
        operational_procedures=(
            "Enregistrer le véhicule sous un identifiant `VEH-[CAT]-[SLUG]` dans `knowledge/entities-registry.csv` et lui associer son Gameplay Tag (`Vehicle.Type.*`).",
            "Vérifier la compatibilité du gabarit géométrique du véhicule avec `knowledge/technical-specs/spatial-metrics.md` (ex: largeur `80 cm` pour `VEH-MOTO-WEWA-01` dans un couloir inter-file de `130 cm`).",
            "Définir la matrice des multiplicateurs d'adhérence (`Friction Scale`) sur les 4 surfaces de Kinshasa : Asphalte Sec, Asphalte Mouillé, Latérite Compactée, Boue Tropicale.",
            "Rédiger la fiche technique dans `templates/vehicle-handling-spec.md`.",
        ),
        decision_rules=(
            ("Moto VEH-MOTO-WEWA-01 chutant trop facilement lors des contacts légers à basse vitesse dans le trafic dense", "Activer un couple gyroscopique d'auto-stabilisation assistée sous 35 km/h et relever le seuil d'éjection ragdoll Chaos à un impact frontal > 55 km/h", "Privilégier le plaisir de slalom urbain simcade sur la frustration punitive"),
            ("Transition de surface par temps de pluie (World.Weather.TropicalStorm) rendant la moto incontrôlable", "Plafonner la perte d'adhérence latérale à -25 % sur asphalte mouillé et -35 % sur boue latéritique avec retour haptique progressif", "Synchroniser avec ENG-05 et AUD-02 (RTPC crissement/éclaboussure)"),
            ("Véhicule lourd (VEH-BUS-TRANSCO-01) incapable de négocier les ronds-points kinois", "Ajuster l'angle de braquage maximal à basse vitesse à 38 degrés sur les voies de 380-400 cm", "Valider la trajectoire spline avec AI-03"),
        ),
        acceptance_criteria=(
            "Chaque véhicule `VEH-*` dispose de ses dimensions en cm, de sa masse en kg, de sa vitesse de pointe et de ses coefficients de friction sur les 4 surfaces.",
            "La différenciation de prise en main entre une moto Wewa agile (`135 kg`) et un bus lourd (`11 500 kg`) est immédiate.",
            "Les seuils d'éjection et de collision sont validés avec `ENG-05` (Chaos Physics).",
        ),
        validation_auditors=("DIR-05", "ENG-05", "AI-03"),
        reference_filename="chaos-vehicle-tuning-guide.md",
        reference_content="""# Paramétrage Simcade des Véhicules Kinois sous UE5 Chaos (`GD-06`)

## 1. Profils Physiques de Référence
| ID Véhicule | Masse (kg) | Gabarit L × l × H (cm) | Vitesse Max (km/h) | 0-60 km/h (s) | Rayon Braquage (m) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `135 kg` (210 avec pilote) | `205 × 80 × 115` | `95 km/h` | `3.2 s` | `2.4 m` |
| `VEH-TAXI-JAUNE-01` | `1 180 kg` | `440 × 180 × 150` | `125 km/h` | `5.8 s` | `5.1 m` |
| `VEH-BUS-TRANSCO-01` | `11 500 kg` | `1200 × 255 × 330` | `80 km/h` | `12.5 s` | `10.8 m` |

## 2. Matrice de Friction par Surface (`ChaosPhysicalMaterial`)
- `PM_Asphalt_Dry` : Friction Latérale = `1.20`, Friction Longitudinale = `1.15`.
- `PM_Asphalt_Wet` (`World.Weather.TropicalStorm`) : Friction Latérale = `0.90`, Longitudinale = `0.88`.
- `PM_Laterite_Dry` (`DST-KALAMU`) : Friction Latérale = `0.95`, Longitudinale = `0.92`.
- `PM_Laterite_Mud` (`World.Weather.TropicalStorm`) : Friction Latérale = `0.78`, Longitudinale = `0.75`.
""",
        template_filename="vehicle-handling-spec.md",
        template_content="""# Spécification de Conduite & Tuning Véhicule (`GD-06`)

- **ID Véhicule** : `VEH-[CAT]-[SLUG]`
- **Gameplay Tag** : `Vehicle.Type.[Nom]`
- **Gabarit (L × l × H en cm)** : `[XXX × XXX × XXX cm]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Paramètres Dynamiques Chaos Vehicles (`ENG-05`)
- **Masse Totale (kg)** : `[XXXX kg]`
- **Centre de Gravité (Offset Z cm)** : `[-XX cm]`
- **Vitesse Max & Accélération (0-60 km/h)** : `[XX km/h | X.X s]`
- **Assistance & Stabilisation** : `[Règles gyroscopiques / anti-retournement]`

## 2. Réponse par Surface & Météo
| Surface (`ChaosPhysicalMaterial`) | Multiplicateur Grip Latéral | Multiplicateur Freinage | Effet Caméra / Audio (`AUD-02`) |
| :--- | :--- | :--- | :--- |
| `PM_Asphalt_Dry` | `1.20` | `1.15` | `[Effet]` |
""",
        example_filename="sample-vehicle-spec.md",
        example_content="""# Exemple `GD-06` — Spécification de `VEH-MOTO-WEWA-01` (Moto-Taxi Wewa 125cc)

- **ID Véhicule** : `VEH-MOTO-WEWA-01`
- **Gameplay Tag** : `Vehicle.Type.MotoWewa`
- **Gabarit (L × l × H en cm)** : `205 × 80 × 115 cm` (compatible couloir inter-file `>= 130 cm`)
- **Statut** : `CONFIRMED`

## 1. Paramètres Dynamiques Chaos Vehicles (`ENG-05`)
- **Masse Totale (kg)** : `210 kg` (moto `135 kg` + `CHR-PROTAG-KOFFI` `75 kg`).
- **Centre de Gravité (Offset Z cm)** : `-28 cm` (abaissé pour stabiliser les changements d'angle rapides en slalom).
- **Vitesse Max & Accélération (0-60 km/h)** : `95 km/h | 3.2 s` (couple élevé à bas régime pour se dégager des carrefours).
- **Assistance & Stabilisation** : Couple de redressement gyroscopique progressif actif de `0 à 35 km/h` ; inclinaison maximale (Lean Angle) plafonnée à `42°` sur sec et `34°` sous `World.Weather.TropicalStorm`.

## 2. Réponse par Surface & Météo
| Surface (`ChaosPhysicalMaterial`) | Multiplicateur Grip Latéral | Multiplicateur Freinage | Effet Caméra / Audio (`AUD-02`) |
| :--- | :--- | :--- | :--- |
| `PM_Asphalt_Dry` (`LOC-GOMBE-BD30JUIN`) | `1.20` | `1.15` | FOV `+4°` à pleine vitesse, RTPC régime moteur clair. |
| `PM_Asphalt_Wet` (`LOC-GOMBE-PORT` pluie) | `0.92` | `0.88` | Légère dérive arrière contrôlable + gerbes d'eau Niagara (`ART-09`). |
| `PM_Laterite_Dry` (`DST-KALAMU`) | `0.96` | `0.92` | Micro-vibrations suspension + traînée de poussière ocre. |
| `PM_Laterite_Mud` (Averse équatoriale) | `0.80` | `0.76` | Patinage roue arrière au démarrage + éclaboussures boueuses. |
""",
    ),
    SkillBlueprint(
        skill_id="GD-07",
        description=(
            "Architecture de l'information, conception du HUD contextuel minimaliste, du téléphone "
            "diégétique de Koffi, de la carte interactive de Kinshasa et des parcours utilisateurs (UX) "
            "sous UE5 Common UI. Garantit le support Unicode Lingala (ɛ, ɔ), l'expansion de texte (+35 %) "
            "et la conformité native aux normes d'accessibilité XAG (PRD-06)."
        ),
        inputs=("game-systems-gd-01", "mission-design-gd-02", "art-bible-art-01", "xag-requirements-prd-06"),
        outputs=("ui-screen-specification.md", "common-ui-navigation-flow.md"),
        activation_triggers=(
            "Conception ou modification d'un écran d'interface, d'un composant HUD, de la carte de Kinshasa ou du téléphone diégétique (`UI.Layer.*`).",
            "Vérification de la tenue des conteneurs de texte face à l'expansion linguistique (+35 %) et aux caractères spéciaux du lingala (`ɛ`, `ɔ`).",
            "Intégration des exigences d'accessibilité visuelle et cognitive (`PRD-06` : double codage forme+couleur, contraste >= 4.5:1, taille des sous-titres).",
        ),
        scope_boundaries=(
            "Ne programme pas le code C++ des `UCommonActivatableWidget` (`ENG-02`).",
            "Interdit tout encombrement permanent de l'écran (pas de mini-carte intrusive verrouillée si le joueur navigue via `SYS-WLD-LANDMARKS`).",
        ),
        operational_procedures=(
            "Rattacher chaque widget à sa couche Common UI (`UI.Layer.HUD` ou `UI.Layer.DiegeticPhone` dans `knowledge/technical-specs/gameplay-tags-taxonomy.csv`).",
            "Appliquer la règle de **Navigation en 3 Actions Maximum** : toute fonction principale (carte de Kinshasa, journal de mission `MSN-*`, station radio `ORG-RADIO-KIN`, inventaire) doit être atteignable en `<= 3` pressions manette ou clavier.",
            "Dimensionner tous les conteneurs de chaînes dynamiques avec une réserve d'expansion horizontale/verticale de **`+35 %`** et imposer une police supportant la plage Unicode Latin Étendu B (`ɛ` U+025B, `ɔ` U+0254).",
            "Appliquer le **Double Codage XAG** : associer systématiquement une icône distincte et une variation de forme à chaque couleur d'état (ennemi, allié, objectif, danger).",
        ),
        decision_rules=(
            ("Information transmise uniquement par la couleur (ex: jauge ou icône rouge vs verte)", "Ajouter immédiatement une différenciation géométrique (losange hachuré vs cercle plein) et une option de palette daltonisme (Deutéranopie, Protanopie, Tritanopie)", "Respecter l'exigence obligatoire XAG (quality-standards.md)"),
            ("Conteneur UI fixe tronquant une chaîne traduite avec expansion de +35 %", "Remplacer la largeur fixe par un conteneur dynamique Auto-Wrap avec marge de sécurité de +35 % sans défilement horizontal", "Synchroniser avec AUD-04"),
            ("Élément HUD restant affiché en permanence hors combat ou navigation active", "Passer le widget en mode Dynamic Auto-Hide (disparition en fondu après 4 secondes d'inactivité)", "Préserver l'immersion visuelle dans Kinshasa (DIR-03 / ART-01)"),
        ),
        acceptance_criteria=(
            "100 % des widgets supportent une expansion de texte de `+35 %` et affichent correctement `ɛ` et `ɔ`.",
            "Contraste typographique mesuré `>= 4.5:1` (texte standard) et `>= 7:1` (sous-titres sur fond semi-opaque).",
            "Navigation complète au pavé directionnel/manette et clavier/souris via les Input Action Tables de UE5 Common UI.",
        ),
        validation_auditors=("PRD-06", "AUD-04", "DIR-05"),
        reference_filename="common-ui-and-xag-ergonomics.md",
        reference_content="""# Architecture UE5 Common UI & Ergonomie Accessible (`GD-07`)

## 1. Hiérarchie des Couches (`UCommonActivatableWidget` Stack)
- `UI.Layer.HUD` : Jauge d'endurance/santé contextuelle (masquée à 100 % hors combat), boussole discrète de landmarks (`SYS-WLD-LANDMARKS`), sous-titres enrichis.
- `UI.Layer.DiegeticPhone` : Téléphone portable de Koffi consultable en temps réel sans couper le monde (SMS d'Amina `CHR-ALLY-AMINA`, tuner `ORG-RADIO-KIN`, carte par commune `DST-*`).

## 2. Normes Typographiques & Accessibilité (`PRD-06` / `AUD-04`)
- **Glyphes Obligatoires** : Support natif de `ɛ`, `Ɛ`, `ɔ`, `Ɔ` et des diacritiques tonals (`á`, `é`, `ɛ́`, `ɔ́`).
- **Taille Minimale Police TV/Console (1080p réf)** : `24 px` pour le corps d'interface, `28 px` à `42 px` (réglable) pour les sous-titres avec préfixe locuteur `[KOFFI]` et fond noir opacité `60-85 %`.
- **Tolérance d'Expansion** : `+35 %` de longueur de chaîne sur tous les boutons, notifications et objectifs.
""",
        template_filename="ui-screen-spec-template.md",
        template_content="""# Spécification d'Écran UI/UX — Common UI (`GD-07`)

- **ID Widget** : `UI-[LAYER]-[SLUG]`
- **Gameplay Tag Layer** : `UI.Layer.[HUD / DiegeticPhone]`
- **Profondeur Navigation** : `[<= 3 actions]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture Visuelle & Comportement Contextuel
- **Condition d'Affichage / Auto-Hide** : `[Règle d'apparition et de masquage]`
- **Binding Gameplay Tags** : `[Tags écoutés]`

## 2. Conformité Localisation (`AUD-04`) & Accessibilité XAG (`PRD-06`)
- **Tolérance Expansion Texte (+35 %)** : `[Validé / Conteneur dynamique]`
- **Support Glyphes Lingala (`ɛ`, `ɔ`)** : `[Police & encodage UTF-8]`
- **Double Codage Forme + Couleur** : `[Icônes associées aux états]`
- **Ratio de Contraste Minimum** : `[>= 4.5:1]`
""",
        example_filename="sample-ui-screen-spec.md",
        example_content="""# Exemple `GD-07` — Spécification du HUD Contextuel & Téléphone Diégétique de Koffi

- **ID Widget** : `UI-HUD-MAIN-OVERLAY` & `UI-PHONE-KINSHASA-HUB`
- **Gameplay Tag Layer** : `UI.Layer.HUD` & `UI.Layer.DiegeticPhone`
- **Profondeur Navigation** : `2 actions max` (`D-Pad Haut` -> Ouverture Téléphone -> `LB/RB` bascule Carte / Radio Lokole / Messages)
- **Statut** : `CONFIRMED`

## 1. Architecture Visuelle & Comportement Contextuel
- **Condition d'Affichage / Auto-Hide** : En exploration libre à `DST-MATONGE` ou `DST-GOMBE`, 0 élément HUD permanent à l'écran. Le réticule de furtivité n'apparaît que sous `State.Character.Stealth.Concealed` ; la jauge de mêlée n'apparaît que sous `State.Character.Combat.Engaged`.
- **Binding Gameplay Tags** : `State.Character.Combat.Engaged`, `State.Character.Stealth.Concealed`, `State.Character.Stealth.Disguised`, `World.District.*`.

## 2. Conformité Localisation (`AUD-04`) & Accessibilité XAG (`PRD-06`)
- **Tolérance Expansion Texte (+35 %)** : Les bannières d'objectifs de mission (`MSN-*`) et les bulles SMS utilisent des `USizeBox` et `UVerticalBox` extensibles acceptant jusqu'à `+40 %` de caractères sans rognage.
- **Support Glyphes Lingala (`ɛ`, `ɔ`)** : Police sans-serif Humanist UTF-8 certifiée sur l'intégralité du glossaire (`Kɛbá!`, `Tɔ́kɛndɛ́`, `Bilɔkɔ`).
- **Double Codage Forme + Couleur** :
  - Vigilance Garde `AI-01` : Cercle blanc pointillé (Calme) -> Triangle jaune strié (Soupçon) -> Losange rouge plein avec point d'exclamation + son distinctif (Alerte).
- **Ratio de Contraste Minimum** : `7.2:1` sur le bandeau de sous-titres (`[KOFFI] : « Tɔ́kɛndɛ́ ! »` sur fond `RGBA(12, 12, 16, 0.78)`).
""",
    ),
)


def build_department_03(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 7 skills du département 03-game-design."""
    created: list[Path] = []
    for bp in GAME_DESIGN_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_03(WORKSPACE_ROOT)
    print(f"[OK] Département 03-game-design généré ({len(paths)} skills).")
