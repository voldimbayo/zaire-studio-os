"""Spécifications et génération du Département 05-ART-ANIMATION (ART-01 à ART-09)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_3D_STANDARDS_SCRIPT = '''"""Validateur de normes géométriques 3D, Texel Density et Nanite pour ART-04."""

from __future__ import annotations

import argparse
import json
import sys


def validate_3d_asset_spec(spec: dict) -> list[str]:
    """Vérifie la conformité d'un asset 3D aux standards ART-04 (Texel Density, WPO, Pivot)."""
    errors: list[str] = []
    tier = spec.get("tier", "EYE_LEVEL")
    td = float(spec.get("texel_density_px_per_cm", 0.0))
    uses_nanite = bool(spec.get("nanite_enabled", False))
    uses_transparency = bool(spec.get("has_translucent_material", False))
    wpo_cull_dist_cm = float(spec.get("wpo_disable_distance_cm", 0.0))
    pivot_snapped = bool(spec.get("pivot_on_grid", False))

    if tier == "EYE_LEVEL" and abs(td - 10.24) > 0.5:
        errors.append(f"Texel density ({td} px/cm) non conforme au standard hauteur d'oeil (10.24 px/cm).")
    if uses_nanite and uses_transparency:
        errors.append("Nanite est interdit sur les matériaux Translucides (utiliser Opaque ou Masked avec WPO cull).")
    if wpo_cull_dist_cm > 3500.0:
        errors.append(f"Distance de désactivation WPO ({wpo_cull_dist_cm} cm) > maximum autorisé 3500 cm (35m).")
    if not pivot_snapped:
        errors.append("Le pivot de l'asset doit être aligné sur la grille modulaire (10/50/100/400 cm).")

    return errors


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Valide la spécification technique d'un asset 3D (ART-04).")
    parser.add_argument("--file", help="Chemin d'un fichier JSON d'asset 3D à valider (optionnel)")
    args = parser.parse_args()
    if args.file:
        from pathlib import Path
        sample = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample = {
            "asset_id": "SM_Kit_Port_Wall_400a",
            "tier": "EYE_LEVEL",
            "texel_density_px_per_cm": 10.24,
            "nanite_enabled": True,
            "has_translucent_material": False,
            "wpo_disable_distance_cm": 0.0,
            "pivot_on_grid": True,
        }
    errs = validate_3d_asset_spec(sample)
    if errs:
        for e in errs:
            print(f"[ERREUR] {e}")
        return 1
    print(f"[OK] Asset {sample.get('asset_id', 'SAMPLE')} conforme aux standards 3D Nanite & Texel Density (10.24 px/cm).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

ART_ANIMATION_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="ART-01",
        description=(
            "Direction artistique globale de ZAÏRE. Définit l'Art Bible, les palettes chromatiques "
            "par commune de Kinshasa (DST-*), la charte des matériaux équatoriaux (latérite, béton "
            "humide, néons de Matonge) et la lisibilité visuelle gameplay."
        ),
        inputs=("creative-pillars-dir-03", "cultural-research-wld-02", "urban-morphology-wld-03"),
        outputs=("art-bible-chapter.md", "art-review-scorecard.md"),
        activation_triggers=(
            "Définition ou mise à jour de l'identité visuelle d'une commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`).",
            "Revue de cohérence chromatique et stylistique sur les environnements (`ART-02`), personnages (`ART-03`), éclairages (`ART-07`) ou interfaces (`GD-07`).",
            "Établissement des règles d'affordance visuelle (couleurs réservées au parkour et aux couverts).",
        ),
        scope_boundaries=(
            "N'outrepasse jamais les budgets GPU (`PERF-GPU-LUMEN`, `PERF-GPU-NANITE`, `PERF-MEM-VRAM`) définis par `DIR-04`.",
            "Ne modélise pas les assets 3D (`ART-02`/`ART-03`) et n'écrit pas le code des shaders (`ART-08`).",
        ),
        operational_procedures=(
            "Définir pour chaque quartier une **Palette Chromatique Tripartite** : (1) Couleur Dominante (60 % architecture/sol), (2) Couleur Secondaire (30 % signalétique/végétation), (3) Couleur d'Accent/Affordance (10 % guidage joueur).",
            "Vérifier la fidélité des références architecturales et vestimentaires avec `WLD-02` et `WLD-03` (`knowledge/world-bible/cultural-guidelines.md`).",
            "Garantir une séparation de luminance claire entre le personnage joueur (`CHR-PROTAG-KOFFI`), les menaces (`AI-01`) et l'arrière-plan dense de Kinshasa.",
            "Émettre la fiche d'évaluation artistique via `templates/art-bible-template.md`.",
        ),
        decision_rules=(
            ("Surcharge visuelle d'un décor de marché masquant les ennemis ou les points d'accroche parkour", "Désaturer de 20 % l'arrière-plan haut (> 300 cm) et réserver la teinte jaune ocre haute saturation aux prises d'escalade et sangles de franchissement", "Préserver la lisibilité gameplay WLD-05"),
            ("Teinte de peau d'un personnage paraissant terne ou grise sous l'éclairage de scène", "Imposer une recalibration du Subsurface Scattering Profile (ART-03) et de la balance des blancs ACES (ART-07)", "Appliquer cultural-guidelines.md Section 3"),
            ("Même palette chromatique utilisée entre la Gombe et Matonge", "Forcer l'opposition : acier/cyan/béton froid pour DST-GOMBE vs ocre latérite/ambre/magenta chaud pour DST-MATONGE", "Maintenir l'identité immédiate de chaque commune"),
        ),
        acceptance_criteria=(
            "Chaque commune `DST-*` dispose de ses codes couleurs hexadécimaux/linéaires PBR et de ses valeurs d'albédo min/max (`30-240 sRGB`).",
            "La couleur d'affordance gameplay est strictement réservée aux éléments interactifs ou franchissables.",
            "Validation d'authenticité obtenue auprès de `DIR-03` et `WLD-02`.",
        ),
        validation_auditors=("DIR-03", "WLD-02"),
        reference_filename="kinshasa-art-bible-rules.md",
        reference_content="""# Charte Chromatique & PBR de Kinshasa (`ART-01`)

## 1. Palettes Officielles par Commune (`DST-*`)
| Commune | Dominante (60 %) | Secondaire (30 %) | Accent & Lumière (10 %) | Contraste & Humeur |
| :--- | :--- | :--- | :--- | :--- |
| `DST-GOMBE` | Béton Brut & Verre (`#7A8288`) | Acier Portuaire & Vert Fluvial (`#2F4F4F`) | LED Froide & Sangles Jaunes (`#F2C94C`) | Vertical, institutionnel, reflets humides. |
| `DST-MATONGE` | Ocre Latérite & Crépi Chaud (`#B85D3B`) | Turquoise & Enseignes Peintes (`#1B998B`) | Néons Ambre/Magenta (`#FF3366`, `#FF9F1C`) | Vibrante, polyphonique, nocturne électrique. |
| `DST-LIMETE` | Béton Monumental Patiné (`#6E6A66`) | Tôle Rouillée & Verdure (`#8C4A27`) | Sodium Industriel (`#FFB347`) | Massif, industriel, silhouettes sur ciel équatorial. |

## 2. Plage de Calibration PBR Obligatoire
- **BaseColor (Albédo sRGB)** : Interdiction de descendre sous `30 sRGB` (charbon/pneu = `35-45 sRGB`) ou de dépasser `240 sRGB` pour laisser travailler Lumen GI (`ART-07`).
""",
        template_filename="art-bible-template.md",
        template_content="""# Directive de Direction Artistique — Art Bible (`ART-01`)

- **Cible Visuelle** : `DST-...` | `LOC-...` | `CHR-...`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Palette Chromatique & Matériaux PBR
- **Dominante (60 %)** : `[Teinte & Matériau]`
- **Secondaire (30 %)** : `[Teinte & Matériau]`
- **Accent & Affordance Gameplay (10 %)** : `[Couleur réservée aux interactions WLD-05]`
- **Plage Albédo PBR (`30-240 sRGB`)** : `[Vérifiée]`

## 2. Règles de Lisibilité & Contraste
- **Séparation Silhouette Joueur / Décor** : `[Directive contraste]`
""",
        example_filename="sample-art-bible-directive.md",
        example_content="""# Exemple `ART-01` — Directive Artistique pour `LOC-GOMBE-PORT` & `DST-MATONGE`

- **Cible Visuelle** : Contraste `LOC-GOMBE-PORT` (`DST-GOMBE`) vs `LOC-MATONGE-VICTOIRE` (`DST-MATONGE`)
- **Statut** : `CONFIRMED`

## 1. Palette Chromatique & Matériaux PBR
- **Dominante (60 %)** : À `LOC-GOMBE-PORT`, béton portuaire gris-bleu humide (`#6C757D`, Roughness `0.35` avec flaques) ; à `DST-MATONGE`, terre latérite rouge-ocre (`#A94A29`, Roughness `0.78`).
- **Secondaire (30 %)** : Conteneurs maritimes bleu/rouille désaturés au port ; façades peintes turquoise et vert émeraude à Matonge.
- **Accent & Affordance Gameplay (10 %)** : Jaune industriel haute visibilité (`#F2C94C`) strictement réservé aux échelles de grues, sangles de caisses franchissables (`100 cm`) et rebords de parkour (`280 cm`).
- **Plage Albédo PBR (`30-240 sRGB`)** : Pneus des motos Wewa calibrés à `42 sRGB` ; murs blanchis à la chaux plafonnés à `225 sRGB`.

## 2. Règles de Lisibilité & Contraste
- **Séparation Silhouette Joueur / Décor** : La veste sombre à col contrasté de `CHR-PROTAG-KOFFI` conserve un ratio de luminance d'au moins `3:1` face au brouillard matinal du fleuve Congo.
""",
    ),
    SkillBlueprint(
        skill_id="ART-02",
        description=(
            "Production des kits architecturaux modulaires de Kinshasa, de la bibliothèque de matériaux "
            "PBR (latérite, béton tropicalisé, tôle ondulée), de la végétation équatoriale et de "
            "l'habillage (set dressing) sous UE5 Nanite et Runtime Virtual Texturing (RVT)."
        ),
        inputs=("environment-briefs-wld-06", "3d-pipeline-standards-art-04"),
        outputs=("modular-kit-specification.md", "pbr-material-library.csv"),
        activation_triggers=(
            "Création des meshes architecturaux modulaires et des matériaux PBR d'un lieu `LOC-*` dont le blockout `WLD-05` est validé.",
            "Configuration de la fusion terrain/bâtiments (poussière de latérite, humidité) via Runtime Virtual Texturing (RVT).",
            "Fourniture des pièces modulaires standardisées au générateur procédural Houdini (`ENG-04`).",
        ),
        scope_boundaries=(
            "Ne modifie jamais l'enveloppe de collision ni les cotes de couverture validées par `WLD-05` (règle Blockout First).",
            "N'utilise jamais de matériaux Translucides sur des géométries Nanite et désactive le WPO du feuillage au-delà de `35 mètres`.",
        ),
        operational_procedures=(
            "Modéliser chaque pièce du kit architectural sur la grille métrique (`100`, `200`, `400 cm`) avec le point de pivot placé au coin inférieur gauche arrière (`ART-04`).",
            "Appliquer une Texel Density de **`10.24 px/cm`** sur tous les modules situés entre `0` et `300 cm` de hauteur d'œil (`5.12 px/cm` sur les étages supérieurs).",
            "Utiliser des **Trim Sheets** et le **Vertex Color / Custom Primitive Data** pour générer des dizaines de variations de façades kinoises sans dupliquer les textures en VRAM.",
            "Intégrer un blend RVT sur les `50 premiers centimètres` à la base des murs pour fondre la poussière latéritique ou les éclaboussures de pluie.",
        ),
        decision_rules=(
            ("Besoin de varier la couleur de 50 conteneurs ou façades commerciales dans le même quartier", "Interdire la création de 50 textures BaseColor distinctes : utiliser un seul matériau maître piloté par Per-Instance Custom Data", "Économiser la VRAM (budget <= 6144 MB)"),
            ("Végétation tropicale (palmiers, manguiers, herbes hautes) causant un surcoût GPU dans Nanite/VSM", "Utiliser de la géométrie opaque/masked découplée au plus près de la feuille et couper le World Position Offset (vent) à 3500 cm (35m)", "Respecter PERF-GPU-NANITE <= 2.5 ms"),
            ("Écart constaté entre le mesh artistique et la boîte de collision du blockout WLD-05", "Conserver la boîte de collision exacte du blockout comme Simple Collision du Static Mesh", "Garantir zéro régression sur le NavMesh et le parkour"),
        ),
        acceptance_criteria=(
            "100 % des modules architecturaux s'assemblent sans couture (watertight) sur la grille `100/200/400 cm`.",
            "Les valeurs PBR respectent la charte `ART-01` (`Albédo 30-240 sRGB`) et la Texel Density `10.24 px/cm`.",
            "Les collisions gameplay sont strictement identiques au blockout `WLD-05` approuvé.",
        ),
        validation_auditors=("ART-04", "ART-08", "ART-01", "WLD-05"),
        reference_filename="nanite-modular-environment.md",
        reference_content="""# Production Environnementale Modulaire Nanite & RVT (`ART-02`)

## 1. Standards de Kits Modulaires Kinois
- **Grille de Snapping** : `100 cm`, `200 cm`, `400 cm` (hauteur d'étage standard = `400 cm` RDC commercial, `350 cm` étages).
- **Texel Density** : `10.24 px/cm` (0 à 3 m) -> `2048 × 2048` couvre exactement `200 × 200 cm`.
- **Channel Packing Obligatoire (`ORM`)** :
  - Canal **R** = Ambient Occlusion
  - Canal **G** = Roughness
  - Canal **B** = Metallic
  (Compression UE5 : `Masks (no sRGB)`, BC7/BC5 pour les normales).
""",
        template_filename="modular-kit-spec.md",
        template_content="""# Spécification de Kit Architectural & Matériaux PBR (`ART-02`)

- **ID Kit** : `KIT-[DST/LOC]-[SLUG]`
- **Brief Source (`WLD-06`)** : `ENV-...`
- **Texel Density** : `10.24 px/cm` (RDC) / `5.12 px/cm` (Étages)
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Inventaire des Modules Géométriques Nanite
| Nom Static Mesh | Dimensions (L × l × H cm) | Pivot | Nanite | Collision Simple |
| :--- | :--- | :--- | :--- | :--- |
| `SM_Kit_...` | `400 × 30 × 400` | `Coin Inf-Gauche` | `Oui` | `Box exacte BLK` |

## 2. Bibliothèque de Matériaux PBR & RVT
| ID Matériau | BaseColor (sRGB min-max) | Roughness | Packing Texture | Blend RVT Sol |
| :--- | :--- | :--- | :--- | :--- |
| `MI_...` | `[45 - 210]` | `[0.35 - 0.85]` | `BC7 + ORM` | `Oui (50 cm)` |
""",
        example_filename="sample-modular-kit-spec.md",
        example_content="""# Exemple `ART-02` — Kit Modulaire `KIT-GOMBE-PORT` & Matériaux Tropicaux

- **ID Kit** : `KIT-GOMBE-PORT`
- **Brief Source (`WLD-06`)** : `ENV-GOMBE-PORT-01`
- **Texel Density** : `10.24 px/cm` (0-3m) / `5.12 px/cm` (Charpentes hautes)
- **Statut** : `CONFIRMED`

## 1. Inventaire des Modules Géométriques Nanite
| Nom Static Mesh | Dimensions (L × l × H cm) | Pivot | Nanite | Collision Simple |
| :--- | :--- | :--- | :--- | :--- |
| `SM_Port_HangarWall_400a` | `400 × 30 × 400` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` calée sur `BLK-GOMBE-PORT-01` |
| `SM_Port_ISOContainer_600a` | `600 × 240 × 240` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` (Couvert haut `240 cm`) |
| `SM_Port_CargoCrate_100a` | `200 × 100 × 100` | `0, 0, 0 (Grille)` | `Oui` | `1 Box Primitive` (Vault `100 cm`) |

## 2. Bibliothèque de Matériaux PBR & RVT
| ID Matériau | BaseColor (sRGB) | Roughness | Packing Texture | Blend RVT Sol |
| :--- | :--- | :--- | :--- | :--- |
| `MI_Concrete_Dock_Wet` | `68 - 165 sRGB` | `0.25 (flaques) - 0.72` | `2K BaseColor + Normal + ORM` | `Oui (Transition limon fluvial 50 cm)` |
| `MI_Corrugated_Iron_Rust` | `55 - 180 sRGB` | `0.45 - 0.82` | `2K Trim Sheet + Custom Data Tint` | `Non (Toitures & Bardages)` |
| `MI_Laterite_Road_Blend` | `85 - 175 sRGB` | `0.30 (boue) - 0.85 (sec)` | `RVT Master Layer` | `Source RVT Principale` |
""",
    ),
    SkillBlueprint(
        skill_id="ART-03",
        description=(
            "Conception et production des modèles 3D des protagonistes (CHR-*) et du système "
            "d'assemblage modulaire des PNJ kinois (AI-01/AI-02). Spécifie les shaders de peau "
            "(Subsurface Profile pour carnations foncées sous soleil équatorial), les vêtements "
            "et la bascule Groom Strands -> Hair Cards."
        ),
        inputs=("character-bibles-nar-03", "cultural-dress-codes-wld-02", "art-bible-art-01", "3d-standards-art-04"),
        outputs=("character-art-specification.md", "modular-npc-assembly-table.csv"),
        activation_triggers=(
            "Production du modèle 3D d'un personnage héroïque (`CHR-PROTAG-KOFFI`, `CHR-ANTAG-MUKENDI`, `CHR-ALLY-AMINA`).",
            "Conception des pièces vestimentaires et morphologiques modulaires alimentant la foule de Kinshasa (`AI-02`, méthodologie Guerrilla Games `SRC-009`).",
            "Étalonnage des shaders de peau et des coiffures africaines (tresses, locks, coupes courtes, foulards) avec `ART-07` et `ART-08`.",
        ),
        scope_boundaries=(
            "Ne programme pas les Animation Blueprints (`ART-05`) et ne construit pas les rigs de déformation complexes (`ART-08`).",
            "Interdit l'usage de Groom Hair Strands (alembic) sur les PNJ de foule `AI-02` (réservé exclusivement aux LOD 0/1 des héros en cinématique).",
        ),
        operational_procedures=(
            "Aligner la topologie de tous les personnages humains sur le **Squelette Maître Unique ZAÏRE (Compatible MetaHuman / UE5 Manny)** afin de mutualiser 100 % des animations (`ART-05`/`ART-06`).",
            "Pour les PNJ (`AI-01`/`AI-02`), découper les meshes en 5 slots modulaires interchangeables : `Head`, `Hair/Headgear`, `UpperBody`, `LowerBody`, `Footwear/Accessories` avec variation chromatique par atlas/palette.",
            "Configurer le **Subsurface Scattering (SSS) / Substrate Skin Profile** pour les carnations foncées : ajuster le libre parcours moyen (Mean Free Path) rouge/ambre et la rugosité micro-cutanée Dual Lobe Specular (`0.28 / 0.45`) pour éviter tout reflet blanc crayeux sous `ART-07`.",
            "Définir les seuils de bascule LOD capillaire : Groom Strands (LOD 0 cinématique héros uniquement) -> Hair Cards optimisées (LOD 1/2 gameplay) -> Casque/Mesh bas (LOD 3 foule lointaine).",
        ),
        decision_rules=(
            ("Coiffure Groom Strands dépassant 0.4 ms GPU en phase de gameplay ouvert", "Forcer la bascule automatique vers le mesh Hair Cards dès le retour en caméra gameplay 3e personne (distance > 180 cm)", "Préserver le budget GPU global <= 16.6 ms"),
            ("Répétition visuelle de clones dans les marchés de Matonge (600 PNJ AI-02)", "Combiner 12 têtes × 15 hauts × 12 bas × 10 coiffures/chapeaux × 8 palettes de motifs wax/streetwear (plus de 170 000 permutations pour < 768 MB VRAM)", "Appliquer le pipeline modulaire Guerrilla Games SRC-009"),
            ("Vêtement flottant causant du clipping lors des mouvements de combat", "Remplacer la simulation Chaos Cloth par du skinning rigide + Normal Map animée sur les PNJ de foule, et limiter Chaos Cloth à la veste de Koffi (LOD 0)", "Respecter le budget PERF-CPU-CHAOS <= 1.5 ms"),
        ),
        acceptance_criteria=(
            "Tous les personnages partagent le squelette maître standardisé et supportent le retargeting `ART-06`.",
            "Le pool VRAM total des kits modulaires PNJ d'une commune reste `<= 768 MB`.",
            "Les carnations et tenues respectent strictement `knowledge/world-bible/cultural-guidelines.md`.",
        ),
        validation_auditors=("ART-01", "ART-04", "WLD-02", "ENG-07"),
        reference_filename="character-skin-and-modularity.md",
        reference_content="""# Pipeline Personnages : Shaders de Peau & Modularité PNJ (`ART-03`)

## 1. Calibration PBR des Carnations Foncées sous Lumière Équatoriale
- **BaseColor (Albédo sRGB)** : Plage réaliste calibrée entre `42 sRGB` et `115 sRGB` (jamais de noir pur, saturation riche dans les sous-tons chauds/dorés/acajou).
- **Dual Specular Lobe (UE5 Skin Shading)** : Lobe primaire `Roughness = 0.28` (sébum naturel), Lobe secondaire `Roughness = 0.48` (micro-relief pores via Cavity Map).
- **Subsurface Profile** : Diffusion sub-cutanée ambre-rouge subtil sur les oreilles, narines et contours sous contre-jour solaire équatorial (`EV100 = 15`).

## 2. Budgets Géométriques & LOD Personnages
| Catégorie | LOD 0 (Triangles) | LOD 1 (Triangles) | LOD 2 (Triangles) | LOD 3 VAT Foule |
| :--- | :--- | :--- | :--- | :--- |
| **Héros (`CHR-PROTAG-KOFFI`)** | `85 000 tris` | `42 000 tris` | `18 000 tris` | N/A |
| **PNJ Actif (`AI-01` Garde)** | `35 000 tris` | `16 000 tris` | `7 500 tris` | `2 800 tris` |
| **Citoyen Foule (`AI-02`)** | `22 000 tris` (Hydraté) | `9 500 tris` | `3 200 tris (VAT)` | `1 400 tris (VAT)` |
""",
        template_filename="character-art-spec.md",
        template_content="""# Spécification Character Art & Modularité (`ART-03`)

- **ID Personnage / Kit Foule** : `CHR-...` | `NPC-KIT-...`
- **Commune / Faction** : `DST-...` | `ORG-...`
- **Squelette Cible** : `SK_Zaire_Master_Humanoid`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Budgets Géométriques, Textures & Groom
- **Polycount (LOD 0 / LOD 1 / LOD 2)** : `[XXk / XXk / XXk tris]`
- **Calibration Shader Peau (Albédo / Dual Lobe Roughness)** : `[Valeurs]`
- **Stratégie Cheveux (Strands vs Hair Cards)** : `[Règle par LOD]`

## 2. Table des Slots Modulaires & Variations (`AI-02`)
| Slot Modulaire | Nombre de Variantes Mesh | Atlas / Palette Shader | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `UpperBody` | `[N]` | `[Custom Data / Atlas]` | `[XX MB]` |
""",
        example_filename="sample-character-art-spec.md",
        example_content="""# Exemple `ART-03` — Spécification de `CHR-PROTAG-KOFFI` & Kit Foule `NPC-KIT-MATONGE`

- **ID Personnage / Kit Foule** : `CHR-PROTAG-KOFFI` & `NPC-KIT-MATONGE`
- **Commune / Faction** : `DST-KALAMU` / `DST-MATONGE`
- **Squelette Cible** : `SK_Zaire_Master_Humanoid`
- **Statut** : `CONFIRMED`

## 1. Budgets Géométriques, Textures & Groom (`CHR-PROTAG-KOFFI`)
- **Polycount (LOD 0 / LOD 1 / LOD 2)** : `82 000 / 40 000 / 16 500 triangles`.
- **Calibration Shader Peau** : Albédo `62 sRGB` (sous-ton chaud cuivré), Dual Specular `0.26 / 0.44` avec Micro-Normal Map pores `4K` et masque de sueur progressif piloté par l'effort/météo.
- **Stratégie Cheveux** : Coupe courte texturée avec dégradé net en Hair Cards haute densité dès le LOD 0 gameplay (`3 800 tris`), zéro surcoût Groom Strands en monde ouvert.

## 2. Table des Slots Modulaires & Variations (`NPC-KIT-MATONGE` pour `AI-02`)
| Slot Modulaire | Nombre de Variantes Mesh | Atlas / Palette Shader | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `Head_Sculpts` | `12 visages distincts` | 3 nuances de carnation SSS + pilosité/maquillage | `140 MB` |
| `Hair_Headgear` | `14 (Tresses, locks, bérets, casques Wewa)` | Hair Cards alpha-to-coverage | `95 MB` |
| `UpperBody_Tops` | `16 (Chemises wax, polos, vestes Sapeurs)` | Motifs procéduraux par index `CustomPrimitiveData` | `210 MB` |
| `LowerBody_Pants` | `12 (Pantalons toile, jeans, jupes pagnes)` | Variations teintes/usure latérite RVT | `135 MB` |
""",
    ),
    SkillBlueprint(
        skill_id="ART-04",
        description=(
            "Ingénierie du pipeline 3D et standardisation géométrique de ZAÏRE STUDIO OS. Définit "
            "les règles de topologie UE5 Nanite, de Texel Density (10.24 px/cm), d'alignement des pivots "
            "sur grille, d'UV mapping, de baking et les règles de validation pré-commit (scripts/check_3d_standards.py)."
        ),
        inputs=("hardware-budgets-dir-04", "art-direction-art-01"),
        outputs=("3d-modeling-standards.md", "asset-validation-rules.json"),
        activation_triggers=(
            "Définition des conventions d'export FBX/USD et des préfixes de nommage UE5 (`SM_`, `SK_`, `M_`, `MI_`, `T_`).",
            "Spécification des règles de validation automatique à implémenter dans l'éditeur UE5 par `ENG-03` (Tools Programmer).",
            "Contrôle de conformité d'un lot d'assets `ART-02` ou `ART-03` via `scripts/check_3d_standards.py`.",
        ),
        scope_boundaries=(
            "Ne code pas le plugin C++ Slate de l'éditeur (`ENG-03`), mais fournit le fichier `asset-validation-rules.json` qui le pilote.",
            "N'accorde aucune dérogation sur l'échelle (`1 UU = 1 cm`), l'orientation (`+X Forward`) ou l'interdiction du Translucide sur Nanite.",
        ),
        operational_procedures=(
            "Vérifier la nomenclature de chaque asset soumis selon la convention : `SM_` (Static Mesh), `SK_` (Skeletal Mesh), `M_` (Master Material), `MI_` (Material Instance), `T_` (Texture avec suffixe `_D`, `_N`, `_ORM`).",
            "Exécuter `scripts/check_3d_standards.py` pour valider la Texel Density (`10.24 px/cm`), le placement du pivot sur la grille et la distance de coupure WPO (`<= 3500 cm`).",
            "Contrôler la présence obligatoire de `UV0` (textures PBR, padding `>= 8 px` en 2K) et `UV1` (si requis pour masques secondaires).",
            "Publier les règles mises à jour dans `templates/asset-validation-rules.json`.",
        ),
        decision_rules=(
            ("Static Mesh architectural soumis avec Nanite activé ET un matériau Blend Mode = Translucent", "Bloquer immédiatement l'asset : séparer les vitres translucides dans un sous-mesh distinct non-Nanite (LOD standard)", "Respecter les contraintes matérielles du rasterizer Nanite UE5"),
            ("Texture soumise avec une dimension non puissance de 2 (ex: 1500x1500)", "Rejeter l'import : imposer des dimensions puissances de 2 (512, 1024, 2048, 4096) pour permettre la génération de MipMaps et la compression BC7", "Éviter tout gaspillage VRAM non streamable"),
            ("Asset modulaire dont le pivot est centré au milieu de la géométrie au lieu du coin de grille", "Renvoyer l'asset en correction DCC (Blender/Maya) pour replacer le pivot sur la grille 10/50/100 cm", "Garantir la compatibilité avec le snapping WLD-05/WLD-06 et Houdini ENG-04"),
        ),
        acceptance_criteria=(
            "`python skills/05-art-animation/art-04-3d-pipeline-specialist/scripts/check_3d_standards.py` retourne un code `0`.",
            "100 % des règles de `asset-validation-rules.json` sont déterministes et vérifiables par `ENG-03`.",
            "Zéro texture non compressée ou sans MipMaps dans le pipeline.",
        ),
        validation_auditors=("ENG-03", "ART-08", "DIR-04"),
        reference_filename="ue5-3d-pipeline-norms.md",
        reference_content="""# Normes Géométriques, UV & Nomenclature UE5 (`ART-04`)

## 1. Convention de Nommage Officielle ZAÏRE STUDIO OS
- `SM_[Kit/District]_[AssetName]_[Variant]` (ex: `SM_Port_HangarWall_400a`)
- `SK_[Category]_[CharacterName]` (ex: `SK_Hero_Koffi`, `SK_Veh_MotoWewa01`)
- `T_[AssetName]_[D|N|ORM]` (`_D` = BaseColor sRGB, `_N` = Normal BC5 Linear, `_ORM` = Occlusion/Roughness/Metallic Linear)

## 2. Contraintes Techniques Nanite & Textures
- **Texel Density** : `10.24 px/cm` (0-3m), `5.12 px/cm` (3-15m), `1.28 px/cm` (HLOD).
- **Taille Max Texture** : `2048 × 2048` en standard environnement ; `4096 × 4096` réservé aux visages héros LOD 0 et trim sheets maîtresses.
- **WPO Cull Distance** : `<= 3500 cm` (`35 m`) obligatoire sur tout matériau utilisant World Position Offset.
""",
        template_filename="asset-validation-rules.json",
        template_content="""{
  "pipeline_version": "1.0.0",
  "owner_skill": "ART-04",
  "enforced_by_tool": "ENG-03",
  "naming_prefixes": {
    "StaticMesh": "SM_",
    "SkeletalMesh": "SK_",
    "MasterMaterial": "M_",
    "MaterialInstance": "MI_",
    "Texture": "T_"
  },
  "geometry_rules": {
    "unit_scale_cm": 1.0,
    "forward_axis": "+X",
    "require_grid_snapped_pivot": true,
    "forbid_translucent_on_nanite": true,
    "max_wpo_disable_distance_cm": 3500.0
  },
  "texture_rules": {
    "target_texel_density_eye_level": 10.24,
    "require_power_of_two": true,
    "orm_channel_packing": "R=AO, G=Roughness, B=Metallic",
    "orm_srgb": false
  }
}
""",
        example_filename="sample-3d-validation-report.md",
        example_content="""# Exemple `ART-04` — Audit de Validation 3D du Lot `KIT-GOMBE-PORT`

## 1. Résultat du Validateur (`scripts/check_3d_standards.py`)
- **Lot Audité** : `KIT-GOMBE-PORT` (`14 Static Meshes`, `18 Textures`)
- **Statut Global** : `PASSED (0 erreur bloquante)`

## 2. Détail des Contrôles par Asset
| Asset | Nomenclature | Pivot Grille | Texel Density | Nanite / Translucide | WPO Cull | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SM_Port_HangarWall_400a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Nanite Opaque (OK)` | `N/A (0 cm)` | **VALIDÉ** |
| `SM_Port_WindowGlass_200a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Non-Nanite Translucent (OK)` | `N/A (0 cm)` | **VALIDÉ** |
| `SM_Palm_Tropical_01a` | `OK (SM_)` | `0,0,0 (OK)` | `10.24 px/cm` | `Nanite Masked (OK)` | `3200 cm (<= 3500)` | **VALIDÉ** |
""",
        scripts={"check_3d_standards.py": CHECK_3D_STANDARDS_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="ART-05",
        description=(
            "Architecture des systèmes d'animation temps réel sous Unreal Engine 5 : locomotion "
            "réactive par Motion Matching (Pose Search), franchissements parkour par Motion Warping "
            "(couverts 100 cm, accroches 260-300 cm), montages de combat (GD-05) et Control Rig IK "
            "dans un budget CPU <= 1.8 ms."
        ),
        inputs=("spatial-metrics-wld-05", "combat-frame-data-gd-05", "cleaned-mocap-art-06"),
        outputs=("animation-graph-specification.md", "locomotion-and-warping-metrics.csv"),
        activation_triggers=(
            "Conception ou optimisation de l'Animation Blueprint de `CHR-PROTAG-KOFFI` ou des gardes `AI-01`.",
            "Paramétrage des fenêtres `Motion Warping` pour aligner les mains et les pieds sur les obstacles de Kinshasa (`100 cm` vault, `280 cm` ledge grab).",
            "Synchronisation des `AnimNotifies` de combat avec la Frame Data à 60 FPS définie par `GD-05`.",
        ),
        scope_boundaries=(
            "Ne dirige pas l'acquisition sur le plateau Motion Capture ni le nettoyage brut des marqueurs optiques (`ART-06`).",
            "Interdit tout calcul d'IK complet (`Control Rig Full Body IK`) sur les PNJ situés à plus de `25 mètres` de la caméra.",
        ),
        operational_procedures=(
            "Configurer la base de données **UE5 Motion Matching (`UPoseSearchDatabase`)** de Koffi avec les canaux de trajectoire future (`+0.2s`, `+0.4s`, `+0.6s`) et de vélocité des pieds pour éliminer tout glissement (*foot sliding*, méthode Rockstar `SRC-015`).",
            "Associer les fenêtres `UMotionWarpingComponent` aux capacités GAS (`Ability.Movement.Vault` à `100 cm`, `LedgeGrab` à `260-300 cm`) définies dans `knowledge/technical-specs/spatial-metrics.md`.",
            "Placer les `UAnimNotifyState` de combat (`ANS_MeleeHitbox`, `ANS_ParryWindow`, `ANS_CancelWindow`) aux frames exactes spécifiées par `GD-05`.",
            "Activer l'**Update Rate Optimization (URO)** et l'évaluation sur Worker Threads (`bUseMultiThreadedAnimationUpdate = true`) pour tenir le budget `PERF-CPU-ANIM <= 1.8 ms`.",
        ),
        decision_rules=(
            ("Latence ressentie (> 100 ms) lors d'un demi-tour brusque en sprint ou en combat", "Augmenter le poids de la réactivité d'input (Trajectory Weight) dans le Pose Search Schema et déclencher un Pivot Transition Montage", "Concilier inertie réaliste et contrôle nerveux DIR-05"),
            ("Dépassement du budget CPU Animation (> 1.8 ms) dans une scène dense", "Désactiver le Foot Placement Control Rig au-delà de 15m, passer les PNJ entre 15m et 30m à 30Hz (URO) et figer l'évaluation squelettique au-delà de 80m (bascule VAT AI-02)", "Respecter PERF-CPU-ANIM"),
            ("Obstacle de blockout situé à 105 cm au lieu de 100 cm", "Autoriser le Motion Warping vertical dans la plage de tolérance [90 cm, 110 cm] sans déformer la vitesse d'animation", "Garantir un franchissement sans accroc géométrique"),
        ),
        acceptance_criteria=(
            "Coût CPU Animation total `<= 1.8 ms` (60 FPS) / `<= 2.5 ms` (30 FPS) avec 100 % des mises à jour sur Worker Threads.",
            "Alignement exact à la frame près entre les `AnimNotifies` et la table Frame Data de `GD-05`.",
            "Zéro glissement des pieds sur les pentes en latérite de `DST-NGALIEMA` grâce au Control Rig Foot IK.",
        ),
        validation_auditors=("GD-05", "WLD-05", "ENG-07"),
        reference_filename="motion-matching-and-warping.md",
        reference_content="""# Architecture UE5 Motion Matching, Motion Warping & URO (`ART-05`)

## 1. Seuils de Synchronisation Spatiale (`WLD-05` <-> `ART-05`)
| Action (`FGameplayTag`) | Hauteur Cible | Fenêtre Tolérance Motion Warping | Durée Animation |
| :--- | :--- | :--- | :--- |
| `Ability.Movement.Vault` (Franchissement bas) | `100 cm` | `90 cm à 110 cm` (Distance d'appel `<= 180 cm`) | `0.55 s (33 frames)` |
| `Ability.Movement.ClimbHigh` (Mur / Conteneur) | `220 - 240 cm` | `200 cm à 250 cm` | `1.10 s (66 frames)` |
| `Ability.Movement.LedgeGrab` (Saut d'accroche) | `280 cm` | `260 cm à 300 cm` | `0.85 s (51 frames)` |

## 2. Paliers d'Optimisation CPU (`PERF-CPU-ANIM <= 1.8 ms`)
- **0 à 15 m** : Tick `60 Hz`, Motion Matching complet + Control Rig Foot/Hand IK actif.
- **15 à 35 m** : Tick `30 Hz` (URO Skip 1 frame), IK désactivé.
- **35 à 80 m** : Tick `15 Hz` (URO Skip 3 frames), State Machine simplifiée.
- **> 80 m** : Vertex Animation Texture (VAT) sur Static Mesh (`AI-02`), `0.0 ms` CPU squelettique.
""",
        template_filename="animation-graph-spec.md",
        template_content="""# Spécification Architecture d'Animation UE5 (`ART-05`)

- **Cible Squelette** : `SK_Zaire_Master_Humanoid` (`CHR-...` / `AI-01`)
- **Budget CPU Max (`PERF-CPU-ANIM`)** : `<= 1.8 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Configuration Motion Matching & Motion Warping
- **Pose Search Channels** : `[Trajectory, Pose, Velocity]`
- **Cibles Motion Warping (`WLD-05`)** : `[Tags & fenêtres cm]`

## 2. Synchronisation Frame Data Combat (`GD-05`)
| Montage Asset | Gameplay Tag | Startup (`f`) | Active Hitbox (`ANS_`) | Recovery / Cancel (`f`) |
| :--- | :--- | :--- | :--- | :--- |
| `AM_...` | `Ability.Melee...` | `f01 - fXX` | `fXX - fYY` | `fYY - fZZ` |
""",
        example_filename="sample-animation-spec.md",
        example_content="""# Exemple `ART-05` — Animation Blueprint de `CHR-PROTAG-KOFFI` (Parkour & Machette)

- **Cible Squelette** : `SK_Zaire_Master_Humanoid` (`CHR-PROTAG-KOFFI`)
- **Budget CPU Max (`PERF-CPU-ANIM`)** : `1.42 ms` mesuré (`<= 1.8 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Configuration Motion Matching & Motion Warping
- **Pose Search Channels** : `PSD_Koffi_Locomotion` indexant 140 clips nettoyés (`ART-06`) sur trajectoire `-0.2s, +0.2s, +0.4s, +0.6s`, vitesse du bassin et phase de contact des pieds.
- **Cibles Motion Warping (`WLD-05`)** :
  - `WarpTarget_VaultApex` : Verrouille la main gauche sur l'arête supérieure des caisses de `100 cm` (`[90, 110] cm`) entre les frames `8` et `16`.
  - `WarpTarget_MotoMount` : Aligne le bassin sur la selle de `VEH-MOTO-WEWA-01` depuis n'importe quel angle d'approche (`180°` gauche/droite/arrière).

## 2. Synchronisation Frame Data Combat (`GD-05`)
| Montage Asset | Gameplay Tag | Startup (`f`) | Active Hitbox (`ANS_`) | Recovery / Cancel (`f`) |
| :--- | :--- | :--- | :--- | :--- |
| `AM_Machete_Light_01` | `Ability.Melee.LightAttack` | `f01 - f12` | `f13 - f17` (`ANS_MacheteTrace`) | `f18 - f31` (`Cancel dès f20`) |
| `AM_Machete_Heavy_01` | `Ability.Melee.HeavyAttack` | `f01 - f24` | `f25 - f30` (`ANS_HeavyGuardBreak`) | `f31 - f50` |
| `AM_Machete_Parry_01` | `State.Character.Combat.Parrying` | `f01 - f03` | `f04 - f15` (`ANS_ParryDeflect`) | `f16 - f25` |
""",
    ),
    SkillBlueprint(
        skill_id="ART-06",
        description=(
            "Planification et pipeline d'acquisition Motion Capture corporelle et faciale (MetaHuman "
            "Animator) de ZAÏRE. Produit les shotlists de capture, les protocoles de nettoyage des "
            "courbes (zéro patinage des pieds, préservation des contacts) et le retargeting IK Rig "
            "vers le squelette maître SK_Zaire_Master_Humanoid."
        ),
        inputs=("mission-scripts-nar-02", "combat-moveset-gd-05"),
        outputs=("mocap-shotlist.csv", "retargeting-and-cleanup-protocol.md"),
        activation_triggers=(
            "Préparation d'une session de capture de mouvement pour les cinématiques (`NAR-02`), le combat (`GD-05`) ou les attitudes quotidiennes des habitants de Kinshasa (`WLD-02`).",
            "Nettoyage (solving & cleaning) des prises optiques/inertielles et faciales avant livraison à `ART-05`.",
            "Configuration des chaînes `UIKRigDefinition` et `UIKRetargeter` sous UE5.",
        ),
        scope_boundaries=(
            "Ne programme pas la logique d'état des Animation Blueprints (`ART-05`).",
            "Ne livre jamais une prise brute non nettoyée ou dont la pose de départ/fin rompt les boucles de Motion Matching.",
        ),
        operational_procedures=(
            "Extraire des scripts `NAR-02` et des matrices `GD-05` la liste exhaustive des prises requises et les codifier sous le format `MCP_[CAT]_[CHR]_[ACTION]_[TAKE]`.",
            "Renseigner pour chaque prise de la shotlist les accessoires physiques requis sur le plateau (gabarit bois de `VEH-MOTO-WEWA-01`, caisse de `100 cm` exacte pour le vault, machette factice `ITM-WPN-MACHETTE`).",
            "Appliquer le protocole de nettoyage en 4 étapes : (1) Stabilisation des contacts plantaires (0 dérive sur les frames d'appui), (2) Filtrage du bruit haute fréquence sans écraser les impacts de combat, (3) Résolution faciale MetaHuman Animator synchronisée au timecode audio (`AUD-04`), (4) Retargeting IK Rig vers `SK_Zaire_Master_Humanoid`.",
            "Exporter la shotlist et le rapport de contrôle qualité dans `templates/mocap-shotlist-template.csv`.",
        ),
        decision_rules=(
            ("Accessoire de plateau MoCap dont les dimensions diffèrent des métriques WLD-05 (ex: table à 75 cm au lieu de caisse à 100 cm)", "Interdire la prise tant que le praticable physique du plateau n'est pas réglé exactement à 100 cm (spatial-metrics.md)", "Éviter une correction destructive en post-production ART-05"),
            ("Perte d'occlusion de marqueurs lors d'une prise de mêlée rapide", "Reconstruire la trajectoire cinématique en respectant strictement la durée de Startup/Active de GD-05 sans lisser le pic d'accélération de l'impact", "Préserver le punch du Game Feel"),
            ("Décalage de synchronisation labiale > 1 frame entre l'audio lingala/français et la capture faciale", "Réaligner le timecode SMPTE sur la piste audio maîtresse avant l'export des courbes MetaHuman ARKit/Animator", "Garantir la qualité cinématique avec AUD-04"),
        ),
        acceptance_criteria=(
            "100 % des prises de la shotlist indiquent les dimensions exactes des praticables du plateau (`spatial-metrics.md`).",
            "0 dérive des pieds (foot sliding `< 0.5 mm/frame`) sur les phases d'appui verrouillées.",
            "Synchronisation timecode audio/visage vérifiée à `60 fps`.",
        ),
        validation_auditors=("ART-05", "NAR-02", "GD-05"),
        reference_filename="mocap-pipeline-and-retargeting.md",
        reference_content="""# Protocole Motion Capture, Praticables & Retargeting UE5 (`ART-06`)

## 1. Alignement Plateau Physique <-> Métriques UE5 (`spatial-metrics.md`)
Tout praticable utilisé sur le volume de capture doit reproduire au centimètre près les cotes moteur :
- **Module Couvert Bas / Vault** : Hauteur `100 cm`, profondeur `100 cm`.
- **Gabarit Moto Wewa (`VEH-MOTO-WEWA-01`)** : Hauteur de selle `78 cm`, largeur guidon `76 cm`, repose-pieds à `32 cm`.
- **Hauteur de Barre d'Accroche (Ledge Grab)** : `280 cm`.
""",
        template_filename="mocap-shotlist-template.csv",
        template_content="""take_id,category,character_id,action_description,stage_props_cm,target_frames_60fps,facial_capture,target_skill_consumer,status
MCP_CMB_KOFFI_MACHETE_L01,COMBAT,CHR-PROTAG-KOFFI,Taille rapide machette combo 1,Machette factice 65cm,31,Non,ART-05,CONFIRMED
MCP_LOC_KOFFI_VAULT_100,PARKOUR,CHR-PROTAG-KOFFI,Franchissement dynamique une main,Praticable caisse H=100cm L=200cm,33,Non,ART-05,CONFIRMED
MCP_CIN_MSN001_ARRIVEE_01,CINEMATIC,CHR-PROTAG-KOFFI,Saut de la barge sur le quai et appel radio Amina,Rebord barge H=90cm + Oreillette,600,Oui (MetaHuman Animator),NAR-02,CONFIRMED
""",
        example_filename="sample-mocap-shotlist.md",
        example_content="""# Exemple `ART-06` — Shotlist MoCap & Protocole Retargeting Acte I

## 1. Extrait de la Shotlist Validée (`mocap-shotlist.csv`)
| Take ID | Catégorie | Personnage | Description Action | Praticables Plateau (cm) | Frames (60fps) | Capture Faciale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MCP_CMB_KOFFI_MACHETE_L01` | `COMBAT` | `CHR-PROTAG-KOFFI` | Taille rapide machette (`Startup 12f / Active 5f / Recovery 14f`) | Machette factice `65 cm` | `31 f` | Non |
| `MCP_LOC_KOFFI_VAULT_100` | `PARKOUR` | `CHR-PROTAG-KOFFI` | Franchissement rapide caisse portuaire | Module bois `H = 100 cm` | `33 f` | Non |
| `MCP_VEH_KOFFI_WEWA_MOUNT` | `VEHICLE` | `CHR-PROTAG-KOFFI` | Enjambement rapide et démarrage au kick | Gabarit `VEH-MOTO-WEWA-01` (`Selle 78 cm`) | `45 f` | Non |
| `MCP_CIN_MSN001_ARRIVEE_01` | `CINEMATIC` | `CHR-PROTAG-KOFFI` | Accostage au quai N°4 et dialogue radio avec Amina | Quai `H = 90 cm` | `600 f (10s)` | Oui (`MetaHuman Animator` 60fps) |

## 2. Contrôle Qualité Retargeting (`IKRT_Zaire_Humanoid`)
- **Chaînes IK Verrouillées (100 % FK/IK Blend)** : `LeftFoot_IK`, `RightFoot_IK`, `LeftHand_WeaponSocket`, `RightHand_WeaponSocket` (aucun décalage sur le guidon de la Wewa ni sur l'arête de `100 cm`).
""",
    ),
    SkillBlueprint(
        skill_id="ART-07",
        description=(
            "Direction et ingénierie de l'éclairage physique équatorial de Kinshasa sous Unreal Engine 5 "
            "(Lumen Global Illumination, Lumen Reflections, Sky Atmosphere, Volumetric Clouds, Virtual "
            "Shadow Maps). Gère le cycle jour/nuit, la météo tropicale (World.Weather.TropicalStorm), "
            "la mise en valeur des carnations foncées et le budget GPU Lumen <= 4.5 ms."
        ),
        inputs=("art-bible-art-01", "level-blockouts-wld-05", "environment-art-art-02", "gpu-budgets-dir-04"),
        outputs=("lighting-preset-matrix.csv", "equatorial-lighting-spec.md"),
        activation_triggers=(
            "Étalonnage des valeurs photométriques physiques (Lux, Kelvin, EV100) du cycle jour/nuit et des orages tropicaux sur Kinshasa.",
            "Mise en lumière d'un niveau dès la phase de blockout (`WLD-05`, méthodologie Naughty Dog `SRC-011`/`SRC-012`) pour guider naturellement l'œil du joueur.",
            "Optimisation du budget GPU `PERF-GPU-LUMEN` (`<= 4.5 ms` en mode 60 FPS / `<= 7.0 ms` en mode 30 FPS).",
        ),
        scope_boundaries=(
            "Ne modifie pas le code C++/USF interne du moteur de rendu (`ENG-06`).",
            "Interdit de placer plus de **3 sources lumineuses dynamiques projetant des ombres Virtual Shadow Maps (VSM) qui se chevauchent** au même endroit.",
        ),
        operational_procedures=(
            "Configurer l'éclairage en unités photométriques physiques réelles adaptées à la latitude de Kinshasa (`4° Sud`) : Soleil Zénithal à `110 000 Lux` (`5600 K`, `EV100 = 15.0`), Ciel couvert d'orage tropical à `12 000 Lux` (`6800 K`, `EV100 = 11.5`), Nuit urbaine Matonge à `EV100 = 3.5`.",
            "Calibrer la courbe d'Auto-Exposure et la LUT colorimétrique **ACES Filmic** en testant systématiquement le rendu sur les shaders de peau de `CHR-PROTAG-KOFFI` et `CHR-ALLY-AMINA` (`ART-03`) pour préserver le détail des tons foncés et l'éclat spéculaire.",
            "Utiliser le contraste lumineux (ratio d'éclairement `4:1`) pour mettre en évidence les sorties d'arènes et les points de franchissement du blockout `WLD-05`.",
            "Plafonner le rayon d'atténuation (`Attenuation Radius`) et la distance d'ombre (`Shadow Max Draw Distance`) des lampadaires et néons nocturnes pour tenir `PERF-GPU-LUMEN <= 4.5 ms`.",
        ),
        decision_rules=(
            ("Coût GPU Lumen GI + Reflections > 4.5 ms dans une rue nocturne de Matonge", "Désactiver la projection d'ombres VSM sur les néons décoratifs secondaires (conserver uniquement l'émission Lumen Surface Cache) et limiter les ombres VSM aux lampadaires directeurs espacés de >= 18m", "Respecter strictement PERF-GPU-LUMEN"),
            ("Transition intérieur/extérieur aveuglante lors de la sortie d'un hangar vers le soleil équatorial", "Régler la vitesse d'adaptation d'Auto-Exposure (Speed Up = 4.5, Speed Down = 2.5) et utiliser un PostProcessVolume de portail pour pré-adapter l'exposition à 300 cm de la porte", "Garantir une lisibilité permanente en combat/poursuite"),
            ("Carnations des personnages apparaissant sous-exposées lors des dialogues nocturnes", "Activer une Rim Light / Key Light diégétique subtile calée sur la source locale la plus proche (phare de Wewa, enseigne de nganda, brasero)", "Valoriser les visages sans trahir le réalisme"),
        ),
        acceptance_criteria=(
            "Le coût GPU combiné `Lumen GI + Lumen Reflections` est `<= 4.5 ms` (60 FPS) / `<= 7.0 ms` (30 FPS).",
            "Maximum 3 lumières locales avec ombres VSM superposées en tout point de la carte.",
            "Lisibilité validée à 100 % sur les 4 états clés : Aube brumeuse, Zénith équatorial, Orage tropical (`World.Weather.TropicalStorm`), Nuit urbaine.",
        ),
        validation_auditors=("ART-01", "ENG-06", "ENG-07"),
        reference_filename="equatorial-lumen-lighting.md",
        reference_content="""# Photométrie Équatoriale (Kinshasa 4°S) & Budgets Lumen (`ART-07`)

## 1. Matrice Photométrique de Référence (PBR Physical Units)
| État Horaire / Météo | Directional Light (Lux) | Température (K) | Sky Light / Rayleigh | Cible EV100 | Budget GPU Lumen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Aube Fluviale (06h15)** | `18 000 Lux` | `3800 K` (Ambre doux) | Brume Exponential Height Fog dense | `11.8` | `<= 4.2 ms` |
| **Zénith Équatorial (12h30)** | `110 000 Lux` | `5600 K` (Blanc pur) | Ombres verticales très franches | `15.0` | `<= 4.0 ms` |
| **Orage (`TropicalStorm`)** | `9 500 Lux` | `7000 K` (Ardoise froid) | Nuages volumétriques bas + éclairs | `11.0` | `<= 4.5 ms` |
| **Nuit Matonge (21h30)** | `0.25 Lux` (Lune) | `4200 K` + Néons `2200-3200K` | Réflexions Lumen sur bitume humide | `3.5` | `<= 4.5 ms` |
""",
        template_filename="lighting-preset-matrix.csv",
        template_content="""preset_id,district_id,time_of_day,weather_tag,sun_illuminance_lux,color_temp_kelvin,target_ev100,max_overlapping_vsm_lights,lumen_gpu_budget_ms,status
LGT_GOMBE_DAWN_FOG,DST-GOMBE,06:15,CLEAR_FOG,18000,3800,11.8,2,4.2,CONFIRMED
LGT_KIN_NOON_EQUATOR,GLOBAL,12:30,CLEAR_SUN,110000,5600,15.0,1,4.0,CONFIRMED
LGT_MATONGE_NIGHT_NEON,DST-MATONGE,21:30,TROPICAL_RAIN,1,2700,3.5,3,4.5,CONFIRMED
""",
        example_filename="sample-lighting-spec.md",
        example_content="""# Exemple `ART-07` — Éclairage de `LOC-GOMBE-PORT` (Aube) & `DST-MATONGE` (Nuit Pluvieuse)

## 1. Presets Photométriques Validés (`lighting-preset-matrix.csv`)
| Preset ID | Commune | Heure | Météo | Soleil (Lux) | Kelvin | EV100 | Max VSM Superposées | Coût GPU Lumen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `LGT_GOMBE_DAWN_FOG` | `DST-GOMBE` | `06h15` | Brume Fluviale | `18 000 Lux` | `3800 K` | `11.8` | `2` | `4.10 ms` |
| `LGT_MATONGE_NIGHT_RAIN` | `DST-MATONGE` | `21h30` | `World.Weather.TropicalStorm` | `0.25 Lux` | `2700 K` (Néons) | `3.5` | `3` | `4.42 ms` |

## 2. Guidage Visuel Gameplay (`WLD-05` <-> `ART-07`)
- Dans `LOC-GOMBE-PORT` (`MSN-MAIN-001-ARRIVEE`), un projecteur halogène chaud (`3200 K`, `2500 Lumens`) éclaire directement l'échelle de la grue ouest (`+400 cm`) et la rampe où stationne `VEH-MOTO-WEWA-01`, créant un ratio de contraste de `4.5:1` sur la brume bleutée du fleuve.
""",
    ),
    SkillBlueprint(
        skill_id="ART-08",
        description=(
            "Ingénierie Technical Art de ZAÏRE : conception des Master Materials HLSL/Substrate, "
            "prévention de l'explosion des permutations shaders (PSO), rigging mécanique/organique "
            "complexe et profilage des draw calls artistiques entre outils DCC et Unreal Engine 5."
        ),
        inputs=("environment-art-art-02", "character-art-art-03", "3d-standards-art-04", "gpu-budgets-dir-04"),
        outputs=("master-material-specification.md", "shader-pso-budget-guidelines.md"),
        activation_triggers=(
            "Conception ou modification d'un Master Material (`M_Env_Master`, `M_Char_Skin`, `M_Vehicle_Paint`, `M_Water_CongoRiver`).",
            "Réduction du nombre de Pipeline State Objects (PSO) pour éliminer les saccades de compilation shaders.",
            "Création des rigs squelettiques de véhicules (`VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`) et de destruction/vêtements.",
        ),
        scope_boundaries=(
            "Ne programme pas la logique C++ gameplay (`ENG-02`) ni l'infrastructure serveur CI/CD (`ENG-08`).",
            "Interdit l'ajout de nouveaux `StaticSwitchParameter` non autorisés dans les Master Materials (utiliser `CustomPrimitiveData` ou des branches dynamiques uniformes).",
        ),
        operational_procedures=(
            "Restreindre l'ensemble du projet à **8 Master Materials fondamentaux** couvrant 98 % des surfaces via des `UMaterialInstanceConstant` (`MI_`).",
            "Remplacer les `StaticSwitchParameter` par des **Per-Instance Custom Primitive Data** (jusqu'à 32 floats par instance HISM/Nanite) pour varier la couleur, la salissure latéritique et l'humidité sans créer un seul PSO supplémentaire.",
            "Auditer la complexité d'instructions shaders dans le Material Editor (`<= 140 instructions` Pixel Shader pour l'environnement opaque, `<= 220` pour la peau SSS).",
            "Documenter l'architecture de chaque Master Material dans `templates/master-material-spec.md`.",
        ),
        decision_rules=(
            ("Artiste demandant un Static Switch supplémentaire doublant le nombre de permutations PSO d'un Master Material", "Refuser le Static Switch et implémenter l'effet via un masque de canal ou un float CustomPrimitiveData évalué dynamiquement", "Éviter l'explosion combinatoire des PSO ($2^N$)"),
            ("Shader d'environnement dépassant 140 instructions Pixel Shader", "Pré-cuire les opérations mathématiques procédurales lourdes dans une texture ORM/Masque 2K ou basculer le calcul sur les Vertex/Interpolants", "Tenir le budget GPU de rendu ENG-06"),
            ("Rig de véhicule (ex: VEH-MOTO-WEWA-01) comportant plus de 35 os actifs", "Simplifier la hiérarchie osseuse à <= 24 os (châssis, fourche, guidon, bras oscillant, 2 roues, béquille, suspension)", "Optimiser le coût CPU Chaos Vehicles ENG-05"),
        ),
        acceptance_criteria=(
            "Le nombre total de Master Materials du studio reste `<= 10` et le nombre de `StaticSwitch` par Master Material est `<= 3`.",
            "Tous les shaders d'environnement standard respectent le plafond de `140 instructions` Pixel Shader.",
            "Les rigs de véhicules et de personnages passent le test de déformation extrême sans artefact.",
        ),
        validation_auditors=("ENG-06", "ENG-07", "DIR-04"),
        reference_filename="shader-pso-and-rigging-rules.md",
        reference_content="""# Gouvernance des Master Materials, PSO & Rigging (`ART-08`)

## 1. Catalogue des 8 Master Materials Officiels ZAÏRE
| Master Material | Domaine | Max Instructions PS | Max Static Switches | Custom Primitive Data |
| :--- | :--- | :--- | :--- | :--- |
| `M_Zaire_Env_Standard` | Architecture & Props Nanite | `<= 135` | `2` (RVT Blend, Triplanar) | `[0-3]` Tint RGB + Wetness |
| `M_Zaire_Env_Decal` | Signalétique, flaques, graffitis | `<= 95` | `1` | `[0]` Opacity / Wear |
| `M_Zaire_Foliage_Masked` | Végétation tropicale (WPO `<= 35m`) | `<= 140` | `1` | `[0]` Phase vent |
| `M_Zaire_Char_Skin` | Peau humaine Dual-Specular SSS | `<= 215` | `1` | `[0]` Sweat / Rain factor |
| `M_Zaire_Char_Cloth` | Vêtements wax / streetwear / cuir | `<= 150` | `2` | `[0-3]` Pattern Index + Tint |
| `M_Zaire_Hair_Cards` | Coiffures africaines Hair Cards | `<= 165` | `0` | `[0-2]` Melanin / Roughness |
| `M_Zaire_Vehicle_Master` | Carrosseries Wewa, Taxis, Bus | `<= 155` | `1` | `[0-4]` Couleur + Boue latérite |
| `M_Zaire_Water_River` | Fleuve Congo & Bassins portuaires | `<= 190` | `1` | Courant & Turbidité limon |
""",
        template_filename="master-material-spec.md",
        template_content="""# Spécification Master Material & Contrôle PSO (`ART-08`)

- **Nom Master Material** : `M_Zaire_...`
- **Domaine** : `[Environment / Character / Vehicle / Water]`
- **Shading Model / Blend Mode** : `[Default Lit / Subsurface Profile | Opaque / Masked]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Budget Instructions & Permutations PSO
- **Instructions Pixel Shader / Vertex Shader** : `[XXX / XXX]`
- **Texture Samplers Utilisés** : `[<= 6 via Shared:Wrap]`
- **Static Switches Autorisés (`<= 3`)** : `[Liste -> Total permutations = 2^N]`

## 2. Mapping Custom Primitive Data (Zéro PSO Supplémentaire)
| Index Float | Nom Paramètre | Plage Valeurs | Effet Visuel Dynamique |
| :--- | :--- | :--- | :--- |
| `Data[0]` | `TintHueShift` | `[0.0 - 1.0]` | `[Variation sans nouvelle instance]` |
""",
        example_filename="sample-master-material-spec.md",
        example_content="""# Exemple `ART-08` — Spécification de `M_Zaire_Env_Standard`

- **Nom Master Material** : `M_Zaire_Env_Standard`
- **Domaine** : Architecture & Props Modulaires Nanite (`ART-02`, `ENG-04`)
- **Shading Model / Blend Mode** : `Default Lit | Opaque`
- **Statut** : `CONFIRMED`

## 1. Budget Instructions & Permutations PSO
- **Instructions Pixel Shader / Vertex Shader** : `128 PS / 42 VS` (Plafond `<= 140 PS` respecté).
- **Texture Samplers Utilisés** : `4 Samplers` (`BaseColor`, `Normal`, `ORM`, `RVT_TerrainSample` en `Shared:Wrap`).
- **Static Switches Autorisés (`2 switches = 4 PSO max`)** : `bUseRVTBaseBlend`, `bUseWorldAlignedMacroDirt`.

## 2. Mapping Custom Primitive Data (Zéro PSO Supplémentaire)
| Index Float | Nom Paramètre | Plage Valeurs | Effet Visuel Dynamique |
| :--- | :--- | :--- | :--- |
| `Data[0..2]` | `InstanceColorTint` | `RGB [0.2 - 1.0]` | Permet de colorer 500 conteneurs ou façades de `DST-MATONGE` en 1 seul draw call instancié. |
| `Data[3]` | `DynamicWetnessAndMud` | `[0.0 - 1.0]` | Piloté par `World.Weather.TropicalStorm` : fonce l'albédo poreux et abaisse la Roughness à `0.22`. |
""",
    ),
    SkillBlueprint(
        skill_id="ART-09",
        description=(
            "Conception des effets visuels temps réel sous UE5 Niagara : averses équatoriales "
            "(World.Weather.TropicalStorm), éclaboussures de boue latéritique, poussière ocre soulevée "
            "par les motos Wewa, fumées d'échappement et impacts de mêlée dans un budget GPU <= 1.5 ms."
        ),
        inputs=("art-bible-art-01", "combat-design-gd-05", "lighting-and-weather-art-07", "gpu-budgets-dir-04"),
        outputs=("vfx-system-specification.md", "niagara-budget-table.csv"),
        activation_triggers=(
            "Création d'un système de particules Niagara atmosphérique (pluie tropicale, brume du fleuve Congo, poussière de rue à Kalamu).",
            "Conception des effets de combat (`SYS-CMB-MELEE` : étincelles de parade machette `ITM-WPN-MACHETTE`, impacts) et de conduite (`VEH-MOTO-WEWA-01`).",
            "Optimisation de l'overdraw transparent et du budget GPU `PERF-GPU-NIAGARA` (`<= 1.5 ms` en mode 60 FPS).",
        ),
        scope_boundaries=(
            "Ne configure pas l'éclairage global de la scène ni les nuages volumétriques de haute altitude (`ART-07`).",
            "Interdit de superposer plus de **4 couches d'overdraw transparent** plein écran lors des averses ou explosions.",
        ),
        operational_procedures=(
            "Exécuter 100 % des systèmes à grand nombre de particules (pluie, poussière, étincelles) en **Simulation GPU Compute Niagara** avec collisions sur le **Global Distance Field** (zéro raycast CPU par particule).",
            "Découper tous les sprites transparents (fumée, poussière latérite) avec de la **Cutout Geometry (8 sommets)** afin d'éliminer les pixels vides transparents (réduction de l'overdraw de `-45 %`).",
            "Packer les textures de flipbooks en un seul fichier **Channel-Packed** (`R` = Fumée/Densité, `G` = Masque d'érosion, `B` = Émission/Chaleur, `A` = Alpha) limité à `1024x1024` ou `2048x2048`.",
            "Configurer les règles de Scalabilité Niagara (`UNiagaraEffectType` : distance de culling strict, plafond d'instances simultanées et réduction automatique de spawn rate si `PERF-GPU-NIAGARA > 1.3 ms`).",
        ),
        decision_rules=(
            ("Système de pluie tropicale (World.Weather.TropicalStorm) dépassant 1.0 ms GPU à lui seul", "Utiliser une boîte d'émission locale attachée à la caméra (rayon 18m) en GPU Compute + un post-process léger de gouttes lointaines plutôt que de simuler des particules sur tout le quartier", "Maintenir le budget total Niagara <= 1.5 ms"),
            ("Nuage de poussière derrière 10 motos Wewa saturant l'overdraw transparent", "Limiter le nombre d'émetteurs de poussière de roue actifs aux 4 véhicules les plus proches et activer un fondu d'opacité à proximité immédiate de la caméra (< 150 cm)", "Préserver le framerate et la visibilité de conduite"),
            ("Effet d'impact de combat masquant l'animation deStartup de la contre-attaque ennemie", "Limiter la durée de vie des étincelles de parade machette à 0.18s (11 frames) avec dispersion radiale hors du torse de l'ennemi", "Garantir la lisibilité tactique exigée par GD-05"),
        ),
        acceptance_criteria=(
            "Le coût GPU total de tous les systèmes Niagara actifs est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).",
            "100 % des sprites de fumée/poussière utilisent la Cutout Geometry et un plafond de 4 couches d'overdraw.",
            "Tous les systèmes Niagara possèdent un `UNiagaraEffectType` avec distance de culling définie.",
        ),
        validation_auditors=("ENG-07", "GD-05", "ART-07"),
        reference_filename="niagara-gpu-and-overdraw.md",
        reference_content="""# Architecture UE5 Niagara GPU & Contrôle d'Overdraw (`ART-09`)

## 1. Répartition du Budget GPU VFX (`PERF-GPU-NIAGARA <= 1.5 ms`)
| Catégorie VFX | Budget GPU Max | Simulation | Culling Distance | Max Instances Simultanées |
| :--- | :--- | :--- | :--- | :--- |
| **Météo (`NS_Weather_TropicalRain`)** | `<= 0.65 ms` | GPU Compute + Distance Field | Attaché Caméra (`18 m`) | `1 (Global)` |
| **Véhicules (`NS_Veh_LateriteDust`)** | `<= 0.40 ms` | GPU Compute + Cutout 8-verts | `4500 cm (45 m)` | `4 véhicules max` |
| **Combat (`NS_Cmb_MacheteParrySparks`)** | `<= 0.25 ms` | GPU / CPU Burst léger | `2500 cm (25 m)` | `4 impacts max` |
| **Ambiance (`NS_Env_StreetSteam_Smoke`)** | `<= 0.20 ms` | GPU Compute | `3500 cm (35 m)` | `12 sources locales` |
""",
        template_filename="vfx-system-spec.md",
        template_content="""# Spécification Système VFX Niagara (`ART-09`)

- **Nom Système Niagara** : `NS_[CAT]_[SLUG]`
- **Gameplay Tag Déclencheur** : `[World.Weather... / Ability.Melee...]`
- **Budget GPU Alloué** : `[<= X.XX ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture Émetteurs & Optimisation Overdraw
- **Mode de Simulation** : `GPU Compute` | `CPU Burst`
- **Collisions** : `Global Distance Field` | `Analytical Plane`
- **Cutout Geometry & Packing Texture** : `[8-verts Cutout / Texture RGBA]`
- **Distance de Culling & Max Instances (`UNiagaraEffectType`)** : `[XXXX cm | N instances]`
""",
        example_filename="sample-vfx-spec.md",
        example_content="""# Exemple `ART-09` — Spécification de `NS_Weather_TropicalRain` & `NS_Cmb_MacheteParry`

- **Nom Système Niagara** : `NS_Weather_TropicalRain` & `NS_Cmb_MacheteParry`
- **Gameplay Tag Déclencheur** : `World.Weather.TropicalStorm` & `State.Character.Combat.Parrying`
- **Budget GPU Alloué** : `0.62 ms` (Pluie) + `0.18 ms` (Parade) = `0.80 ms` (`<= 1.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Architecture Émetteurs & Optimisation Overdraw
- **`NS_Weather_TropicalRain`** :
  - **Simulation** : `GPU Compute` (12 000 gouttes en boîte caméra `1800 × 1800 × 800 cm`).
  - **Collisions** : Évaluation sur le **Global Distance Field** générant automatiquement les impacts d'éclaboussures sur les toits en tôle, les conteneurs de `LOC-GOMBE-PORT` et la chaussée, tout en gardant les intérieurs et le dessous des auvents (`180 cm` de `DST-MATONGE`) parfaitement secs.
- **`NS_Cmb_MacheteParry`** :
  - **Simulation** : Burst instantané de `35 étincelles chaudes` (`0.18 s` de durée de vie) lors d'une parade réussie avec `ITM-WPN-MACHETTE`, synchronisé sur le Hitstop de `85 ms` (`GD-05`).
  - **Distance de Culling & Max Instances** : `2500 cm | Max 4 instances`.
""",
    ),
)


def build_department_05(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 9 skills du département 05-art-animation."""
    created: list[Path] = []
    for bp in ART_ANIMATION_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_05(WORKSPACE_ROOT)
    print(f"[OK] Département 05-art-animation généré ({len(paths)} skills).")
