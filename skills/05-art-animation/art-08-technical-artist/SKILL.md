---
name: art-08-technical-artist
description: "Ingénierie Technical Art de ZAÏRE : conception des Master Materials HLSL/Substrate, prévention de l'explosion des permutations shaders (PSO), rigging mécanique/organique complexe et profilage des draw calls artistiques entre outils DCC et Unreal Engine 5."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-08
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "environment-art-art-02"
    - "character-art-art-03"
    - "3d-standards-art-04"
    - "gpu-budgets-dir-04"
  outputs:
    - "master-material-specification.md"
    - "shader-pso-budget-guidelines.md"
  upstream_dependencies:
    - "ART-02"
    - "ART-03"
    - "ART-04"
    - "DIR-04"
---

# `ART-08` — Technical Artist (`art-08-technical-artist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception ou modification d'un Master Material (`M_Env_Master`, `M_Char_Skin`, `M_Vehicle_Paint`, `M_Water_CongoRiver`).
- Réduction du nombre de Pipeline State Objects (PSO) pour éliminer les saccades de compilation shaders.
- Création des rigs squelettiques de véhicules (`VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`) et de destruction/vêtements.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `environment-art-art-02`, `character-art-art-03`, `3d-standards-art-04`, `gpu-budgets-dir-04`
- **Sorties produites** : `master-material-specification.md`, `shader-pso-budget-guidelines.md`
- **Dépendances Amont Canoniques (DAG)** : `ART-02`, `ART-03`, `ART-04`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas la logique C++ gameplay (`ENG-02`) ni l'infrastructure serveur CI/CD (`ENG-08`).
- **Interdiction / Limite** : Interdit l'ajout de nouveaux `StaticSwitchParameter` non autorisés dans les Master Materials (utiliser `CustomPrimitiveData` ou des branches dynamiques uniformes).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Restreindre l'ensemble du projet à **8 Master Materials fondamentaux** couvrant 98 % des surfaces via des `UMaterialInstanceConstant` (`MI_`).
2. Remplacer les `StaticSwitchParameter` par des **Per-Instance Custom Primitive Data** (jusqu'à 32 floats par instance HISM/Nanite) pour varier la couleur, la salissure latéritique et l'humidité sans créer un seul PSO supplémentaire.
3. Auditer la complexité d'instructions shaders dans le Material Editor (`<= 140 instructions` Pixel Shader pour l'environnement opaque, `<= 220` pour la peau SSS).
4. Documenter l'architecture de chaque Master Material dans `templates/master-material-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Artiste demandant un Static Switch supplémentaire doublant le nombre de permutations PSO d'un Master Material | Refuser le Static Switch et implémenter l'effet via un masque de canal ou un float CustomPrimitiveData évalué dynamiquement | Éviter l'explosion combinatoire des PSO ($2^N$) |
| Shader d'environnement dépassant 140 instructions Pixel Shader | Pré-cuire les opérations mathématiques procédurales lourdes dans une texture ORM/Masque 2K ou basculer le calcul sur les Vertex/Interpolants | Tenir le budget GPU de rendu ENG-06 |
| Rig de véhicule (ex: VEH-MOTO-WEWA-01) comportant plus de 35 os actifs | Simplifier la hiérarchie osseuse à <= 24 os (châssis, fourche, guidon, bras oscillant, 2 roues, béquille, suspension) | Optimiser le coût CPU Chaos Vehicles ENG-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/shader-pso-and-rigging-rules.md`
- **Modèle Officiel de Livrable** : `templates/master-material-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-master-material-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-master-material-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/master-material-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-08` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le nombre total de Master Materials du studio reste `<= 10` et le nombre de `StaticSwitch` par Master Material est `<= 3`.
- [ ] Tous les shaders d'environnement standard respectent le plafond de `140 instructions` Pixel Shader.
- [ ] Les rigs de véhicules et de personnages passent le test de déformation extrême sans artefact.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-06`, `ENG-07`, `DIR-04`.
