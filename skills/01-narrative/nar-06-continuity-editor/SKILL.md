---
name: nar-06-continuity-editor
description: "Contrôle qualité éditorial et audit anti-contradiction de ZAÏRE STUDIO OS. Vérifie la continuité narrative, temporelle, spatiale et d'état des personnages (vivant/mort/allié/hostile) entre toutes les missions (GD-02) et tous les livrables narratifs (NAR-01 à NAR-05)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-06
  department: 01-narrative
  stratum: 5
  version: "1.1.0"
  inputs:
    - "all-narrative-deliverables-nar-01-to-05"
    - "mission-state-machines-gd-02"
    - "knowledge/entities-registry.csv"
  outputs:
    - "continuity-audit-report.md"
    - "narrative-conflict-tickets.csv"
  upstream_dependencies:
    - "NAR-01"
    - "NAR-02"
    - "NAR-03"
    - "NAR-04"
    - "NAR-05"
    - "GD-02"
---

# `NAR-06` — Continuity Editor (`nar-06-continuity-editor`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **5**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Avant toute promotion d'un livrable narratif (`NAR-01`..`NAR-05`) ou d'une mission (`GD-02`) au statut `CONFIRMED`.
- Modification d'un embranchement dans `NAR-01` ou d'une condition d'état dans `GD-02`.
- Audit de fin de vague (Strate 5 du DAG) commandé par `DIR-01`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `all-narrative-deliverables-nar-01-to-05`, `mission-state-machines-gd-02`, `knowledge/entities-registry.csv`
- **Sorties produites** : `continuity-audit-report.md`, `narrative-conflict-tickets.csv`
- **Dépendances Amont Canoniques (DAG)** : `NAR-01`, `NAR-02`, `NAR-03`, `NAR-04`, `NAR-05`, `GD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne réécrit jamais intégralement une scène ou une mission ; identifie précisément la contradiction et émet un ticket de correction vers le skill auteur.
- **Interdiction / Limite** : Ne valide jamais un livrable contenant une référence fantôme absente de `knowledge/entities-registry.csv`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Extraire tous les identifiants (`CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*`, `ITM-*`, `VEH-*`, `SYS-*`) cités dans le livrable et vérifier leur existence dans `knowledge/entities-registry.csv`.
2. Contrôler la **Matrice d'États Temporels** : s'assurer qu'aucun personnage indisponible, arrêté ou hostile à l'étape $T$ n'apparaît comme donneur de quête amical à l'étape $T+1$ sans condition explicite.
3. Vérifier la cohérence des registres de voix avec `NAR-03` et du lexique lingala avec `knowledge/world-bible/lingala-french-glossary.csv`.
4. Émettre le verdict (`CONTINUITY_PASSED` ou `CONTINUITY_BLOCKED`) dans `templates/continuity-checklist.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Quête secondaire accessible alors que son donneur CHR-* est indisponible dans l'Acte courant | Émettre un verdict CONTINUITY_BLOCKED et exiger de GD-02 l'ajout d'une précondition Gameplay Tag sur la machine à états | Empêcher tout paradoxe narratif en monde ouvert |
| Contradiction biographique ou territoriale entre deux fiches (ex: QG d'une faction situé dans deux communes différentes) | Bloquer la promotion et renvoyer les deux fiches à NAR-03/NAR-05 pour alignement sur entities-registry.csv | Noter le conflit dans narrative-conflict-tickets.csv |
| Usage d'un terme lingala altéré sans ses caractères Unicode (ex: 'Tokende' au lieu de 'Tɔ́kɛndɛ́') | Demander la normalisation orthographique immédiate selon lingala-french-glossary.csv | Garantir la qualité LQA avec AUD-04 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/continuity-audit-rules.md`
- **Modèle Officiel de Livrable** : `templates/continuity-checklist.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-continuity-audit.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-continuity-audit.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/continuity-checklist.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 0 contradiction d'état de personnage, de lieu ou de chronologie sur l'ensemble du graphe de quêtes audité.
- [ ] 100 % des IDs référencés dans les scripts et dialogues existent dans `knowledge/entities-registry.csv`.
- [ ] Conformité orthographique totale avec `knowledge/world-bible/lingala-french-glossary.csv`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-06`, `DIR-07`.
