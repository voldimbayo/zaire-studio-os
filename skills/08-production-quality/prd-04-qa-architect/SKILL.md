---
name: prd-04-qa-architect
description: "Architecture globale de l'Assurance Qualité (QA) de ZAÏRE : plans de test Open World par quadrillage géographique des cellules World Partition de Kinshasa, matrices de test des machines à états de quêtes (zéro soft-lock), protocoles de reproductibilité déterministe (>= 90 %) et checklists de certification plateforme."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: PRD-04
  department: 08-production-quality
  stratum: 5
  version: "1.1.0"
  inputs:
    - "mission-design-gd-02"
    - "open-world-grid-wld-04"
    - "gameplay-cpp-specs-eng-02"
  outputs:
    - "master-qa-test-plan.md"
    - "deterministic-bug-report.json"
  upstream_dependencies:
    - "GD-02"
    - "WLD-04"
    - "ENG-02"
---

# `PRD-04` — QA Architect (`prd-04-qa-architect`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`08-production-quality`** (Strate DAG **5**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception du plan de test fonctionnel et destructif (Destructive QA) d'une nouvelle mission (`MSN-*`), d'un système (`SYS-*`) ou d'une commune (`DST-*`).
- Triage et qualification de la sévérité (`SEV-A Blocker`, `SEV-B Critical`, `SEV-C Major`, `SEV-D Minor`) des anomalies avant passage de jalon.
- Préparation du cahier de tests à automatiser par `PRD-05` sous Unreal Gauntlet.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `mission-design-gd-02`, `open-world-grid-wld-04`, `gameplay-cpp-specs-eng-02`
- **Sorties produites** : `master-qa-test-plan.md`, `deterministic-bug-report.json`
- **Dépendances Amont Canoniques (DAG)** : `GD-02`, `WLD-04`, `ENG-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'écrit pas le code C++ des contrôleurs automatisés Gauntlet (`PRD-05`).
- **Interdiction / Limite** : Refuse tout rapport de bug dépourvu des coordonnées exactes World Partition, du `GlobalSeed`, de l'état des Gameplay Tags et des étapes de reproduction déterministes.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Découper chaque commune (`DST-*`) selon la grille de cellules `World Partition (128 m × 128 m)` et vérifier aux frontières de cellules : (1) Continuité des collisions et du NavMesh, (2) Absence de perte d'état de quête lors du déchargement/rechargement de `Data Layers`, (3) Transition fluide des splines `ZoneGraph`.
2. Exécuter sur chaque mission `GD-02` la **Matrice de Tests Destructifs Anti-Soft-Lock** : détruire volontairement `VEH-MOTO-WEWA-01`, fuir à `> 500 m` en plein dialogue, déclencher le combat pendant une phase d'infiltration sociale (`ITM-DOC-PASSEPORT`), changer la météo en `World.Weather.TropicalStorm`.
3. Normaliser tout ticket d'anomalie selon `templates/qa-test-plan-template.md` afin de garantir un taux de reproductibilité **`>= 90 %`**.
4. Remonter immédiatement tout bug `SEV-A` à `DIR-07` pour passage de l'entité au statut `BLOCKED`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Rapport de bug intermittent avec un taux de reproduction < 90 % | Exiger la capture automatique du Snapshot d'État (Coordonnées X/Y/Z cm, GlobalSeed, GameplayTags actifs, DataLayers chargés) avant validation du ticket | Atteindre le standard de reproductibilité >= 90 % (quality-standards.md) |
| Détection d'un cas où la destruction de la moto Wewa bloque la progression d'une quête sans alternative | Classer l'anomalie en SEV-A (Blocker), marquer la mission BLOCKED et assigner le correctif de machine à états à GD-02 | Appliquer la tolérance zéro sur les soft-locks |
| Scénario de test répétitif validé manuellement à chaque build (ex: traversée Gombe -> Matonge) | Transférer le cas de test à PRD-05 pour conversion en test de non-régression nocturne automatisé Gauntlet | Maximiser la couverture automatisée >= 80 % |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/open-world-qa-grid-methodology.md`
- **Modèle Officiel de Livrable** : `templates/qa-test-plan-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-qa-test-plan.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-qa-test-plan.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/qa-test-plan-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `PRD-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des étapes de la machine à états de mission (`GD-02`) sont couvertes par un cas de test nominal ET un cas de test destructif (interruption/fuite/perte véhicule).
- [ ] Taux de reproductibilité des rapports d'anomalies `>= 90 %`.
- [ ] Couverture spatiale de 100 % des cellules World Partition actives du jalon.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-07`, `PRD-05`.
