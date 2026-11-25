---
name: eng-04-houdini-specialist
description: "Ingénierie procédurale sous SideFX Houdini (HDA / PDG TOPs) et Unreal Engine 5 PCG (Procedural Content Generation). Transforme les données OpenStreetMap/DEM et les règles d'urbanisme de Kinshasa (WLD-03) en réseaux routiers ZoneGraph (AI-03), îlots modulaires HISM/Nanite (ART-02), câblages aériens et végétation déterministes."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-04
  department: 07-engineering
  stratum: 3
  version: "1.1.0"
  inputs:
    - "urban-typology-wld-03"
    - "modular-kits-art-02"
    - "traffic-zonegraph-rules-ai-03"
  outputs:
    - "hda-pcg-pipeline-spec.md"
    - "procedural-generation-rules.csv"
  upstream_dependencies:
    - "WLD-03"
    - "ART-02"
    - "GD-06"
---

# `ENG-04` — Houdini Specialist (`eng-04-houdini-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Génération ou mise à jour procédurale d'une commune de Kinshasa (`DST-*`) à partir des tracés routiers OSM et des gabarits `WLD-03`.
- Assemblage automatique des façades modulaires (`ART-02`) par îlots urbains (méthodologie Insomniac Games `SRC-008` & Epic City Sample `SRC-004`).
- Génération automatique des splines `ZoneGraph` (voies véhicules `350-400 cm`, sous-voies Wewa `130-150 cm`, trottoirs piétons `AI-02`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `urban-typology-wld-03`, `modular-kits-art-02`, `traffic-zonegraph-rules-ai-03`
- **Sorties produites** : `hda-pcg-pipeline-spec.md`, `procedural-generation-rules.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-03`, `ART-02`, `GD-06`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'altère jamais les monuments héroïques sculptés sur mesure (`LOC-LIMETE-ECHANGEUR`) ni les arènes de mission en blockout manuel (`WLD-05`).
- **Interdiction / Limite** : Interdit toute génération non déterministe (tout graphe HDA/PCG doit utiliser un `GlobalSeed` fixe reproductible à 100 %).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Étape 1 (Réseau Viaire & ZoneGraph) : Ingérer les courbes OSM dans le HDA `HDA_Zaire_RoadNetwork`, extruder les chaussées aux cotes exactes de `WLD-03` et exporter simultanément les meshes routiers et les tags de voies `ZoneGraph` pour `AI-02`/`AI-03`.
2. Étape 2 (Subdivision Parcellaire & Bâti) : Subdiviser les îlots en lots (`1200 cm` de façade à Matonge), en excluant automatiquement tout volume couvert par un tag `PCG_Exclusion_ManualLevelDesign` (`WLD-05`).
3. Étape 3 (Instanciation Nanite & Custom Data) : Peupler les façades via des `UHierarchicalInstancedStaticMeshComponent` (HISM) / `PCG Static Mesh Spawner` en injectant les variations de couleur et d'usure dans `CustomPrimitiveData[0..3]` (`ART-08`).
4. Étape 4 (Habillage Secondaire PCG) : Générer les poteaux électriques, câbles caténaires, étals de rue et végétation tropicale en respectant la marge libre minimale de `350 cm` sur les cheminements piétons.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Intersection entre un îlot procédural Houdini/PCG et un blockout de mission WLD-05 (ex: LOC-GOMBE-PORT) | Prioriser à 100 % le volume manuel WLD-05 via un Box Volume taggé PCG_Exclude_ManualArena qui soustrait les points PCG dans son empreinte | Garantir zéro obstacle procédural dans une arène de mission |
| Secteur dont la couverture OSM des ruelles secondaires est incomplète (ex: DST-MASINA en RESEARCH_REQUIRED) | Appliquer l'algorithme de subdivision L-System / Voronoï orthogonal calibré par WLD-03 uniquement sur un Data Layer de prévisualisation taggé PROPOSED_PROCEDURAL | Séparer clairement la donnée SIG vérifiée du remplissage procédural |
| Génération d'îlot créant plus de 1500 acteurs individuels dans l'Outliner UE5 | Fusionner les descripteurs d'instances par cellule World Partition (128m) dans des composants Instanced Static Mesh (ISM/HISM) packés | Maintenir un coût d'instanciation minimal en mémoire et en draw calls |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/houdini-pdg-and-ue5-pcg.md`
- **Modèle Officiel de Livrable** : `templates/hda-pipeline-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-hda-pcg-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-hda-pcg-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/hda-pipeline-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Génération 100 % déterministe à seed fixe (`GlobalSeed = 19600630`).
- [ ] Les splines `ZoneGraph` générées respectent les largeurs de voies (`350-400 cm`) et les couloirs inter-files Wewa (`>= 130 cm`).
- [ ] Respect absolu des volumes d'exclusion `WLD-05` (zéro prop procédural sur un chemin critique ou un couvert).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `WLD-04`, `ENG-07`, `AI-03`.
