"""Spécifications et génération du Département 07-ENGINEERING (ENG-01 à ENG-08)."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools import WORKSPACE_ROOT
from tools.skill_builder import SkillBlueprint, write_skill_from_blueprint

CHECK_PERF_BUDGET_SCRIPT = '''"""Auditeur de budget de performance frametime (P99 <= 16.6 ms / 33.3 ms) et VRAM pour ENG-07."""

from __future__ import annotations

import argparse
import json
import sys


def evaluate_frame_profile(metrics: dict, mode: str = "perf_60fps") -> dict:
    """Compare un relevé de profilage Unreal Insights aux budgets officiels ZAÏRE STUDIO OS."""
    limits = (
        {
            "total_frame_p99_ms": 16.6,
            "cpu_game_thread_ms": 6.5,
            "cpu_npc_ai_ms": 2.5,
            "cpu_mass_crowd_traffic_ms": 2.0,
            "cpu_chaos_physics_ms": 1.5,
            "cpu_animation_ms": 1.8,
            "gpu_lumen_ms": 4.5,
            "gpu_nanite_ms": 2.5,
            "gpu_niagara_vfx_ms": 1.5,
            "vram_used_mb": 6144.0,
        }
        if mode == "perf_60fps"
        else {
            "total_frame_p99_ms": 33.3,
            "cpu_game_thread_ms": 12.0,
            "cpu_npc_ai_ms": 3.0,
            "cpu_mass_crowd_traffic_ms": 2.5,
            "cpu_chaos_physics_ms": 2.0,
            "cpu_animation_ms": 2.5,
            "gpu_lumen_ms": 7.0,
            "gpu_nanite_ms": 4.0,
            "gpu_niagara_vfx_ms": 2.0,
            "vram_used_mb": 8192.0,
        }
    )

    violations: list[str] = []
    for key, max_val in limits.items():
        actual = float(metrics.get(key, 0.0))
        if actual > max_val:
            violations.append(f"{key}: mesuré={actual} > plafond={max_val}")

    return {
        "mode": mode,
        "district_tested": metrics.get("district_id", "DST-MATONGE"),
        "passed": len(violations) == 0,
        "violations": violations,
        "headroom_p99_ms": round(limits["total_frame_p99_ms"] - float(metrics.get("total_frame_p99_ms", 0.0)), 2),
    }


def main() -> int:
    # Sortie console en UTF-8 (accents, glyphes lingala) même sous cp1252 (Windows).
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Audite un profil de performance UE5 (ENG-07).")
    parser.add_argument("--mode", choices=["perf_60fps", "quality_30fps"], default="perf_60fps")
    parser.add_argument("--file", help="Chemin d'un fichier JSON de capture Unreal Insights à auditer (optionnel)")
    args = parser.parse_args()

    if args.file:
        from pathlib import Path
        sample_capture = json.loads(Path(args.file).read_text(encoding="utf-8"))
    else:
        sample_capture = {
            "district_id": "DST-MATONGE",
            "total_frame_p99_ms": 15.85,
            "cpu_game_thread_ms": 5.9,
            "cpu_npc_ai_ms": 2.1,
            "cpu_mass_crowd_traffic_ms": 1.75,
            "cpu_chaos_physics_ms": 1.25,
            "cpu_animation_ms": 1.55,
            "gpu_lumen_ms": 4.25,
            "gpu_nanite_ms": 2.2,
            "gpu_niagara_vfx_ms": 1.15,
            "vram_used_mb": 5620.0,
        }
    report = evaluate_frame_profile(sample_capture, args.mode)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
'''

ENGINEERING_BLUEPRINTS: tuple[SkillBlueprint, ...] = (
    SkillBlueprint(
        skill_id="ENG-01",
        description=(
            "Architecture C++20 fondamentale sous Unreal Engine 5 : World Partition, Data Layers, "
            "One File Per Actor (OFPA), Hierarchical LOD (HLOD), Subsystems modulaires et streaming "
            "asynchrone (FStreamableManager / TSoftObjectPtr) garantissant zéro chargement bloquant."
        ),
        inputs=("technical-adr-dir-04", "open-world-grid-wld-04", "3d-pipeline-norms-art-04"),
        outputs=("ue5-cpp-architecture-spec.md", "world-partition-streaming-config.md"),
        activation_triggers=(
            "Conception d'un nouveau `UGameInstanceSubsystem`, `UWorldSubsystem` ou module C++ UE5.",
            "Configuration de la grille spatiale `World Partition` (`12800 cm`), des `Data Layers` et des rayons de streaming pour Kinshasa.",
            "Revue de code C++ pour vérifier l'application stricte de la règle Zero Synchronous Loading (`PERF-CPU-GAME <= 6.5 ms`).",
        ),
        scope_boundaries=(
            "N'implémente pas les capacités individuelles de combat ou de mission (`ENG-02`) ni les shaders RHI bas niveau (`ENG-06`).",
            "Interdit formellement tout appel à `LoadSynchronous()`, `FlushAsyncLoading()` ou `ConstructorHelpers::FObjectFinder` en cours de gameplay.",
        ),
        operational_procedures=(
            "Structurer la logique globale du monde en `UWorldSubsystem` découplés (`UZaireDistrictStreamingSubsystem`, `UZaireTimeWeatherSubsystem`) sans dépendance circulaire entre modules `.Build.cs`.",
            "Configurer `World Partition` avec une grille principale `MainGrid` (taille de cellule `12800 cm`, rayon de chargement `25600 cm` à pied / `38400 cm` en `VEH-MOTO-WEWA-01`) et une grille `LowResGrid` pour les Landmarks Tier 1 (`LOC-LIMETE-ECHANGEUR`).",
            "Imposer l'utilisation exclusive de `TSoftObjectPtr<T>`, `FPrimaryAssetId` et `UAssetManager::GetStreamableManager().RequestAsyncLoad()` avec callback non bloquant.",
            "Documenter les contrats d'en-têtes C++20 et la configuration `.ini` dans `templates/ue5-architecture-spec.md`.",
        ),
        decision_rules=(
            ("Présence d'un appel LoadSynchronous() ou d'une référence Hard Pointer UPROPERTY() vers un asset lourd dans un Blueprint/C++", "Remplacer immédiatement le pointeur dur par un TSoftObjectPtr<T> chargé via FStreamableManager avant d'activer l'acteur", "Éliminer tout hitch > 2 ms sur le Game Thread"),
            ("Transition rapide en moto Wewa (95 km/h) provoquant un retard de chargement de cellule World Partition", "Activer un Streaming Source secondaire prédictif projeté à +4000 cm en avant du vecteur vitesse du véhicule", "Prévenir tout trou géométrique ou pop-in à haute vitesse"),
            ("Conflit de verrouillage de fichiers entre deux level designers travaillant sur la même commune", "Vérifier l'activation obligatoire de One File Per Actor (OFPA) et isoler les acteurs de mission dans un Data Layer dédié", "Permettre le travail parallèle sans conflit Git LFS / Perforce"),
        ),
        acceptance_criteria=(
            "0 appel `LoadSynchronous()` dans le code runtime ; 100 % des chargements passent par `UAssetManager` / `FStreamableManager`.",
            "Le coût Game Thread global (`PERF-CPU-GAME`) reste `<= 6.5 ms` lors du franchissement de frontière entre deux communes (`DST-GOMBE` -> `DST-KALAMU`).",
            "Configuration World Partition + HLOD validée sur les vitesses de déplacement à pied et en `VEH-MOTO-WEWA-01`.",
        ),
        validation_auditors=("DIR-04", "ENG-07"),
        reference_filename="ue5-world-partition-and-async.md",
        reference_content="""# Architecture C++20 UE5 : World Partition & Streaming Asynchrone (`ENG-01`)

## 1. Configuration des Grilles World Partition (`SYS-WLD-STREAMING`)
| Nom Grille | Taille Cellule (cm) | Rayon Chargement (cm) | Contenu Cible | Stratégie HLOD |
| :--- | :--- | :--- | :--- | :--- |
| `MainGrid_Kinshasa` | `12800 cm (128 m)` | `25600 cm (256 m)` | Architecture modulaire (`ART-02`), Couverts, Routes | `HLOD0_Instanced` -> `HLOD1_MergedMesh` |
| `PropsAndInteriorGrid` | `6400 cm (64 m)` | `12800 cm (128 m)` | Props intérieurs, étals de marché, petits débris | Culled hors rayon (Pas de HLOD) |
| `LandmarkMacroGrid` | `51200 cm (512 m)` | `153600 cm (1.53 km)` | `LOC-LIMETE-ECHANGEUR`, Grues `LOC-GOMBE-PORT` | `HLOD_AlwaysLoaded_LowPoly` |

