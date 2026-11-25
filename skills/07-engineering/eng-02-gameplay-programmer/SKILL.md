---
name: eng-02-gameplay-programmer
description: "Programmation C++20 des systèmes de gameplay sous Unreal Engine 5 : Gameplay Ability System (GAS : UAbilitySystemComponent, UGameplayAbility, UAttributeSet), Enhanced Input, composants modulaires d'interaction, caméra 3e personne et intégration Common UI."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-02
  department: 07-engineering
  stratum: 4
  version: "1.1.0"
  inputs:
    - "system-design-gd-01"
    - "mission-state-machines-gd-02"
    - "combat-frame-data-gd-05"
    - "vehicle-specs-gd-06"
    - "ue5-architecture-eng-01"
  outputs:
    - "gameplay-cpp-specification.md"
    - "gas-attributes-and-abilities-header.h"
  upstream_dependencies:
    - "GD-01"
    - "GD-02"
    - "GD-03"
    - "GD-04"
    - "GD-05"
    - "GD-06"
    - "GD-07"
    - "ENG-01"
---

# `ENG-02` — Gameplay Programmer (`eng-02-gameplay-programmer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **4**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Implémentation C++ d'une capacité de combat (`SYS-CMB-MELEE`), d'infiltration (`SYS-STEALTH`), de parkour (`Ability.Movement.Vault`) ou d'interaction véhicule (`VEH-MOTO-WEWA-01`).
- Exposition de fonctions C++ déterministes et performantes aux designers (`BlueprintCallable` / `BlueprintPure` sans logique lourde en Blueprint Tick).
- Implémentation de la caméra 3e personne évitant tout clipping dans les couloirs de `>= 350 cm` (`WLD-05`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `system-design-gd-01`, `mission-state-machines-gd-02`, `combat-frame-data-gd-05`, `vehicle-specs-gd-06`, `ue5-architecture-eng-01`
- **Sorties produites** : `gameplay-cpp-specification.md`, `gas-attributes-and-abilities-header.h`
- **Dépendances Amont Canoniques (DAG)** : `GD-01`, `GD-02`, `GD-03`, `GD-04`, `GD-05`, `GD-06`, `GD-07`, `ENG-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne développe pas les plugins d'automatisation éditeur (`ENG-03`) ni les passes de rendu RHI (`ENG-06`).
- **Interdiction / Limite** : Interdit l'utilisation du `Event Tick` en Blueprint pour de la logique gameplay continue (toute logique tickée critique est écrite en C++ natif ou pilotée par événements Gameplay Tags).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Implémenter chaque action de `CHR-PROTAG-KOFFI` comme une sous-classe C++ de `UZaireGameplayAbility` configurée avec ses `ActivationOwnedTags`, `CancelAbilitiesWithTag` et `BlockAbilitiesWithTag` issus de `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.
2. Centraliser les statistiques de combat et d'endurance dans `UZaireCombatAttributeSet` (`Health`, `MaxHealth`, `Stamina`, `Poise`, `ParryWindowMs`) avec validation dans `PreAttributeChange` et `PostGameplayEffectExecute`.
3. Coder le `UZaireSpringArmComponent` de caméra avec multi-whisker raycasts prédictifs pour glisser sans à-coup le long des murs de `350 cm` (`WLD-05`).
4. Documenter les signatures C++ et les contrats d'interface dans `templates/gameplay-cpp-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Logique de combat ou de machine à états implémentée dans un Event Tick Blueprint consommant > 0.3 ms | Migrer immédiatement la logique en C++ natif ou la convertir en Timer/Delegate déclenché par changement de FGameplayTag | Maintenir un Game Thread propre et déterministe |
| Fenêtre de parade (State.Character.Combat.Parrying) sensible aux fluctuations de framerate | Évaluer la fenêtre d'impact en temps réel continu (DeltaSeconds / ServerWorldTime) avec buffer d'input Enhanced Input de 120 ms | Garantir la précision < 100 ms exigée par GD-05 |
| Destruction ou sortie imprévue d'un véhicule pendant une GameplayAbility de conduite | Forcer l'exécution de EndAbility() sur le callback OnVehicleDestroyed/OnExitVehicle pour nettoyer tous les Gameplay Tags actifs | Prévenir tout blocage d'état (soft-lock GD-02) |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/gas-and-enhanced-input-cpp.md`
- **Modèle Officiel de Livrable** : `templates/gameplay-cpp-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-gameplay-cpp-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-gameplay-cpp-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/gameplay-cpp-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des capacités utilisent des `FGameplayTag` typés (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`) sans chaînes magiques (`FName` codés en dur).
- [ ] 0 logique gameplay lourde dans le `Tick` Blueprint ; code C++ compilable sans warning au niveau `/W4`.
- [ ] Couverture par tests fonctionnels automatisés (`PRD-05`) sur l'activation, l'annulation et le nettoyage des capacités.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-01`, `PRD-05`, `DIR-05`.
