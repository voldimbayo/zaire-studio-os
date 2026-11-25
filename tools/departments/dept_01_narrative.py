"""Spécifications et génération du Département 01-NARRATIVE (NAR-01 à NAR-06)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

VALIDATE_DIALOGUE_SCRIPT = '''"""Validateur structurel de graphes de dialogue interactifs JSON pour NAR-04."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

VALID_EMOTION_TAGS = frozenset({"NEUTRAL", "TENSE", "ANGRY", "WARM", "URGENT", "IRONIC"})
VALID_CAMERA_FRAMINGS = frozenset({"OTS_LEFT", "OTS_RIGHT", "CLOSE_UP", "TWO_SHOT", "WIDE_ESTABLISHING"})


def validate_dialogue_graph(payload: dict) -> list[str]:
    """Vérifie l'absence d'impasse (dead-end), la limite de 20 mots par bulle et les tags caméra/émotion."""
    errors: list[str] = []
    nodes = payload.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        return ["Le graphe de dialogue doit contenir une liste 'nodes' non vide."]

    node_ids = {n.get("node_id") for n in nodes if isinstance(n, dict) and n.get("node_id")}
    for idx, node in enumerate(nodes, start=1):
        nid = node.get("node_id", f"INDEX_{idx}")
        speaker = node.get("speaker_id", "")
        text = str(node.get("line_text", "")).strip()
        emotion = node.get("emotion_tag", "")
        camera = node.get("camera_framing", "")
        next_nodes = node.get("next_nodes", [])
        is_terminal = bool(node.get("is_terminal", False))

        if not speaker.startswith("CHR-"):
            errors.append(f"Noeud {nid}: speaker_id ({speaker!r}) doit commencer par 'CHR-'.")
        word_count = len(text.split())
        if word_count == 0 or word_count > 20:
            errors.append(f"Noeud {nid}: réplique hors calibre UI ({word_count} mots, max=20).")
        if emotion not in VALID_EMOTION_TAGS:
            errors.append(f"Noeud {nid}: emotion_tag invalide ({emotion!r}).")
        if camera not in VALID_CAMERA_FRAMINGS:
            errors.append(f"Noeud {nid}: camera_framing invalide ({camera!r}).")
        if not is_terminal and not next_nodes:
            errors.append(f"Noeud {nid}: impasse narrative détectée (non terminal sans next_nodes).")
        for target in next_nodes:
            if target not in node_ids:
                errors.append(f"Noeud {nid}: transition vers un node_id inexistant ({target!r}).")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide un graphe de dialogue JSON (NAR-04).")
    parser.add_argument("--file", help="Chemin du fichier JSON à valider (optionnel, mode auto-test sinon)")
    args = parser.parse_args()

    if args.file:
        data = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        data = {
            "dialogue_id": "DLG-MSN-001-PORT",
            "nodes": [
                {
                    "node_id": "N01",
                    "speaker_id": "CHR-PROTAG-KOFFI",
                    "line_text": "Mbote vieux! J'ai le laissez-passer ONATRA pour le quai numéro quatre.",
                    "emotion_tag": "WARM",
                    "camera_framing": "OTS_LEFT",
                    "is_terminal": False,
                    "next_nodes": ["N02"],
                },
                {
                    "node_id": "N02",
                    "speaker_id": "CHR-ALLY-AMINA",
                    "line_text": "Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue principale. Tɔ́kɛndɛ́!",
                    "emotion_tag": "URGENT",
                    "camera_framing": "CLOSE_UP",
                    "is_terminal": True,
                    "next_nodes": [],
                },
            ],
        }

    errs = validate_dialogue_graph(data)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Graphe de dialogue {data.get('dialogue_id', 'SAMPLE')} validé ({len(data['nodes'])} noeuds, 0 impasse).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