## 2. Pattern C++20 Obligatoire de Chargement Asynchrone
```cpp
void UZaireStreamingSubsystem::RequestDistrictAssets(const TArray<FSoftObjectPath>& AssetsToLoad, FSimpleDelegate OnLoaded)
{
    FStreamableManager& Streamable = UAssetManager::GetStreamableManager();
    ActiveHandle = Streamable.RequestAsyncLoad(AssetsToLoad, MoveTemp(OnLoaded), FStreamableManager::DefaultAsyncLoadPriority);
}
```
""",
        template_filename="ue5-architecture-spec.md",
        template_content="""# Spécification d'Architecture C++20 Unreal Engine 5 (`ENG-01`)

- **Module / Subsystem** : `ZaireCore` | `UZaire...Subsystem`
- **Système Associé** : `SYS-...`
- **Budget Game Thread (`PERF-CPU-GAME`)** : `<= 6.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture des Classes C++ & Dépendances Modules
- **Classe Principale** : `U...` (Héritage, cycle de vie)
- **Gestion Mémoire & Streaming** : `[TSoftObjectPtr / FStreamableManager]`

## 2. Configuration World Partition & Data Layers
| Data Layer | Type (`Runtime` / `Editor`) | Condition d'Activation | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `DL_...` | `Runtime` | `[Gameplay Tag / État Quête]` | `[XX MB]` |
""",
        example_filename="sample-ue5-architecture-spec.md",
        example_content="""# Exemple `ENG-01` — Architecture de `UZaireDistrictStreamingSubsystem` (`SYS-WLD-STREAMING`)

- **Module / Subsystem** : `ZaireWorldRuntime` | `UZaireDistrictStreamingSubsystem : public UWorldSubsystem`
- **Système Associé** : `SYS-WLD-STREAMING`
- **Budget Game Thread (`PERF-CPU-GAME`)** : `0.45 ms` mesuré (inclus dans `<= 6.5 ms`)
- **Statut** : `CONFIRMED`

## 1. Architecture des Classes C++ & Dépendances Modules
- **Classe Principale** : `UZaireDistrictStreamingSubsystem` pilote l'activation asynchrone des `UDataLayerAsset` selon la progression des missions (`MSN-*`) et projette une `FWorldPartitionStreamingSource` anticipée de `+4000 cm` lorsque le joueur pilote `VEH-MOTO-WEWA-01` à plus de `50 km/h`.
- **Gestion Mémoire & Streaming** : Zéro pointeur dur vers les acteurs de mission ; pré-chargement asynchrone déclenché `180 m` avant l'entrée dans l'arène `LOC-GOMBE-PORT`.

## 2. Configuration World Partition & Data Layers
| Data Layer | Type | Condition d'Activation | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `DL_Gombe_Port_Base` | `Runtime` | Permanent dans le rayon `256 m` de `LOC-GOMBE-PORT` | `420 MB` |
| `DL_MSN001_SyndicateAlert` | `Runtime` | Actif uniquement pendant `MSN-MAIN-001-ARRIVEE` | `115 MB` |
| `DL_Matonge_NightMarket` | `Runtime` | Heure `[18h00 - 04h00]` dans `World.District.Matonge` | `280 MB` |
""",
    ),
    SkillBlueprint(
        skill_id="ENG-02",
        description=(
            "Programmation C++20 des systèmes de gameplay sous Unreal Engine 5 : Gameplay Ability "
            "System (GAS : UAbilitySystemComponent, UGameplayAbility, UAttributeSet), Enhanced Input, "
            "composants modulaires d'interaction, caméra 3e personne et intégration Common UI."
        ),
        inputs=("system-design-gd-01", "mission-state-machines-gd-02", "combat-frame-data-gd-05", "vehicle-specs-gd-06", "ue5-architecture-eng-01"),
        outputs=("gameplay-cpp-specification.md", "gas-attributes-and-abilities-header.h"),
        activation_triggers=(
            "Implémentation C++ d'une capacité de combat (`SYS-CMB-MELEE`), d'infiltration (`SYS-STEALTH`), de parkour (`Ability.Movement.Vault`) ou d'interaction véhicule (`VEH-MOTO-WEWA-01`).",
            "Exposition de fonctions C++ déterministes et performantes aux designers (`BlueprintCallable` / `BlueprintPure` sans logique lourde en Blueprint Tick).",
            "Implémentation de la caméra 3e personne évitant tout clipping dans les couloirs de `>= 350 cm` (`WLD-05`).",
        ),
        scope_boundaries=(
            "Ne développe pas les plugins d'automatisation éditeur (`ENG-03`) ni les passes de rendu RHI (`ENG-06`).",
            "Interdit l'utilisation du `Event Tick` en Blueprint pour de la logique gameplay continue (toute logique tickée critique est écrite en C++ natif ou pilotée par événements Gameplay Tags).",
        ),
        operational_procedures=(
            "Implémenter chaque action de `CHR-PROTAG-KOFFI` comme une sous-classe C++ de `UZaireGameplayAbility` configurée avec ses `ActivationOwnedTags`, `CancelAbilitiesWithTag` et `BlockAbilitiesWithTag` issus de `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.",
            "Centraliser les statistiques de combat et d'endurance dans `UZaireCombatAttributeSet` (`Health`, `MaxHealth`, `Stamina`, `Poise`, `ParryWindowMs`) avec validation dans `PreAttributeChange` et `PostGameplayEffectExecute`.",
            "Coder le `UZaireSpringArmComponent` de caméra avec multi-whisker raycasts prédictifs pour glisser sans à-coup le long des murs de `350 cm` (`WLD-05`).",
            "Documenter les signatures C++ et les contrats d'interface dans `templates/gameplay-cpp-spec.md`.",
        ),
        decision_rules=(
            ("Logique de combat ou de machine à états implémentée dans un Event Tick Blueprint consommant > 0.3 ms", "Migrer immédiatement la logique en C++ natif ou la convertir en Timer/Delegate déclenché par changement de FGameplayTag", "Maintenir un Game Thread propre et déterministe"),
            ("Fenêtre de parade (State.Character.Combat.Parrying) sensible aux fluctuations de framerate", "Évaluer la fenêtre d'impact en temps réel continu (DeltaSeconds / ServerWorldTime) avec buffer d'input Enhanced Input de 120 ms", "Garantir la précision < 100 ms exigée par GD-05"),
            ("Destruction ou sortie imprévue d'un véhicule pendant une GameplayAbility de conduite", "Forcer l'exécution de EndAbility() sur le callback OnVehicleDestroyed/OnExitVehicle pour nettoyer tous les Gameplay Tags actifs", "Prévenir tout blocage d'état (soft-lock GD-02)"),
        ),
        acceptance_criteria=(
            "100 % des capacités utilisent des `FGameplayTag` typés (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`) sans chaînes magiques (`FName` codés en dur).",
            "0 logique gameplay lourde dans le `Tick` Blueprint ; code C++ compilable sans warning au niveau `/W4`.",
            "Couverture par tests fonctionnels automatisés (`PRD-05`) sur l'activation, l'annulation et le nettoyage des capacités.",
        ),
        validation_auditors=("ENG-01", "PRD-05", "DIR-05"),
        reference_filename="gas-and-enhanced-input-cpp.md",
        reference_content="""# Architecture C++ UE5 Gameplay Ability System & Enhanced Input (`ENG-02`)

## 1. Déclaration Native des Gameplay Tags (`ZaireGameplayTags.h`)
Tous les tags de `knowledge/technical-specs/gameplay-tags-taxonomy.csv` sont enregistrés en C++ natif :
```cpp
namespace ZaireGameplayTags
{
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Character_Combat_Engaged);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Character_Combat_Parrying);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Character_Stealth_Concealed);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(State_Character_Stealth_Disguised);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Melee_LightAttack);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Melee_HeavyAttack);
    UE_DECLARE_GAMEPLAY_TAG_EXTERN(Ability_Movement_Vault);
}
```
""",
        template_filename="gameplay-cpp-spec.md",
        template_content="""# Spécification d'Implémentation C++ Gameplay & GAS (`ENG-02`)

- **Classe C++** : `UZaireGA_...` | `UZaire...Component`
- **Système Game Design Source** : `SYS-...` (`GD-01`..`GD-07`)
- **Budget CPU Tick** : `0.0 ms (Event-Driven)` | `[<= 0.15 ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Contrat de Classe C++20 & Configuration GAS
```cpp
UCLASS()
class ZAIREGAME_API UZaireGA_Example : public UZaireGameplayAbility
{
    GENERATED_BODY()
    // ...
};
```

## 2. Sécurité d'État & Nettoyage (`EndAbility` / Anti-Soft-Lock)
- **Tags Octroyés (`ActivationOwnedTags`)** : `[Tags]`
- **Tags Annulés (`CancelAbilitiesWithTag`)** : `[Tags]`
- **Garantie de Nettoyage sur Interruption** : `[Comportement EndAbility]`
""",
        example_filename="sample-gameplay-cpp-spec.md",
        example_content="""# Exemple `ENG-02` — Implémentation C++ de `UZaireGA_MeleeParry` (`SYS-CMB-MELEE`)

- **Classe C++** : `UZaireGA_MeleeParry : public UZaireGameplayAbility`
- **Système Game Design Source** : `SYS-CMB-MELEE` (`GD-05`) & `ITM-WPN-MACHETTE`
- **Budget CPU Tick** : `0.0 ms (100 % Event-Driven par AnimNotifyState & GameplayEvents)`
- **Statut** : `CONFIRMED`

## 1. Contrat de Classe C++20 & Configuration GAS
```cpp
UCLASS()
class ZAIREGAME_API UZaireGA_MeleeParry : public UZaireGameplayAbility
{
    GENERATED_BODY()
public:
    UZaireGA_MeleeParry();
    virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
    virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;

protected:
    UFUNCTION()
    void OnIncomingStrikeDeflected(FGameplayEventData Payload);

    UPROPERTY(EditDefaultsOnly, Category = "Zaire|Combat")
    float PerfectParryHitstopSeconds = 0.085f; // 85 ms (GD-05)
};
```

## 2. Sécurité d'État & Nettoyage (`EndAbility` / Anti-Soft-Lock)
- **Tags Octroyés** : `State.Character.Combat.Parrying` pendant la fenêtre active (`frames 4 à 15` à 60 FPS).
- **Tags Annulés** : Annule la phase `Recovery` de `Ability.Melee.LightAttack` dès la frame 20 (`GD-05`).
- **Garantie de Nettoyage** : Si `EndAbility` est appelé suite à une chute ou une explosion pendant le Hitstop (`0.085 s`), le `CustomTimeDilation` de Koffi et de l'assaillant est systématiquement restauré à `1.0f`.
""",
    ),
    SkillBlueprint(
        skill_id="ENG-03",
        description=(
            "Développement des outils éditeur Unreal Engine 5 (C++ Slate, UEditorValidatorBase, "
            "Editor Utility Widgets, API Python UE5) et automatisation des contrôles pré-commit. "
            "Applique la philosophie Immutable Data & Fast Iteration pour bloquer tout asset non conforme "
            "avant son entrée dans le dépôt."
        ),
        inputs=("3d-validation-rules-art-04", "ue5-architecture-eng-01"),
        outputs=("editor-validator-spec.md", "ue5-python-automation-script.py"),
        activation_triggers=(
            "Implémentation dans l'éditeur UE5 des règles de validation géométriques et textures définies par `ART-04` (`asset-validation-rules.json`).",
            "Création d'un outil d'assistance au placement ou à l'audit des métriques spatiales (`WLD-05`) et des identifiants du registre (`PRD-03`).",
            "Automatisation par lots (batch processing) de la configuration des LODs, collisions ou Custom Primitive Data.",
        ),
        scope_boundaries=(
            "N'écrit pas de code exécuté dans le build client final (tous les modules d'outils sont isolés en `Type: Editor` dans le `.uplugin`/`.uproject`).",
            "Ne modifie jamais silencieusement un asset en cours d'édition sans journaliser l'action et offrir une prévisualisation sèche (`--dry-run`).",
        ),
        operational_procedures=(
            "Dériver des sous-classes C++ de `UEditorValidatorBase` (`UZaireNamingAndNaniteValidator`, `UZaireTexturePackingValidator`, `UZaireSoftPointerValidator`) exécutées automatiquement lors du `Save` et du `Submit` Perforce/Git.",
            "Lire les seuils directement depuis le fichier de configuration externalisé `asset-validation-rules.json` (`ART-04`) sans coder de constantes magiques en dur.",
            "Fournir aux artistes et level designers une action de correction en un clic (*Auto-Fix*) pour les erreurs mécaniques simples (ex: décocher `sRGB` sur une texture `_ORM`, activer `Nanite` sur un `SM_Kit_*` opaque).",
            "Documenter le validateur dans `templates/editor-tool-spec.md`.",
        ),
        decision_rules=(
            ("Artiste tentant de soumettre un Static Mesh Nanite avec un matériau Translucide ou une texture non puissance de 2", "Faire échouer le DataValidationSubsystem (EDataValidationResult::Invalid) et afficher un message explicite indiquant l'asset, la règle ART-04 violée et la procédure de correction", "Bloquer 100 % des régressions avant le commit"),
            ("Opération manuelle répétitive identifiée sur plus de 20 assets (ex: assignation des ChaosPhysicalMaterial sur les kits routiers)", "Écrire un script Python UE5 idempotent utilisant unreal.EditorAssetLibrary avec support --dry-run", "Réduire le temps d'itération de l'équipe Art/World"),
            ("Outil éditeur introduisant une dépendance dans le module Runtime du jeu", "Déplacer immédiatement le code dans le module ZaireEditor (TargetType::Editor uniquement)", "Empêcher tout alourdissement ou échec de compilation du build client ENG-08"),
        ),
        acceptance_criteria=(
            "Les validateurs `UEditorValidatorBase` interceptent 100 % des violations définies par `ART-04` et `ENG-01`.",
            "Tous les modules d'outils sont strictement bornés à l'environnement `Editor`.",
            "Chaque erreur retournée à l'utilisateur contient le code de la règle et la solution actionnable.",
        ),
        validation_auditors=("DIR-04", "ART-04", "ENG-01"),
        reference_filename="ue5-data-validation-and-tools.md",
        reference_content="""# Architecture des Validateurs Pré-Commit UE5 (`ENG-03`)

## 1. Liste des Validateurs Automatisés (`UDataValidationSubsystem`)
1. `UZaireAssetNamingValidator` : Vérifie les préfixes `SM_`, `SK_`, `M_`, `MI_`, `T_`, `NS_`, `BP_`.
2. `UZaireNaniteAndMaterialValidator` : Interdit `BLEND_Translucent` sur Nanite et vérifie que `WPO Disable Distance <= 3500 cm`.
3. `UZaireTextureORMValidator` : Vérifie les dimensions puissances de 2 et force `sRGB = false` + `TC_Masks` sur le suffixe `_ORM`.
4. `UZaireHardReferenceValidator` : Scanne les Blueprints de quête/monde pour interdire les références dures vers des acteurs hors Data Layer courant.
""",
        template_filename="editor-tool-spec.md",
        template_content="""# Spécification d'Outil Éditeur & Validateur UE5 (`ENG-03`)

- **Nom du Validateur / Outil** : `UZaire...Validator` | `EUW_Zaire_...`
- **Module Cible** : `ZaireEditor (Type: Editor)`
- **Règles Métier Appliquées** : `[ART-04 / ENG-01 / WLD-05]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Logique de Validation & Auto-Fix
- **Condition d'Activation (`CanValidateAsset`)** : `[Classes UObject ciblées]`
- **Contrôles Exécutés (`ValidateLoadedAsset`)** : `[Règles déterministes]`
- **Action Auto-Fix Disponible** : `[Correction automatique proposée]`
""",
        example_filename="sample-editor-tool-spec.md",
        example_content="""# Exemple `ENG-03` — Validateur `UZaireNaniteAndTextureValidator`

- **Nom du Validateur / Outil** : `UZaireNaniteAndTextureValidator : public UEditorValidatorBase`
- **Module Cible** : `ZaireEditor (Type: Editor)`
- **Règles Métier Appliquées** : `ART-04 (asset-validation-rules.json)`
- **Statut** : `CONFIRMED`

## 1. Logique de Validation & Auto-Fix
- **Condition d'Activation (`CanValidateAsset`)** : S'exécute sur tout `UStaticMesh` et `UTexture2D` situé sous `/Game/Zaire/Art/` et `/Game/Zaire/World/`.
- **Contrôles Exécutés (`ValidateLoadedAsset`)** :
  1. Si `UStaticMesh` a `NaniteSettings.bEnabled == true` : parcourt `StaticMaterials` et retourne `EDataValidationResult::Invalid` si un matériau utilise `BLEND_Translucent` ou si `WorldPositionOffsetDisableDistance > 3500.0f`.
  2. Si `UTexture2D` se termine par `_ORM` : vérifie que `SRGB == false` et que `CompressionSettings == TC_Masks`.
- **Action Auto-Fix Disponible** : Menu contextuel *"Zaire Studio OS -> Fix ORM Texture Compression & WPO Cull Distance (3500 cm)"*.
""",
    ),
    SkillBlueprint(
        skill_id="ENG-04",
        description=(
            "Ingénierie procédurale sous SideFX Houdini (HDA / PDG TOPs) et Unreal Engine 5 PCG "
            "(Procedural Content Generation). Transforme les données OpenStreetMap/DEM et les règles "
            "d'urbanisme de Kinshasa (WLD-03) en réseaux routiers ZoneGraph (AI-03), îlots modulaires "
            "HISM/Nanite (ART-02), câblages aériens et végétation déterministes."
        ),
        inputs=("urban-typology-wld-03", "modular-kits-art-02", "traffic-zonegraph-rules-ai-03"),
        outputs=("hda-pcg-pipeline-spec.md", "procedural-generation-rules.csv"),
        activation_triggers=(
            "Génération ou mise à jour procédurale d'une commune de Kinshasa (`DST-*`) à partir des tracés routiers OSM et des gabarits `WLD-03`.",
            "Assemblage automatique des façades modulaires (`ART-02`) par îlots urbains (méthodologie Insomniac Games `SRC-008` & Epic City Sample `SRC-004`).",
            "Génération automatique des splines `ZoneGraph` (voies véhicules `350-400 cm`, sous-voies Wewa `130-150 cm`, trottoirs piétons `AI-02`).",
        ),
        scope_boundaries=(
            "N'altère jamais les monuments héroïques sculptés sur mesure (`LOC-LIMETE-ECHANGEUR`) ni les arènes de mission en blockout manuel (`WLD-05`).",
            "Interdit toute génération non déterministe (tout graphe HDA/PCG doit utiliser un `GlobalSeed` fixe reproductible à 100 %).",
        ),
        operational_procedures=(
            "Étape 1 (Réseau Viaire & ZoneGraph) : Ingérer les courbes OSM dans le HDA `HDA_Zaire_RoadNetwork`, extruder les chaussées aux cotes exactes de `WLD-03` et exporter simultanément les meshes routiers et les tags de voies `ZoneGraph` pour `AI-02`/`AI-03`.",
            "Étape 2 (Subdivision Parcellaire & Bâti) : Subdiviser les îlots en lots (`1200 cm` de façade à Matonge), en excluant automatiquement tout volume couvert par un tag `PCG_Exclusion_ManualLevelDesign` (`WLD-05`).",
            "Étape 3 (Instanciation Nanite & Custom Data) : Peupler les façades via des `UHierarchicalInstancedStaticMeshComponent` (HISM) / `PCG Static Mesh Spawner` en injectant les variations de couleur et d'usure dans `CustomPrimitiveData[0..3]` (`ART-08`).",
            "Étape 4 (Habillage Secondaire PCG) : Générer les poteaux électriques, câbles caténaires, étals de rue et végétation tropicale en respectant la marge libre minimale de `350 cm` sur les cheminements piétons.",
        ),
        decision_rules=(
            ("Intersection entre un îlot procédural Houdini/PCG et un blockout de mission WLD-05 (ex: LOC-GOMBE-PORT)", "Prioriser à 100 % le volume manuel WLD-05 via un Box Volume taggé PCG_Exclude_ManualArena qui soustrait les points PCG dans son empreinte", "Garantir zéro obstacle procédural dans une arène de mission"),
            ("Secteur dont la couverture OSM des ruelles secondaires est incomplète (ex: DST-MASINA en RESEARCH_REQUIRED)", "Appliquer l'algorithme de subdivision L-System / Voronoï orthogonal calibré par WLD-03 uniquement sur un Data Layer de prévisualisation taggé PROPOSED_PROCEDURAL", "Séparer clairement la donnée SIG vérifiée du remplissage procédural"),
            ("Génération d'îlot créant plus de 1500 acteurs individuels dans l'Outliner UE5", "Fusionner les descripteurs d'instances par cellule World Partition (128m) dans des composants Instanced Static Mesh (ISM/HISM) packés", "Maintenir un coût d'instanciation minimal en mémoire et en draw calls"),
        ),
        acceptance_criteria=(
            "Génération 100 % déterministe à seed fixe (`GlobalSeed = 19600630`).",
            "Les splines `ZoneGraph` générées respectent les largeurs de voies (`350-400 cm`) et les couloirs inter-files Wewa (`>= 130 cm`).",
            "Respect absolu des volumes d'exclusion `WLD-05` (zéro prop procédural sur un chemin critique ou un couvert).",
        ),
        validation_auditors=("WLD-04", "ENG-07", "AI-03"),
        reference_filename="houdini-pdg-and-ue5-pcg.md",
        reference_content="""# Pipeline Procédural Hybride : SideFX Houdini PDG -> UE5 PCG (`ENG-04`)

## 1. Répartition des Responsabilités Houdini (Offline PDG) vs UE5 PCG (In-Engine)
- **SideFX Houdini 20.5+ (HDA / PDG TOP Network)** :
  - Nettoyage topologique des graphes routiers OpenStreetMap et projection sur le MNT (DEM) du bassin du fleuve Congo.
  - Calcul géométrique lourd des carrefours complexes (`LOC-MATONGE-VICTOIRE`, bretelles de `LOC-LIMETE-ECHANGEUR`) et génération des profils `ZoneGraph`.
  - Subdivision des îlots urbains en lots orientés et export de **Point Clouds `.pcg` / Alembics légers** dotés d'attributs (`@kit_id`, `@floor_count`, `@district_tint`).
- **Unreal Engine 5 PCG Framework (Runtime / Editor Graphs)** :
  - Lecture des Point Clouds Houdini et instanciation directe des meshes Nanite (`ART-02`) avec injection de `CustomPrimitiveData`.
  - Adaptation dynamique locale aux volumes d'exclusion `WLD-05` et au matériau RVT du terrain.
""",
        template_filename="hda-pipeline-spec.md",
        template_content="""# Spécification Pipeline Procédural Houdini HDA & UE5 PCG (`ENG-04`)

- **Nom de l'Outil HDA / Graphe PCG** : `HDA_Zaire_...` | `PCG_Zaire_...`
- **Commune / Typologie Cible (`WLD-03`)** : `DST-...` (`TYP-...`)
- **Global Seed Déterministe** : `19600630`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Attributs du Nuage de Points (Houdini -> UE5 PCG)
| Nom Attribut | Type | Source (`WLD-03` / OSM) | Utilisation dans UE5 PCG / ZoneGraph |
| :--- | :--- | :--- | :--- |
| `@kit_piece_id` | `string` | Règle façade | Sélectionne le `SM_Kit_*` dans la DataTable `ART-02`. |

## 2. Règles d'Exclusion Gameplay (`WLD-05`) & Optimisation Instances
- **Tags de Volumes d'Exclusion** : `PCG_Exclude_ManualArena`, `PCG_Exclude_NavPath_350cm`
- **Regroupement d'Instances** : `ISM packé par cellule World Partition de 12800 cm`
""",
        example_filename="sample-hda-pcg-spec.md",
        example_content="""# Exemple `ENG-04` — Génération Procédurale des Îlots et Routes de `DST-MATONGE`

- **Nom de l'Outil HDA / Graphe PCG** : `HDA_Zaire_UrbanBlock_Gen` & `PCG_Matonge_StreetDressing`
- **Commune / Typologie Cible (`WLD-03`)** : `DST-MATONGE` (`TYP-MATONGE-COMM`)
- **Global Seed Déterministe** : `19600630`
- **Statut** : `CONFIRMED`

## 1. Attributs du Nuage de Points (Houdini -> UE5 PCG)
| Nom Attribut | Type | Source (`WLD-03` / OSM) | Utilisation dans UE5 PCG / ZoneGraph |
| :--- | :--- | :--- | :--- |
| `@road_lane_width` | `float` | `350.0` ou `380.0 cm` | Génère les voies véhicules `ZoneGraph` et insère une sous-voie Wewa (`150 cm`) entre deux files. |
| `@building_floors` | `int` | `1 à 3` (`TYP-MATONGE-COMM`) | Empile un RDC commercial (`400 cm` avec auvent `180 cm`) + `0 à 2` étages (`350 cm`). |
| `@cpd_tint_rgb` | `vector3` | Palette `ART-01` Matonge | Écrit directement dans `CustomPrimitiveData[0..2]` de `M_Zaire_Env_Standard` (0 PSO ajouté). |

## 2. Règles d'Exclusion Gameplay (`WLD-05`) & Optimisation Instances
- **Exclusion** : Toute arène de mission ou trottoir principal applique un filtre `Difference` dans le graphe PCG garantissant un couloir piéton libre de `>= 350 cm` exempt de poteaux ou d'étals.
- **Performance** : Un îlot complet de `80 m × 45 m` est compilé en seulement `14 composants ISM Nanite` par cellule de `128 m`.
""",
    ),
    SkillBlueprint(
        skill_id="ENG-05",
        description=(
            "Ingénierie de la simulation physique temps réel sous UE5 Chaos Physics, Chaos Vehicles, "
            "Chaos Destruction et Chaos Cloth (SYS-PHYS-CHAOS). Gère la matrice des canaux de collision, "
            "l'Async Physics Tick, la mise en sommeil agressive des débris et le budget CPU <= 1.5 ms."
        ),
        inputs=("vehicle-handling-specs-gd-06", "environment-kits-art-02", "cpu-budgets-dir-04"),
        outputs=("chaos-physics-specification.md", "collision-channels-matrix.csv"),
        activation_triggers=(
            "Implémentation du modèle physique Chaos des véhicules kinois (`VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`, `VEH-BUS-TRANSCO-01`).",
            "Configuration des éléments destructibles urbains (étals de marché en bois, barrières portuaires, poteaux) via Chaos Geometry Collections.",
            "Optimisation des profils de collision et du budget CPU `PERF-CPU-CHAOS` (`<= 1.5 ms` en mode 60 FPS).",
        ),
        scope_boundaries=(
            "Ne modifie pas le design ludique des vitesses cibles (`GD-06`), mais implémente les paramètres de solveur qui les rendent stables et sans tremblement (jitter).",
            "Interdit l'utilisation de `Complex Collision as Simple` (Triangle Mesh Collision) sur tout objet mobile ou prop de décor standard.",
        ),
        operational_procedures=(
            "Activer l'**Async Physics Tick** (`p.Chaos.AsyncPhysics = 1` à `60 Hz` fixe) afin de découpler la stabilité des suspensions de `VEH-MOTO-WEWA-01` des variations de frametime rendu.",
            "Restreindre la matrice des canaux de collision (`DefaultEngine.ini`) aux profils strictement nécessaires (`Pawn`, `Vehicle`, `WorldStatic`, `WorldDynamic`, `CombatHitbox`, `Visibility`, `Camera`) en désactivant les tests croisés inutiles (ex: débris légers ignorent les autres débris et la caméra).",
            "Configurer les **Geometry Collections (Chaos Destruction)** des props destructibles avec un maximum de `18 fragments convexes` par prop, une mise en sommeil forcée (`Sleep Threshold`) après `1.2 seconde` et une disparition par rétrécissement (fade-out) après `4.0 secondes`.",
            "Assigner à chaque matériau de surface l'un des 5 `UChaosPhysicalMaterial` officiels (`PM_Asphalt_Dry`, `PM_Asphalt_Wet`, `PM_Laterite_Dry`, `PM_Laterite_Mud`, `PM_Corrugated_Iron`).",
        ),
        decision_rules=(
            ("Véhicule Wewa traversant un étal de marché à Matonge et provoquant un pic CPU Chaos > 1.5 ms", "Désactiver les collisions inter-fragments (CollisionGroup = Debris_NoSelfCollide) sur les morceaux d'étal brisés et plafonner les corps rigides de débris actifs à 45 simultanés", "Maintenir PERF-CPU-CHAOS <= 1.5 ms en toutes circonstances"),
            ("Tremblement (jitter) ou rebond anormal de la moto Wewa à l'arrêt sur une pente en latérite", "Activer le Velocity/Angular Sleep Threshold sur les suspensions au repos et utiliser un Raycast/SphereCast Wheel lissé au lieu d'un cylindre rigide complexe", "Garantir une stabilité physique parfaite"),
            ("Static Mesh de décor soumis avec plus de 4 primitives convexes de collision", "Remplacer la collision par 1 à 2 primitives analytiques (Box, Capsule, Sphere) qui coûtent 5x moins cher en Broadphase/Narrowphase", "Optimiser les requêtes de balayage (Sweeps) du Game Thread"),
        ),
        acceptance_criteria=(
            "Le coût CPU Chaos Physics global (`PERF-CPU-CHAOS`) est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).",
            "0 tremblement (jitter) ni traversée de sol (tunneling) sur `VEH-MOTO-WEWA-01` jusqu'à `95 km/h`.",
            "Tous les débris destructibles passent à l'état `Sleeping` ou sont recyclés en moins de `4.0 secondes`.",
        ),
        validation_auditors=("ENG-07", "PRD-05", "GD-06"),
        reference_filename="chaos-physics-and-collisions.md",
        reference_content="""# Architecture UE5 Chaos Physics & Matrice de Collisions (`ENG-05`)

## 1. Matrice de Réponse des Profils de Collision (`SYS-PHYS-CHAOS`)
| Profil Collision | `WorldStatic` | `Pawn (Koffi/PNJ)` | `Vehicle (Wewa/Bus)` | `CombatHitbox` | `ChaosDebris` | `Camera` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`WorldStatic`** | Ignore | **Block** | **Block** | Overlap | **Block** | **Block** |
| **`Pawn`** | **Block** | **Block** | **Block** | **Overlap** | Ignore | Ignore |
| **`Vehicle`** | **Block** | **Block** | **Block** | Overlap | **Block** (Impulse) | **Block** |
| **`ChaosDebris`** | **Block** | Ignore | Ignore (Post-break) | Ignore | **Ignore** | **Ignore** |
""",
        template_filename="chaos-physics-spec.md",
        template_content="""# Spécification Simulation Physique Chaos (`ENG-05`)

- **Système** : `SYS-PHYS-CHAOS`
- **Cible Physique** : `[VEH-* / Props Destructibles / Ragdoll]`
- **Budget CPU Max (`PERF-CPU-CHAOS`)** : `<= 1.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Paramètres du Solveur Chaos & Async Tick
- **Fréquence Async Tick** : `60 Hz (16.66 ms pas fixe)`
- **Iterations Solveur (Position / Velocity)** : `[8 / 2]`
- **Seuils de Mise en Sommeil (Linear / Angular Sleep)** : `[Valeurs]`

## 2. Règles de Collision & Destruction (`Geometry Collection`)
- **Primitives autorisées** : `[Box / Sphere / Capsule / Convex <= 18]`
- **Politique de recyclage des débris** : `[Sleep <= 1.2s, Cull <= 4.0s]`
""",
        example_filename="sample-chaos-physics-spec.md",
        example_content=r"""# Exemple `ENG-05` — Configuration Chaos pour `VEH-MOTO-WEWA-01` & Étals Destructibles

- **Système** : `SYS-PHYS-CHAOS`
- **Cible Physique** : `VEH-MOTO-WEWA-01` & `GC_Matonge_MarketStall_01`
- **Budget CPU Max (`PERF-CPU-CHAOS`)** : `1.18 ms` mesuré en collision de marché (`<= 1.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Paramètres du Solveur Chaos & Async Tick
- **Fréquence Async Tick** : `60 Hz` asynchrone (`bTickPhysicsAsync = true`), interpolation lissée du châssis sur le Render Thread.
- **Suspension `VEH-MOTO-WEWA-01`** : `SphereCast` de rayon `32 cm` par roue (élimine les accrocs sur les bordures de caniveaux de `WLD-03`), ressort `Stiffness = 45.0`, `Damping = 6.8`.
- **Contrainte Anti-Retournement** : Couple angulaire de stabilisation latérale proportionnel à $(1 - \min(v / 35\text{ km/h}, 1))$ implémenté dans `FZaireMotoPhysicsSim`.

## 2. Règles de Collision & Destruction (`GC_Matonge_MarketStall_01`)
- **Fracturation** : 1 seul niveau de Voronoï (`14 fragments convexes`).
- **Profil Post-Rupture** : Bascule immédiate sur le profil `ChaosDebris` (ignore `Pawn`, `Camera` et les autres `ChaosDebris`), mise en sommeil forcée à `1.2 s` et disparition alpha-dithered à `3.5 s`.
""",
    ),
    SkillBlueprint(
        skill_id="ENG-06",
        description=(
            "Ingénierie du pipeline de rendu bas niveau DX12/Vulkan sous Unreal Engine 5 : optimisation "
            "de Lumen (Surface Cache / Reflections), Nanite (VisBuffer / WPO culling), Virtual Shadow "
            "Maps (VSM page caching), shader du fleuve Congo (Single Layer Water) et Temporal Super "
            "Resolution (TSR)."
        ),
        inputs=("gpu-budgets-dir-04", "lighting-specs-art-07", "master-materials-art-08"),
        outputs=("rendering-pipeline-spec.md", "scalability-presets-matrix.csv"),
        activation_triggers=(
            "Optimisation des passes GPU (`Lumen <= 4.5 ms`, `Nanite <= 2.5 ms`, `VSM`) suite à une capture RenderDoc ou PIX.",
            "Définition des profils de scalabilité graphique (`Mode Performance 60 FPS` vs `Mode Qualité 30 FPS` / PC Low -> Epic).",
            "Implémentation et optimisation du rendu de l'eau turbide du fleuve Congo (`LOC-GOMBE-PORT`, rapides de `DST-NGALIEMA`).",
        ),
        scope_boundaries=(
            "Ne modifie pas l'intention artistique des palettes de couleurs ou de l'ambiance d'éclairage (`ART-01`/`ART-07`).",
            "Interdit l'activation du Hardware Ray Tracing lourd en Mode Performance 60 FPS lorsque le Software Ray Tracing Lumen (Global Distance Field + Surface Cache) respecte le budget de `4.5 ms`.",
        ),
        operational_procedures=(
            "Optimiser les **Virtual Shadow Maps (VSM)** en activant le cache de pages statiques (`r.Shadow.Virtual.Cache = 1`) et en désactivant l'invalidation dynamique des pages d'ombre par le WPO de la végétation au-delà de `3500 cm` (`35 m`).",
            "Configurer **Lumen** en Mode Performance 60 FPS sur `Software Ray Tracing` (`r.Lumen.TraceMeshSDFs = 0` au-delà de `40 m`, `Final Gather Quality = 1.0`, `Reflection Downsample Factor = 2`) et réserver le `Hardware Ray Tracing (Hit Lighting)` au Mode Qualité 30 FPS.",
            "Implémenter le shader du fleuve Congo (`M_Zaire_Water_River`) sous **UE5 Single Layer Water** avec coefficients d'absorption/diffusion du limon brun-ocre équatorial et réflexions hybrides Screen-Space + Lumen Sky.",
            "Définir les CVar exactes de chaque mode dans `templates/rendering-pipeline-spec.md`.",
        ),
        decision_rules=(
            ("Invalidation massive des pages Virtual Shadow Maps (> 2.0 ms GPU) causée par les palmiers agités par le vent ou les foules Mass", "Forcer r.Shadow.Virtual.NonNanite.IncludeInCachedPage et couper l'invalidation WPO des ombres du feuillage à 2500 cm", "Stopper l'effondrement du cache VSM"),
            ("Réflexions Lumen sur les flaques de pluie de Matonge dépassant 2.2 ms à elles seules", "Utiliser un seuil de Roughness de réflexion stricte (MaxRoughnessToTrace = 0.40) afin que le bitume rugueux (> 0.40) réutilise directement l'irradiance du Lumen Surface Cache sans lancer de rayons de réflexion dédiés", "Maintenir Lumen GI + Reflections <= 4.5 ms"),
            ("Scintillement temporel (ghosting/shimmering) sur les câbles électriques aériens et les grilles en TSR", "Activer le matériau Responsive AA / Translucency Mask sur les câbles fins et ajuster r.TSR.History.ScreenPercentage", "Garantir la stabilité temporelle de l'image"),
        ),
        acceptance_criteria=(
            "Les passes GPU cumulées respectent `PERF-GPU-LUMEN <= 4.5 ms` et `PERF-GPU-NANITE <= 2.5 ms` en Mode Performance 60 FPS.",
            "Le taux de hit du cache de pages statiques VSM est `>= 92 %` lors des déplacements normaux.",
            "La matrice de scalabilité distingue explicitement les CVar du Mode Performance (`16.6 ms`) et du Mode Qualité (`33.3 ms`).",
        ),
        validation_auditors=("DIR-04", "ENG-07", "ART-07"),
        reference_filename="ue5-lumen-nanite-vsm-tuning.md",
        reference_content="""# Optimisation Bas Niveau du Pipeline Graphique UE5 (`ENG-06`)

## 1. Matrice des CVar de Référence (Mode Performance 60 FPS vs Mode Qualité 30 FPS)
| Sous-Système / CVar UE5 | Mode Performance (60 FPS / `<= 16.6 ms`) | Mode Qualité (30 FPS / `<= 33.3 ms`) | Impact GPU |
| :--- | :--- | :--- | :--- |
| **Résolution Interne -> TSR Output** | `1080p..1440p -> 4K TSR` | `1440p..1800p -> 4K TSR` | Gain `-3.2 ms` |
| `r.Lumen.HardwareRayTracing` | `0 (Software SDF + Surface Cache)` | `1 (Hardware RT Reflections)` | Gain `-2.4 ms` |
| `r.Lumen.Reflections.MaxRoughnessToTrace` | `0.40` (Au-delà : Surface Cache) | `0.55` | Gain `-0.8 ms` |
| `r.Shadow.Virtual.ResolutionLodBiasDirectional` | `-0.5` | `-1.0` | Gain `-0.7 ms` |
| **WPO Shadow Invalidation Distance** | `2500 cm (25 m)` | `3500 cm (35 m)` | Préserve le cache VSM |
""",
        template_filename="rendering-pipeline-spec.md",
        template_content="""# Spécification Pipeline de Rendu & Scalabilité (`ENG-06`)

- **Passe Graphique / Feature** : `[Lumen / Nanite / VSM / Water / TSR]`
- **Budget GPU Mode Perf (60 FPS)** : `[<= X.X ms]`
- **Budget GPU Mode Qualité (30 FPS)** : `[<= Y.Y ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Configuration des Passes RHI & CVar (`DefaultEngine.ini` / `Scalability.ini`)
| CVar / Paramètre | Valeur Perf (60 FPS) | Valeur Qualité (30 FPS) | Justification Technique |
| :--- | :--- | :--- | :--- |
| `r.Lumen...` | `[Val]` | `[Val]` | `[Impact RenderDoc]` |

## 2. Contrôles de Stabilité Temporelle & Cache VSM
- **Taux de Cache VSM Cible** : `[>= 92 %]`
- **Gestion Anti-Ghosting TSR** : `[Paramètre]`
""",
        example_filename="sample-rendering-spec.md",
        example_content="""# Exemple `ENG-06` — Pipeline Lumen/VSM Urbain & Shader d'Eau du Fleuve Congo

- **Passe Graphique / Feature** : `Lumen GI/Reflections`, `VSM Caching` & `Single Layer Water (Fleuve Congo)`
- **Budget GPU Mode Perf (60 FPS)** : `4.25 ms` (Lumen) + `2.20 ms` (Nanite/VSM) + `0.45 ms` (Fleuve)
- **Budget GPU Mode Qualité (30 FPS)** : `6.60 ms` (Lumen HW RT) + `3.50 ms` (Nanite/VSM)
- **Statut** : `CONFIRMED`

## 1. Configuration des Passes RHI & CVar
| CVar / Paramètre | Valeur Perf (60 FPS) | Valeur Qualité (30 FPS) | Justification Technique |
| :--- | :--- | :--- | :--- |
| `r.Lumen.HardwareRayTracing` | `0` | `1` | Le Software Ray Tracing sur Global Distance Field tient en `4.25 ms` dans `DST-MATONGE`. |
| `r.Lumen.Reflections.MaxRoughnessToTrace` | `0.40` | `0.55` | Concentre les rayons de réflexion sur les flaques de pluie, vitres de la Gombe et carrosseries. |
| `r.Shadow.Virtual.Cache.StaticSeparate` | `1` | `1` | Isole les ombres de l'architecture statique Nanite des acteurs mobiles `AI-02`/`AI-03`. |

## 2. Rendu du Fleuve Congo (`LOC-GOMBE-PORT` & `DST-NGALIEMA`)
- Utilisation du shading model **`SingleLayerWater`** avec diffusion anisotrope (`ScatteringCoefficients` brun-ocre du limon fluvial, profondeur de visibilité optique `85 cm`) et champ de vecteurs de courant (`FlowMap 2D`) ralentissant près des quais ONATRA et s'accélérant dans les rapides de Kinsuka.
""",
    ),
    SkillBlueprint(
        skill_id="ENG-07",
        description=(
            "Ingénierie de la performance et profilage continu CPU/GPU/RAM/VRAM de ZAÏRE (Unreal Insights, "
            "RenderDoc, CSVProfiler). Surveille le respect des budgets P99 (<= 16.6 ms à 60 FPS, <= 33.3 ms "
            "à 30 FPS, <= 6144 MB VRAM), pilote la collecte du cache PSO et émet les blocages techniques."
        ),
        inputs=("all-engineering-subsystems-eng-01-to-06", "lighting-art-07", "niagara-vfx-art-09", "knowledge/technical-specs/performance-budgets.csv"),
        outputs=("performance-budget-report.md", "pso-precaching-protocol.md"),
        activation_triggers=(
            "Analyse des traces Unreal Insights et des métriques issues des parcours automatisés Gauntlet (`PRD-05`) dans chaque commune (`DST-*`).",
            "Exécution du script d'audit `scripts/check_perf_budget.py` avant toute validation de jalon (`DIR-04`/`DIR-07`).",
            "Diagnostic et élimination des saccades (hitches P99) liées à la compilation de shaders (PSO) ou au streaming World Partition.",
        ),
        scope_boundaries=(
            "Ne supprime pas arbitrairement une mécanique de gameplay (`GD-01`) sans passer par le protocole d'arbitrage `DIR-01` (`DIR-04` + `DIR-05`).",
            "Détient l'autorité de marquer tout livrable hors budget au statut **`BLOCKED`**.",
        ),
        operational_procedures=(
            "Collecter les percentiles **P50 (Médiane), P95 et P99** du frametime CPU et GPU sur le parcours de référence traversant `DST-GOMBE`, `DST-KALAMU`, `DST-MATONGE` et `DST-LIMETE` à `95 km/h` en `VEH-MOTO-WEWA-01`.",
            "Exécuter `scripts/check_perf_budget.py` pour confronter chaque sous-système (`PERF-CPU-NPCAI`, `PERF-CPU-MASS`, `PERF-CPU-CHAOS`, `PERF-GPU-LUMEN`, `PERF-GPU-NANITE`, `PERF-GPU-NIAGARA`, `PERF-MEM-VRAM`) à son plafond officiel de `knowledge/technical-specs/performance-budgets.csv`.",
            "Vérifier l'efficacité du **PSO Precaching UE5** (`r.PSOPrecaching = 1` + bundlé `.upipelinecache` généré par `ENG-08`) : exiger `0 hitch de compilation PSO > 5 ms` en jeu.",
            "Publier le rapport d'audit et les actions correctives assignées dans `templates/performance-budget-report.md`.",
        ),
        decision_rules=(
            ("Un sous-système dépasse son budget dans check_perf_budget.py (ex: PERF-GPU-LUMEN = 5.4 ms > 4.5 ms)", "Marquer immédiatement la zone ou le système au statut BLOCKED et assigner un ticket d'optimisation prioritaire au skill responsable (ART-07 / ENG-06)", "Interdire la promotion CONFIRMED tant que P99 > 16.6 ms"),
            ("Hitch ponctuel (> 25 ms sur 1 frame) détecté lors du premier coup de machette ou de la première explosion Niagara", "Capturer le PSO manquant via les logs de PSO Precaching et l'ajouter à la passe d'échauffement (warmup) du build nocturne ENG-08", "Éliminer 100 % des shader compilation stutters"),
            ("Consommation VRAM dépassant 5900 MB (proche du plafond de 6144 MB)", "Auditer le pool de textures via memreport -full, rétrograder les textures non-héroïques de 4K vers 2K et resserrer le budget du pool Streaming Virtual Texturing", "Prévenir tout crash Out-Of-Memory (OOM)"),
        ),
        acceptance_criteria=(
            "`python skills/07-engineering/eng-07-performance-engineer/scripts/check_perf_budget.py` retourne un code `0` (`passed: true`).",
            "Le percentile P99 du frametime global est `<= 16.6 ms` (Mode Performance) et `<= 33.3 ms` (Mode Qualité).",
            "Zéro fuite mémoire (memory leak) constatée après 2 heures de boucle d'exploration Gauntlet (`PRD-05`).",
        ),
        validation_auditors=("DIR-04", "DIR-07", "PRD-05"),
        reference_filename="unreal-insights-and-pso-caching.md",
        reference_content="""# Protocole de Profilage Unreal Insights & PSO Precaching (`ENG-07`)

## 1. Grille de Contrôle P99 Obligatoire (`knowledge/technical-specs/performance-budgets.csv`)
| ID Budget | Sous-Système | Plafond 60 FPS | Plafond 30 FPS | Skill Responsable |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | Frametime Global P99 | `<= 16.6 ms` | `<= 33.3 ms` | `ENG-07` |
| `PERF-CPU-GAME` | Game Thread Total | `<= 6.5 ms` | `<= 12.0 ms` | `ENG-01` |
| `PERF-CPU-NPCAI` | NPC AI (`<= 24` acteurs) | `<= 2.5 ms` | `<= 3.0 ms` | `AI-01` |
| `PERF-CPU-MASS` | Mass Crowd & Traffic (`600+`) | `<= 2.0 ms` | `<= 2.5 ms` | `AI-02` / `AI-03` |
| `PERF-CPU-CHAOS` | Chaos Physics & Vehicles | `<= 1.5 ms` | `<= 2.0 ms` | `ENG-05` |
| `PERF-CPU-ANIM` | Animation & Motion Matching | `<= 1.8 ms` | `<= 2.5 ms` | `ART-05` |
| `PERF-GPU-LUMEN` | Lumen GI & Reflections | `<= 4.5 ms` | `<= 7.0 ms` | `ART-07` / `ENG-06` |
| `PERF-GPU-NANITE` | Nanite Raster & VisBuffer | `<= 2.5 ms` | `<= 4.0 ms` | `ART-04` / `ENG-06` |
| `PERF-GPU-NIAGARA` | Niagara VFX | `<= 1.5 ms` | `<= 2.0 ms` | `ART-09` |
| `PERF-MEM-VRAM` | VRAM Totale Allouée | `<= 6144 MB` | `<= 8192 MB` | `DIR-04` |
""",
        template_filename="performance-budget-report.md",
        template_content="""# Rapport d'Audit de Performance & Budgets UE5 (`ENG-07`)

- **Parcours / Commune Testée** : `DST-...` (`LOC-...`)
- **Mode Cible** : `Mode Performance (60 FPS / <= 16.6 ms)`
- **Résultat `check_perf_budget.py`** : `PASS` | `FAIL (BLOCKED)`
- **Marge P99 (Headroom)** : `[+X.XX ms]`

## 1. Relevé détaillé par Sous-Système (Unreal Insights / RenderDoc)
| ID Budget | Plafond (ms/MB) | Mesuré P95 | Mesuré P99 | Statut (`OK` / `OVER_BUDGET`) |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | `16.6 ms` | `[XX.X ms]` | `[XX.X ms]` | `OK` |

## 2. Statut PSO Precaching & Streaming
- **Hitches PSO (> 5 ms)** : `[0 détecté]`
- **Actions d'Optimisation Requises** : `[Aucune / Tickets assignés]`
""",
        example_filename="sample-performance-report.md",
        example_content="""# Exemple `ENG-07` — Audit de Performance de `DST-MATONGE` (Heure de Pointe + Pluie)

- **Parcours / Commune Testée** : Traversée `LOC-GOMBE-PORT` -> `LOC-MATONGE-VICTOIRE` en `VEH-MOTO-WEWA-01` sous `World.Weather.TropicalStorm`
- **Mode Cible** : `Mode Performance (60 FPS / <= 16.6 ms)`
- **Résultat `check_perf_budget.py`** : `PASS (0 violation)`
- **Marge P99 (Headroom)** : `+0.75 ms` (`15.85 ms` mesuré pour `16.60 ms` max)

## 1. Relevé détaillé par Sous-Système (Unreal Insights / RenderDoc)
| ID Budget | Plafond | Mesuré P95 | Mesuré P99 | Statut |
| :--- | :--- | :--- | :--- | :--- |
| `PERF-TOTAL-FRAME` | `16.60 ms` | `14.40 ms` | `15.85 ms` | **OK** |
| `PERF-CPU-GAME` | `6.50 ms` | `5.30 ms` | `5.90 ms` | **OK** |
| `PERF-CPU-NPCAI` (`18 acteurs`) | `2.50 ms` | `1.85 ms` | `2.10 ms` | **OK** |
| `PERF-CPU-MASS` (`600 piétons + 75 véh.`) | `2.00 ms` | `1.55 ms` | `1.75 ms` | **OK** |
| `PERF-CPU-CHAOS` | `1.50 ms` | `1.05 ms` | `1.25 ms` | **OK** |
| `PERF-GPU-LUMEN` | `4.50 ms` | `3.95 ms` | `4.25 ms` | **OK** |
| `PERF-GPU-NANITE` | `2.50 ms` | `1.95 ms` | `2.20 ms` | **OK** |
| `PERF-GPU-NIAGARA` | `1.50 ms` | `0.95 ms` | `1.15 ms` | **OK** |
| `PERF-MEM-VRAM` | `6144 MB` | `5480 MB` | `5620 MB` | **OK** |

## 2. Statut PSO Precaching & Streaming
- **Hitches PSO (> 5 ms)** : `0` (100 % des PSO des 8 Master Materials `ART-08` pré-cachés au chargement asynchrone).
""",
        scripts={"check_perf_budget.py": CHECK_PERF_BUDGET_SCRIPT},
    ),
    SkillBlueprint(
        skill_id="ENG-08",
        description=(
            "Ingénierie Build, CI/CD et Sécurité de ZAÏRE STUDIO OS : pipelines Unreal Automation Tool "
            "(UAT), BuildGraph, Epic Horde, cache dérivé partagé Zen Server DDC, compilation incrémentale "
            "(<= 15 minutes), collecte automatisée des caches PSO et packaging .pak/.utoc signé et chiffré "
            "en AES-256 sans secrets codés en dur."
        ),
        inputs=("cpp-codebase-eng-01-to-06", "perf-pso-specs-eng-07", "gauntlet-test-suites-prd-05"),
        outputs=("ci-cd-buildgraph-spec.xml", "pak-security-and-ddc-protocol.md"),
        activation_triggers=(
            "Configuration ou maintenance du pipeline CI/CD BuildGraph / Horde pour les builds incrémentaux et nocturnes.",
            "Optimisation du temps de cooking et de compilation via Zen Server Derived Data Cache (DDC) partagé (`PERF-CI-BUILD <= 15 minutes`).",
            "Configuration de la signature cryptographique RSA et du chiffrement AES-256 des archives IoStore (`.pak`/`.utoc`/`.ucas`) via variables d'environnement sécurisées.",
        ),
        scope_boundaries=(
            "Ne modifie jamais le code logique de gameplay (`ENG-02`).",
            "Interdit formellement le stockage de clés de chiffrement AES, certificats de signature ou jetons d'API en clair dans le dépôt Git/Perforce (injection exclusive par coffre-fort CI / variables d'environnement).",
        ),
        operational_procedures=(
            "Structurer le pipeline **UE5 BuildGraph** en 5 noeuds parallélisés sous Epic Horde : (1) `Compile_ZaireEditor_And_Game`, (2) `Run_EditorValidators_ENG03`, (3) `Cook_And_Package_IoStore`, (4) `Collect_PSO_And_Run_Gauntlet_PRD05`, (5) `Sign_And_Publish_Build`.",
            "Maintenir un **Zen Server Shared DDC** chaud sur le réseau de build afin de garantir un temps de build incrémental **`<= 15.0 minutes`** (`PERF-CI-BUILD`).",
            "Injecter la clé de chiffrement AES-256 des tables d'index IoStore (`.utoc`) au moment du packaging via `-EncryptionKeyOverrideEnvVar=ZAIRE_PAK_AES256_KEY` (ne chiffrer que l'index `.utoc` et les assets sensibles pour limiter l'overhead CPU de décompression à `< 0.5 %`).",
            "Déclencher automatiquement la suite de tests Gauntlet (`PRD-05`) et l'audit de budget (`ENG-07`) sur chaque build nocturne.",
        ),
        decision_rules=(
            ("Temps de build incrémental dépassant 15 minutes sur la ferme CI", "Auditer les inclusions d'en-têtes C++ via Include-What-You-Use (IWYU), activer UnrealBuildAccelerator (UBA) et vérifier le taux de Cache Hit du Zen Server DDC (>= 95 %)", "Ramener PERF-CI-BUILD sous le seuil de 15.0 minutes"),
            ("Clé ou secret détecté en dur dans un fichier .ini ou script de build", "Faire échouer immédiatement le pipeline CI (Secret Scanner Fail), révoquer la clé exposée et remplacer par une lecture de variable d'environnement du coffre-fort CI", "Respecter la politique Zéro Secret Codé en Dur"),
            ("Échec d'un validateur ENG-03 ou d'un test critique Gauntlet PRD-05 pendant le build", "Stopper la promotion du build vers la branche QA/Stable et notifier automatiquement le skill propriétaire de la régression", "Maintenir la branche principale 100 % verte"),
        ),
        acceptance_criteria=(
            "Temps de build et cooking incrémental `<= 15.0 minutes` (`PERF-CI-BUILD`).",
            "0 secret ou clé de chiffrement stocké en clair dans les fichiers du dépôt.",
            "Déclenchement automatique des validateurs `ENG-03`, des tests Gauntlet `PRD-05` et de la fusion du cache PSO `ENG-07`.",
        ),
        validation_auditors=("DIR-04", "PRD-05", "ENG-07"),
        reference_filename="buildgraph-horde-and-security.md",
        reference_content="""# Architecture CI/CD BuildGraph, Zen DDC & Sécurité IoStore (`ENG-08`)

## 1. Pipeline CI/CD en 5 Étapes (Budget Incrémental `<= 15 min`)
1. **Pre-Flight & Secret Scan (`< 30 s`)** : Vérifie l'absence de secrets en dur, exécute `tools/validate_registry.py`, `tools/check_dag_cycles.py` et `tools/lint_skills.py`.
2. **Compile C++20 via UnrealBuildAccelerator (UBA) (`<= 4 min`)** : Compilation distribuée avec `/W4` et `IWYU`.
3. **Asset Validation (`ENG-03`, `<= 2 min`)** : Exécution headless du commandlet `ValidateAssets`.
4. **Incremental Cook & IoStore Package via Zen DDC (`<= 7 min`)** : Génération des conteneurs `.utoc`/`.ucas`/`.pak` avec injection de `$ENV{ZAIRE_PAK_AES256_KEY}`.
5. **Automated Gauntlet & PSO Merge (`PRD-05` / `ENG-07`)** : Exécution des tests rapides de fumée (Smoke Tests) et consolidation du cache `.upipelinecache`.
""",
        template_filename="ci-cd-buildgraph-spec.md",
        template_content="""# Spécification Pipeline CI/CD BuildGraph & Packaging (`ENG-08`)

- **Nom du Pipeline** : `BG_Zaire_...`
- **Cible Temps Build Incrémental (`PERF-CI-BUILD`)** : `<= 15.0 minutes`
- **Taux de Cache Hit Zen DDC Requis** : `>= 95 %`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Étapes du Graphe BuildGraph / Horde
| Étape | Commande UAT / Commandlet | Timeout (min) | Condition d'Échec Bloquant |
| :--- | :--- | :--- | :--- |
| `1_Validate` | `RunUnreal -Commandlet=DataValidation` | `3 min` | `> 0 asset invalide (ENG-03)` |

## 2. Sécurité Packaging IoStore & Gestion des Secrets
- **Chiffrement Index `.utoc`** : `AES-256 via Variable d'Environnement (Zéro clé en dur)`
- **Overhead CPU Décompression** : `[< 0.5 %]`
""",
        example_filename="sample-buildgraph-spec.md",
        example_content="""# Exemple `ENG-08` — Pipeline BuildGraph `BG_Zaire_Incremental_And_Nightly`

- **Nom du Pipeline** : `BG_Zaire_Incremental_And_Nightly`
- **Cible Temps Build Incrémental (`PERF-CI-BUILD`)** : `11.4 minutes` mesuré (`<= 15.0 minutes` requis)
- **Taux de Cache Hit Zen DDC Requis** : `97.2 %` sur le cluster Zen Server
- **Statut** : `CONFIRMED`

## 1. Étapes du Graphe BuildGraph / Horde
| Étape | Commande UAT / Commandlet | Durée Moyenne | Condition d'Échec Bloquant |
| :--- | :--- | :--- | :--- |
| `0_StudioOS_Verify` | `python -m unittest discover -s tests` | `0.2 min` | Erreur de registre, cycle DAG ou skill invalide. |
| `1_Compile_UBA` | `BuildCookRun -build -uba -WarningsAsErrors` | `3.5 min` | Tout warning ou erreur C++20. |
| `2_DataValidation` | `UnrealEditor-Cmd -run=DataValidation` | `1.8 min` | Violation `ART-04` / `ENG-01` détectée par `ENG-03`. |
| `3_Cook_IoStore` | `BuildCookRun -cook -iostore -pak -compressed` | `5.9 min` | Asset corrompu ou référence manquante. |
| `4_Gauntlet_Smoke` | `RunUnreal -test=ZaireSmokeTestSuite` | `4.0 min` (Post-Build) | Crash, P99 > `16.6 ms` (`ENG-07`) ou soft-lock (`PRD-05`). |

## 2. Sécurité Packaging IoStore & Gestion des Secrets
- **Chiffrement Index `.utoc` & Signature RSA** : Les clés `ZAIRE_PAK_AES256_KEY` et `ZAIRE_PAK_RSA_SIGN_KEY` sont lues exclusivement depuis le coffre-fort d'environnement du runner Horde au moment de l'étape `3_Cook_IoStore`, puis purgées de la mémoire volatile.
- **Overhead CPU Runtime** : `0.35 %` (`< 1 %` requis grâce au chiffrement ciblé de la table d'allocation `.utoc` et compression `Oodle Kraken`).
""",
    ),
)


def build_department_07(workspace: Path = WORKSPACE_ROOT) -> list[Path]:
    """Génère les 8 skills du département 07-engineering."""
    created: list[Path] = []
    for bp in ENGINEERING_BLUEPRINTS:
        created.append(write_skill_from_blueprint(bp, workspace))
    return created


if __name__ == "__main__":
    paths = build_department_07(WORKSPACE_ROOT)
    print(f"[OK] Département 07-engineering généré ({len(paths)} skills).")
