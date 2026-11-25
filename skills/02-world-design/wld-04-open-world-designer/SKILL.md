---
name: wld-04-open-world-designer
description: "Macro-conception de la carte monde ouvert de Kinshasa. Définit le découpage en cellules UE5 World Partition, la hiérarchie des repères visuels (landmarks : Tour de l'Échangeur, Fleuve Congo), la distribution des Points d'Intérêt (LOC-*) et la règle de rythme des 40 secondes."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-04
  department: 02-world-design
  stratum: 1
  version: "1.1.0"
  inputs:
    - "world-bible-wld-01"
    - "urban-typology-wld-03"
    - "game-systems-gd-01"
    - "streaming-budgets-dir-04"
  outputs:
    - "poi-specification.md"
    - "world-pacing-matrix.csv"
    - "landmark-sightlines-map.md"
  upstream_dependencies:
    - "WLD-01"
    - "WLD-03"
    - "GD-01"
    - "DIR-04"
    - "DIR-05"
---

# `WLD-04` — Open World Designer (`wld-04-open-world-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou placement d'un nouveau Point d'Intérêt (`LOC-*`) dans une commune de Kinshasa (`DST-*`).
- Calibrage des distances de traversée à pied et en véhicule (`VEH-*`) et des lignes de mire (sightlines) entre quartiers.
- Définition des règles de densité d'activités et des cellules de streaming World Partition avec `ENG-01`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `world-bible-wld-01`, `urban-typology-wld-03`, `game-systems-gd-01`, `streaming-budgets-dir-04`
- **Sorties produites** : `poi-specification.md`, `world-pacing-matrix.csv`, `landmark-sightlines-map.md`
- **Dépendances Amont Canoniques (DAG)** : `WLD-01`, `WLD-03`, `GD-01`, `DIR-04`, `DIR-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne conçoit pas le blockout géométrique intérieur ni le placement micro des couverts de combat (`WLD-05`).
- **Interdiction / Limite** : Ne modifie pas les budgets mémoire VRAM ou la taille technique du pool de streaming C++ (`DIR-04`/`ENG-01`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Attribuer au Point d'Intérêt un identifiant `LOC-[DST]-[SLUG]` et l'associer à sa commune parente `DST-*` dans `knowledge/entities-registry.csv`.
2. Appliquer la **Règle des 40 Secondes** : vérifier qu'un joueur se déplaçant à pied rencontre une opportunité visuelle, systémique (`AI-04`) ou ludique toutes les 35 à 45 secondes.
3. Configurer la **Hiérarchie des Landmarks (`SYS-WLD-LANDMARKS`)** : s'assurer qu'au moins un repère de Niveau 1 (ex: `LOC-LIMETE-ECHANGEUR` à l'est, le fleuve Congo au nord) ou de Niveau 2 est visible depuis chaque carrefour principal.
4. Documenter les contraintes de streaming (Data Layers jour/nuit/mission, rayon HLOD) dans `templates/poi-specification-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Deux POI lourds ( > 20 PNJ AI-01 actifs) placés à moins de 150 mètres l'un de l'autre | Espacer les POI d'au moins 250 mètres (2 cellules World Partition de 128m) ou placer une barrière d'occlusion visuelle (bâtiment coudé) | Prévenir tout pic simultané sur le Game Thread et le streaming |
| Quartier où le joueur perd ses repères cardinaux sans ouvrir la carte UI | Ouvrir un cône de visibilité (sightline) sur l'axe routier vers le landmark majeur de la commune | Garantir la navigation diégétique SYS-WLD-LANDMARKS |
| POI situé dans une commune au statut RESEARCH_REQUIRED | Marquer le POI au statut RESEARCH_REQUIRED ou PROPOSED [CONCEPT] | Attendre la validation WLD-03 avant blockout WLD-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/open-world-pacing-and-landmarks.md`
- **Modèle Officiel de Livrable** : `templates/poi-specification-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-poi-specification.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-poi-specification.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/poi-specification-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque `LOC-*` possède un ID valide, des coordonnées de cellule World Partition et une fonction claire dans les Core Loops.
- [ ] Aucun chevauchement de rayon d'activation IA critique (`AI-01`) entre deux POI adjacents.
- [ ] Orientation cardinale possible sans mini-carte grâce aux lignes de mire documentées.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `ENG-01`, `WLD-05`.
