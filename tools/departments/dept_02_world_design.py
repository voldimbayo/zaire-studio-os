"""Spécifications et génération du Département 02-WORLD-DESIGN (WLD-01 à WLD-06)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_METRICS_SCRIPT = '''"""Validateur de métriques spatiales de blockout Level Design pour WLD-05."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def validate_blockout_metrics(spec: dict) -> list[str]:
    """Vérifie la conformité d'un blockout aux gabarits UE5 de spatial-metrics.md."""
    errors: list[str] = []
    min_corridor = float(spec.get("min_corridor_width_cm", 0))
    ceiling = float(spec.get("min_ceiling_height_cm", 0))
    low_cover = float(spec.get("low_cover_height_cm", 0))
    high_cover = float(spec.get("high_cover_height_cm", 0))
    wewa_gap = float(spec.get("min_wewa_lane_gap_cm", 0))

    if min_corridor < 350.0:
        errors.append(f"Largeur couloir ({min_corridor} cm) < minimum requis 350 cm (risque collision caméra).")
    if ceiling < 320.0:
        errors.append(f"Hauteur sous plafond ({ceiling} cm) < minimum requis 320 cm.")
    if not (90.0 <= low_cover <= 110.0):
        errors.append(f"Hauteur couvert bas ({low_cover} cm) hors plage [90, 110] cm (cible 100 cm).")
    if high_cover < 200.0:
        errors.append(f"Hauteur couvert haut ({high_cover} cm) < minimum requis 200 cm.")
    if wewa_gap < 130.0:
        errors.append(f"Passage inter-file moto Wewa ({wewa_gap} cm) < minimum requis 130 cm.")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide les métriques spatiales d'un blockout WLD-05.")
    parser.add_argument("--file", help="Fichier JSON de métriques blockout (optionnel)")
    args = parser.parse_args()

    if args.file:
        payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        payload = {
            "blockout_id": "BLK-GOMBE-PORT-01",
            "location_id": "LOC-GOMBE-PORT",
            "min_corridor_width_cm": 400.0,
            "min_ceiling_height_cm": 360.0,
            "low_cover_height_cm": 100.0,
            "high_cover_height_cm": 220.0,
            "min_wewa_lane_gap_cm": 150.0,
        }

    errs = validate_blockout_metrics(payload)
    if errs:
        for err in errs:
            print(f"[ERREUR] {err}")
        return 1
    print(f"[OK] Blockout {payload.get('blockout_id')} conforme à 100% aux métriques spatiales UE5.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

WORLD_DESIGN_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="WLD-01",
        description=(
            "Conception macroscopique du monde de Kinshasa dans ZAÏRE. Définit l'identité socio-économique, "
            "architecturale, sécuritaire et sensorielle de chaque commune (DST-*), leurs frontières et "
            "leurs interactions systémiques dans la World Bible."
        ),
        inputs=("creative-pillars-dir-03", "cultural-research-wld-02", "urban-morphology-wld-03"),
        outputs=("district-profile.md", "kinshasa-world-bible-update.md"),
        activation_triggers=(
            "Création ou mise à jour du profil d'une commune de Kinshasa (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`, `DST-NGALIEMA`, `DST-MASINA`).",
            "Définition des contrastes sociaux, économiques et de présence des factions (`ORG-*`) entre deux quartiers.",
            "Cadrage initial avant le découpage spatial Open World (`WLD-04`) et l'écriture des arcs d'actes (`NAR-01`).",
        ),
        scope_boundaries=(
            "Ne réalise pas le placement précis des Points d'Intérêt sur la grille World Partition (`WLD-04`) ni le blockout 3D (`WLD-05`).",
            "N'invente aucune donnée démographique ou topographique sans validation préalable par `WLD-02` et `WLD-03`.",
        ),
        operational_procedures=(
            "Enregistrer ou vérifier l'identifiant `DST-[COMMUNE]` dans `knowledge/entities-registry.csv` et `knowledge/world-bible/kinshasa-districts.md`.",
            "Spécifier les 4 couches identitaires de la commune : (1) Sociologie & Économie, (2) Morphologie & Verticalité, (3) Signature Visuelle & Sonore, (4) Factions & Gameplay dominant.",
            "Associer le Gameplay Tag de territoire (`World.District.*` dans `knowledge/technical-specs/gameplay-tags-taxonomy.csv`).",
            "Générer la fiche complète selon `templates/district-profile-template.md`.",
        ),
        decision_rules=(
            ("Commune dont les données SIG secondaires sont incomplètes (ex: DST-MASINA)", "Maintenir explicitement le statut RESEARCH_REQUIRED sur les sous-secteurs non vérifiés", "Transmettre une requête ciblée à WLD-03"),
            ("Deux communes présentent la même densité de foule et la même ambiance visuelle", "Accentuer le contraste structurel (ex: tours administratives et port industriel de Gombe vs galeries musicales et marchés nocturnes de Matonge)", "Faire valider la différenciation par DIR-03 et ART-01"),
            ("Introduction d'une nouvelle faction dans un quartier", "Vérifier la cohérence territoriale avec NAR-05 et mettre à jour les dépendances dans entities-registry.csv", "Soumettre à DIR-06"),
        ),
        acceptance_criteria=(
            "Chaque fiche `DST-*` définit clairement ses communes limitrophes, son landmark directeur (`LOC-*`) et ses densités cibles de foule/trafic.",
            "Alignement total avec `knowledge/world-bible/kinshasa-districts.md` et `cultural-guidelines.md`.",
            "Validation créative obtenue auprès de `DIR-03`.",
        ),
        validation_auditors=("WLD-02", "WLD-03", "DIR-03"),
        reference_filename="kinshasa-macro-worldbuilding.md",
        reference_content="""# Principes de Worldbuilding Macroscopique — Kinshasa (`WLD-01`)

## 1. Contraste des Strates Urbaines
- **Axe Fluvial & Institutionnel (`DST-GOMBE`)** : Pouvoir financier, ambassades, port lourd ONATRA (`LOC-GOMBE-PORT`), boulevards à 2x3 voies (`LOC-GOMBE-BD30JUIN`).
- **Cœur Culturel & Commercial (`DST-MATONGE` / `DST-KALAMU`)** : Économie créative, studios, ngandas, marchés denses, ateliers mécaniques (`FAM-KABONGO`).
- **Colonne Vertébrale Industrielle (`DST-LIMETE`)** : Usines, dépôts logistiques, carrefour monumental de la Tour de l'Échangeur (`LOC-LIMETE-ECHANGEUR`).
- **Flancs Fluviaux Occidentaux (`DST-NGALIEMA`)** : Relief prononcé, rapides de Kinsuka, carrières et zones résidentielles.
""",
        template_filename="district-profile-template.md",
        template_content="""# Profil de Commune — World Bible (`WLD-01`)

- **ID Registre** : `DST-[COMMUNE]`
- **Nom de la Commune** : `[Nom]`
- **Gameplay Tag Associé** : `World.District.[Nom]`
- **Statut** : `CONFIRMED` | `PROPOSED` | `RESEARCH_REQUIRED`

## 1. Identité Socio-Économique & Factions
- **Profil Social & Activités** : `[Description]`
- **Factions Dominantes (`ORG-*`)** : `[Liste]`
- **Landmark Directeur (`LOC-*`)** : `LOC-...`

## 2. Paramètres de Simulation & Ambiance
- **Densité Foule (`AI-02`)** : `[Jour / Nuit]`
- **Profil Trafic (`AI-03`)** : `[Types de véhicules VEH-*]`
- **Signature Visuelle (`ART-01`) & Sonore (`AUD-01`)** : `[Synthèse]`
""",
        example_filename="sample-district-profile.md",
        example_content="""# Exemple `WLD-01` — Profil de `DST-MATONGE` (Quartier Matonge)

- **ID Registre** : `DST-MATONGE`
- **Nom de la Commune** : Quartier Matonge (Commune de Kalamu)
- **Gameplay Tag Associé** : `World.District.Matonge`
- **Statut** : `CONFIRMED`

## 1. Identité Socio-Économique & Factions
- **Profil Social & Activités** : Épicentre culturel, musical et commercial de Kinshasa. Terrasses de ngandas, disquaires, tailleurs de la Sape, marchés vivriers et studio de `ORG-RADIO-KIN`.
- **Factions Dominantes (`ORG-*`)** : `ORG-RADIO-KIN` (alliés citoyens), collecteurs informels liés à `ORG-CARTEL-FLEUVE`.
- **Landmark Directeur (`LOC-*`)** : `LOC-MATONGE-VICTOIRE` (Place du Rond-Point Victoire).

## 2. Paramètres de Simulation & Ambiance
- **Densité Foule (`AI-02`)** : Très haute de jour comme de nuit (500 à 600+ entités Mass Crowd).
- **Profil Trafic (`AI-03`)** : Concentration maximale de taxis `VEH-TAXI-JAUNE-01` et de motos-taxis `VEH-MOTO-WEWA-01`.
- **Signature Visuelle (`ART-01`) & Sonore (`AUD-01`)** : Façades basses vibrantes, enseignes peintes, néons chauds nocturnes et diffusion polyphonique de rumba/ndombolo.
""",
    ),
    SkillBlueprint(
        skill_id="WLD-02",
        description=(
            "Recherche culturelle, historique, linguistique, vestimentaire et musicale sur Kinshasa et "
            "la République Démocratique du Congo. Maintient le glossaire Lingala/Français Unicode (ɛ, ɔ) "
            "et garantit l'absence totale de clichés ou d'anachronismes."
        ),
        inputs=("research-requests", "knowledge/world-bible/cultural-guidelines.md", "knowledge/world-bible/lingala-french-glossary.csv"),
        outputs=("cultural-research-brief.md", "glossary-expansion-entries.csv"),
        activation_triggers=(
            "Demande de vérification culturelle ou linguistique émise par un skill ayant rencontré un point `RESEARCH_REQUIRED`.",
            "Validation des expressions en lingala / français kinois utilisées dans les scripts (`NAR-02`), dialogues (`NAR-04`) et doublages (`AUD-04`).",
            "Documentation des tenues vestimentaires (`ART-03`), genres musicaux (`AUD-03`) et codes sociaux quotidiens de Kinshasa.",
        ),
        scope_boundaries=(
            "Ne conçoit pas les règles de gameplay (`GD-01`) ni l'équilibrage mathématique (`GD-03`).",
            "N'extrapole jamais un fait historique ou linguistique incertain : si une source primaire manque, le point reste marqué `RESEARCH_REQUIRED`.",
        ),
        operational_procedures=(
            "Consulter `knowledge/world-bible/cultural-guidelines.csv`, `lingala-french-glossary.csv` et `research/source-registry.csv`.",
            "Fournir des références anthropologiques, linguistiques et urbaines précises (ex: travaux de Filip De Boeck sur Kinshasa, structure de la rumba congolaise, terminologie fluviale).",
            "Pour chaque nouveau terme lingala introduit, spécifier sa graphie Unicode exacte (`ɛ`, `ɔ` et tons), son indice phonétique pour les comédiens (`AUD-04`), son registre et son sens en français et anglais.",
            "Rédiger le dossier dans `templates/cultural-brief-template.md`.",
        ),
        decision_rules=(
            ("Terme argotique ou culturel d'origine incertaine ou non attesté à Kinshasa", "Rejeter le terme et proposer une alternative attestée de lingala kinois ou marquer RESEARCH_REQUIRED", "Protéger l'authenticité culturelle du jeu"),
            ("Texte en lingala soumis avec des caractères ASCII dégradés ('e'/'o' au lieu de 'ɛ'/'ɔ')", "Corriger systématiquement la graphie Unicode et mettre à jour lingala-french-glossary.csv", "Synchroniser avec AUD-04 et GD-07"),
            ("Représentation vestimentaire ou architecturale caricaturale", "Émettre une directive corrective immédiate appuyée sur la réalité urbaine contemporaine de Kinshasa", "Escalader à DIR-03 en cas de blocage"),
        ),
        acceptance_criteria=(
            "100 % des termes lingala fournis incluent la graphie Unicode (`ɛ`, `ɔ`), la phonétique et le contexte d'usage.",
            "Les sources documentaires sont citées et exemptes de tout stéréotype 'Afrique générique'.",
            "Le brief culturel est directement exploitable par `NAR-02`, `NAR-04`, `ART-02`, `ART-03` et `AUD-03`.",
        ),
        validation_auditors=("PRD-03", "DIR-03", "DIR-06"),
        reference_filename="kinshasa-cultural-reference.md",
        reference_content="""# Référentiel Socio-Culturel & Linguistique de Kinshasa (`WLD-02`)

## 1. Phonologie & Orthographe Unicode du Lingala Kinois
Le système vocalique du lingala distingue 7 voyelles : `a, e, ɛ, i, o, ɔ, u`.
- `ɛ` (U+025B — *e ouvert*, comme dans *Kɛbá!*, *Tɔ́kɛndɛ́*).
- `ɔ` (U+0254 — *o ouvert*, comme dans *Tɔ́kɛndɛ́*, *Bilɔkɔ*).
Toute chaîne destinée à l'interface UE5 (`GD-07`) ou aux sous-titres (`AUD-04`) doit préserver ces points de code UTF-8.

## 2. Repères Sociologiques Contemporains
- **Mobilité Urbaine** : Coexistence des grands bus (`ORG-TRANSCO`), des taxis collectifs jaunes (*Ketchs*, `VEH-TAXI-JAUNE-01`) et des motos-taxis (*Wewa*, `VEH-MOTO-WEWA-01`).
- **Sociabilité** : Les *ngandas* (`LEX-011`) de Matonge et Kalamu servent de carrefours d'information, de débat et de diffusion musicale.
""",
        template_filename="cultural-brief-template.md",
        template_content="""# Dossier de Recherche Culturelle & Linguistique (`WLD-02`)

- **ID Dossier** : `CUL-2026-NNN`
- **Commune / Sujet** : `[DST-* / Thème]`
- **Skills Destinataires** : `[NAR-* / ART-* / AUD-*]`
- **Statut de Vérification** : `CONFIRMED` | `RESEARCH_REQUIRED`

## 1. Synthèse Factuelle & Codes Sociaux
`[Description détaillée et sourcée]`

## 2. Entrées Lexicales Certifiées (`lingala-french-glossary.csv`)
| ID Terme | Graphie Unicode | Phonétique | Sens Français | Sens Anglais | Contexte |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `LEX-...` | `[Terme]` | `[Phonétique]` | `[FR]` | `[EN]` | `[Usage]` |

## 3. Directives Anti-Clichés (À Faire / À Proscrire)
- **À Faire** : `[Pratique authentique]`
- **À Proscrire** : `[Stéréotype interdit]`
""",
        example_filename="sample-cultural-brief.md",
        example_content="""# Exemple `WLD-02` — Dossier Culturel sur la Vie Portuaire & les Coursiers Wewa

- **ID Dossier** : `CUL-2026-001`
- **Commune / Sujet** : `DST-GOMBE` (`LOC-GOMBE-PORT`) & Mobilité `VEH-MOTO-WEWA-01`
- **Skills Destinataires** : `NAR-02`, `NAR-04`, `ART-02`, `ART-03`, `AUD-02`
- **Statut de Vérification** : `CONFIRMED`

## 1. Synthèse Factuelle & Codes Sociaux
Sur les quais fluviaux (*libongo*), l'activité démarre dès l'aube à l'arrivée des barges. Les dockers, transitaires et coursiers à moto (*Wewa*) utilisent un français kinois nerveux mêlé de termes techniques en lingala. Les conducteurs de Wewa personnalisent souvent leurs motos avec des protège-mains colorés et communiquent par codes de klaxon brefs.

## 2. Entrées Lexicales Certifiées
| ID Terme | Graphie Unicode | Phonétique | Sens Français | Sens Anglais | Contexte |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `LEX-004` | `Wewa` | `WE-wa` | Moto-taxi / Coursier | Motorcycle taxi | Transport rapide urbain (`VEH-MOTO-WEWA-01`). |
| `LEX-006` | `Libongo` | `li-BO-ngo` | Port / Quai fluvial | Harbor / Dock | Désigne `LOC-GOMBE-PORT` et les berges du fleuve. |
| `LEX-007` | `Kɛbá!` | `KE-ba` | Attention ! | Watch out! | Cri d'alerte trafic ou combat. |
| `LEX-012` | `Bilɔkɔ` | `bi-LO-ko` | Marchandises / Colis | Goods / Cargo | Caisses et cargaisons inspectées au port. |

## 3. Directives Anti-Clichés (À Faire / À Proscrire)
- **À Faire** : Montrer des infrastructures portuaires réelles (grues sur rails, conteneurs ISO, barges fluviales métalliques, tenues de travail pragmatiques).
- **À Proscrire** : Pirogues en bois archaïques au cœur du terminal industriel ONATRA de la Gombe.
""",
    ),
    SkillBlueprint(
        skill_id="WLD-03",
        description=(
            "Analyse de la morphologie urbaine, du réseau viaire, de la topographie et des typologies "
            "architecturales de Kinshasa. Traduit les données SIG/OpenStreetMap en règles géométriques "
            "d'urbanisme exploitables par Open World Design (WLD-04), Houdini (ENG-04) et Traffic AI (AI-03)."
        ),
        inputs=("osm-gis-data", "district-profiles-wld-01", "knowledge/technical-specs/spatial-metrics.md"),
        outputs=("urban-typology-spec.md", "road-network-hierarchy.csv"),
        activation_triggers=(
            "Définition des règles de génération procédurale d'une commune (`DST-*`) pour SideFX Houdini (`ENG-04`).",
            "Spécification des profils de voirie (largeur des voies, trottoirs, terre-pleins, drainage) et des ronds-points pour `AI-03`.",
            "Classification des gabarits d'îlots urbains et de hauteur de bâti entre la Gombe, Limete, Matonge et Kalamu.",
        ),
        scope_boundaries=(
            "Ne programme pas directement les noeuds VEX ou graphes HDA dans Houdini (`ENG-04`).",
            "Ne modélise pas les meshes 3D finaux (`ART-02`) ; fournit les règles dimensionnelles et d'implantation.",
        ),
        operational_procedures=(
            "Classer le tissu urbain de la zone cible selon les 4 typologies kinoises : (A) Grille Administrative/Moderne (`DST-GOMBE`), (B) Tissu Commercial Dense (`DST-MATONGE`), (C) Parcellaire Résidentiel Organique (`DST-KALAMU`), (D) Zone Industrielle/Portuaire (`DST-LIMETE`, `LOC-GOMBE-PORT`).",
            "Spécifier les dimensions de voirie en conformité stricte avec `knowledge/technical-specs/spatial-metrics.md` (`400 cm`/voie sur boulevard, `350 cm`/voie sur avenue, trottoirs `250-600 cm`).",
            "Identifier les zones où les données OpenStreetMap sont incomplètes (`research/research-gaps.md`) et définir les règles de subdivision procédurale compensatoire ou le statut `RESEARCH_REQUIRED`.",
            "Documenter les règles dans `templates/urban-typology-spec.md`.",
        ),
        decision_rules=(
            ("Quartier secondaire (ex: DST-MASINA) dépourvu de tracés de ruelles précis dans OSM", "Fournir une règle de subdivision d'îlots orthogonale/organique paramétrique (parcelles 15x25m) et marquer les repères spécifiques en RESEARCH_REQUIRED", "Permettre à ENG-04 de tester le HDA sans inventer de monuments erronés"),
            ("Axe routier trop étroit pour le croisement de deux bus VEH-BUS-TRANSCO-01", "Imposer une largeur minimale de chaussée de 700 cm (2 voies de 350 cm) ou restreindre la spline ZoneGraph aux taxis et motos Wewa", "Synchroniser avec AI-03"),
            ("Transition abrupte entre sol en asphalte et ruelle en latérite", "Spécifier une bande de transition de 200 cm avec caniveau de drainage ouvert pour l'intégration RVT (ART-02)", "Respecter la morphologie réelle des voiries kinoises"),
        ),
        acceptance_criteria=(
            "Toutes les cotes routières et parcellaires sont exprimées en centimètres UE5 (`1 UU = 1 cm`).",
            "Chaque typologie d'îlot définit le nombre d'étages min/max, le retrait de façade et la densité de câblage/végétation.",
            "Compatibilité validée avec le générateur procédural `ENG-04` et le graphe routier `AI-03`.",
        ),
        validation_auditors=("WLD-04", "ENG-04", "AI-03"),
        reference_filename="kinshasa-urban-morphology.md",
        reference_content="""# Morphologie Urbaine & Réseau Viaire de Kinshasa (`WLD-03`)

## 1. Hiérarchie du Réseau Routier (Standards UE5 / ZoneGraph)
1. **Artères Primaires (Boulevard du 30 Juin `LOC-GOMBE-BD30JUIN`, Boulevard Lumumba)** :
   - 2 × 3 ou 2 × 4 voies de `400 cm` chacune + terre-plein central arboré ou bétonné (`200-400 cm`) + trottoirs `400 cm`.
2. **Avenues Secondaires & Carrefours (`LOC-MATONGE-VICTOIRE`, Avenue Kasa-Vubu)** :
   - 2 × 2 voies de `350 cm` + stationnement latéral informel (`220 cm`) + trottoirs/galeries `300-600 cm`.
3. **Ruelles Tertiaires (`DST-KALAMU`, quartiers intérieurs)** :
   - Chaussée mixte asphalte dégradé / latérite compactée de `450 cm` à `600 cm` + caniveaux latéraux de `60 cm` (accès privilégié `VEH-MOTO-WEWA-01` et piétons).
""",
        template_filename="urban-typology-spec.md",
        template_content="""# Spécification de Typologie Urbaine (`WLD-03`)

- **Zone / Commune** : `DST-...` (`LOC-...`)
- **Code Typologie** : `TYP-[GOMBE-GRID / MATONGE-COMM / KALAMU-RES / INDUS-PORT]`
- **Statut Données SIG/OSM** : `CONFIRMED` | `RESEARCH_REQUIRED`

## 1. Règles Géométriques d'Îlots & Bâti (en cm UE5)
- **Dimensions moyennes d'îlot** : `[Longueur x Largeur cm]`
- **Hauteur de bâti (Étages / cm)** : `[Min - Max étages (400 cm/étage)]`
- **Matériaux dominants (`ART-02`)** : `[Béton, latérite, tôle, verre...]`

## 2. Profil de Voirie & Réseau (`ENG-04` / `AI-03`)
| Type de Voie | Nombre de Voies | Largeur par Voie (cm) | Trottoir (cm) | Véhicules Autorisés (`VEH-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `[Artère / Ruelle]` | `[N]` | `[350 / 400]` | `[250-600]` | `[VEH-*]` |
""",
        example_filename="sample-urban-typology.md",
        example_content="""# Exemple `WLD-03` — Typologie Urbaine de `DST-MATONGE` & `LOC-MATONGE-VICTOIRE`

- **Zone / Commune** : `DST-MATONGE` (`LOC-MATONGE-VICTOIRE`)
- **Code Typologie** : `TYP-MATONGE-COMM`
- **Statut Données SIG/OSM** : `CONFIRMED`

## 1. Règles Géométriques d'Îlots & Bâti (en cm UE5)
- **Dimensions moyennes d'îlot** : `8000 cm × 4500 cm` (`80 m × 45 m`), subdivisés en parcelles commerciales de `1200 cm` de façade.
- **Hauteur de bâti (Étages / cm)** : `1 à 3 étages` (`400 cm` au rez-de-chaussée commercial avec auvent en porte-à-faux de `180 cm`, `350 cm` aux étages supérieurs).
- **Matériaux dominants (`ART-02`)** : Béton peint patiné par l'humidité, enseignes métalliques peintes, toitures en tôle galvanisée ondulée, trottoirs bordés de terre rouge latéritique.

## 2. Profil de Voirie & Réseau (`ENG-04` / `AI-03`)
| Type de Voie | Nombre de Voies | Largeur par Voie (cm) | Trottoir (cm) | Véhicules Autorisés (`VEH-*`) |
| :--- | :--- | :--- | :--- | :--- |
| Anneau Rond-Point Victoire | 3 voies circulaires | `380 cm` | `500 cm` (avec étals) | `VEH-BUS-TRANSCO-01`, `VEH-TAXI-JAUNE-01`, `VEH-MOTO-WEWA-01` |
| Avenues Radiales Commerciales | 2 × 1 voie + bande arrêt | `350 cm` | `400 cm` | `VEH-TAXI-JAUNE-01`, `VEH-MOTO-WEWA-01` |
| Passages Piétons / Galeries | Voie partagée | `400 cm` | Sans bordure haute | Piétons `AI-02` + `VEH-MOTO-WEWA-01` à basse vitesse |
""",
    ),
    SkillBlueprint(
        skill_id="WLD-04",
        description=(
            "Macro-conception de la carte monde ouvert de Kinshasa. Définit le découpage en cellules "
            "UE5 World Partition, la hiérarchie des repères visuels (landmarks : Tour de l'Échangeur, "
            "Fleuve Congo), la distribution des Points d'Intérêt (LOC-*) et la règle de rythme des 40 secondes."
        ),
        inputs=("world-bible-wld-01", "urban-typology-wld-03", "game-systems-gd-01", "streaming-budgets-dir-04"),
        outputs=("poi-specification.md", "world-pacing-matrix.csv", "landmark-sightlines-map.md"),
        activation_triggers=(
            "Création ou placement d'un nouveau Point d'Intérêt (`LOC-*`) dans une commune de Kinshasa (`DST-*`).",
            "Calibrage des distances de traversée à pied et en véhicule (`VEH-*`) et des lignes de mire (sightlines) entre quartiers.",
            "Définition des règles de densité d'activités et des cellules de streaming World Partition avec `ENG-01`.",
        ),
        scope_boundaries=(
            "Ne conçoit pas le blockout géométrique intérieur ni le placement micro des couverts de combat (`WLD-05`).",
            "Ne modifie pas les budgets mémoire VRAM ou la taille technique du pool de streaming C++ (`DIR-04`/`ENG-01`).",
        ),
        operational_procedures=(
            "Attribuer au Point d'Intérêt un identifiant `LOC-[DST]-[SLUG]` et l'associer à sa commune parente `DST-*` dans `knowledge/entities-registry.csv`.",
            "Appliquer la **Règle des 40 Secondes** : vérifier qu'un joueur se déplaçant à pied rencontre une opportunité visuelle, systémique (`AI-04`) ou ludique toutes les 35 à 45 secondes.",
            "Configurer la **Hiérarchie des Landmarks (`SYS-WLD-LANDMARKS`)** : s'assurer qu'au moins un repère de Niveau 1 (ex: `LOC-LIMETE-ECHANGEUR` à l'est, le fleuve Congo au nord) ou de Niveau 2 est visible depuis chaque carrefour principal.",
            "Documenter les contraintes de streaming (Data Layers jour/nuit/mission, rayon HLOD) dans `templates/poi-specification-template.md`.",
        ),
        decision_rules=(
            ("Deux POI lourds ( > 20 PNJ AI-01 actifs) placés à moins de 150 mètres l'un de l'autre", "Espacer les POI d'au moins 250 mètres (2 cellules World Partition de 128m) ou placer une barrière d'occlusion visuelle (bâtiment coudé)", "Prévenir tout pic simultané sur le Game Thread et le streaming"),
            ("Quartier où le joueur perd ses repères cardinaux sans ouvrir la carte UI", "Ouvrir un cône de visibilité (sightline) sur l'axe routier vers le landmark majeur de la commune", "Garantir la navigation diégétique SYS-WLD-LANDMARKS"),
            ("POI situé dans une commune au statut RESEARCH_REQUIRED", "Marquer le POI au statut RESEARCH_REQUIRED ou PROPOSED [CONCEPT]", "Attendre la validation WLD-03 avant blockout WLD-05"),
        ),
        acceptance_criteria=(
            "Chaque `LOC-*` possède un ID valide, des coordonnées de cellule World Partition et une fonction claire dans les Core Loops.",
            "Aucun chevauchement de rayon d'activation IA critique (`AI-01`) entre deux POI adjacents.",
            "Orientation cardinale possible sans mini-carte grâce aux lignes de mire documentées.",
        ),
        validation_auditors=("DIR-05", "ENG-01", "WLD-05"),
        reference_filename="open-world-pacing-and-landmarks.md",
        reference_content="""# Règles d'Urbanisme Ludique & Pacing Open World (`WLD-04`)

## 1. Grille UE5 World Partition & Streaming
- **Taille de Cellule Standard** : `12800 cm × 12800 cm` (`128 m × 128 m`).
- **Distance Minimale Inter-Missions Majeures** : `>= 256 m` (2 cellules complètes) pour permettre le déchargement complet (`Data Layers`) de l'arène précédente lors d'une fuite en `VEH-MOTO-WEWA-01`.

## 2. Hiérarchie des Landmarks (`SYS-WLD-LANDMARKS`)
- **Tier 1 (Macro-Repères Régionaux, visibles à > 1.5 km via HLOD)** : `LOC-LIMETE-ECHANGEUR` (Tour de 210 m à l'Est), Fleuve Congo & Grues de `LOC-GOMBE-PORT` (Nord), Skyline des tours de `DST-GOMBE`.
- **Tier 2 (Repères de Commune, visibles à 300-600 m)** : `LOC-MATONGE-VICTOIRE`, château d'eau, antenne émettrice de `ORG-RADIO-KIN`.
- **Tier 3 (Micro-Repères de Rue, < 100 m)** : Fresques murales, enseignes lumineuses de ngandas, arbres remarquables.
""",
        template_filename="poi-specification-template.md",
        template_content="""# Spécification de Point d'Intérêt Open World (`WLD-04`)

- **ID Lieu** : `LOC-[DST]-[SLUG]`
- **Commune Parente** : `DST-...`
- **Catégorie de POI** : `LANDMARK_TIER_1` | `MISSION_HUB` | `SYSTEMIC_ARENA` | `SAFEHOUSE`
- **Cellules World Partition (128m)** : `[Ex: Grid_X12_Y04]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Fonction Ludique & Intégration Monde Ouvert
- **Missions / Systèmes Rattachés** : `[MSN-* / SYS-*]`
- **Accès & Approches** : `[Axes routiers, fluviaux ou piétons]`
- **Lignes de Mire (Sightlines)** : `[Landmarks visibles depuis ce POI]`

## 2. Budget Streaming & Data Layers (`ENG-01`)
- **Data Layers Associés** : `[DL_Base, DL_Mission_..., DL_Night_...]`
- **Distance minimale au POI lourd voisin** : `[>= 250 m]`
""",
        example_filename="sample-poi-specification.md",
        example_content="""# Exemple `WLD-04` — Spécification de `LOC-LIMETE-ECHANGEUR`

- **ID Lieu** : `LOC-LIMETE-ECHANGEUR`
- **Commune Parente** : `DST-LIMETE`
- **Catégorie de POI** : `LANDMARK_TIER_1` & `MISSION_HUB`
- **Cellules World Partition (128m)** : `Grid_X24_Y10` à `Grid_X25_Y11`
- **Statut** : `CONFIRMED`

## 1. Fonction Ludique & Intégration Monde Ouvert
- **Missions / Systèmes Rattachés** : `SYS-WLD-LANDMARKS` (repère vertical directeur de tout l'Est de Kinshasa), hub d'observation et d'interception radio pour l'Acte II.
- **Accès & Approches** : Connecté directement à l'anneau routier du Boulevard Lumumba (bretelles rapides `VEH-MOTO-WEWA-01`) et accessible à pied via l'esplanade piétonne.
- **Lignes de Mire (Sightlines)** : Visible jusqu'à `2.5 km` depuis `DST-MATONGE` et `DST-KALAMU` grâce à sa flèche de 210 mètres en béton brut.

## 2. Budget Streaming & Data Layers (`ENG-01`)
- **Data Layers Associés** : `DL_Limete_Permanent_HLOD0`, `DL_Act2_Syndicate_Blockade`.
- **Distance minimale au POI lourd voisin** : `420 m` (dépôt logistique sud de Limete), garantissant zéro surcharge CPU simultanée.
""",
    ),
    SkillBlueprint(
        skill_id="WLD-05",
        description=(
            "Conception spatiale détaillée des espaces jouables (LOC-*), blockout/greyboxing 3D, "
            "application stricte des métriques de déplacement, de caméra, de couverture et de parkour "
            "(spatial-metrics.md) selon la méthodologie Blockout First avant tout habillage artistique."
        ),
        inputs=("poi-specs-wld-04", "mission-design-gd-02", "combat-metrics-gd-05", "knowledge/technical-specs/spatial-metrics.md"),
        outputs=("level-blockout-brief.md", "blockout-metrics-validation.json"),
        activation_triggers=(
            "Création de la géométrie de gameplay (greybox) d'une arène de mission (`MSN-*`) ou d'un intérieur/extérieur de POI (`LOC-*`).",
            "Placement des couverts de combat (`100 cm` / `200 cm`), des points d'accroche parkour (`260-300 cm`) et des volumes NavMesh / Smart Links (`AI-01`).",
            "Vérification métrique obligatoire avant le passage de relais à `WLD-06` (Environment Designer) et `ART-02` (Environment Artist).",
        ),
        scope_boundaries=(
            "N'applique jamais de matériaux PBR finaux, de végétation haute densité ou de set dressing purement esthétique (`ART-02`).",
            "Ne transmet jamais un niveau à `WLD-06`/`ART-02` tant que le script `scripts/check_spatial_metrics.py` et le playtest `DIR-05` ne sont pas validés.",
        ),
        operational_procedures=(
            "Charger `knowledge/technical-specs/spatial-metrics.md` et fixer la grille de snapping UE5 sur `10 / 50 / 100 / 400 cm`.",
            "Construire les volumes de circulation en garantissant une largeur minimale de **`350 cm`** pour tout couloir jouable (`500 cm` en zone de mêlée) et **`130 cm`** pour tout passage moto Wewa.",
            "Intégrer le guidage visuel précoce par le contraste lumineux dès le blockmesh (méthodologie Naughty Dog `SRC-012`) en collaboration avec `ART-07`.",
            "Exécuter `scripts/check_spatial_metrics.py` sur les paramètres du blockout et consigner le résultat dans `templates/level-blockout-brief.md`.",
        ),
        decision_rules=(
            ("Couloir ou passage intérieur < 350 cm détecté par check_spatial_metrics.py", "Élargir immédiatement le volume géométrique à >= 350 cm avant toute validation", "Éliminer les collisions de SpringArm caméra 3e personne"),
            ("Arène de combat dépourvue d'options de flanquement ou de verticalité", "Ajouter au moins une boucle de circulation latérale et un point d'élévation accessible en vault (100 cm) ou ledge grab (280 cm)", "Synchroniser avec GD-05 et AI-01 (requêtes EQS)"),
            ("Demande d'habillage artistique anticipé par ART-02 sur un blockout non validé", "Refuser le handoff en vertu de la règle Blockout First (quality-standards.md)", "Maintenir le verrou jusqu'au feu vert DIR-05"),
        ),
        acceptance_criteria=(
            "`python skills/02-world-design/wld-05-level-designer/scripts/check_spatial_metrics.py` retourne un code `0`.",
            "Chaque arène supporte les approches prévues par `GD-02` (infiltration, mêlée/tir, fuite) sans cul-de-sac involontaire.",
            "Les volumes NavMesh, Smart Links et zones d'occlusion sont explicitement balisés.",
        ),
        validation_auditors=("DIR-05", "AI-01", "WLD-06"),
        reference_filename="blockout-and-spatial-rules.md",
        reference_content="""# Méthodologie Blockout First & Gabarits UE5 (`WLD-05`)

## 1. Tableau Récapitulatif des Cotes Obligatoires (`spatial-metrics.md`)
| Élément Géométrique | Cote Cible (cm) | Seuil Minimal Absolu | Justification Gameplay / Caméra |
| :--- | :--- | :--- | :--- |
| Largeur Couloir Jouable | `400 cm` | `350 cm` | Croisement 2 PNJ + rotation caméra SpringArm sans clipping. |
| Largeur Arène Mêlée (`GD-05`) | `600 cm` | `500 cm` | Espace requis pour esquives et gestion de 2 Attack Tokens. |
| Hauteur Sous Plafond | `360 cm` | `320 cm` | Évite l'écrasement vertical de la caméra 3e personne. |
| Couvert Bas (Vault / Crouch) | `100 cm` | `90 - 110 cm` | Alignement exact avec `Ability.Movement.Vault` (`ART-05`). |
| Couvert Haut (Full Cover) | `220 cm` | `200 cm` | Occultation complète de la capsule `180 cm`. |
| Inter-file Moto Wewa | `150 cm` | `130 cm` | Passage fluide de `VEH-MOTO-WEWA-01` (largeur 80 cm). |
""",
        template_filename="level-blockout-brief.md",
        template_content="""# Spécification de Blockout Level Design (`WLD-05`)

- **ID Blockout** : `BLK-[LOC]-[NUM]`
- **Lieu & Mission** : `LOC-...` | `MSN-...`
- **Validation Script Métriques** : `PASS (check_spatial_metrics.py)`
- **Statut Blockout** : `PROPOSED_FOR_PLAYTEST` | `APPROVED_FOR_ENV_ART`

## 1. Relevé des Métriques Spatiales (en cm UE5)
- **Largeur minimale couloir** : `[>= 350 cm]`
- **Hauteur sous plafond minimale** : `[>= 320 cm]`
- **Couverts Bas / Hauts** : `[100 cm / >= 200 cm]`
- **Couloir exfiltration Wewa** : `[>= 130 cm]`

## 2. Topologie des Parcours & Approches (`GD-02`)
- **Voie A (Furtivité / Social)** : `[Cheminement & cônes de vue]`
- **Voie B (Verticalité / Parkour)** : `[Accroches 260-300 cm & Smart Links]`
- **Voie C (Mêlée / Exfiltration)** : `[Arènes >= 500 cm & sortie véhicule]`
""",
        example_filename="sample-level-blockout.md",
        example_content="""# Exemple `WLD-05` — Blockout `BLK-GOMBE-PORT-01` (`LOC-GOMBE-PORT`)

- **ID Blockout** : `BLK-GOMBE-PORT-01`
- **Lieu & Mission** : `LOC-GOMBE-PORT` | `MSN-MAIN-001-ARRIVEE`
- **Validation Script Métriques** : `PASS (check_spatial_metrics.py)`
- **Statut Blockout** : `APPROVED_FOR_ENV_ART`

## 1. Relevé des Métriques Spatiales (en cm UE5)
- **Largeur minimale couloir** : `400 cm` entre les rangées de conteneurs ISO.
- **Hauteur sous plafond minimale** : `360 cm` dans les bureaux de douane ; `900 cm` sous la charpente du hangar N°4.
- **Couverts Bas / Hauts** : Caisses de fret standardisées à `100 cm` ; conteneurs et piliers béton à `240 cm`.
- **Couloir exfiltration Wewa** : `150 cm` garantis le long de la rampe de chargement est jusqu'au Boulevard du 30 Juin.

## 2. Topologie des Parcours & Approches (`GD-02`)
- **Voie A (Social / Disguise)** : Entrée principale sud via la guérite douanière (utilise `ITM-DOC-PASSEPORT` + tag `State.Character.Stealth.Disguised`).
- **Voie B (Parkour / Infiltration)** : Échelle de grue à l'ouest -> passerelle suspendue (`hauteur +400 cm`) -> saut d'accroche (`280 cm`) sur le toit des conteneurs.
- **Voie C (Combat & Fuite)** : Cour centrale de déchargement (`1200 cm × 1800 cm`) offrant 6 couverts bas et un accès direct à la moto `VEH-MOTO-WEWA-01` garée sous l'auvent.
""",
        scripts={"check_spatial_metrics.py": CHECK_METRICS_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="WLD-06",
        description=(
            "Direction environnementale par lieu (LOC-*). Traduit les blockouts gameplay validés (WLD-05), "
            "l'Art Bible (ART-01) et la recherche urbaine/culturelle (WLD-02/WLD-03) en briefs de "
            "production détaillés, listes de kits architecturaux modulaires et plans de narration environnementale."
        ),
        inputs=("validated-blockouts-wld-05", "art-bible-art-01", "cultural-briefs-wld-02", "urban-typology-wld-03"),
        outputs=("environment-design-brief.md", "modular-asset-kit-manifest.csv"),
        activation_triggers=(
            "Réception d'un blockout `WLD-05` ayant obtenu le statut `APPROVED_FOR_ENV_ART` auprès de `DIR-05`.",
            "Définition des kits architecturaux modulaires, de la végétation tropicale et de l'habillage (set dressing) d'un lieu `LOC-*`.",
            "Conception du storytelling visuel par couches (histoire du lieu, traces de vie quotidienne kinoise, météo et patine).",
        ),
        scope_boundaries=(
            "N'altère jamais les dimensions de collision ni la hauteur des couverts validés dans le blockout `WLD-05`.",
            "Ne modélise pas directement les géométries dans Blender/Maya (`ART-02`) et ne programme pas les shaders HLSL (`ART-08`).",
        ),
        operational_procedures=(
            "Décomposer les volumes gris du blockout `WLD-05` en modules architecturaux standardisés sur la grille (`400x400 cm`, `200x400 cm`, `100x200 cm`).",
            "Appliquer les **3 Couches de Narration Environnementale** : (1) Structure Architecturale & Histoire, (2) Fonction Économique & Signalétique (`NAR-05`), (3) Micro-traces de Vie Quotidienne & Météo.",
            "Dresser le manifeste exact des kits modulaires, matériaux PBR (latérite, béton humide, tôle) et props requis dans `templates/environment-brief-template.md`.",
            "Vérifier que l'habillage préserve à 100 % la lisibilité des parcours et des points d'accroche parkour.",
        ),
        decision_rules=(
            ("Demande d'ajout d'éléments de décor réduisant un couloir de 400 cm en dessous de 350 cm", "Interdire tout prop à collision dans l'enveloppe des 350 cm ou placer l'habillage en retrait mural/plafond", "Préserver l'intégrité du NavMesh et de la caméra WLD-05"),
            ("Besoin d'un asset architectural unique non réutilisable", "Limiter les meshes uniques aux Landmarks Tier 1/2 et composer 85 % du bâti avec les kits modulaires partagés", "Respecter le budget VRAM de DIR-04 et ART-04"),
            ("Signalétique ou enseigne de rue requise sur une façade", "Utiliser exclusivement les textes validés par NAR-05 et WLD-02", "Éviter tout texte placeholder générique"),
        ),
        acceptance_criteria=(
            "Le taux de réutilisation modulaire du manifeste d'assets est `>= 80 %` sur le quartier.",
            "Les 3 couches de narration environnementale sont détaillées avec références culturelles (`WLD-02`).",
            "0 collision ajoutée dans les volumes de franchissement ou de couverture du blockout `WLD-05`.",
        ),
        validation_auditors=("ART-01", "WLD-05", "ART-08"),
        reference_filename="environmental-storytelling-layers.md",
        reference_content="""# Narration Environnementale & Découpage Modulaire (`WLD-06`)

## 1. Les 3 Couches d'Habillage d'un Lieu Kinois (`LOC-*`)
1. **Couche 1 — Ossature & Patine Climatique** : Structure béton/brique, traces de ruissellement des pluies équatoriales, oxydation des tôles, poussière rouge latéritique à la base des murs (via Runtime Virtual Texturing `ART-02`).
2. **Couche 2 — Activité Sociale & Signalétique** : Enseignes peintes à la main (`NAR-05`), étals modulaires, câblages aériens, mobilier de nganda, caisses de fret portuaires.
3. **Couche 3 — Affordance Gameplay & Guidage Visuel** : Marquage chromatique subtil (bâches jaunes/bleues, éclairage fonctionnel `ART-07`, usure des rebords) sur les points de franchissement (`100 cm`) et d'escalade (`280 cm`).
""",
        template_filename="environment-brief-template.md",
        template_content="""# Brief de Design Environnemental (`WLD-06`)

- **ID Brief** : `ENV-[LOC]-[NUM]`
- **Blockout Source Validé** : `BLK-...` (`WLD-05`)
- **Lieu & Commune** : `LOC-...` (`DST-...`)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Narration Environnementale en 3 Couches
- **Couche 1 (Architecture & Patine)** : `[Matériaux, usure, météo]`
- **Couche 2 (Activité Sociale & Signalétique `NAR-05`)** : `[Enseignes, mobilier, vie locale]`
- **Couche 3 (Affordance Gameplay `WLD-05`)** : `[Marquage visuel des couverts et accroches]`

## 2. Manifeste des Kits Modulaires Requis (`ART-02` / `ART-04`)
| Kit ID | Dimensions Grille (cm) | Texel Density (px/cm) | Réutilisabilité | Usage Collision |
| :--- | :--- | :--- | :--- | :--- |
| `KIT-...` | `400x400` | `10.24` | `Haute` | `Conforme BLK` |
""",
        example_filename="sample-environment-brief.md",
        example_content="""# Exemple `WLD-06` — Brief Environnemental `ENV-GOMBE-PORT-01` (`LOC-GOMBE-PORT`)

- **ID Brief** : `ENV-GOMBE-PORT-01`
- **Blockout Source Validé** : `BLK-GOMBE-PORT-01` (`WLD-05`)
- **Lieu & Commune** : `LOC-GOMBE-PORT` (`DST-GOMBE`)
- **Statut** : `CONFIRMED`

## 1. Narration Environnementale en 3 Couches
- **Couche 1 (Architecture & Patine)** : Quais en béton armé strié avec flaques d'eau réfléchissant les grues (Lumen Reflections), hangars à charpente métallique rivetés, rouille tropicale et traces de pneus de chariots élévateurs.
- **Couche 2 (Activité Sociale & Signalétique `NAR-05`)** : Panneaux réglementaires portuaires bilingues, conteneurs marqués au pochoir, guérite de contrôle avec poste radio diffusant `ORG-RADIO-KIN` à bas volume.
- **Couche 3 (Affordance Gameplay `WLD-05`)** : Sangles d'arrimage jaune vif et projecteurs de chantier orientant l'œil vers l'échelle de la grue ouest (`+400 cm`) et les caisses de couvert bas (`100 cm`).

## 2. Manifeste des Kits Modulaires Requis (`ART-02` / `ART-04`)
| Kit ID | Dimensions Grille (cm) | Texel Density (px/cm) | Réutilisabilité | Usage Collision |
| :--- | :--- | :--- | :--- | :--- |
| `KIT-PORT-WALL-400` | `400 × 400 × 30` | `10.24` | `Haute (Hangars Gombe & Limete)` | Box simple calée sur `BLK-GOMBE-PORT-01` |
| `KIT-ISO-CONTAINER-600` | `600 × 240 × 240` | `10.24` | `Très Haute (Variations couleurs Custom Data)` | Couvert haut `240 cm` + toit franchissable |
| `KIT-CARGO-CRATE-100` | `200 × 100 × 100` | `10.24` | `Très Haute` | Couvert bas `100 cm` certifié Vault |
""",
    ),
)


def build_department_02(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 6 skills du département 02-world-design."""
    created: list[Path] = []
    for bp in WORLD_DESIGN_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_02(WORKSPACE_ROOT)
    print(f"[OK] Département 02-world-design généré ({len(paths)} skills).")
