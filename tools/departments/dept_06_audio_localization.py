"""Spécifications et génération du Département 06-AUDIO-LOCALIZATION (AUD-01 à AUD-04)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_L10N_UNICODE_SCRIPT = '''"""Validateur Unicode Lingala (ɛ, ɔ) et budget d'expansion UI (+35 %) pour AUD-04."""

from __future__ import annotations

import argparse
import json
import sys


def validate_localization_entries(entries: list[dict]) -> list[str]:
    """Vérifie la présence des glyphes Unicode lingala, du préfixe locuteur XAG et l'expansion <= +35%."""
    errors: list[str] = []
    for item in entries:
        key = item.get("loc_key", "UNKNOWN")
        src_text = str(item.get("source_fr_cd", ""))
        target_text = str(item.get("target_text", ""))
        max_container_chars = int(item.get("ui_container_max_chars", 0))
        requires_open_vowels = bool(item.get("requires_lingala_open_vowels", False))
        is_subtitle = bool(item.get("is_subtitle", False))

        if not key or key == "TXT_MISSING":
            errors.append(f"Clé de localisation manquante ou invalide ({key!r}).")
        if requires_open_vowels and not ("ɛ" in src_text or "ɔ" in src_text or "ɛ" in target_text or "ɔ" in target_text):
            errors.append(f"Clé {key}: glyphes Unicode lingala ('ɛ' ou 'ɔ') manquants.")
        if is_subtitle and not (src_text.startswith("[") and "]" in src_text):
            errors.append(f"Clé {key}: sous-titre dépourvu du préfixe locuteur XAG (ex: '[KOFFI]').")
        required_budget = int(len(src_text) * 1.35)
        if max_container_chars < required_budget or len(target_text) > max_container_chars:
            errors.append(
                f"Clé {key}: risque de troncature UI (container={max_container_chars}, requis +35%={required_budget})."
            )

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide un lot de chaînes localisées (AUD-04).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de chaînes localisées à valider (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample_batch = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_batch = [
            {
                "loc_key": "SUB_MSN001_AMINA_02",
                "source_fr_cd": "[AMINA] : Kɛbá Koffi, les hommes de Mukendi contrôlent la grue ! Tɔ́kɛndɛ́ !",
                "target_text": "[AMINA] : Watch out Koffi, Mukendi's men already control the main crane! Let's go!",
                "ui_container_max_chars": 115,
                "requires_lingala_open_vowels": True,
                "is_subtitle": True,
            }
        ]
    errs = validate_localization_entries(sample_batch)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Lot de localisation AUD-04 validé (Unicode 'ɛ'/'ɔ', préfixe locuteur XAG et budget +35% OK).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

AUDIO_LOCALIZATION_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="AUD-01",
        description=(
            "Direction audio globale de ZAÏRE. Définit l'Audio Bible, la hiérarchie des bus de mixage "
            "HDR sous Audiokinetic Wwise, l'identité acoustique de chaque commune de Kinshasa (DST-*) "
            "et le respect strict du budget mémoire audio (<= 512 MB RAM, <= 64 voix physiques)."
        ),
        inputs=("creative-pillars-dir-03", "world-bible-wld-01", "cultural-research-wld-02"),
        outputs=("audio-bible-specification.md", "wwise-mixing-bus-hierarchy.md"),
        activation_triggers=(
            "Définition de la signature sonore d'une commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`, `DST-NGALIEMA`).",
            "Paramétrage des règles de priorité de mixage dynamique (HDR Audio / Side-Chaining) entre dialogues, indices critiques de combat et ambiances urbaines.",
            "Surveillance du budget `PERF-MEM-AUDIO` (`<= 512 MB` RAM, plafond de `64 voix physiques` simultanées).",
        ),
        scope_boundaries=(
            "Ne compose pas les pistes musicales (`AUD-03`) et ne développe pas le code C++ du moteur (`ENG-01`).",
            "Interdit que la musique diégétique ou le bruit du trafic ne masque un dialogue de quête ou le signal sonore d'une attaque ennemie (`GD-05`).",
        ),
        operational_procedures=(
            "Organiser la hiérarchie des bus maîtres Wwise selon 5 priorités décroissantes : (1) `BUS_VO_Critical` (Priorité 100), (2) `BUS_SFX_CombatTelegraph` (Priorité 90), (3) `BUS_Music_ScoreAndRadio` (Priorité 75), (4) `BUS_SFX_PlayerVehicle` (Priorité 70), (5) `BUS_Ambience_Kinshasa` (Priorité 50).",
            "Configurer le **Side-Chain Ducking HDR** : toute réplique sur `BUS_VO_Critical` abaisse automatiquement `BUS_Music_ScoreAndRadio` et `BUS_Ambience_Kinshasa` de `-6.0 dB` (temps d'attaque `40 ms`, relâchement `350 ms`).",
            "Fixer le plafond global à **64 voix physiques simultanées** avec bascule automatique en **Virtual Voices (`From Elapsed Time`)** pour toute source en dessous de `-48 dB`.",
            "Documenter la charte dans `templates/audio-bible-template.md`.",
        ),
        decision_rules=(
            ("Marché de Matonge générant plus de 64 sources sonores simultanées (foule + radios + motos Wewa)", "Agréger les voix de foule lointaines en un lit granulaire multicanal 5.1/7.1.4 (1 seule voix Wwise) et limiter les émetteurs individuels ponctuels aux 12 objets les plus proches", "Maintenir le plafond de 64 voix physiques et PERF-MEM-AUDIO <= 512 MB"),
            ("Dialogue radio d'Amina (CHR-ALLY-AMINA) couvert par le moteur de la Wewa en pleine course", "Activer un filtre High-Pass + boost de présence (2.5 kHz) sur le bus radio et abaisser le bus moteur véhicule de -4.5 dB pendant la réplique", "Garantir l'intelligibilité vocale à 100 %"),
            ("Dépassement de l'enveloppe RAM Audio (> 512 MB)", "Passer toutes les ambiances longues (> 8 secondes) et musiques de radio en Streaming Disk Wwise (Zero-Latency prefetch 64 KB) au lieu de chargement In-Memory", "Respecter le budget mémoire DIR-04"),
        ),
        acceptance_criteria=(
            "La cible de sonie globale est étalonnée à **`-23 LUFS` (±1 LU)** selon la norme broadcast EBU R128 / console AAA.",
            "Budget RAM Audio total `<= 512 MB` et voix physiques actives `<= 64` en stress test.",
            "Chaque commune `DST-*` possède son empreinte acoustique distincte documentée.",
        ),
        validation_auditors=("DIR-03", "DIR-04", "ENG-07"),
        reference_filename="wwise-hdr-and-bus-hierarchy.md",
        reference_content="""# Architecture Wwise HDR, Priorités de Mixage & Budgets (`AUD-01`)

## 1. Hiérarchie des Bus & Règles d'Atténuation (Ducking)
| Bus Wwise | Priorité | Cible LUFS | Ducking Appliqué sur Autres Bus | Stratégie Mémoire |
| :--- | :--- | :--- | :--- | :--- |
| `BUS_VO_Critical` | `100 (Max)` | `-20 LUFS` | `-6 dB` sur Musique & Ambiances, `-4.5 dB` sur Véhicules | Streamed + Prefetch `32 KB` |
| `BUS_SFX_CombatTelegraph` | `90` | `-18 LUFS Peak` | `-4 dB` sur Ambiances pendant Startup attaque `GD-05` | In-Memory (`Opus / ADPCM`) |
| `BUS_SFX_PlayerVehicle` | `75` | `-23 LUFS` | `-2 dB` sur Trafic IA distant | In-Memory (`Vorbis Q6`) |
| `BUS_Music_ScoreAndRadio` | `70` | `-24 LUFS` | Ducké par VO et Télégraphes Combat | Streamed + Prefetch `64 KB` |
| `BUS_Ambience_Kinshasa` | `50` | `-28 LUFS` | Ducké par tous les bus prioritaires | Streamed Multichannel |
""",
        template_filename="audio-bible-template.md",
        template_content="""# Spécification Audio Bible & Architecture Mixage (`AUD-01`)

- **Zone / Système** : `DST-...` | `SYS-...`
- **Budget RAM Audio Max** : `<= 512 MB`
- **Plafond Voix Physiques Wwise** : `<= 64 voix`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Signature Acoustique & Couches d'Ambiance
- **Fond Continu (Bed Quad/Ambisonic)** : `[Description]`
- **Ponctuels Spatialisés (3D One-Shots)** : `[Sources locales]`
- **Réverbération Spatiale (Wwise Late Reverb)** : `[RT60 & pré-délai]`

## 2. Règles de Mixage HDR & Ducking
- **Priorité Voix (`BUS_VO_Critical`)** : `[Règle d'atténuation]`
- **Signalétique Sonore Gameplay (`PRD-06` XAG)** : `[Indice audio distinctif]`
""",
        example_filename="sample-audio-bible.md",
        example_content="""# Exemple `AUD-01` — Audio Bible de `DST-GOMBE` (`LOC-GOMBE-PORT`) vs `DST-MATONGE`

- **Zone / Système** : `LOC-GOMBE-PORT` & `LOC-MATONGE-VICTOIRE`
- **Budget RAM Audio Max** : `385 MB` alloués (`<= 512 MB` requis)
- **Plafond Voix Physiques Wwise** : `48 voix moyennes / 64 max`
- **Statut** : `CONFIRMED`

## 1. Signature Acoustique & Couches d'Ambiance
- **`LOC-GOMBE-PORT` (Quais ONATRA)** :
  - *Bed Ambisonic* : Courant grave du fleuve Congo (`LEX-005 Ebale`), clapotis contre les coques métalliques des barges.
  - *Ponctuels 3D* : Grincement des câbles de grues, choc sourd des conteneurs ISO, mouettes fluviales.
  - *Réverbération* : `RT60 = 2.4 s` à l'intérieur du hangar N°4 (réflexions métalliques franches).
- **`LOC-MATONGE-VICTOIRE`** :
  - *Bed Ambisonic* : Murmure polyphonique chaleureux de foule, circulation dense.
  - *Ponctuels 3D* : Appels de chauffeurs taxis, coups de klaxon codés de `VEH-MOTO-WEWA-01`, diffusion spatialisée de `ORG-RADIO-KIN` depuis les terrasses de ngandas.

## 2. Règles de Mixage HDR & Ducking
- **Priorité Voix (`BUS_VO_Critical`)** : Ducking immédiat de `-6.0 dB` sur les enceintes des ngandas de Matonge dès qu'un dialogue de quête (`NAR-04`) débute.
- **Signalétique Sonore Gameplay (`PRD-06` XAG)** : L'attaque lourde imblocable de `ENM-CARTEL-BRUTE` (`GD-05`) déclenche un sifflement métallique montant à `1.8 kHz` sur `BUS_SFX_CombatTelegraph`, identifiable même sans indice visuel.
""",
    ),
    SkillBlueprint(
        skill_id="AUD-02",
        description=(
            "Conception des effets sonores (SFX), bruitages de combat (ITM-WPN-MACHETTE), moteurs "
            "de véhicules kinois (VEH-MOTO-WEWA-01), météo équatoriale et architecture acoustique "
            "spatiale sous Audiokinetic Wwise (RTPC, Random Containers, Spatial Audio Rooms & Portals) "
            "et UE5 MetaSounds."
        ),
        inputs=("audio-bible-aud-01", "combat-design-gd-05", "vehicle-specs-gd-06", "environment-briefs-wld-06"),
        outputs=("sfx-asset-catalog.csv", "wwise-rtpc-and-spatial-spec.md"),
        activation_triggers=(
            "Création des banques d'effets sonores pour un véhicule (`VEH-*`), une arme (`ITM-*`) ou une météo (`World.Weather.TropicalStorm`).",
            "Paramétrage des courbes RTPC (Real-Time Parameter Controls) reliant la physique UE5 Chaos (`ENG-05`) au moteur Wwise/MetaSounds.",
            "Configuration des volumes acoustiques `UAkRoomComponent` et `UAkPortalComponent` sur les bâtiments de `WLD-05`/`WLD-06`.",
        ),
        scope_boundaries=(
            "Ne gère pas la composition musicale (`AUD-03`) ni l'enregistrement des comédiens de doublage (`AUD-04`).",
            "Interdit tout effet sonore de pas, d'impact ou de moteur reposant sur un échantillon unique sans variation de hauteur (Pitch) et de conteneur aléatoire.",
        ),
        operational_procedures=(
            "Construire chaque événement SFX fréquent (pas sur latérite/béton, coups de machette, klaxons Wewa) sous forme d'un **Wwise Random/Blend Container** combinant au moins `6 échantillons` distincts avec randomisation de Pitch (`±120 cents`) et de filtre Low-Pass.",
            "Relier la pluie tropicale (`World.Weather.TropicalStorm`) à la nature physique du matériau touché (`ChaosPhysicalMaterial` : crépitement métallique aigu sur les toits en tôle `MI_Corrugated_Iron_Rust`, clapotis lourd sur les flaques du port, impact mat sur la boue latéritique).",
            "Configurer le moteur de la moto `VEH-MOTO-WEWA-01` via 3 RTPC continus : `RTPC_Veh_RPM` (`1000 - 9500 tr/min`), `RTPC_Veh_Load` (`0.0 - 1.0` couple accélération) et `RTPC_Surface_Wetness` (`0.0 - 1.0` sifflement de pneu sur bitume mouillé).",
            "Placer des `AkSpatialAudioVolume` (Rooms & Portals) sur toutes les ouvertures de hangars et de ngandas pour calculer dynamiquement la diffraction et l'occlusion.",
        ),
        decision_rules=(
            ("Effet sonore répétitif détecté (fatigue auditive sur le moteur Wewa ou la pluie sur tôle)", "Ajouter une modulation procédurale granulaire MetaSounds / Wwise LFO sur l'égalisation et croiser 3 couches de boucles asynchrones de longueurs premières entre elles", "Éliminer toute périodicité audible"),
            ("Son d'intérieur de hangar traversant un mur plein en béton sans atténuation", "Vérifier la fermeture hermétique du UAkRoomComponent et l'assignation du profil d'absorption acoustique Concrete_Heavy sur la géométrie WLD-05", "Corriger la fuite acoustique Spatial Audio"),
            ("Surcharge CPU due à 40 véhicules MassTraffic jouant chacun un synthétiseur moteur complet", "Limiter le modèle moteur 4-couches complet au véhicule du joueur et aux 3 véhicules les plus proches (< 25m) ; basculer le reste du trafic sur un bus d'ambiance routière global", "Préserver le budget CPU et le plafond de 64 voix AUD-01"),
        ),
        acceptance_criteria=(
            "100 % des événements SFX récurrents comportent `>= 6 variations` par surface (`PM_Asphalt_Dry`, `PM_Asphalt_Wet`, `PM_Laterite_Dry`, `PM_Laterite_Mud`).",
            "Les courbes RTPC sont bornées, lissées (Slew Rate / Interpolation) et reliées aux variables physiques de `GD-06`/`ENG-05`.",
            "La propagation intérieure/extérieure via Wwise Rooms & Portals est validée sans coupure brusque.",
        ),
        validation_auditors=("AUD-01", "ENG-07", "GD-05", "GD-06"),
        reference_filename="wwise-rtpc-and-spatial-audio.md",
        reference_content="""# Design Sonore Systémique : RTPC, Surfaces & Spatial Audio (`AUD-02`)

## 1. Mapping `ChaosPhysicalMaterial` -> Switch Group Wwise `SW_Surface_Type`
- `PM_Asphalt_Dry` -> `SW_Surface_Asphalt_Dry`
- `PM_Asphalt_Wet` -> `SW_Surface_Asphalt_Wet` (ajoute la couche d'éclaboussure haute fréquence)
- `PM_Laterite_Dry` -> `SW_Surface_Laterite_Dry` (crissement granuleux de terre sèche)
- `PM_Laterite_Mud` -> `SW_Surface_Laterite_Mud` (succion visqueuse de boue tropicale)
- `PM_Corrugated_Iron` -> `SW_Surface_SheetMetal` (résonance métallique caractéristique des toits kinois sous l'averse)
""",
        template_filename="wwise-rtpc-spec.md",
        template_content="""# Spécification SFX, RTPC & Spatial Audio Wwise (`AUD-02`)

- **ID Banque / Système** : `SB_[DOMAINE]_[SLUG]`
- **Bus Wwise Parent (`AUD-01`)** : `BUS_...`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Catalogue d'Événements Wwise & Variations
| Event Name (`Play_...`) | Type Conteneur | Variations Min | Pitch Random (cents) | Rayon Atténuation Max (cm) |
| :--- | :--- | :--- | :--- | :--- |
| `Play_...` | `Random / Blend` | `6` | `±120` | `[XXXX cm]` |

## 2. Matrice des Paramètres Temps Réel (RTPC / Switches)
| Nom RTPC / Switch | Source UE5 (`ENG-02`/`ENG-05`) | Plage Entrée | Paramètre Audio Piloté |
| :--- | :--- | :--- | :--- |
| `RTPC_...` | `[Variable C++/Chaos]` | `[Min - Max]` | `[Pitch / LPF / Volume dB]` |
""",
        example_filename="sample-sfx-wwise-spec.md",
        example_content="""# Exemple `AUD-02` — Spécification SFX de `VEH-MOTO-WEWA-01` & Pluie sur Tôle

- **ID Banque / Système** : `SB_VEH_MOTO_WEWA` & `SB_WEATHER_TROPICAL`
- **Bus Wwise Parent (`AUD-01`)** : `BUS_SFX_PlayerVehicle` & `BUS_Ambience_Kinshasa`
- **Statut** : `CONFIRMED`

## 1. Catalogue d'Événements Wwise & Variations
| Event Name | Type Conteneur | Variations Min | Pitch Random | Rayon Atténuation Max (cm) |
| :--- | :--- | :--- | :--- | :--- |
| `Play_Veh_Wewa_Engine_Loop` | `Blend Container (4 couches RPM)` | Synthèse continue + 4 boucles | Piloté par RTPC | `6500 cm (65 m)` |
| `Play_Veh_Wewa_Horn_Short` | `Random Container` | `8 coups de klaxon kinois` | `±80 cents` | `5000 cm (50 m)` |
| `Play_Cmb_Machete_Parry` | `Blend (Impact + Résonance lame)` | `8 impacts métalliques` | `±150 cents` | `3000 cm (30 m)` |
| `Play_Amb_Rain_SheetMetal_Roof` | `Granular MetaSound / Blend` | `3 boucles asynchrones` | `±50 cents` | `2500 cm (Local Portal)` |

## 2. Matrice des Paramètres Temps Réel (RTPC / Switches)
| Nom RTPC / Switch | Source UE5 | Plage Entrée | Paramètre Audio Piloté |
| :--- | :--- | :--- | :--- |
| `RTPC_Veh_Wewa_RPM` | `UChaosVehicleMovement::GetEngineRPM()` | `1100 - 9200` | Crossfade `Idle -> Low -> Mid -> High` + Pitch shift. |
| `RTPC_Weather_RainIntensity` | Tag `World.Weather.TropicalStorm` | `0.0 - 1.0` | Volume crépitement tôle (`-48 dB à 0 dB`) + niveau éclaboussures pneus. |
| `SW_Surface_Type` | `FHitResult::PhysMaterial` | 5 états | Sélectionne instantanément la couche de roulement/pas (Asphalte, Latérite, Boue, Tôle). |
""",
    ),
    SkillBlueprint(
        skill_id="AUD-03",
        description=(
            "Conception de la musique interactive adaptative (score dramatique par stems synchronisés "
            "sous Wwise Interactive Music) et programmation musicale de Radio Lokole 104.5 FM (ORG-RADIO-KIN : "
            "rumba congolaise, ndombolo, rap kinois) avec garantie d'un mode Streamer Safe 100 % libre de droits."
        ),
        inputs=("audio-bible-aud-01", "cultural-music-research-wld-02", "gameplay-states-gd-01-gd-05"),
        outputs=("interactive-music-specification.md", "radio-lokole-programming.csv"),
        activation_triggers=(
            "Conception des transitions musicales dynamiques entre exploration (`DST-*`), infiltration (`SYS-STEALTH`), combat (`SYS-CMB-MELEE`) et poursuite Wewa (`VEH-MOTO-WEWA-01`).",
            "Programmation de la grille musicale et des jingles de `ORG-RADIO-KIN` diffusés dans les véhicules et les ngandas de `DST-MATONGE`.",
            "Configuration du flag de conformité juridique `STREAMER_SAFE_FALLBACK` avec `PRD-02` (Risk Manager).",
        ),
        scope_boundaries=(
            "Ne gère pas les bruitages physiques d'environnement ou de véhicules (`AUD-02`).",
            "Interdit l'intégration de toute piste musicale sous licence commerciale tiers sans qu'une piste de remplacement interne (`Streamer Safe`) ne soit assignée dans le Switch Container Wwise.",
        ),
        operational_procedures=(
            "Structurer le score interactif en **4 Stems Verticaux Synchronisés** (`Stem_1_SubBass_Pulse`, `Stem_2_Percussion_Lokole`, `Stem_3_Sebene_Guitar_Tension`, `Stem_4_Brass_CombatFull`) pilotés par les Gameplay Tags (`State.Character.Stealth.Concealed`, `State.Character.Combat.Engaged`).",
            "Calibrer les règles de transition horizontale dans **Wwise Interactive Music Hierarchy** : transitions d'entrée en combat sur la **prochaine noire (`Next Beat`)** avec stinger percussif, transitions de sortie de combat sur la **prochaine mesure (`Next Bar`)**.",
            "Construire la grille de `ORG-RADIO-KIN` en alternant morceaux musicaux, jingles d'antenne et flashs d'information réactifs de `CHR-ALLY-AMINA` (`NAR-05`).",
            "Associer à chaque piste le booléen `bIsStreamerSafe` et son ID de fallback libre de droits dans `templates/radio-stations-programming.csv`.",
        ),
        decision_rules=(
            ("Superposition cacophonique entre le score dramatique non-diégétique et une radio diégétique de nganda à Matonge", "Lorsque le score de combat ou d'infiltration s'active, atténuer de -12 dB et appliquer un filtre Low-Pass (800 Hz) sur les sources musicales diégétiques environnantes", "Éviter tout conflit harmonique ou rythmique"),
            ("Option 'Mode Créateur / Streamer Safe' activée dans les paramètres du jeu", "Basculer le Switch Wwise SW_Music_LicenseMode sur STREAMER_SAFE, remplaçant 100 % des titres sous licence tiers par les compositions originales de rumba/ndombolo produites par le studio", "Garantir zéro strike DMCA (risque PRD-02)"),
            ("Bascule trop brusque entre exploration calme et combat lors d'une embuscade brève (< 6 secondes)", "Introduire un palier intermédiaire 'Tension/Alerte' (Stems 1+2+3) avant de déclencher le Stem 4 Cuivres/Sébène complet", "Maintenir une respiration musicale naturelle"),
        ),
        acceptance_criteria=(
            "Toutes les transitions d'état musical s'exécutent en synchronisation métrique (`Next Beat` ou `Next Bar`) sans clic ni coupe brute.",
            "100 % des pistes de `ORG-RADIO-KIN` disposent d'un statut de licence vérifié et d'un fallback `Streamer Safe`.",
            "Respect des structures musicales authentiques congolaises documentées par `WLD-02`.",
        ),
        validation_auditors=("AUD-01", "WLD-02", "PRD-02"),
        reference_filename="interactive-music-and-radio.md",
        reference_content="""# Architecture Wwise Interactive Music & Radio Lokole (`AUD-03`)

## 1. Matrice d'Activation des Stems par Gameplay Tag
| État Gameplay (`FGameplayTag`) | Stem 1 (Pulse) | Stem 2 (Percus Congolaises) | Stem 3 (Guitare Mi-Solo) | Stem 4 (Sébène / Cuivres) | Règle Transition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Exploration Libre** | Muets (Priorité Radio/Ville) | Muet | Muet | Muet | Fondu `2.0 s` |
| `State.Character.Stealth.Concealed` | **Actif (`0 dB`)** | Actif (`-6 dB`, filtré) | Muet | Muet | `Next Bar` |
| **Alerte / Poursuite Wewa** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | Muet | `Next Beat` + Stinger |
| `State.Character.Combat.Engaged` | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | `Next Beat` + Impact |
""",
        template_filename="radio-stations-programming.csv",
        template_content="""track_id,station_id,title,genre,bpm,time_signature,license_type,streamer_safe_fallback_id,trigger_condition,status
MUS_SCORE_PORT_STEALTH_01,NON_DIEGETIC_SCORE,Brume sur l'ONATRA (4 Stems),Afro-Cinematic Tension,98,4/4,STUDIO_ORIGINAL,SELF,LOC-GOMBE-PORT,CONFIRMED
MUS_RAD_LOKOLE_RUMBA_01,ORG-RADIO-KIN,Soleil de Victoire,Rumba Congolaise / Sébène,112,4/4,STUDIO_ORIGINAL,SELF,World.District.Matonge,CONFIRMED
MUS_RAD_LOKOLE_NDOMBOLO_02,ORG-RADIO-KIN,Wewa Express,Ndombolo Urbain,126,4/4,LICENSED_THIRD_PARTY,MUS_RAD_LOKOLE_RUMBA_01,Vehicle.Type.MotoWewa,CONFIRMED
""",
        example_filename="sample-interactive-music-spec.md",
        example_content="""# Exemple `AUD-03` — Score Interactif `MSN-MAIN-001-ARRIVEE` & Grille `ORG-RADIO-KIN`

## 1. Score Adaptatif de `LOC-GOMBE-PORT` (`MUS_SCORE_PORT_STEALTH_01`)
- **Tempo & Signature** : `98 BPM`, `4/4` (Grid Wwise synchronisée à la double-croche).
- **Couches Actives par Phase de `MSN-MAIN-001-ARRIVEE`** :
  1. *Approche en barge & Quai (`State.Character.Stealth.Disguised`)* : Nappe grave analogique + percussions bois *lokole* feutrées (`Stem 1 + Stem 2 à -6 dB`).
  2. *Infiltration Hangar N°4 (`State.Character.Stealth.Concealed`)* : Entrée d'une basse fretless syncopée sur la mesure suivante (`Next Bar`).
  3. *Combat ou Exfiltration en `VEH-MOTO-WEWA-01`* : Déclenchement sur le temps suivant (`Next Beat`) de la guitare sébène électrique rapide et des cuivres (`Stem 3 + Stem 4`).

## 2. Programmation `ORG-RADIO-KIN` & Conformité Streamer Safe
- Chaque piste `LICENSED_THIRD_PARTY` pointe vers une composition originale `STUDIO_ORIGINAL` (`MUS_RAD_LOKOLE_RUMBA_01`) activée instantanément lorsque `SW_Music_LicenseMode = STREAMER_SAFE`.
""",
    ),
    SkillBlueprint(
        skill_id="AUD-04",
        description=(
            "Ingénierie de localisation (i18n/L10n) sous UE5 Localization Dashboard (.po/.locres), "
            "direction du doublage vocal multilingue (fr-CD, ln-CD, en-US) et contrôle LQA. Garantit "
            "la préservation des glyphes Unicode du lingala (ɛ, ɔ), le préfixe locuteur XAG ([KOFFI]) "
            "et la tolérance d'expansion de texte de +35 %."
        ),
        inputs=("dialogue-trees-nar-04", "ui-screen-specs-gd-07", "lingala-glossary-wld-02"),
        outputs=("localization-pipeline-spec.md", "localized-string-table.csv"),
        activation_triggers=(
            "Intégration et traduction des graphes de dialogue (`NAR-04`) et des chaînes d'interface utilisateur (`GD-07`).",
            "Préparation des scripts d'enregistrement vocal (Voice-Over) avec indications phonétiques pour le français de RDC (`fr-CD`) et le lingala (`ln-CD`).",
            "Exécution du contrôle automatisé `scripts/check_l10n_unicode.py` avant tout String Freeze.",
        ),
        scope_boundaries=(
            "Ne modifie jamais l'intention dramatique ou les embranchements de quête (`NAR-01`/`NAR-02`/`GD-02`).",
            "Interdit toute chaîne codée en dur (hardcoded string) hors des `FText` / `LOCTEXT` et des String Tables UE5.",
        ),
        operational_procedures=(
            "Assigner à chaque réplique ou texte UI une clé unique immuable au format `[CAT]_[MSN/UI]_[SPEAKER]_[NUM]` (ex: `SUB_MSN001_AMINA_02`).",
            "Préfixer systématiquement chaque chaîne de sous-titre par le nom du locuteur entre crochets (`[KOFFI] : ...`, `[AMINA] : ...`) conformément aux normes d'accessibilité XAG (`PRD-06`).",
            "Vérifier que les termes du glossaire `knowledge/world-bible/lingala-french-glossary.csv` conservent leurs caractères Unicode exacts (`ɛ` U+025B, `ɔ` U+0254) dans toutes les langues cibles.",
            "Exécuter `scripts/check_l10n_unicode.py` pour certifier l'absence de `TXT_MISSING` et la réserve d'expansion de `+35 %` sur chaque conteneur UI (`GD-07`).",
        ),
        decision_rules=(
            ("Terme culturel kinois (ex: Wewa, Libongo, Nganda, Mbote) rencontré lors de la traduction vers l'anglais (en-US)", "Conserver le terme kinois d'origine en italique dans le dialogue anglais lorsque le contexte visuel est explicite, ou utiliser la tournure naturelle du glossaire WLD-02", "Préserver la couleur locale authentique de Kinshasa en version internationale"),
            ("Chaîne traduite dépassant la limite de caractères du widget Common UI", "Alerter GD-07 pour élargir la boîte ou reformuler la traduction sous le plafond de +35 % validé par check_l10n_unicode.py", "Éliminer 100 % des troncatures de texte"),
            ("Police de caractères de secours (fallback font) remplaçant 'ɛ' ou 'ɔ' par un carré vide (tofu □)", "Bloquer le build LQA et imposer l'inclusion des plages Unicode Latin Extended-B (U+0180..U+024F) et IPA Extensions (U+0250..U+02AF) dans l'asset UFont UE5", "Garantir un rendu typographique irréprochable"),
        ),
        acceptance_criteria=(
            "`python skills/06-audio-localization/aud-04-voice-localization-specialist/scripts/check_l10n_unicode.py` retourne un code `0`.",
            "0 clé manquante (`TXT_MISSING`) et 0 caractère corrompu sur `ɛ` / `ɔ`.",
            "100 % des sous-titres incluent le préfixe locuteur `[NOM]` et un timecode synchronisé avec `ART-06`.",
        ),
        validation_auditors=("PRD-04", "PRD-06", "WLD-02"),
        reference_filename="ue5-localization-and-vo-pipeline.md",
        reference_content=r"""# Pipeline UE5 Localization Dashboard & Doublage (`AUD-04`)

## 1. Locales Supportées & Règles de Transcréation
- **`fr-CD` (Locale Native Maîtresse)** : Français de Kinshasa avec code-switching naturel en lingala (`LEX-001` à `LEX-012`).
- **`ln-CD` (Doublage & Sous-titres Lingala Complet)** : Version intégrale en lingala kinois utilisant l'alphabet Unicode normalisé (`a, e, ɛ, i, o, ɔ, u`).
- **`en-US` / `en-GB` (Internationalisation)** : Sous-titres et doublage anglais conservant les marqueurs identitaires (*Mbote*, *Wewa*, *Nganda*) accompagnés d'un contexte limpide.

## 2. Formule de Budget d'Expansion UI (`GD-07` <-> `AUD-04`)
$$\text{Capacité Conteneur UI (chars)} \ge \lceil \text{Longueur}(\text{Source}_{fr-CD}) \times 1.35 \rceil$$
""",
        template_filename="localized-string-table.csv",
        template_content="""loc_key,speaker_id,source_fr_cd,target_ln_cd,target_en_us,phonetic_vo_note,ui_container_max_chars,status
SUB_MSN001_KOFFI_01,CHR-PROTAG-KOFFI,"[KOFFI] : Mbote vieux ! J'ai le laissez-passer ONATRA pour le quai numéro quatre.","[KOFFI] : Mbote kulutu! Nazali na mokanda ya ONATRA mpo na libongo ya minei.","[KOFFI] : Mbote boss! I've got the ONATRA pass for dock number four.",m-BO-te / li-BO-ngo,120,CONFIRMED
SUB_MSN001_AMINA_02,CHR-ALLY-AMINA,"[AMINA] : Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue ! Tɔ́kɛndɛ́ !","[AMINA] : Kɛbá Koffi, bato ya Mukendi bakangi déjà grue! Tɔ́kɛndɛ́!","[AMINA] : Kɛbá Koffi, Mukendi's men already control the main crane! Let's move!",KE-ba / to-KEN-de,120,CONFIRMED
""",
        example_filename="sample-localization-spec.md",
        example_content="""# Exemple `AUD-04` — Table de Localisation & Doublage de `MSN-MAIN-001-ARRIVEE`

## 1. Validation Automatisée (`scripts/check_l10n_unicode.py`)
- **Clés vérifiées** : `SUB_MSN001_KOFFI_01`, `SUB_MSN001_AMINA_02`, `UI_OBJ_MSN001_ST01`
- **Glyphes Unicode (`ɛ`, `ɔ`)** : Présents et intègres en UTF-8 (`Kɛbá`, `Tɔ́kɛndɛ́`).
- **Marge d'Expansion UI (+35 %)** : Chaîne source max = `79 chars` -> Requis `+35 %` = `107 chars` -> Conteneur UI configuré à `120 chars` (**CONFORME**).

## 2. Extrait de la String Table Multilingue (`localized-string-table.csv`)
| Clé Localisation | Locuteur | Texte Source (`fr-CD`) | Adaptation Lingala (`ln-CD`) | Adaptation Anglaise (`en-US`) |
| :--- | :--- | :--- | :--- | :--- |
| `SUB_MSN001_KOFFI_01` | `CHR-PROTAG-KOFFI` | `[KOFFI] : Mbote vieux ! J'ai le laissez-passer ONATRA pour le quai numéro quatre.` | `[KOFFI] : Mbote kulutu! Nazali na mokanda ya ONATRA mpo na libongo ya minei.` | `[KOFFI] : Mbote boss! I've got the ONATRA pass for dock number four.` |
| `SUB_MSN001_AMINA_02` | `CHR-ALLY-AMINA` | `[AMINA] : Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue ! Tɔ́kɛndɛ́ !` | `[AMINA] : Kɛbá Koffi, bato ya Mukendi bakangi déjà grue! Tɔ́kɛndɛ́!` | `[AMINA] : Kɛbá Koffi, Mukendi's men already control the main crane! Let's move!` |
""",
        scripts={"check_l10n_unicode.py": CHECK_L10N_UNICODE_SCRIPT},
    ),
)


def build_department_06(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 4 skills du département 06-audio-localization."""
    created: list[Path] = []
    for bp in AUDIO_LOCALIZATION_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_06(WORKSPACE_ROOT)
    print(f"[OK] Département 06-audio-localization généré ({len(paths)} skills).")
