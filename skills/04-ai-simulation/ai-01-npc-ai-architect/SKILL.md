---
name: ai-01-npc-ai-architect
description: "Architecture des comportements individuels des PNJ (gardes ORG-CARTEL-FLEUVE, alliés, cibles prioritaires) sous UE5 State Trees, Environment Query System (EQS), AI Perception et Smart Objects dans un budget CPU strict <= 2.5 ms (max 24 acteurs actifs)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AI-01
  department: 04-ai-simulation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "combat-archetypes-gd-05"
    - "level-blockouts-wld-05"
    - "cpu-budgets-dir-04"
  outputs:
    - "npc-ai-architecture.md"
    - "eqs-and-statetree-spec.md"
  upstream_dependencies:
    - "GD-05"
    - "WLD-05"
    - "DIR-04"
---

# `AI-01` — NPC AI Architect (`ai-01-npc-ai-architect`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`04-ai-simulation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception des boucles de patrouille, d'investigation furtive (`SYS-STEALTH`) et de combat tactique (`SYS-CMB-MELEE`) des PNJ individuels.
- Paramétrage des requêtes spatiales EQS (recherche de couvert `100 cm`/`200 cm`, flanquement dans les hangars de `LOC-GOMBE-PORT`) et du gestionnaire d'Attack Tokens.
- Optimisation du budget CPU `PERF-CPU-NPCAI` (`<= 2.5 ms` en mode 60 FPS).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `combat-archetypes-gd-05`, `level-blockouts-wld-05`, `cpu-budgets-dir-04`
- **Sorties produites** : `npc-ai-architecture.md`, `eqs-and-statetree-spec.md`
- **Dépendances Amont Canoniques (DAG)** : `GD-05`, `WLD-05`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne gère jamais les foules de centaines de citoyens passifs (`AI-02` Mass Crowd) ni le flux routier (`AI-03` Mass Traffic).
- **Interdiction / Limite** : Interdit de dépasser **24 acteurs `AI-01` actifs simultanément** dans la bulle de simulation du joueur.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer la logique décisionnelle du PNJ sous **UE5 State Trees** en 4 états racines : `Idle/SmartObject`, `Patrol/Suspicion`, `Combat/Tactical` et `Search/De-escalation`.
2. Configurer `UAIPerceptionComponent` (Sight + Hearing) pour réagir dynamiquement aux Gameplay Tags du joueur (`State.Character.Stealth.Concealed`, `State.Character.Stealth.Disguised`, `World.Weather.TropicalStorm`).
3. Appliquer un **Time-Slicing strict sur les requêtes EQS** (maximum 2 évaluations EQS complètes par frame sur l'ensemble de l'escouade, rafraîchissement de couvert toutes les `0.4 s`).
4. Relier l'exécution des attaques au gestionnaire d'**Attack Tokens (`GD-05`)** et aux déclencheurs de barks (`NAR-04`).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Mission demandant plus de 24 PNJ actifs dans la même zone | Conserver au maximum 24 acteurs AI-01 et transférer tous les figurants/travailleurs vers AI-02 Mass Crowd avec hydratation à la demande | Respecter le plafond absolu PERF-CPU-NPCAI <= 2.5 ms |
| Requête EQS provoquant un pic > 0.5 ms sur le Game Thread | Réduire la densité de la grille de points EQS (espacement 150 cm au lieu de 50 cm) et activer le tri préalable par distance avant les raycasts de visibilité | Garantir la fluidité 60 FPS |
| PNJ bloqué devant un obstacle dynamique ou un véhicule garé de travers | Activer un NavModifier dynamique autour des véhicules à l'arrêt et un fallback de contournement Smart Link (escalade couvert 100 cm) | Éliminer tout blocage NavMesh |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/statetree-and-eqs-optimization.md`
- **Modèle Officiel de Livrable** : `templates/npc-ai-architecture.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-npc-ai-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-npc-ai-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/npc-ai-architecture.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AI-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le coût CPU cumulé des 24 acteurs `AI-01` est `<= 2.5 ms` (60 FPS) / `<= 3.0 ms` (30 FPS).
- [ ] Le système d'Attack Tokens empêche formellement plus de 2 assauts de mêlée simultanés.
- [ ] Les seuils de détection visuelle et auditive s'adaptent aux Gameplay Tags de météo et de déguisement.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-07`, `GD-05`, `WLD-05`.
