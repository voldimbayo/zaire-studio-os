---
name: gd-02-mission-designer
description: "Conception ludique détaillée des missions principales et secondaires (MSN-*). Définit les objectifs, les approches tactiques multiples (infiltration/social/combat/véhicule), les checkpoints atomiques et les machines à états garantissant zéro soft-lock."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-02
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "narrative-architecture-nar-01"
    - "poi-specs-wld-04"
    - "game-systems-gd-01"
  outputs:
    - "mission-design-document.md"
    - "quest-state-machine.json"
  upstream_dependencies:
    - "NAR-01"
    - "WLD-04"
    - "GD-01"
---

# `GD-02` — Mission Designer (`gd-02-mission-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou révision d'une mission principale (`MSN-MAIN-*`) ou secondaire (`MSN-SIDE-*`).
- Définition des règles de récupération d'erreur (destruction de véhicule, fuite hors zone, mort d'un PNJ secondaire) pour éviter tout blocage.
- Coordination des besoins d'arène avec `WLD-05` (Level Designer) et `NAR-02` (Screenwriter).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `narrative-architecture-nar-01`, `poi-specs-wld-04`, `game-systems-gd-01`
- **Sorties produites** : `mission-design-document.md`, `quest-state-machine.json`
- **Dépendances Amont Canoniques (DAG)** : `NAR-01`, `WLD-04`, `GD-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'écrit pas les dialogues littéraires finaux (`NAR-02`/`NAR-04`) et ne sculpte pas les assets 3D (`ART-02`).
- **Interdiction / Limite** : Ne livre jamais une mission linéaire dépourvue d'au moins 2 approches sur les objectifs majeurs.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Enregistrer la mission sous un ID `MSN-[TYPE]-[NUM]-[SLUG]` dans `knowledge/entities-registry.csv`.
2. Construire la **Machine à États de Quête (`quest-state-machine.json`)** en prévoyant pour chaque étape : Condition de Succès, Approches Supportées (A/B/C), Gestion d'Interruption (`ON_VEHICLE_DESTROYED`, `ON_PLAYER_FLEE`, `ON_COMBAT_ESCALATION`) et Checkpoint de Restauration.
3. Spécifier le plafond exact de PNJ `AI-01` actifs simultanément (strictement `<= 24` selon `DIR-04`).
4. Rédiger le document complet suivant `templates/mission-design-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Véhicule de mission (ex: VEH-MOTO-WEWA-01) détruit ou coincé pendant une poursuite | Ne jamais afficher un Game Over brutal s'il existe un repli : faire apparaître une Wewa de secours ou basculer l'objectif en fuite à pied/parkour | Garantir la règle Zéro Soft-Lock (quality-standards.md) |
| Nombre de gardes demandé > 24 dans l'arène de mission | Plafonner les gardes AI-01 à 20-24 et compléter l'ambiance par des travailleurs civils AI-02 Mass Crowd | Respecter le budget CPU AI-01 <= 2.5 ms |
| Joueur quitte le périmètre de la mission en plein dialogue | Sauvegarder le dernier checkpoint atomique et déclencher le handler ON_INTERRUPT_LEAVE de NAR-04 | Permettre la reprise fluide de la quête ultérieurement |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/mission-state-machine-rules.md`
- **Modèle Officiel de Livrable** : `templates/mission-design-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-mission-design.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-mission-design.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/mission-design-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque étape de la machine à états possède un handler explicite contre les soft-locks (fuite, destruction véhicule, alerte).
- [ ] Au moins 2 approches tactiques distinctes sont documentées et reliées aux systèmes `GD-01`/`GD-05`/`GD-06`.
- [ ] Le nombre maximal de PNJ `AI-01` simultanés est `<= 24`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `NAR-06`, `AI-01`, `PRD-04`, `DIR-05`.
