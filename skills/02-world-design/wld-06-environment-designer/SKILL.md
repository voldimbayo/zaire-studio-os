---
name: wld-06-environment-designer
description: "Direction environnementale par lieu (LOC-*). Traduit les blockouts gameplay validés (WLD-05), l'Art Bible (ART-01) et la recherche urbaine/culturelle (WLD-02/WLD-03) en briefs de production détaillés, listes de kits architecturaux modulaires et plans de narration environnementale."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-06
  department: 02-world-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "validated-blockouts-wld-05"
    - "art-bible-art-01"
    - "cultural-briefs-wld-02"
    - "urban-typology-wld-03"
  outputs:
    - "environment-design-brief.md"
    - "modular-asset-kit-manifest.csv"
  upstream_dependencies:
    - "WLD-05"
    - "ART-01"
    - "WLD-02"
    - "WLD-03"
---

# `WLD-06` — Environment Designer (`wld-06-environment-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Réception d'un blockout `WLD-05` ayant obtenu le statut `APPROVED_FOR_ENV_ART` auprès de `DIR-05`.
- Définition des kits architecturaux modulaires, de la végétation tropicale et de l'habillage (set dressing) d'un lieu `LOC-*`.
- Conception du storytelling visuel par couches (histoire du lieu, traces de vie quotidienne kinoise, météo et patine).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `validated-blockouts-wld-05`, `art-bible-art-01`, `cultural-briefs-wld-02`, `urban-typology-wld-03`
- **Sorties produites** : `environment-design-brief.md`, `modular-asset-kit-manifest.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-05`, `ART-01`, `WLD-02`, `WLD-03`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'altère jamais les dimensions de collision ni la hauteur des couverts validés dans le blockout `WLD-05`.
- **Interdiction / Limite** : Ne modélise pas directement les géométries dans Blender/Maya (`ART-02`) et ne programme pas les shaders HLSL (`ART-08`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Décomposer les volumes gris du blockout `WLD-05` en modules architecturaux standardisés sur la grille (`400x400 cm`, `200x400 cm`, `100x200 cm`).
2. Appliquer les **3 Couches de Narration Environnementale** : (1) Structure Architecturale & Histoire, (2) Fonction Économique & Signalétique (`NAR-05`), (3) Micro-traces de Vie Quotidienne & Météo.
3. Dresser le manifeste exact des kits modulaires, matériaux PBR (latérite, béton humide, tôle) et props requis dans `templates/environment-brief-template.md`.
4. Vérifier que l'habillage préserve à 100 % la lisibilité des parcours et des points d'accroche parkour.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Demande d'ajout d'éléments de décor réduisant un couloir de 400 cm en dessous de 350 cm | Interdire tout prop à collision dans l'enveloppe des 350 cm ou placer l'habillage en retrait mural/plafond | Préserver l'intégrité du NavMesh et de la caméra WLD-05 |
| Besoin d'un asset architectural unique non réutilisable | Limiter les meshes uniques aux Landmarks Tier 1/2 et composer 85 % du bâti avec les kits modulaires partagés | Respecter le budget VRAM de DIR-04 et ART-04 |
| Signalétique ou enseigne de rue requise sur une façade | Utiliser exclusivement les textes validés par NAR-05 et WLD-02 | Éviter tout texte placeholder générique |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/environmental-storytelling-layers.md`
- **Modèle Officiel de Livrable** : `templates/environment-brief-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-environment-brief.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-environment-brief.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/environment-brief-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le taux de réutilisation modulaire du manifeste d'assets est `>= 80 %` sur le quartier.
- [ ] Les 3 couches de narration environnementale sont détaillées avec références culturelles (`WLD-02`).
- [ ] 0 collision ajoutée dans les volumes de franchissement ou de couverture du blockout `WLD-05`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ART-01`, `WLD-05`, `ART-08`.
