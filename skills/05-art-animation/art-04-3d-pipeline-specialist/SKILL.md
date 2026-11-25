---
name: art-04-3d-pipeline-specialist
description: "Ingénierie du pipeline 3D et standardisation géométrique de ZAÏRE STUDIO OS. Définit les règles de topologie UE5 Nanite, de Texel Density (10.24 px/cm), d'alignement des pivots sur grille, d'UV mapping, de baking et les règles de validation pré-commit (scripts/check_3d_standards.py)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-04
  department: 05-art-animation
  stratum: 1
  version: "1.1.0"
  inputs:
    - "hardware-budgets-dir-04"
    - "art-direction-art-01"
  outputs:
    - "3d-modeling-standards.md"
    - "asset-validation-rules.json"
  upstream_dependencies:
    - "DIR-04"
    - "ART-01"
---

# `ART-04` — 3D Pipeline Specialist (`art-04-3d-pipeline-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Définition des conventions d'export FBX/USD et des préfixes de nommage UE5 (`SM_`, `SK_`, `M_`, `MI_`, `T_`).
- Spécification des règles de validation automatique à implémenter dans l'éditeur UE5 par `ENG-03` (Tools Programmer).
- Contrôle de conformité d'un lot d'assets `ART-02` ou `ART-03` via `scripts/check_3d_standards.py`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `hardware-budgets-dir-04`, `art-direction-art-01`
- **Sorties produites** : `3d-modeling-standards.md`, `asset-validation-rules.json`
- **Dépendances Amont Canoniques (DAG)** : `DIR-04`, `ART-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne code pas le plugin C++ Slate de l'éditeur (`ENG-03`), mais fournit le fichier `asset-validation-rules.json` qui le pilote.
- **Interdiction / Limite** : N'accorde aucune dérogation sur l'échelle (`1 UU = 1 cm`), l'orientation (`+X Forward`) ou l'interdiction du Translucide sur Nanite.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Vérifier la nomenclature de chaque asset soumis selon la convention : `SM_` (Static Mesh), `SK_` (Skeletal Mesh), `M_` (Master Material), `MI_` (Material Instance), `T_` (Texture avec suffixe `_D`, `_N`, `_ORM`).
2. Exécuter `scripts/check_3d_standards.py` pour valider la Texel Density (`10.24 px/cm`), le placement du pivot sur la grille et la distance de coupure WPO (`<= 3500 cm`).
3. Contrôler la présence obligatoire de `UV0` (textures PBR, padding `>= 8 px` en 2K) et `UV1` (si requis pour masques secondaires).
4. Publier les règles mises à jour dans `templates/asset-validation-rules.json`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Static Mesh architectural soumis avec Nanite activé ET un matériau Blend Mode = Translucent | Bloquer immédiatement l'asset : séparer les vitres translucides dans un sous-mesh distinct non-Nanite (LOD standard) | Respecter les contraintes matérielles du rasterizer Nanite UE5 |
| Texture soumise avec une dimension non puissance de 2 (ex: 1500x1500) | Rejeter l'import : imposer des dimensions puissances de 2 (512, 1024, 2048, 4096) pour permettre la génération de MipMaps et la compression BC7 | Éviter tout gaspillage VRAM non streamable |
| Asset modulaire dont le pivot est centré au milieu de la géométrie au lieu du coin de grille | Renvoyer l'asset en correction DCC (Blender/Maya) pour replacer le pivot sur la grille 10/50/100 cm | Garantir la compatibilité avec le snapping WLD-05/WLD-06 et Houdini ENG-04 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/ue5-3d-pipeline-norms.md`
- **Modèle Officiel de Livrable** : `templates/asset-validation-rules.json`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-3d-validation-report.md`
- `scripts/check_3d_standards.py` : Script exécutable déterministe associé à `ART-04` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-3d-validation-report.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/asset-validation-rules.json` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/05-art-animation/art-04-3d-pipeline-specialist/scripts/check_3d_standards.py` retourne un code `0`.
- [ ] 100 % des règles de `asset-validation-rules.json` sont déterministes et vérifiables par `ENG-03`.
- [ ] Zéro texture non compressée ou sans MipMaps dans le pipeline.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-03`, `ART-08`, `DIR-04`.
