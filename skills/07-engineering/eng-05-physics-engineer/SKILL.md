---
name: eng-05-physics-engineer
description: "Ingénierie de la simulation physique temps réel sous UE5 Chaos Physics, Chaos Vehicles, Chaos Destruction et Chaos Cloth (SYS-PHYS-CHAOS). Gère la matrice des canaux de collision, l'Async Physics Tick, la mise en sommeil agressive des débris et le budget CPU <= 1.5 ms."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-05
  department: 07-engineering
  stratum: 4
  version: "1.1.0"
  inputs:
    - "vehicle-handling-specs-gd-06"
    - "environment-kits-art-02"
    - "cpu-budgets-dir-04"
  outputs:
    - "chaos-physics-specification.md"
    - "collision-channels-matrix.csv"
  upstream_dependencies:
    - "GD-06"
    - "ART-02"
    - "DIR-04"
---

# `ENG-05` — Physics Engineer (`eng-05-physics-engineer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **4**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Implémentation du modèle physique Chaos des véhicules kinois (`VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`, `VEH-BUS-TRANSCO-01`).
- Configuration des éléments destructibles urbains (étals de marché en bois, barrières portuaires, poteaux) via Chaos Geometry Collections.
- Optimisation des profils de collision et du budget CPU `PERF-CPU-CHAOS` (`<= 1.5 ms` en mode 60 FPS).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `vehicle-handling-specs-gd-06`, `environment-kits-art-02`, `cpu-budgets-dir-04`
- **Sorties produites** : `chaos-physics-specification.md`, `collision-channels-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `GD-06`, `ART-02`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie pas le design ludique des vitesses cibles (`GD-06`), mais implémente les paramètres de solveur qui les rendent stables et sans tremblement (jitter).
- **Interdiction / Limite** : Interdit l'utilisation de `Complex Collision as Simple` (Triangle Mesh Collision) sur tout objet mobile ou prop de décor standard.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Activer l'**Async Physics Tick** (`p.Chaos.AsyncPhysics = 1` à `60 Hz` fixe) afin de découpler la stabilité des suspensions de `VEH-MOTO-WEWA-01` des variations de frametime rendu.
2. Restreindre la matrice des canaux de collision (`DefaultEngine.ini`) aux profils strictement nécessaires (`Pawn`, `Vehicle`, `WorldStatic`, `WorldDynamic`, `CombatHitbox`, `Visibility`, `Camera`) en désactivant les tests croisés inutiles (ex: débris légers ignorent les autres débris et la caméra).
3. Configurer les **Geometry Collections (Chaos Destruction)** des props destructibles avec un maximum de `18 fragments convexes` par prop, une mise en sommeil forcée (`Sleep Threshold`) après `1.2 seconde` et une disparition par rétrécissement (fade-out) après `4.0 secondes`.
4. Assigner à chaque matériau de surface l'un des 5 `UChaosPhysicalMaterial` officiels (`PM_Asphalt_Dry`, `PM_Asphalt_Wet`, `PM_Laterite_Dry`, `PM_Laterite_Mud`, `PM_Corrugated_Iron`).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Véhicule Wewa traversant un étal de marché à Matonge et provoquant un pic CPU Chaos > 1.5 ms | Désactiver les collisions inter-fragments (CollisionGroup = Debris_NoSelfCollide) sur les morceaux d'étal brisés et plafonner les corps rigides de débris actifs à 45 simultanés | Maintenir PERF-CPU-CHAOS <= 1.5 ms en toutes circonstances |
| Tremblement (jitter) ou rebond anormal de la moto Wewa à l'arrêt sur une pente en latérite | Activer le Velocity/Angular Sleep Threshold sur les suspensions au repos et utiliser un Raycast/SphereCast Wheel lissé au lieu d'un cylindre rigide complexe | Garantir une stabilité physique parfaite |
| Static Mesh de décor soumis avec plus de 4 primitives convexes de collision | Remplacer la collision par 1 à 2 primitives analytiques (Box, Capsule, Sphere) qui coûtent 5x moins cher en Broadphase/Narrowphase | Optimiser les requêtes de balayage (Sweeps) du Game Thread |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/chaos-physics-and-collisions.md`
- **Modèle Officiel de Livrable** : `templates/chaos-physics-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-chaos-physics-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-chaos-physics-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/chaos-physics-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le coût CPU Chaos Physics global (`PERF-CPU-CHAOS`) est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).
- [ ] 0 tremblement (jitter) ni traversée de sol (tunneling) sur `VEH-MOTO-WEWA-01` jusqu'à `95 km/h`.
- [ ] Tous les débris destructibles passent à l'état `Sleeping` ou sont recyclés en moins de `4.0 secondes`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-07`, `PRD-05`, `GD-06`.
