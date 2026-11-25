---
name: eng-01-unreal-engine-specialist
description: "Architecture C++20 fondamentale sous Unreal Engine 5 : World Partition, Data Layers, One File Per Actor (OFPA), Hierarchical LOD (HLOD), Subsystems modulaires et streaming asynchrone (FStreamableManager / TSoftObjectPtr) garantissant zéro chargement bloquant."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-01
  department: 07-engineering
  stratum: 1
  version: "1.1.0"
  inputs:
    - "technical-adr-dir-04"
    - "open-world-grid-wld-04"
    - "3d-pipeline-norms-art-04"
  outputs:
    - "ue5-cpp-architecture-spec.md"
    - "world-partition-streaming-config.md"
  upstream_dependencies:
    - "DIR-04"
    - "WLD-04"
    - "ART-04"
---

# `ENG-01` — Unreal Engine Specialist (`eng-01-unreal-engine-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception d'un nouveau `UGameInstanceSubsystem`, `UWorldSubsystem` ou module C++ UE5.
- Configuration de la grille spatiale `World Partition` (`12800 cm`), des `Data Layers` et des rayons de streaming pour Kinshasa.
- Revue de code C++ pour vérifier l'application stricte de la règle Zero Synchronous Loading (`PERF-CPU-GAME <= 6.5 ms`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `technical-adr-dir-04`, `open-world-grid-wld-04`, `3d-pipeline-norms-art-04`
- **Sorties produites** : `ue5-cpp-architecture-spec.md`, `world-partition-streaming-config.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-04`, `WLD-04`, `ART-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'implémente pas les capacités individuelles de combat ou de mission (`ENG-02`) ni les shaders RHI bas niveau (`ENG-06`).
- **Interdiction / Limite** : Interdit formellement tout appel à `LoadSynchronous()`, `FlushAsyncLoading()` ou `ConstructorHelpers::FObjectFinder` en cours de gameplay.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer la logique globale du monde en `UWorldSubsystem` découplés (`UZaireDistrictStreamingSubsystem`, `UZaireTimeWeatherSubsystem`) sans dépendance circulaire entre modules `.Build.cs`.
2. Configurer `World Partition` avec une grille principale `MainGrid` (taille de cellule `12800 cm`, rayon de chargement `25600 cm` à pied / `38400 cm` en `VEH-MOTO-WEWA-01`) et une grille `LowResGrid` pour les Landmarks Tier 1 (`LOC-LIMETE-ECHANGEUR`).
3. Imposer l'utilisation exclusive de `TSoftObjectPtr<T>`, `FPrimaryAssetId` et `UAssetManager::GetStreamableManager().RequestAsyncLoad()` avec callback non bloquant.
4. Documenter les contrats d'en-têtes C++20 et la configuration `.ini` dans `templates/ue5-architecture-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Présence d'un appel LoadSynchronous() ou d'une référence Hard Pointer UPROPERTY() vers un asset lourd dans un Blueprint/C++ | Remplacer immédiatement le pointeur dur par un TSoftObjectPtr<T> chargé via FStreamableManager avant d'activer l'acteur | Éliminer tout hitch > 2 ms sur le Game Thread |
| Transition rapide en moto Wewa (95 km/h) provoquant un retard de chargement de cellule World Partition | Activer un Streaming Source secondaire prédictif projeté à +4000 cm en avant du vecteur vitesse du véhicule | Prévenir tout trou géométrique ou pop-in à haute vitesse |
| Conflit de verrouillage de fichiers entre deux level designers travaillant sur la même commune | Vérifier l'activation obligatoire de One File Per Actor (OFPA) et isoler les acteurs de mission dans un Data Layer dédié | Permettre le travail parallèle sans conflit Git LFS / Perforce |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/ue5-world-partition-and-async.md`
- **Modèle Officiel de Livrable** : `templates/ue5-architecture-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-ue5-architecture-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-ue5-architecture-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/ue5-architecture-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 0 appel `LoadSynchronous()` dans le code runtime ; 100 % des chargements passent par `UAssetManager` / `FStreamableManager`.
- [ ] Le coût Game Thread global (`PERF-CPU-GAME`) reste `<= 6.5 ms` lors du franchissement de frontière entre deux communes (`DST-GOMBE` -> `DST-KALAMU`).
- [ ] Configuration World Partition + HLOD validée sur les vitesses de déplacement à pied et en `VEH-MOTO-WEWA-01`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-04`, `ENG-07`.
