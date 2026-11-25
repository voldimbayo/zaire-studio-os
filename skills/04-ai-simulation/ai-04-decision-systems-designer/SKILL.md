---
name: ai-04-decision-systems-designer
description: "Conception des systèmes de décision de haut niveau (Utility AI), des routines quotidiennes des habitants de Kinshasa et du générateur d'événements systémiques émergents (micro-scènes de rue, pannes mécaniques, contrôles du Syndicat, musiciens de rue) réagissant à la réputation du joueur (SYS-WLD-REPUTATION), à l'heure et à la météo."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AI-04
  department: 04-ai-simulation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "world-bible-wld-01"
    - "reputation-system-gd-01"
    - "barks-catalog-nar-04"
  outputs:
    - "utility-ai-decision-matrix.csv"
    - "systemic-events-catalog.md"
  upstream_dependencies:
    - "WLD-01"
    - "GD-01"
    - "NAR-04"
---

# `AI-04` — Decision Systems Designer (`ai-04-decision-systems-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`04-ai-simulation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception des micro-événements non scriptés qui animent Kinshasa entre deux points d'intérêt (règle des 40 secondes `WLD-04`).
- Modélisation des courbes d'utilité (Utility AI) gouvernant le choix d'activité des citoyens selon le cycle jour/nuit, la pluie (`World.Weather.TropicalStorm`) et la réputation de Koffi.
- Rattachement des événements émergents aux banques de barks (`NAR-04`) et aux gains de réputation (`GD-04`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `world-bible-wld-01`, `reputation-system-gd-01`, `barks-catalog-nar-04`
- **Sorties produites** : `utility-ai-decision-matrix.csv`, `systemic-events-catalog.md`
- **Dépendances Amont Canoniques (DAG)** : `WLD-01`, `GD-01`, `NAR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas les arbres de recherche de chemin bas niveau (`AI-01`) ni les processeurs vectorisés C++ (`AI-02`).
- **Interdiction / Limite** : Interdit de déclencher un événement systémique à moins de `80 mètres` d'une mission principale active (`MSN-MAIN-*`) pour ne pas parasiter la mise en scène de `GD-02`/`NAR-02`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Calculer le score d'utilité $U \in [0.0, 1.0]$ de chaque événement candidat à partir de 4 variables normalisées : (1) Tag de Commune (`World.District.*`), (2) Heure du jour, (3) Météo (`World.Weather.*`), (4) Niveau de Réputation (`SYS-WLD-REPUTATION`).
2. Imposer un **Temps de Recharge (Cooldown)** de `15 minutes` réelles par catégorie de micro-événement pour éliminer toute sensation de répétition mécanique.
3. Limiter l'empreinte technique de chaque événement systémique à **`<= 4 acteurs AI-01` hydratés** maximum.
4. Documenter le catalogue et les formules de pondération dans `templates/systemic-events-catalog.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Mission principale MSN-MAIN-* en cours d'exécution à proximité (< 80 m) | Forcer le multiplicateur d'utilité des événements systémiques aléatoires à 0.0 dans un rayon de 80 m autour de l'objectif de quête | Éviter toute interférence avec le script de mission GD-02 |
| Même événement systémique tiré deux fois dans le même quartier en moins de 15 minutes | Appliquer une pénalité de fraîcheur (Decay Factor = 0.05) sur le score d'utilité de cet événement | Garantir la variété de l'exploration open world |
| Réputation de Koffi au palier 'Enfant du Quartier' (>= 600 points) dans la commune | Activer les événements d'entraide citoyenne (avertissement de patrouille, diversion spontanée de foule, prêt de Wewa) | Récompenser concrètement l'investissement social du joueur |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/utility-ai-and-systemic-world.md`
- **Modèle Officiel de Livrable** : `templates/systemic-events-catalog.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-systemic-events.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-systemic-events.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/systemic-events-catalog.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AI-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque événement du catalogue spécifie sa formule de score Utility AI, son cooldown, ses tags requis et son plafond d'acteurs (`<= 4`).
- [ ] Exclusion mutuelle garantie avec les arènes de missions principales actives.
- [ ] Tous les dialogues courts de l'événement proviennent des tables de barks validées par `NAR-04`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `NAR-06`, `WLD-04`.
