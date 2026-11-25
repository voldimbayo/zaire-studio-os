---
name: prd-05-test-engineer
description: "Ingénierie des tests automatisés sous Unreal Engine 5 : Unreal Gauntlet Automation Framework, AFunctionalTest Actors et bots d'exploration autonome de Kinshasa. Garantit une couverture >= 80 % des systèmes critiques (SYS-*) et un taux de faux positifs < 2 % grâce à une synchronisation 100 % événementielle (zéro sleep arbitraire)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: PRD-05
  department: 08-production-quality
  stratum: 5
  version: "1.1.0"
  inputs:
    - "qa-test-plans-prd-04"
    - "performance-budgets-eng-07"
    - "ci-cd-pipelines-eng-08"
  outputs:
    - "gauntlet-automation-spec.md"
    - "automated-test-suite-summary.csv"
  upstream_dependencies:
    - "PRD-04"
    - "ENG-07"
    - "ENG-08"
---

# `PRD-05` — Test Engineer (`prd-05-test-engineer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`08-production-quality`** (Strate DAG **5**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Implémentation en C++ / Python UE5 des cas de test prioritaires identifiés par `PRD-04`.
- Création des bots de traversée nocturne (*Soak & Traversal Bots*) mesurant le frametime P99 (`ENG-07`), la mémoire VRAM et l'absence de deadlock trafic (`AI-03`) sur 2 heures.
- Intégration de la suite de tests dans le pipeline BuildGraph / Horde de `ENG-08`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `qa-test-plans-prd-04`, `performance-budgets-eng-07`, `ci-cd-pipelines-eng-08`
- **Sorties produites** : `gauntlet-automation-spec.md`, `automated-test-suite-summary.csv`
- **Dépendances Amont Canoniques (DAG)** : `PRD-04`, `ENG-07`, `ENG-08`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne remplace pas l'évaluation qualitative humaine du Game Feel (`DIR-05`) ou de l'authenticité culturelle (`WLD-02`).
- **Interdiction / Limite** : Interdit formellement l'utilisation de délais fixes (`FPlatformProcess::Sleep` ou `Delay(5.0f)`) pour attendre la fin d'un chargement ou d'une animation dans un test automatisé.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Écrire les tests unitaires et fonctionnels sous `IMPLEMENT_SIMPLE_AUTOMATION_TEST` et `AFunctionalTest` en synchronisant chaque étape sur des **Delegates événementiels explicites** (`OnStreamingCompleted`, `OnGameplayTagChanged`, `OnAbilityEnded`, `OnQuestStateReached`).
2. Configurer le contrôleur **`UZaireGauntletTraversalController`** pour faire parcourir à un bot une boucle de `2 heures` à travers `DST-GOMBE`, `DST-KALAMU`, `DST-MATONGE` et `DST-LIMETE` tout en enregistrant un rapport `CSVProfiler` pour `ENG-07`.
3. Maintenir la couverture automatisée des systèmes critiques (`SYS-WLD-STREAMING`, `SYS-CMB-MELEE`, `SYS-STEALTH`, `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS`) à **`>= 80 %`**.
4. Documenter l'architecture de la suite dans `templates/gauntlet-test-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Test automatisé échouant de manière aléatoire (Flaky Test > 2 % de faux positifs) sur la ferme CI | Remplacer immédiatement toute attente temporelle fixe par un abonnement au delegate d'achèvement du sous-système (ex: UWorldPartitionSubsystem::OnStreamingStateUpdated) | Ramener le taux de faux positifs sous la barre des 2 % |
| Couverture automatisée d'un nouveau système SYS-* inférieure à 80 % | Refuser le passage du système au jalon Beta/Gold et ajouter les AFunctionalTest manquants dans la map de test dédiée | Respecter le seuil obligatoire >= 80 % (quality-standards.md) |
| Bot Gauntlet détectant une hausse de consommation RAM/VRAM monotone (+50 MB/heure) pendant le test d'endurance de 2h | Émettre une alerte automatique de fuite mémoire (Memory Leak) vers ENG-01 et ENG-07 avec le diff d'allocations Unreal Insights | Bloquer le build nocturne |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/unreal-gauntlet-event-driven-tests.md`
- **Modèle Officiel de Livrable** : `templates/gauntlet-test-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-gauntlet-test-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-gauntlet-test-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/gauntlet-test-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `PRD-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Couverture des systèmes critiques `SYS-*` par tests automatisés `>= 80 %`.
- [ ] Taux de faux positifs (flakiness) `< 2 %` sur 50 exécutions CI consécutives (0 `Sleep` fixe).
- [ ] Exécution automatique intégrée à l'étape 4 du BuildGraph `ENG-08`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `PRD-04`, `ENG-08`, `DIR-07`.
