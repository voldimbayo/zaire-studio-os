---
name: prd-01-production-planner
description: "Planification opérationnelle de la production de ZAÏRE : découpage en sprints Agiles/Hybrides, matrices RACI inter-départements, suivi du chemin critique (Blockout WLD-05 -> Env Art ART-02 -> Lighting ART-07 -> Perf ENG-07) et intégration d'un buffer de contingence de 15 %."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: PRD-01
  department: 08-production-quality
  stratum: 1
  version: "1.1.0"
  inputs:
    - "orchestration-dag-dir-01"
    - "milestone-targets-dir-02"
    - "architecture/skill-dependencies.md"
  outputs:
    - "sprint-execution-plan.md"
    - "department-raci-matrix.csv"
  upstream_dependencies:
    - "DIR-01"
    - "DIR-02"
---

# `PRD-01` — Production Planner (`prd-01-production-planner`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`08-production-quality`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Traduction d'un jalon exécutif (`DIR-02` : Vertical Slice, Alpha, Beta, Gold) en plannings de sprints de 2 semaines pour les 8 départements.
- Résolution d'un goulot d'étranglement inter-départements (ex: attente de validation d'un blockout `WLD-05` avant démarrage d'`ART-02`).
- Replanification dynamique suite à l'apparition d'un ticket `BLOCKED` ou `RESEARCH_REQUIRED`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `orchestration-dag-dir-01`, `milestone-targets-dir-02`, `architecture/skill-dependencies.md`
- **Sorties produites** : `sprint-execution-plan.md`, `department-raci-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-01`, `DIR-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne décide pas seul d'une coupe de fonctionnalité majeure (`DIR-02`) ni d'un compromis sur les budgets techniques (`DIR-04`).
- **Interdiction / Limite** : Interdit toute planification de sprint saturée à 100 % sans la réserve de **15 % de buffer d'aléas Open World**.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Ordonner les tâches du sprint en respectant les 6 strates topologiques de `architecture/skill-dependencies.md` (Strate 0 -> Strate 5).
2. Allouer maximum **85 % de la capacité** de chaque département aux tâches planifiées et réserver **15 % de buffer** pour absorber les itérations playtest (`DIR-05`) et optimisations P99 (`ENG-07`).
3. Établir la matrice **RACI** (*Responsible, Accountable, Consulted, Informed*) de chaque livrable en s'assurant qu'un seul skill est `Responsible (R)`.
4. Documenter le plan de sprint dans `templates/sprint-plan-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Tâche d'Environment Art (ART-02) planifiée dans le même sprint que le blockout Level Design (WLD-05) du même lieu | Décaler la production ART-02 au sprint N+1 : le sprint N est consacré au blockout WLD-05 et à sa validation playtest DIR-05 | Appliquer strictement la règle Blockout First |
| Blocage de plus de 24h sur une dépendance RESEARCH_REQUIRED (ex: WLD-02/WLD-03) | Basculer la capacité du département aval sur une commune CONFIRMED (ex: DST-GOMBE ou DST-MATONGE) pendant que la recherche aboutit | Éviter tout temps mort sur le chemin critique |
| Consommation complète du buffer de 15 % avant la fin de la première semaine du sprint | Déclencher une alerte précoce vers DIR-02 et PRD-02 pour déprioriser les tâches P2 du sprint | Garantir un taux de complétion des engagements P0 >= 90 % |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/agile-openworld-production.md`
- **Modèle Officiel de Livrable** : `templates/sprint-plan-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-sprint-plan.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-sprint-plan.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/sprint-plan-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `PRD-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque tâche du sprint possède un unique skill `Responsible (R)` et respecte l'ordre DAG.
- [ ] Un buffer de capacité de `15 %` est explicitement provisionné.
- [ ] Aucun livrable `ART-02` n'est planifié sans un blockout `WLD-05` préalablement validé.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-01`, `DIR-02`.
