---
name: wld-05-level-designer
description: "Conception spatiale détaillée des espaces jouables (LOC-*), blockout/greyboxing 3D, application stricte des métriques de déplacement, de caméra, de couverture et de parkour (spatial-metrics.md) selon la méthodologie Blockout First avant tout habillage artistique."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-05
  department: 02-world-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "poi-specs-wld-04"
    - "mission-design-gd-02"
    - "combat-metrics-gd-05"
    - "knowledge/technical-specs/spatial-metrics.md"
  outputs:
    - "level-blockout-brief.md"
    - "blockout-metrics-validation.json"
  upstream_dependencies:
    - "WLD-04"
    - "GD-02"
    - "GD-05"
    - "DIR-05"
---

# `WLD-05` — Level Designer (`wld-05-level-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création de la géométrie de gameplay (greybox) d'une arène de mission (`MSN-*`) ou d'un intérieur/extérieur de POI (`LOC-*`).
- Placement des couverts de combat (`100 cm` / `200 cm`), des points d'accroche parkour (`260-300 cm`) et des volumes NavMesh / Smart Links (`AI-01`).
- Vérification métrique obligatoire avant le passage de relais à `WLD-06` (Environment Designer) et `ART-02` (Environment Artist).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `poi-specs-wld-04`, `mission-design-gd-02`, `combat-metrics-gd-05`, `knowledge/technical-specs/spatial-metrics.md`
- **Sorties produites** : `level-blockout-brief.md`, `blockout-metrics-validation.json`
- **Dépendances Amont Canoniques (DAG)** : `WLD-04`, `GD-02`, `GD-05`, `DIR-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'applique jamais de matériaux PBR finaux, de végétation haute densité ou de set dressing purement esthétique (`ART-02`).
- **Interdiction / Limite** : Ne transmet jamais un niveau à `WLD-06`/`ART-02` tant que le script `scripts/check_spatial_metrics.py` et le playtest `DIR-05` ne sont pas validés.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Charger `knowledge/technical-specs/spatial-metrics.md` et fixer la grille de snapping UE5 sur `10 / 50 / 100 / 400 cm`.
2. Construire les volumes de circulation en garantissant une largeur minimale de **`350 cm`** pour tout couloir jouable (`500 cm` en zone de mêlée) et **`130 cm`** pour tout passage moto Wewa.
3. Intégrer le guidage visuel précoce par le contraste lumineux dès le blockmesh (méthodologie Naughty Dog `SRC-012`) en collaboration avec `ART-07`.
4. Exécuter `scripts/check_spatial_metrics.py` sur les paramètres du blockout et consigner le résultat dans `templates/level-blockout-brief.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Couloir ou passage intérieur < 350 cm détecté par check_spatial_metrics.py | Élargir immédiatement le volume géométrique à >= 350 cm avant toute validation | Éliminer les collisions de SpringArm caméra 3e personne |
| Arène de combat dépourvue d'options de flanquement ou de verticalité | Ajouter au moins une boucle de circulation latérale et un point d'élévation accessible en vault (100 cm) ou ledge grab (280 cm) | Synchroniser avec GD-05 et AI-01 (requêtes EQS) |
| Demande d'habillage artistique anticipé par ART-02 sur un blockout non validé | Refuser le handoff en vertu de la règle Blockout First (quality-standards.md) | Maintenir le verrou jusqu'au feu vert DIR-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/blockout-and-spatial-rules.md`
- **Modèle Officiel de Livrable** : `templates/level-blockout-brief.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-level-blockout.md`
- `scripts/check_spatial_metrics.py` : Script exécutable déterministe associé à `WLD-05` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-level-blockout.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/level-blockout-brief.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/02-world-design/wld-05-level-designer/scripts/check_spatial_metrics.py` retourne un code `0`.
- [ ] Chaque arène supporte les approches prévues par `GD-02` (infiltration, mêlée/tir, fuite) sans cul-de-sac involontaire.
- [ ] Les volumes NavMesh, Smart Links et zones d'occlusion sont explicitement balisés.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `AI-01`, `WLD-06`.
