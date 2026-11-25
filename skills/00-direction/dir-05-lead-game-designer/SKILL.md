---
name: dir-05-lead-game-designer
description: "Direction du Game Design de ZAÏRE. Garantit la cohérence systémique entre les boucles de gameplay (Core Loops), le combat, la conduite des véhicules kinois, l'économie, la progression, les missions et le respect des métriques spatiales."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: DIR-05
  department: 00-direction
  stratum: 0
  version: "1.1.0"
  inputs:
    - "game-design-specs-gd-01-to-07"
    - "level-blockouts-wld-05"
    - "knowledge/technical-specs/spatial-metrics.md"
  outputs:
    - "gameplay-coherence-review.md"
    - "systemic-balance-directive.md"
  upstream_dependencies:
    - "DIR-01"
    - "DIR-03"
---

# `DIR-05` — Lead Game Designer (`dir-05-lead-game-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`00-direction`** (Strate DAG **0**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Validation de tout nouveau système de jeu (`SYS-*`), mission (`MSN-*`), véhicule (`VEH-*`) ou archétype de combat.
- Arbitrage d'équilibrage entre économie (`GD-03`), progression (`GD-04`) et difficulté de combat (`GD-05`).
- Validation du playtest d'un blockout Level Design (`WLD-05`) avant autorisation du passage à l'Environment Art (`WLD-06`/`ART-02`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `game-design-specs-gd-01-to-07`, `level-blockouts-wld-05`, `knowledge/technical-specs/spatial-metrics.md`
- **Sorties produites** : `gameplay-coherence-review.md`, `systemic-balance-directive.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-01`, `DIR-03`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'écrit pas le code C++ des GameplayAbilities (`ENG-02`).
- **Interdiction / Limite** : N'autorise jamais la mise en production artistique d'un niveau dont le blockout (`WLD-05`) viole `spatial-metrics.md`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Vérifier l'intégration du système ou de la mission dans les Core Loops de ZAÏRE (Observer -> S'infiltrer/Négocier/Combattre -> Traverser Kinshasa -> Réinvestir dans le réseau local).
2. Contrôler l'interopérabilité via la taxonomie officielle `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.
3. Auditer la conformité aux métriques spatiales (`knowledge/technical-specs/spatial-metrics.md` : couloirs `>= 350 cm`, couverts `100 cm`/`200 cm`, voies routières `350-400 cm`).
4. Émettre la directive de validation ou de rééquilibrage dans `templates/gameplay-coherence-review.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Blockout WLD-05 comportant un couloir jouable < 350 cm ou une impasse non intentionnelle | Rejeter le handoff vers WLD-06/ART-02 et exiger une reprise géométrique du blockout | Appliquer strictement la règle Blockout First |
| Mission GD-02 n'offrant qu'une seule approche linéaire ou vulnérable au soft-lock | Exiger au moins 2 approches distinctes (ex: infiltration sociale ITM-DOC-PASSEPORT + parcours parkour/mêlée) et une gestion de fuite | Bloquer le passage en CONFIRMED |
| Mécanique introduisant un tag absent de gameplay-tags-taxonomy.csv | Valider la pertinence systémique du tag et ordonner son ajout normalisé dans la taxonomie | Interdire les variables booléennes ad-hoc non composables |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/core-loops-and-metrics.md`
- **Modèle Officiel de Livrable** : `templates/gameplay-coherence-review.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-gameplay-review.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-gameplay-review.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/gameplay-coherence-review.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `DIR-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des interactions inter-systèmes passent par des `FGameplayTag` répertoriés.
- [ ] 100 % des espaces de mission respectent les gabarits de caméra, de couvert et de circulation véhicule.
- [ ] L'équilibrage numérique évite à la fois l'inflation monétaire (`GD-03`) et la trivialisation du combat (`GD-05`).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-03`, `DIR-07`.
