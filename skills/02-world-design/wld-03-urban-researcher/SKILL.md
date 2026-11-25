---
name: wld-03-urban-researcher
description: "Analyse de la morphologie urbaine, du réseau viaire, de la topographie et des typologies architecturales de Kinshasa. Traduit les données SIG/OpenStreetMap en règles géométriques d'urbanisme exploitables par Open World Design (WLD-04), Houdini (ENG-04) et Traffic AI (AI-03)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-03
  department: 02-world-design
  stratum: 1
  version: "1.1.0"
  inputs:
    - "osm-gis-data"
    - "district-profiles-wld-01"
    - "knowledge/technical-specs/spatial-metrics.md"
  outputs:
    - "urban-typology-spec.md"
    - "road-network-hierarchy.csv"
  upstream_dependencies:
    - "DIR-03"
    - "DIR-04"
---

# `WLD-03` — Urban Researcher (`wld-03-urban-researcher`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Définition des règles de génération procédurale d'une commune (`DST-*`) pour SideFX Houdini (`ENG-04`).
- Spécification des profils de voirie (largeur des voies, trottoirs, terre-pleins, drainage) et des ronds-points pour `AI-03`.
- Classification des gabarits d'îlots urbains et de hauteur de bâti entre la Gombe, Limete, Matonge et Kalamu.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `osm-gis-data`, `district-profiles-wld-01`, `knowledge/technical-specs/spatial-metrics.md`
- **Sorties produites** : `urban-typology-spec.md`, `road-network-hierarchy.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas directement les noeuds VEX ou graphes HDA dans Houdini (`ENG-04`).
- **Interdiction / Limite** : Ne modélise pas les meshes 3D finaux (`ART-02`) ; fournit les règles dimensionnelles et d'implantation.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Classer le tissu urbain de la zone cible selon les 4 typologies kinoises : (A) Grille Administrative/Moderne (`DST-GOMBE`), (B) Tissu Commercial Dense (`DST-MATONGE`), (C) Parcellaire Résidentiel Organique (`DST-KALAMU`), (D) Zone Industrielle/Portuaire (`DST-LIMETE`, `LOC-GOMBE-PORT`).
2. Spécifier les dimensions de voirie en conformité stricte avec `knowledge/technical-specs/spatial-metrics.md` (`400 cm`/voie sur boulevard, `350 cm`/voie sur avenue, trottoirs `250-600 cm`).
3. Identifier les zones où les données OpenStreetMap sont incomplètes (`research/research-gaps.md`) et définir les règles de subdivision procédurale compensatoire ou le statut `RESEARCH_REQUIRED`.
4. Documenter les règles dans `templates/urban-typology-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Quartier secondaire (ex: DST-MASINA) dépourvu de tracés de ruelles précis dans OSM | Fournir une règle de subdivision d'îlots orthogonale/organique paramétrique (parcelles 15x25m) et marquer les repères spécifiques en RESEARCH_REQUIRED | Permettre à ENG-04 de tester le HDA sans inventer de monuments erronés |
| Axe routier trop étroit pour le croisement de deux bus VEH-BUS-TRANSCO-01 | Imposer une largeur minimale de chaussée de 700 cm (2 voies de 350 cm) ou restreindre la spline ZoneGraph aux taxis et motos Wewa | Synchroniser avec AI-03 |
| Transition abrupte entre sol en asphalte et ruelle en latérite | Spécifier une bande de transition de 200 cm avec caniveau de drainage ouvert pour l'intégration RVT (ART-02) | Respecter la morphologie réelle des voiries kinoises |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/kinshasa-urban-morphology.md`
- **Modèle Officiel de Livrable** : `templates/urban-typology-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-urban-typology.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-urban-typology.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/urban-typology-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Toutes les cotes routières et parcellaires sont exprimées en centimètres UE5 (`1 UU = 1 cm`).
- [ ] Chaque typologie d'îlot définit le nombre d'étages min/max, le retrait de façade et la densité de câblage/végétation.
- [ ] Compatibilité validée avec le générateur procédural `ENG-04` et le graphe routier `AI-03`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `WLD-04`, `ENG-04`, `AI-03`.
