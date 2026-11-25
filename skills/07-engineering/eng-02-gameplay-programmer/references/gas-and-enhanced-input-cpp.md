# Architecture C++ UE5 Gameplay Ability System & Enhanced Input (`ENG-02`)

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

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-02` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-01`, `GD-02`, `GD-03`, `GD-04`, `GD-05`, `GD-06`, `GD-07`, `ENG-01`
- **Audit des Entrées (`inputs`)** :
  - `system-design-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `mission-state-machines-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-frame-data-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `vehicle-specs-gd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `ue5-architecture-eng-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `gameplay-cpp-specification.md` : Doit respecter le gabarit `templates/gameplay-cpp-spec.md` et passer l'audit croisé.
  - `gas-attributes-and-abilities-header.h` : Doit respecter le gabarit `templates/gameplay-cpp-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-01`, `PRD-05`, `DIR-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Logique de combat ou de machine à états implémentée dans un Event Tick Blueprint consommant > 0.3 ms | Blocage / Dégradation si ignoré | Migrer immédiatement la logique en C++ natif ou la convertir en Timer/Delegate déclenché par changement de FGameplayTag | Escalade vers Maintenir un Game Thread propre et déterministe |
| Mode de Défaillance 2: Fenêtre de parade (State.Character.Combat.Parrying) sensible aux fluctuations de framerate | Blocage / Dégradation si ignoré | Évaluer la fenêtre d'impact en temps réel continu (DeltaSeconds / ServerWorldTime) avec buffer d'input Enhanced Input de 120 ms | Escalade vers Garantir la précision < 100 ms exigée par GD-05 |
| Mode de Défaillance 3: Destruction ou sortie imprévue d'un véhicule pendant une GameplayAbility de conduite | Blocage / Dégradation si ignoré | Forcer l'exécution de EndAbility() sur le callback OnVehicleDestroyed/OnExitVehicle pour nettoyer tous les Gameplay Tags actifs | Escalade vers Prévenir tout blocage d'état (soft-lock GD-02) |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-02`)

- [ ] **Contrôle DoD #1** : 100 % des capacités utilisent des `FGameplayTag` typés (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`) sans chaînes magiques (`FName` codés en dur).
- [ ] **Contrôle DoD #2** : 0 logique gameplay lourde dans le `Tick` Blueprint ; code C++ compilable sans warning au niveau `/W4`.
- [ ] **Contrôle DoD #3** : Couverture par tests fonctionnels automatisés (`PRD-05`) sur l'activation, l'annulation et le nettoyage des capacités.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