NARRATIVE_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="NAR-01",
        description=(
            "Conception de l'architecture narrative macroscopique de ZAÏRE : structure en 3 actes, "
            "arcs thématiques, embranchements majeurs à conséquences persistantes par commune de Kinshasa "
            "(DST-*) et alignement ludo-narratif avec les systèmes de monde ouvert."
        ),
        inputs=("creative-pillars-dir-03", "kinshasa-world-bible-wld-01", "cultural-briefs-wld-02"),
        outputs=("narrative-architecture.md", "branching-consequences-matrix.csv"),
        activation_triggers=(
            "Structuration initiale ou révision des actes principaux du jeu ZAÏRE.",
            "Conception d'un embranchement narratif majeur modifiant l'état politique, économique ou sécuritaire d'une commune (`DST-*`).",
            "Alignement entre la progression dramatique de `CHR-PROTAG-KOFFI` et le déblocage des systèmes de gameplay (`GD-01`/`GD-04`).",
        ),
        scope_boundaries=(
            "N'écrit jamais les dialogues réplique par réplique (`NAR-04`) ni les scripts de scènes détaillés (`NAR-02`).",
            "Ne crée pas les profils psychologiques micro-individuels des personnages secondaires (`NAR-03`).",
        ),
        operational_procedures=(
            "Ancrer chaque acte dramatique dans un territoire précis de Kinshasa (`DST-GOMBE`, `DST-KALAMU`, `DST-MATONGE`, `DST-LIMETE`, `DST-NGALIEMA`) en consultant `knowledge/world-bible/kinshasa-districts.md`.",
            "Définir les **Points de Pivot (Plot Pivots)** où les choix du joueur modifient durablement les variables d'état du monde (`SYS-WLD-REPUTATION`, Data Layers UE5).",
            "Vérifier que chaque arc narratif s'exprime par les boucles de gameplay (infiltration portuaire, courses Wewa, réseaux d'informateurs radio `ORG-RADIO-KIN`) et non uniquement par des cinématiques passives.",
            "Documenter la matrice d'embranchements dans `templates/act-structure-template.md` et soumettre à `NAR-06`.",
        ),
        decision_rules=(
            ("Embranchement créant une divergence exponentielle ingérable en production", "Appliquer le modèle 'Diamond Branching' (divergence locale forte sur le quartier, reconvergence sur les jalons d'actes avec mémoire d'état persistante)", "Faire valider le coût de production par DIR-02"),
            ("Arc narratif déconnecté de l'environnement urbain de Kinshasa", "Rattacher obligatoirement le conflit à une institution ou réalité locale (port ONATRA, transport, coupures réseau, scène musicale)", "Consulter WLD-01 et WLD-02"),
            ("Mort potentielle d'un personnage clé avant sa dernière mission critique", "Interdire la létalité hors noeud canonique ou prévoir un remplaçant systémique documenté", "Soumettre le graphe d'état à NAR-06"),
        ),
        acceptance_criteria=(
            "Chaque acte définit son conflit central, ses communes (`DST-*`), ses factions (`ORG-*`) et son évolution du protagoniste (`CHR-PROTAG-KOFFI`).",
            "100 % des embranchements majeurs produisent un impact mesurable sur `SYS-WLD-REPUTATION` ou sur les Data Layers du quartier.",
            "Aucune contradiction avec les 3 piliers créatifs de `DIR-03`.",
        ),
        validation_auditors=("NAR-06", "DIR-03"),
        reference_filename="macro-narrative-design.md",
        reference_content="""# Architecture Narrative Interactive en Monde Ouvert (`NAR-01`)

## 1. Structure en 3 Actes de ZAÏRE
- **Acte I — Les Courants du Fleuve (`DST-KALAMU` & `DST-GOMBE`)** : Koffi Kabongo (`CHR-PROTAG-KOFFI`) découvre la mainmise du Syndicat du Fleuve (`ORG-CARTEL-FLEUVE`, dirigé par `CHR-ANTAG-MUKENDI`) sur les docks d'ONATRA (`LOC-GOMBE-PORT`).
- **Acte II — La Fréquence de Matonge (`DST-MATONGE` & `DST-LIMETE`)** : Alliance avec Amina Nzuzi (`CHR-ALLY-AMINA`) et `ORG-RADIO-KIN` pour fédérer les coursiers Wewa et les artisans face au blocus logistique autour de `LOC-LIMETE-ECHANGEUR`.
- **Acte III — L'Orage Équatorial (`DST-GOMBE` & `DST-NGALIEMA`)** : Confrontation finale entre les réseaux citoyens et la dynastie `FAM-MUKENDI` lors de la grande crue de la saison des pluies.

## 2. Règle de Convergence "Diamond Pattern"
Les choix du joueur dans l'Acte II altèrent l'allié dominant et le niveau d'alerte de `DST-GOMBE` en Acte III sans dupliquer les 100 % de la carte ouverte.
""",
        template_filename="act-structure-template.md",
        template_content="""# Architecture d'Acte Narratif (`NAR-01`)

- **Acte** : `ACTE-[I / II / III]`
- **Titre** : `[Titre dramatique]`
- **Communes Principales** : `[DST-*]`
- **Personnages Pivots** : `[CHR-*]`

## 1. Progression Dramatique & Alignement Gameplay
| Séquence | Objectif Dramatique | Mission Associée (`MSN-*`) | Système Gameplay Sollicité (`SYS-*`) |
| :--- | :--- | :--- | :--- |
| 1 | `[Introduction / Incident]` | `MSN-MAIN-...` | `SYS-...` |

## 2. Embranchements & Conséquences Monde Ouvert
| Point de Choix | Option A (Impact Monde) | Option B (Impact Monde) | Variable d'État Persistante |
| :--- | :--- | :--- | :--- |
| `[Pivot]` | `[Conséquence A]` | `[Conséquence B]` | `WorldState.Act...` |
""",
        example_filename="sample-act-architecture.md",
        example_content="""# Exemple `NAR-01` — Architecture de l'Acte I : Les Courants du Fleuve

- **Acte** : `ACTE-I`
- **Titre** : Les Courants du Fleuve
- **Communes Principales** : `DST-GOMBE`, `DST-KALAMU`
- **Personnages Pivots** : `CHR-PROTAG-KOFFI`, `CHR-ANTAG-MUKENDI`, `CHR-ALLY-AMINA`

## 1. Progression Dramatique & Alignement Gameplay
| Séquence | Objectif Dramatique | Mission Associée | Système Gameplay Sollicité |
| :--- | :--- | :--- | :--- |
| 1 | Retour de Koffi sur les barges du fleuve et saisie de l'atelier familial `FAM-KABONGO` | `MSN-MAIN-001-ARRIVEE` | `SYS-STEALTH`, `SYS-WLD-LANDMARKS` |
| 2 | Première alliance avec `ORG-RADIO-KIN` pour exposer la saisie illégale des grues | `MSN-SIDE-014-WEWA` | `SYS-TRAFFIC-ZONE`, `SYS-WLD-REPUTATION` |

## 2. Embranchements & Conséquences Monde Ouvert
| Point de Choix | Option A (Impact Monde) | Option B (Impact Monde) | Variable d'État Persistante |
| :--- | :--- | :--- | :--- |
| Sabotage ou Saisie des registres à `LOC-GOMBE-PORT` | **Sabotage** : Patrouilles doublées à la Gombe, +25 Réputation à Kalamu | **Saisie discrète** : Accès maintenu via `ITM-DOC-PASSEPORT`, bonus monétaire `GD-03` | `WorldState.Act1.PortApproach` |
""",
    ),
    SkillBlueprint(
        skill_id="NAR-02",
        description=(
            "Écriture des scénarios de missions principales et secondaires (MSN-*), beat sheets "
            "dramatiques, cinématiques temps réel (UE5 Sequencer) et didascalies de mise en scène "
            "ancrées dans le rythme visuel et linguistique de Kinshasa."
        ),
        inputs=("narrative-architecture-nar-01", "character-bibles-nar-03", "mission-design-gd-02"),
        outputs=("mission-script.md", "cinematic-beatsheet.md"),
        activation_triggers=(
            "Rédaction du scénario complet d'une mission (`MSN-*`) après validation de sa structure ludique par `GD-02`.",
            "Conception d'une cinématique temps réel sous UE5 Sequencer (ouverture/clôture de quête, confrontation de boss).",
            "Adaptation dramatique d'une séquence de gameplay pour intégrer la narration pendant l'action (Walk-and-Talk ou conduite Wewa).",
        ),
        scope_boundaries=(
            "Ne programme pas les graphes logiques conditionnels de dialogue (`NAR-04`) ni les machines à états de quête (`GD-02`).",
            "N'écrit jamais d'instructions de code Blueprint ou C++ (`ENG-02`).",
        ),
        operational_procedures=(
            "Lire la fiche de mission `GD-02` et les fiches personnages `NAR-03` pour respecter la voix de chaque protagoniste (`CHR-*`).",
            "Découper la mission en **Beats Dramatiques** alternant tension, révélation et respiration, en privilégiant la narration en mouvement plutôt que les coupures caméra prolongées.",
            "Intégrer les termes certifiés du glossaire `knowledge/world-bible/lingala-french-glossary.csv` (`LEX-*`) dans les intentions de dialogue.",
            "Formater le script selon `templates/mission-script-template.md` en précisant la durée cible (max 90 secondes par cinématique non interactive).",
        ),
        decision_rules=(
            ("Cinématique passive dépassant 90 secondes consécutives", "Convertir la moitié de l'exposition en séquence jouable (Walk-and-Talk dans le port ou dialogue en moto Wewa)", "Synchroniser avec GD-02 et WLD-05"),
            ("Besoin d'une expression en lingala non présente dans lingala-french-glossary.csv", "Baliser la réplique avec [RESEARCH_REQUIRED: WLD-02] au lieu d'inventer une traduction approximative", "Soumettre la demande lexicale à WLD-02"),
            ("Action dramatique exigeant une animation unique non standard", "Annoter le beat avec [MOCAP_REQ: ART-06] pour inclusion dans la shotlist Motion Capture", "Vérifier le budget d'animation avec ART-05"),
        ),
        acceptance_criteria=(
            "Le script respecte scrupuleusement les identifiants `CHR-*`, `LOC-*` et `MSN-*` du registre.",
            "Chaque scène indique l'heure, la météo (`ART-07`), l'ambiance sonore (`AUD-02`) et le minutage estimé.",
            "Le principe 'Show, Don't Tell' est appliqué : l'action visuelle à Kinshasa prime sur les monologues explicatifs.",
        ),
        validation_auditors=("NAR-03", "WLD-02", "NAR-06"),
        reference_filename="screenwriting-standards.md",
        reference_content="""# Standards Scénaristiques & Cinématiques Temps Réel (`NAR-02`)

## 1. Règles de Rythme (Pacing AAA)
- **Durée maximale d'une Cutscene UE5 Sequencer** : `90 secondes` (au-delà, basculer en dialogue interactif `NAR-04` ou en phase jouable).
- **Continuité Caméra (Méthode Naughty Dog `SRC-011`)** : Les transitions entre gameplay et cinématique s'effectuent en plan-séquence sans fondu au noir, en conservant le même rig d'éclairage Lumen.
- **Usage du Code-Switching** : Le lingala intervient naturellement sur les salutations (`Mbote`), les exclamations d'urgence (`Kɛbá!`, `Tɔ́kɛndɛ́`) et les termes culturels (`Libongo`, `Wewa`, `Mosolo`).
""",
        template_filename="mission-script-template.md",
        template_content="""# Script Scénaristique de Mission (`NAR-02`)

- **Mission ID** : `MSN-...`
- **Lieu Principal** : `LOC-...` (`DST-...`)
- **Personnages Présents** : `[CHR-*]`
- **Durée Cinématique Estimée** : `[XX secondes]`

## 1. Beat Sheet Dramatique
| Beat # | Type (`CUTSCENE` / `GAMEPLAY_TALK`) | Enjeu Émotionnel | Action Visuelle & Mise en Scène |
| :--- | :--- | :--- | :--- |
| B01 | `CUTSCENE` | `[Enjeu]` | `[Action caméra & décor]` |

## 2. Script Détaillé des Scènes
### Scène 1 — `[INT/EXT. LIEU - HEURE / MÉTÉO]`
- **Ambiance Sonore (`AUD-02`)** : `[Description]`
- **Didascalie** : `[Action]`
- **Dialogues Clés** :
  - **[CHR-ID]** *(Intention)* : « `[Texte avec termes LEX-*]` »
""",
        example_filename="sample-mission-script.md",
        example_content="""# Exemple `NAR-02` — Script de `MSN-MAIN-001-ARRIVEE` (Séquence d'Ouverture)

- **Mission ID** : `MSN-MAIN-001-ARRIVEE`
- **Lieu Principal** : `LOC-GOMBE-PORT` (`DST-GOMBE`)
- **Personnages Présents** : `CHR-PROTAG-KOFFI`, `CHR-ALLY-AMINA` (par radio), Gardes `ORG-CARTEL-FLEUVE`
- **Durée Cinématique Estimée** : `55 secondes`

## 1. Beat Sheet Dramatique
| Beat # | Type | Enjeu Émotionnel | Action Visuelle & Mise en Scène |
| :--- | :--- | :--- | :--- |
| B01 | `CUTSCENE` | Tension du retour à Kinshasa | La barge fend la brume du fleuve Congo (`LEX-005 Ebale`) à l'aube ; les grues de `LOC-GOMBE-PORT` émergent à contre-jour. |
| B02 | `GAMEPLAY_TALK` | Urgence de l'infiltration | Transition caméra fluide dans le dos de Koffi sur le quai (`LEX-006 Libongo`) ; Amina le guide via l'oreillette. |

## 2. Script Détaillé des Scènes
### Scène 1 — `EXT. LOC-GOMBE-PORT (QUAI N°4) - AUBE / BRUME TROPICALE`
- **Ambiance Sonore (`AUD-02`)** : Corne de brume grave sur le fleuve, claquement des amarres métalliques, rumeur lointaine du Boulevard du 30 Juin.
- **Didascalie** : `CHR-PROTAG-KOFFI` saute sur le béton humide du quai en vérifiant dans sa poche son laissez-passer (`ITM-DOC-PASSEPORT`). Au bout de l'allée de conteneurs, deux vigiles de `ORG-CARTEL-FLEUVE` filtrent les dockers.
- **Dialogues Clés** :
  - **CHR-ALLY-AMINA** *(Radio, ton pressant)* : « Mbote Koffi ! Tu es enfin à terre ? Le général Mukendi a fait verrouiller tout le secteur nord du *libongo*. »
  - **CHR-PROTAG-KOFFI** *(Calme, observant les grues)* : « Malamu Amina. J'ai le papier d'ONATRA, et si ça chauffe, j'ai repéré une *Wewa* près de la grille est. Tɔ́kɛndɛ́. »
""",
    ),
    SkillBlueprint(
        skill_id="NAR-03",
        description=(
            "Conception biographique, psychologique, linguistique et relationnelle des personnages "
            "(CHR-*) et des familles/dynasties (FAM-*) de ZAÏRE. Définit la voix distinctive, les "
            "motivations, les failles et le registre de langue (français soutenu, français kinois, lingala)."
        ),
        inputs=("narrative-architecture-nar-01", "kinshasa-world-bible-wld-01", "cultural-guidelines-wld-02"),
        outputs=("character-bible-sheet.md", "family-lineage-dossier.md", "character-relationship-matrix.csv"),
        activation_triggers=(
            "Création d'un nouveau personnage principal, antagoniste, allié ou figure de quartier (`CHR-*`).",
            "Structuration d'une famille ou dynastie kinoise (`FAM-*`) et de son ancrage socio-économique.",
            "Relecture de conformité des voix de personnages sur un script produit par `NAR-02` ou `NAR-04`.",
        ),
        scope_boundaries=(
            "Ne définit pas la topologie 3D, les shaders de peau ou le système modulaire de vêtements (`ART-03`).",
            "Ne calibre pas les points de vie, dégâts ou arbres de comportement IA de combat (`GD-05`/`AI-01`).",
        ),
        operational_procedures=(
            "Attribuer un identifiant conforme `CHR-[ROLE]-[SLUG]` ou `FAM-[NOM]` et vérifier son unicité dans `knowledge/entities-registry.csv`.",
            "Ancrer le personnage dans une commune d'origine (`DST-*`) et une organisation ou famille existante.",
            "Définir sa **Signature Linguistique** (ratio français/lingala, rythme des phrases, vocabulaire métier, termes `LEX-*` privilégiés).",
            "Documenter son arc psychologique (Désir conscient vs Besoin profond vs Faille) dans `templates/character-bible-template.md`.",
        ),
        decision_rules=(
            ("Deux personnages majeurs partagent le même registre de langue et la même posture morale", "Différencier immédiatement leur sociolecte (ex: français technocratique de la Gombe vs phrasé imagé et musical de Matonge)", "Valider l'authenticité sociolinguistique avec WLD-02"),
            ("Personnage créé sans lien avec le tissu social ou familial de Kinshasa", "Rattacher le personnage à une famille (FAM-*), une faction (ORG-*) ou un lieu de vie (LOC-*)", "Interdire les archétypes génériques apatrides"),
            ("Incohérence de ton détectée dans un script NAR-02", "Émettre une demande de réécriture ciblée des répliques hors-caractère", "Consigner l'observation pour NAR-06"),
        ),
        acceptance_criteria=(
            "Chaque fiche `CHR-*` comporte une voix reconnaissable à l'aveugle sans lire le nom du locuteur.",
            "Les relations avec les autres `CHR-*`, `FAM-*` et `ORG-*` sont bidirectionnelles et explicites.",
            "Les recommandations vestimentaires et d'attitude fournissent un brief actionnable pour `ART-03` et `ART-06`.",
        ),
        validation_auditors=("WLD-02", "NAR-06", "DIR-06"),
        reference_filename="character-psychology-and-voice.md",
        reference_content="""# Méthodologie de Conception des Personnages Kinois (`NAR-03`)

## 1. Grille Socio-Linguistique de Kinshasa
- **Profil Élite Technocratique / Sécuritaire (`DST-GOMBE`, ex: `CHR-ANTAG-MUKENDI`)** : Syntaxe française froide, chirurgicale, usage rare mais tranchant du lingala d'autorité pour intimider.
- **Profil Artiste / Média Urbain (`DST-MATONGE`, ex: `CHR-ALLY-AMINA`)** : Débit vif, métaphores empruntées à la rumba et à la radio (`ORG-RADIO-KIN`), code-switching fluide et chaleureux.
- **Profil Artisan / Coursier de Terrain (`DST-KALAMU`, ex: `CHR-PROTAG-KOFFI`)** : Pragmatique, économe en mots sous pression, maîtrise des codes du port (`Libongo`) comme de la rue (`Wewa`).
""",
        template_filename="character-bible-template.md",
        template_content="""# Fiche Bible Personnage (`NAR-03`)

- **ID Registre** : `CHR-[ROLE]-[SLUG]`
- **Nom Complet** : `[Prénom Nom]`
- **Commune & Affiliation** : `DST-...` | `FAM-...` | `ORG-...`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Psychologie & Arc Dramatique
- **Désir Externe (Objectif)** : `[Objectif concret]`
- **Besoin Interne & Faille** : `[Conflit intérieur]`
- **Évolution (Acte I -> Acte III)** : `[Transformation]`

## 2. Signature Linguistique & Voix (`NAR-04` / `AUD-04`)
- **Registre dominant** : `[Français / Lingala / Code-switching]`
- **Expressions clés (`LEX-*`)** : `[Termes récurrents]`
- **Échantillon de 3 répliques étalons** :
  1. *(Calme)* : « `[Réplique]` »
  2. *(Conflit)* : « `[Réplique]` »
  3. *(Urgence)* : « `[Réplique]` »

## 3. Matrice Relationnelle
| Entité Liée (`CHR-*`/`ORG-*`) | Nature de la Relation | Tension Dramatique |
| :--- | :--- | :--- |
| `CHR-...` | `[Allié / Rival / Mentor]` | `[Enjeu]` |
""",
        example_filename="sample-character-bible.md",
        example_content="""# Exemple `NAR-03` — Fiche Bible de `CHR-PROTAG-KOFFI` (Koffi Kabongo)

- **ID Registre** : `CHR-PROTAG-KOFFI`
- **Nom Complet** : Koffi Kabongo
- **Commune & Affiliation** : `DST-KALAMU` | `FAM-KABONGO`
- **Statut** : `CONFIRMED`

## 1. Psychologie & Arc Dramatique
- **Désir Externe (Objectif)** : Sauver l'atelier mécanique familial de `FAM-KABONGO` à Kalamu de l'expropriation orchestrée par le consortium de `CHR-ANTAG-MUKENDI`.
- **Besoin Interne & Faille** : Ayant quitté Kinshasa pendant trois ans sur les barges du fleuve, Koffi croit pouvoir régler la crise en solitaire avant de comprendre qu'il doit fédérer sa communauté.
- **Évolution (Acte I -> Acte III)** : Du coursier solitaire naviguant dans la zone grise au catalyseur de la résistance citoyenne entre Kalamu, Matonge et la Gombe.

## 2. Signature Linguistique & Voix (`NAR-04` / `AUD-04`)
- **Registre dominant** : Français urbain kinois direct, ponctué de lingala pragmatique.
- **Expressions clés (`LEX-*`)** : `LEX-001 (Mbote)`, `LEX-003 (Malamu)`, `LEX-004 (Wewa)`, `LEX-006 (Libongo)`, `LEX-008 (Tɔ́kɛndɛ́)`.
- **Échantillon de 3 répliques étalons** :
  1. *(Calme)* : « Mbote papa. Laisse le moteur refroidir, je m'occupe de la courroie avant la pluie. »
  2. *(Conflit)* : « Tes hommes peuvent acheter les bureaux de la Gombe, Mukendi, mais pas les quais du *libongo*. »
  3. *(Urgence)* : « Kɛbá ! Accroche-toi à la *Wewa*, on coupe par le rond-point ! Tɔ́kɛndɛ́ ! »

## 3. Matrice Relationnelle
| Entité Liée | Nature de la Relation | Tension Dramatique |
| :--- | :--- | :--- |
| `CHR-ANTAG-MUKENDI` | Antagoniste principal | Mukendi détient les créances portuaires menaçant `FAM-KABONGO`. |
| `CHR-ALLY-AMINA` | Alliée stratégique & amie d'enfance | Amina pousse Koffi à exposer publiquement `ORG-CARTEL-FLEUVE` sur `ORG-RADIO-KIN`. |
""",
    ),
    SkillBlueprint(
        skill_id="NAR-04",
        description=(
            "Conception des arbres de dialogue interactifs, banques de répliques systémiques (barks "
            "de combat, foule, trafic) et métadonnées de mise en scène procédurale (tags d'émotion, "
            "cadrage caméra automatique, conditions Gameplay Tags)."
        ),
        inputs=("mission-scripts-nar-02", "character-bibles-nar-03", "quest-states-gd-02", "lingala-french-glossary.csv"),
        outputs=("dialogue-tree.json", "contextual-barks-table.csv"),
        activation_triggers=(
            "Implémentation des dialogues à choix multiples d'une mission (`MSN-*`) ou d'un commerçant/informateur.",
            "Création des banques de barks réactifs pour l'IA de combat (`AI-01`), la foule de Kinshasa (`AI-02`) ou le trafic (`AI-03`).",
            "Génération des métadonnées de caméra procédurale (méthodologie Ubisoft Quebec `SRC-014`) pour les quêtes secondaires.",
        ),
        scope_boundaries=(
            "Ne code pas le sous-système C++ de lecture de dialogues (`ENG-02`) ni la compilation binaire `.locres` (`AUD-04`).",
            "N'autorise aucune réplique dépassant **20 mots par bulle UI** afin de garantir la lisibilité et la tolérance d'expansion de +35 % (`AUD-04`/`PRD-06`).",
        ),
        operational_procedures=(
            "Structurer la conversation en noeuds atomiques identifiés (`node_id`), reliés par des conditions basées sur `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.",
            "Attacher à chaque noeud un tag d'émotion (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et une directive de caméra procédurale (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`).",
            "Prévoir systématiquement des répliques d'interruption et de reprise (`ON_INTERRUPT_COMBAT`, `ON_INTERRUPT_LEAVE`, `ON_RESUME`) pour éviter tout soft-lock en monde ouvert.",
            "Valider le fichier JSON généré en exécutant `scripts/validate_dialogue_json.py`.",
        ),
        decision_rules=(
            ("Réplique dépassant 20 mots dans un noeud de dialogue", "Scinder la réplique en 2 noeuds consécutifs ou condenser le texte", "Garantir la conformité au validateur validate_dialogue_json.py et aux normes XAG"),
            ("Noeud non terminal dépourvu de transition sortante (impasse)", "Relier le noeud à une sortie de repli valide ou marquer explicitement is_terminal: true", "Corriger avant tout handoff vers AUD-04 et ENG-02"),
            ("Dialogue de mission susceptible d'être interrompu par une averse ou une collision routière", "Ajouter les hooks système ON_INTERRUPT et ON_RESUME reliés à la machine à états GD-02", "Empêcher toute perte de progression narrative"),
        ),
        acceptance_criteria=(
            "`python skills/01-narrative/nar-04-dialogue-designer/scripts/validate_dialogue_json.py` valide le graphe avec 0 erreur.",
            "100 % des répliques font `<= 20 mots` et identifient le locuteur via un ID `CHR-*` valide.",
            "Les barks contextuels couvrent au moins 4 variations par déclencheur pour éviter la répétition auditive.",
        ),
        validation_auditors=("GD-02", "AUD-04", "NAR-06"),
        reference_filename="procedural-dialogue-staging.md",
        reference_content="""# Mise en Scène Procédurale & Architecture de Barks (`NAR-04`)

## 1. Pipeline de Cadrage Automatique (Inspiré d'Ubisoft GDC 2019 `SRC-014`)
Chaque ligne de dialogue porte deux métadonnées exploitées par le système caméra UE5 :
- `emotion_tag` : Pilote l'animation procédurale faciale/gestuelle (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`).
- `camera_framing` : Pilote la sélection de caméra virtuelle (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`).

## 2. Calibrage UI & Accessibilité (`PRD-06` / `AUD-04`)
- **Maximum 20 mots par noeud** (environ 110 caractères en français, laissant la marge de +35 % d'expansion multilingue sans troncature).
- **Préfixe Locuteur Obligatoire** : Exporté sous la forme `[KOFFI]` ou `[AMINA]` pour les sous-titres enrichis XAG.
""",
        template_filename="dialogue-tree-schema.json",
        template_content="""{
  "dialogue_id": "DLG-MSN-XXX-SLUG",
  "mission_id": "MSN-MAIN-001-ARRIVEE",
  "location_id": "LOC-GOMBE-PORT",
  "interrupt_handlers": {
    "on_combat_triggered": "BARK_INTERRUPT_COMBAT",
    "on_player_walk_away": "BARK_INTERRUPT_DISTANCE",
    "on_resume_conversation": "N01"
  },
  "nodes": [
    {
      "node_id": "N01",
      "speaker_id": "CHR-PROTAG-KOFFI",
      "line_text": "Mbote! Voici le laissez-passer ONATRA pour accéder au quai numéro quatre.",
      "emotion_tag": "WARM",
      "camera_framing": "OTS_LEFT",
      "required_gameplay_tag": "State.Character.Stealth.Disguised",
      "is_terminal": true,
      "next_nodes": []
    }
  ]
}
""",
        example_filename="sample-dialogue-and-barks.md",
        example_content="""# Exemple `NAR-04` — Dialogue & Barks de `MSN-MAIN-001-ARRIVEE`

## 1. Graphe de Dialogue Validé (`DLG-MSN-001-PORT.json`)
```json
{
  "dialogue_id": "DLG-MSN-001-PORT",
  "mission_id": "MSN-MAIN-001-ARRIVEE",
  "location_id": "LOC-GOMBE-PORT",
  "interrupt_handlers": {
    "on_combat_triggered": "BARK_CMB_ALERT_01",
    "on_player_walk_away": "BARK_WAIT_KOFFI_01",
    "on_resume_conversation": "N01"
  },
  "nodes": [
    {
      "node_id": "N01",
      "speaker_id": "CHR-PROTAG-KOFFI",
      "line_text": "Mbote vieux! J'ai le laissez-passer ONATRA pour le quai numéro quatre.",
      "emotion_tag": "WARM",
      "camera_framing": "OTS_LEFT",
      "required_gameplay_tag": "State.Character.Stealth.Disguised",
      "is_terminal": false,
      "next_nodes": ["N02"]
    },
    {
      "node_id": "N02",
      "speaker_id": "CHR-ALLY-AMINA",
      "line_text": "Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue principale. Tɔ́kɛndɛ́!",
      "emotion_tag": "URGENT",
      "camera_framing": "CLOSE_UP",
      "required_gameplay_tag": "",
      "is_terminal": true,
      "next_nodes": []
    }
  ]
}
```

## 2. Table de Barks Contextuels (`LOC-GOMBE-PORT` & `DST-MATONGE`)
| Bark ID | Catégorie IA | Déclencheur Gameplay Tag | Texte Français / Lingala (`<= 20 mots`) | Émotion |
| :--- | :--- | :--- | :--- | :--- |
| `BRK-PORT-01` | Garde `AI-01` | `State.Character.Stealth.Disguised` | « Papier ONATRA validé. Reste loin des grues du secteur nord, compris ? » | `TENSE` |
| `BRK-PORT-02` | Garde `AI-01` | `State.Character.Combat.Engaged` | « Kɛbá ! Un intrus près des conteneurs ! Verrouillez la grille du *libongo* ! » | `ANGRY` |
| `BRK-CROWD-01` | Citoyen `AI-02` | `Vehicle.Type.MotoWewa` | « Eh *Wewa* ! Attention aux flaques devant le rond-point Victoire ! » | `URGENT` |
| `BRK-CROWD-02` | Citoyen `AI-02` | `World.Weather.TropicalStorm` | « La pluie arrive fort sur Matonge, abritez les marchandises sous la tôle ! » | `URGENT` |
""",
        scripts={"validate_dialogue_json.py": VALIDATE_DIALOGUE_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="NAR-05",
        description=(
            "Gouvernance de l'encyclopédie canonique (Lore) de ZAÏRE, de la chronologie historique "
            "et fictionnelle, des dossiers d'organisations/factions (ORG-*) et des textes diégétiques "
            "urbains (émissions de Radio Lokole, enseignes peintes, presse, archives portuaires)."
        ),
        inputs=("kinshasa-world-bible-wld-01", "cultural-research-wld-02", "narrative-architecture-nar-01"),
        outputs=("organization-dossier.md", "diegetic-media-pack.md", "master-timeline.csv"),
        activation_triggers=(
            "Création ou enrichissement d'une faction, entreprise, syndicat ou média in-game (`ORG-*`).",
            "Rédaction de contenus diégétiques pour habiller l'environnement (`ART-02` : affiches, graffitis, enseignes) ou alimenter `ORG-RADIO-KIN` (`AUD-03`) et le téléphone de Koffi (`GD-07`).",
            "Vérification de la chronologie des événements précédant le début de l'Acte I.",
        ),
        scope_boundaries=(
            "N'invente jamais de faits historiques réels sur la RDC qui contrediraient les dossiers documentaires de `WLD-02`.",
            "Ne modifie pas la structure des quêtes principales (`GD-02`/`NAR-01`).",
        ),
        operational_procedures=(
            "Enregistrer toute nouvelle faction sous un identifiant `ORG-[TYPE]-[SLUG]` dans `knowledge/entities-registry.csv` au statut `PROPOSED`.",
            "Définir pour chaque organisation son territoire d'influence (`DST-*`), ses dirigeants (`CHR-*`), ses ressources économiques et son identité visuelle/sonore.",
            "Produire des textes diégétiques courts et percutants (bulletins flash de `ORG-RADIO-KIN` réagissant aux missions terminées, slogans d'enseignes pour `WLD-06`/`ART-02`).",
            "Vérifier l'alignement chronologique de chaque événement dans la ligne du temps maître.",
        ),
        decision_rules=(
            ("Besoin d'une référence à une institution réelle de Kinshasa", "Utiliser un équivalent fictionnel respectueux ou le statut RESEARCH_REQUIRED pour validation juridique PRD-02 et culturelle WLD-02", "Éviter tout risque de diffamation ou d'inexactitude"),
            ("Mission principale terminée par le joueur", "Générer systématiquement 2 variantes de bulletin radio (ORG-RADIO-KIN) correspondant aux 2 approches possibles du joueur", "Renforcer la réactivité du monde ouvert"),
            ("Texte d'enseigne urbaine destiné aux textures 3D (ART-02)", "Fournir le texte exact avec vérification orthographique française/lingala Unicode", "Empêcher toute faute de frappe gravée dans les textures PBR"),
        ),
        acceptance_criteria=(
            "Chaque dossier `ORG-*` est relié à au moins un quartier `DST-*` et un personnage `CHR-*`.",
            "La chronologie ne comporte aucun chevauchement ou paradoxe temporel.",
            "Les textes diégétiques respectent la charte linguistique (`cultural-guidelines.md`).",
        ),
        validation_auditors=("WLD-02", "NAR-06", "PRD-03"),
        reference_filename="lore-and-diegetic-media.md",
        reference_content="""# Architecture du Lore & Médias Diégétiques (`NAR-05`)

## 1. Factions & Organisations Clés (`ORG-*`)
- `ORG-CARTEL-FLEUVE` (**Syndicat du Fleuve**) : Consortium paramilitaire et logistique contrôlé par `CHR-ANTAG-MUKENDI` à `DST-GOMBE` (`LOC-GOMBE-PORT`).
- `ORG-TRANSCO` (**Réseau de Transport Urbain**) : Opérateur des grands bus structurant les axes routiers majeurs (`VEH-BUS-TRANSCO-01`).
- `ORG-RADIO-KIN` (**Radio Lokole 104.5 FM**) : Voix culturelle et citoyenne émettant depuis `DST-MATONGE`, animée par `CHR-ALLY-AMINA`.

## 2. Catégories de Médias Diégétiques
1. **Bulletins Radio Réactifs (`AUD-03`)** : Flashs de 15 à 25 secondes diffusés entre deux morceaux de rumba après chaque mission.
2. **Signalétique & Enseignes Peintes (`WLD-06`/`ART-02`)** : Textes d'ateliers mécaniques, salons de coiffure, ngandas et consignes portuaires.
""",
        template_filename="organization-dossier-template.md",
        template_content="""# Dossier d'Organisation Canonique (`NAR-05`)

- **ID Registre** : `ORG-[TYPE]-[SLUG]`
- **Nom Officiel** : `[Nom de l'Organisation]`
- **Quartier Général** : `LOC-...` (`DST-...`)
- **Dirigeant(s)** : `[CHR-*]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Mandat, Ressources & Influence Urbaine
- **Façade Publique** : `[Activité visible]`
- **Activité Réelle / Enjeu Ludique** : `[Rôle dans le conflit de ZAÏRE]`
- **Présence par Commune (`DST-*`)** : `[Répartition]`

## 2. Contenus Diégétiques Associés (Radio / Signalétique)
- **Flash Radio `ORG-RADIO-KIN`** : « `[Texte de 25 mots max]` »
- **Signalétique Environnementale (`ART-02`)** : `[Slogan / Panneau]`
""",
        example_filename="sample-organization-dossier.md",
        example_content="""# Exemple `NAR-05` — Dossier de `ORG-RADIO-KIN` (Radio Lokole 104.5 FM)

- **ID Registre** : `ORG-RADIO-KIN`
- **Nom Officiel** : Radio Lokole 104.5 FM — "La Voix du Carrefour"
- **Quartier Général** : `LOC-MATONGE-VICTOIRE` (`DST-MATONGE`)
- **Dirigeant(s)** : `CHR-ALLY-AMINA`
- **Statut** : `CONFIRMED`

## 1. Mandat, Ressources & Influence Urbaine
- **Façade Publique** : Station musicale indépendante diffusant le meilleur de la rumba congolaise, du ndombolo et des chroniques de quartier.
- **Activité Réelle / Enjeu Ludique** : Réseau d'alerte citoyenne et de partage d'informations permettant à `CHR-PROTAG-KOFFI` de suivre les mouvements de `ORG-CARTEL-FLEUVE` et l'évolution de `SYS-WLD-REPUTATION`.
- **Présence par Commune (`DST-*`)** : Écoutée dans 90 % des taxis (`VEH-TAXI-JAUNE-01`) et ngandas de `DST-MATONGE`, `DST-KALAMU` et `DST-LIMETE`.

## 2. Contenus Diégétiques Associés (Radio / Signalétique)
- **Flash Radio post-`MSN-MAIN-001-ARRIVEE`** : « Ici Amina sur Radio Lokole 104.5 ! Agitation inhabituelle ce matin au *libongo* de la Gombe où plusieurs grues ont été immobilisées. Conducteurs de *Wewa*, évitez l'accès nord du port ! »
- **Signalétique Environnementale (`ART-02`)** : Fresque murale peinte à Matonge : *"RADIO LOKOLE 104.5 FM — Sango ya solo, miziki ya mboka !"*
""",
    ),
    SkillBlueprint(
        skill_id="NAR-06",
        description=(
            "Contrôle qualité éditorial et audit anti-contradiction de ZAÏRE STUDIO OS. Vérifie la "
            "continuité narrative, temporelle, spatiale et d'état des personnages (vivant/mort/allié/hostile) "
            "entre toutes les missions (GD-02) et tous les livrables narratifs (NAR-01 à NAR-05)."
        ),
        inputs=("all-narrative-deliverables-nar-01-to-05", "mission-state-machines-gd-02", "knowledge/entities-registry.csv"),
        outputs=("continuity-audit-report.md", "narrative-conflict-tickets.csv"),
        activation_triggers=(
            "Avant toute promotion d'un livrable narratif (`NAR-01`..`NAR-05`) ou d'une mission (`GD-02`) au statut `CONFIRMED`.",
            "Modification d'un embranchement dans `NAR-01` ou d'une condition d'état dans `GD-02`.",
            "Audit de fin de vague (Strate 5 du DAG) commandé par `DIR-01`.",
        ),
        scope_boundaries=(
            "Ne réécrit jamais intégralement une scène ou une mission ; identifie précisément la contradiction et émet un ticket de correction vers le skill auteur.",
            "Ne valide jamais un livrable contenant une référence fantôme absente de `knowledge/entities-registry.csv`.",
        ),
        operational_procedures=(
            "Extraire tous les identifiants (`CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*`, `ITM-*`, `VEH-*`, `SYS-*`) cités dans le livrable et vérifier leur existence dans `knowledge/entities-registry.csv`.",
            "Contrôler la **Matrice d'États Temporels** : s'assurer qu'aucun personnage indisponible, arrêté ou hostile à l'étape $T$ n'apparaît comme donneur de quête amical à l'étape $T+1$ sans condition explicite.",
            "Vérifier la cohérence des registres de voix avec `NAR-03` et du lexique lingala avec `knowledge/world-bible/lingala-french-glossary.csv`.",
            "Émettre le verdict (`CONTINUITY_PASSED` ou `CONTINUITY_BLOCKED`) dans `templates/continuity-checklist.md`.",
        ),
        decision_rules=(
            ("Quête secondaire accessible alors que son donneur CHR-* est indisponible dans l'Acte courant", "Émettre un verdict CONTINUITY_BLOCKED et exiger de GD-02 l'ajout d'une précondition Gameplay Tag sur la machine à états", "Empêcher tout paradoxe narratif en monde ouvert"),
            ("Contradiction biographique ou territoriale entre deux fiches (ex: QG d'une faction situé dans deux communes différentes)", "Bloquer la promotion et renvoyer les deux fiches à NAR-03/NAR-05 pour alignement sur entities-registry.csv", "Noter le conflit dans narrative-conflict-tickets.csv"),
            ("Usage d'un terme lingala altéré sans ses caractères Unicode (ex: 'Tokende' au lieu de 'Tɔ́kɛndɛ́')", "Demander la normalisation orthographique immédiate selon lingala-french-glossary.csv", "Garantir la qualité LQA avec AUD-04"),
        ),
        acceptance_criteria=(
            "0 contradiction d'état de personnage, de lieu ou de chronologie sur l'ensemble du graphe de quêtes audité.",
            "100 % des IDs référencés dans les scripts et dialogues existent dans `knowledge/entities-registry.csv`.",
            "Conformité orthographique totale avec `knowledge/world-bible/lingala-french-glossary.csv`.",
        ),
        validation_auditors=("DIR-06", "DIR-07"),
        reference_filename="continuity-audit-rules.md",
        reference_content="""# Protocole d'Audit de Continuité & Anti-Paradoxe (`NAR-06`)

## 1. Les 4 Axes de Vérification Canonique
1. **Intégrité d'Entité** : Tout `CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*` cité existe dans `knowledge/entities-registry.csv` et n'est ni `DEPRECATED` ni `BLOCKED`.
2. **Cohérence d'État (State Continuity)** : Vérification des préconditions de quête (ex: `CHR-ALLY-AMINA` ne peut pas guider Koffi par radio si l'émetteur de `ORG-RADIO-KIN` est en panne dans la quête courante).
3. **Cohérence Spatiale & Temps de Trajet** : Un personnage ne peut pas se téléporter instantanément de `LOC-GOMBE-PORT` à `LOC-LIMETE-ECHANGEUR` au sein de la même scène.
4. **Cohérence Linguistique** : Respect des glyphes Unicode (`ɛ`, `ɔ`) et de la voix définie par `NAR-03`.
""",
        template_filename="continuity-checklist.md",
        template_content="""# Rapport d'Audit de Continuité Narrative (`NAR-06`)

- **Livrables Audités** : `[Liste des fichiers / IDs]`
- **Verdict de Continuité** : `CONTINUITY_PASSED` | `CONTINUITY_BLOCKED`
- **Auditeur** : `NAR-06 (Continuity Editor)`

## 1. Grille de Contrôle Croisé
| Axe d'Audit | Statut (`OK` / `CONFLICT`) | Détail / Entités Vérifiées |
| :--- | :--- | :--- |
| 1. Existence & Statut des IDs Registre | `OK` | `[IDs vérifiés]` |
| 2. États des Personnages (`CHR-*`) | `OK` | `[Aucun paradoxe d'état]` |
| 3. Cohérence Géographique (`DST-*`/`LOC-*`) | `OK` | `[Distances et communes cohérentes]` |
| 4. Glossaire Lingala Unicode (`LEX-*`) | `OK` | `[Glyphes ɛ, ɔ conformes]` |

## 2. Tickets de Correction Émis
- `[Aucun / Liste des correctifs requis avant promotion CONFIRMED]`
""",
        example_filename="sample-continuity-audit.md",
        example_content="""# Exemple `NAR-06` — Audit de Continuité sur `MSN-MAIN-001-ARRIVEE` & `DLG-MSN-001-PORT`

- **Livrables Audités** : `MSN-MAIN-001-ARRIVEE`, `DLG-MSN-001-PORT.json`, `CHR-PROTAG-KOFFI`, `ORG-RADIO-KIN`
- **Verdict de Continuité** : `CONTINUITY_PASSED`
- **Auditeur** : `NAR-06 (Continuity Editor)`

## 1. Grille de Contrôle Croisé
| Axe d'Audit | Statut | Détail / Entités Vérifiées |
| :--- | :--- | :--- |
| 1. Existence & Statut des IDs Registre | `OK` | `CHR-PROTAG-KOFFI`, `CHR-ALLY-AMINA`, `LOC-GOMBE-PORT`, `ITM-DOC-PASSEPORT`, `VEH-MOTO-WEWA-01` tous `CONFIRMED`. |
| 2. États des Personnages (`CHR-*`) | `OK` | `CHR-ALLY-AMINA` intervient uniquement par radio depuis `DST-MATONGE`, cohérent avec son rôle à `ORG-RADIO-KIN`. |
| 3. Cohérence Géographique (`DST-*`/`LOC-*`) | `OK` | Arrivée fluviale à `LOC-GOMBE-PORT` puis repli vers `DST-KALAMU` géographiquement exacts. |
| 4. Glossaire Lingala Unicode (`LEX-*`) | `OK` | Usage conforme de `LEX-001 (Mbote)`, `LEX-006 (Libongo)`, `LEX-007 (Kɛbá!)`, `LEX-008 (Tɔ́kɛndɛ́)`. |

## 2. Tickets de Correction Émis
- Aucun conflit détecté. Prêt pour signature `DIR-06` / `DIR-07`.
""",
    ),
)


def build_department_01(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 6 skills du département 01-narrative."""
    created: list[Path] = []
    for bp in NARRATIVE_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_01(WORKSPACE_ROOT)
    print(f"[OK] Département 01-narrative généré ({len(paths)} skills).")
