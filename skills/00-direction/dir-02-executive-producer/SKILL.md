---
name: dir-02-executive-producer
description: "Gouvernance exécutive, cadrage du périmètre (scope), arbitrage budgétaire et validation des jalons majeurs (Vertical Slice, Alpha, Beta, Gold) de ZAÏRE. Garantit l'équilibre entre ambition open-world à Kinshasa, vélocité de production et maîtrise des risques."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: DIR-02
  department: 00-direction
  stratum: 0
  version: "1.1.0"
  inputs:
    - "execution-plan-dag.json"
    - "risk-register.csv"
    - "sprint-velocity-metrics"
  outputs:
    - "milestone-gate-review.md"
    - "scope-arbitration-decision.md"
  upstream_dependencies:
    - "DIR-01"
---

# `DIR-02` — Executive Producer (`dir-02-executive-producer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`00-direction`** (Strate DAG **0**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Validation d'un passage de jalon (Concept, Vertical Slice, Alpha, Beta, Certification Gold).
- Demande d'ajout d'une fonctionnalité majeure ou d'une nouvelle commune de Kinshasa non planifiée.
- Escalade par DIR-01 ou PRD-02 d'un risque critique (score >= 12/25) menaçant le chemin critique.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `execution-plan-dag.json`, `risk-register.csv`, `sprint-velocity-metrics`
- **Sorties produites** : `milestone-gate-review.md`, `scope-arbitration-decision.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'intervient jamais dans l'écriture du code C++ (`ENG-01`/`ENG-02`) ni dans le réglage artistique des shaders (`ART-08`).
- **Interdiction / Limite** : Ne sacrifie jamais la conformité d'accessibilité XAG (`PRD-06`) ou la stabilité technique (`DIR-04`) pour accélérer un jalon.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Évaluer la proposition de fonctionnalité ou l'état du jalon par rapport à la capacité des 8 départements et au buffer de contingence de 15 %.
2. Croiser les dépendances avec le registre des risques (`PRD-02`) et les lacunes documentaires (`research/research-gaps.md`).
3. Classer chaque livrable du jalon en `MUST_HAVE (P0)`, `SHOULD_HAVE (P1)` ou `DEFERRED_POST_LAUNCH (P2)`.
4. Prononcer la décision d'arbitrage (`GO`, `CONDITIONAL_GO`, `NO_GO_SCOPE_CUT`) dans `templates/milestone-gate-review.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Dérive de charge estimée > +10 % sur un jalon | Activer le Feature Gating : déprioriser les éléments P2 ou restreindre la densité aux communes P0 (Gombe, Matonge, Kalamu, Limete) | Marquer les entités coupées au statut DEPRECATED via DIR-06 |
| Commune en statut RESEARCH_REQUIRED (ex: DST-MASINA) sur le chemin critique | Isoler la commune hors du Vertical Slice et maintenir le focus sur DST-GOMBE et DST-MATONGE | Assigner une tâche prioritaire d'acquisition SIG à WLD-03 |
| Risque juridique sur licences musicales (AUD-03) | Exiger l'activation par défaut du fallback Streamer Safe composé en interne | Bloquer l'intégration de la piste jusqu'à validation contractuelle |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/milestone-governance.md`
- **Modèle Officiel de Livrable** : `templates/milestone-gate-review.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-scope-arbitration.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-scope-arbitration.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/milestone-gate-review.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `DIR-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Écart budgétaire et capacitaire maintenu dans l'enveloppe de tolérance de ±5 %.
- [ ] 100 % des coupes de périmètre (Scope Cuts) identifient les IDs d'entités à passer en `DEPRECATED`.
- [ ] Chaque jalon dispose de critères d'entrée et de sortie mesurables validés avec `DIR-04` et `DIR-07`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-01`, `DIR-07`.
