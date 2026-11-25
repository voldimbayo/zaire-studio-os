---
name: eng-08-build-engineer
description: "Ingénierie Build, CI/CD et Sécurité de ZAÏRE STUDIO OS : pipelines Unreal Automation Tool (UAT), BuildGraph, Epic Horde, cache dérivé partagé Zen Server DDC, compilation incrémentale (<= 15 minutes), collecte automatisée des caches PSO et packaging .pak/.utoc signé et chiffré en AES-256 sans secrets codés en dur."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-08
  department: 07-engineering
  stratum: 4
  version: "1.1.0"
  inputs:
    - "cpp-codebase-eng-01-to-06"
    - "perf-pso-specs-eng-07"
    - "gauntlet-test-suites-prd-05"
  outputs:
    - "ci-cd-buildgraph-spec.xml"
    - "pak-security-and-ddc-protocol.md"
  upstream_dependencies:
    - "ENG-01"
    - "ENG-02"
    - "ENG-03"
    - "ENG-07"
---

# `ENG-08` — Build Engineer (`eng-08-build-engineer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **4**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Configuration ou maintenance du pipeline CI/CD BuildGraph / Horde pour les builds incrémentaux et nocturnes.
- Optimisation du temps de cooking et de compilation via Zen Server Derived Data Cache (DDC) partagé (`PERF-CI-BUILD <= 15 minutes`).
- Configuration de la signature cryptographique RSA et du chiffrement AES-256 des archives IoStore (`.pak`/`.utoc`/`.ucas`) via variables d'environnement sécurisées.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `cpp-codebase-eng-01-to-06`, `perf-pso-specs-eng-07`, `gauntlet-test-suites-prd-05`
- **Sorties produites** : `ci-cd-buildgraph-spec.xml`, `pak-security-and-ddc-protocol.md`
- **Dépendances Amont Canoniques (DAG)** : `ENG-01`, `ENG-02`, `ENG-03`, `ENG-07`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie jamais le code logique de gameplay (`ENG-02`).
- **Interdiction / Limite** : Interdit formellement le stockage de clés de chiffrement AES, certificats de signature ou jetons d'API en clair dans le dépôt Git/Perforce (injection exclusive par coffre-fort CI / variables d'environnement).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer le pipeline **UE5 BuildGraph** en 5 noeuds parallélisés sous Epic Horde : (1) `Compile_ZaireEditor_And_Game`, (2) `Run_EditorValidators_ENG03`, (3) `Cook_And_Package_IoStore`, (4) `Collect_PSO_And_Run_Gauntlet_PRD05`, (5) `Sign_And_Publish_Build`.
2. Maintenir un **Zen Server Shared DDC** chaud sur le réseau de build afin de garantir un temps de build incrémental **`<= 15.0 minutes`** (`PERF-CI-BUILD`).
3. Injecter la clé de chiffrement AES-256 des tables d'index IoStore (`.utoc`) au moment du packaging via `-EncryptionKeyOverrideEnvVar=ZAIRE_PAK_AES256_KEY` (ne chiffrer que l'index `.utoc` et les assets sensibles pour limiter l'overhead CPU de décompression à `< 0.5 %`).
4. Déclencher automatiquement la suite de tests Gauntlet (`PRD-05`) et l'audit de budget (`ENG-07`) sur chaque build nocturne.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Temps de build incrémental dépassant 15 minutes sur la ferme CI | Auditer les inclusions d'en-têtes C++ via Include-What-You-Use (IWYU), activer UnrealBuildAccelerator (UBA) et vérifier le taux de Cache Hit du Zen Server DDC (>= 95 %) | Ramener PERF-CI-BUILD sous le seuil de 15.0 minutes |
| Clé ou secret détecté en dur dans un fichier .ini ou script de build | Faire échouer immédiatement le pipeline CI (Secret Scanner Fail), révoquer la clé exposée et remplacer par une lecture de variable d'environnement du coffre-fort CI | Respecter la politique Zéro Secret Codé en Dur |
| Échec d'un validateur ENG-03 ou d'un test critique Gauntlet PRD-05 pendant le build | Stopper la promotion du build vers la branche QA/Stable et notifier automatiquement le skill propriétaire de la régression | Maintenir la branche principale 100 % verte |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/buildgraph-horde-and-security.md`
- **Modèle Officiel de Livrable** : `templates/ci-cd-buildgraph-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-buildgraph-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-buildgraph-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/ci-cd-buildgraph-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-08` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Temps de build et cooking incrémental `<= 15.0 minutes` (`PERF-CI-BUILD`).
- [ ] 0 secret ou clé de chiffrement stocké en clair dans les fichiers du dépôt.
- [ ] Déclenchement automatique des validateurs `ENG-03`, des tests Gauntlet `PRD-05` et de la fusion du cache PSO `ENG-07`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-04`, `PRD-05`, `ENG-07`.
