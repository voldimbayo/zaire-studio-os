---
name: ai-03-traffic-ai-specialist
description: "Simulation du trafic routier et fluvial de Kinshasa (SYS-TRAFFIC-ZONE) sous UE5 ZoneGraph et Mass Traffic. Gère les priorités aux grands ronds-points (Rond-Point Victoire, Échangeur), le slalom inter-file des motos Wewa (VEH-MOTO-WEWA-01), les arrêts des taxis jaunes et l'algorithme anti-deadlock."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AI-03
  department: 04-ai-simulation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "urban-road-specs-wld-03"
    - "vehicle-profiles-gd-06"
    - "houdini-zonegraph-splines-eng-04"
  outputs:
    - "traffic-rules-specification.md"
    - "intersection-priority-matrix.csv"
  upstream_dependencies:
    - "ENG-04"
    - "GD-06"
    - "WLD-03"
    - "DIR-04"
---

# `AI-03` — Traffic AI Specialist (`ai-03-traffic-ai-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`04-ai-simulation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Configuration des règles de circulation `MassTraffic` sur les voies `ZoneGraph` générées par Houdini (`ENG-04`).
- Modélisation des comportements typiques du trafic kinois (slalom des motos Wewa dans les espaces `>= 130 cm`, arrêts opportuns des taxis `VEH-TAXI-JAUNE-01`, inertie des bus `VEH-BUS-TRANSCO-01`).
- Prévention et résolution automatique des embouteillages bloquants (deadlocks) aux intersections complexes.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `urban-road-specs-wld-03`, `vehicle-profiles-gd-06`, `houdini-zonegraph-splines-eng-04`
- **Sorties produites** : `traffic-rules-specification.md`, `intersection-priority-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `ENG-04`, `GD-06`, `WLD-03`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne règle pas les courbes de couple ou de suspension du véhicule contrôlé par le joueur (`GD-06`/`ENG-05`).
- **Interdiction / Limite** : N'active jamais la simulation physique complète Chaos sur les véhicules IA situés à plus de `45 mètres` du joueur (suivi cinématique léger sur spline `ZoneGraph`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Tagger chaque voie `ZoneGraph` avec ses types de véhicules autorisés (`Vehicle.Type.MotoWewa`, `Vehicle.Type.HeavyBus`, `StandardCar`) et sa vitesse cible en fonction de `WLD-03`.
2. Implémenter la règle de **Sub-Lane Splitting (Slalom Wewa)** : lorsqu'une file de voitures roule à `< 20 km/h` et que l'écart inter-file est `>= 130 cm`, autoriser les entités `VEH-MOTO-WEWA-01` à emprunter la sous-voie virtuelle inter-file à `30-40 km/h`.
3. Configurer le **Watchdog Anti-Deadlock aux Carrefours** : si une intersection a une vitesse moyenne `< 2 km/h` pendant plus de `8 secondes`, forcer la libération prioritaire de l'anneau intérieur du rond-point etrecycler hors-champ (`> 120 m` hors frustum caméra) les véhicules bloquants.
4. Documenter les règles dans `templates/traffic-rules-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Collision ou proximité immédiate (< 15 m) entre le joueur et un véhicule MassTraffic | Promouvoir instantanément l'entité MassTraffic de sa spline cinématique vers un acteur Chaos Vehicle physique complet (ENG-05) | Garantir des réactions de choc et d'évitement réalistes |
| Saturation d'un rond-point (ex: LOC-MATONGE-VICTOIRE) menaçant de bloquer une mission de course Wewa | Déclencher le protocole Anti-Deadlock après 8s d'immobilisation et maintenir en permanence un couloir inter-file de 150 cm franchissable à moto | Éviter tout soft-lock routier sur MSN-SIDE-014-WEWA |
| Dépassement du budget CPU combiné Mass Crowd + Mass Traffic (> 2.0 ms) | Réduire le plafond de véhicules simulés de 120 à 85 en privilégiant la densité dans le cône de vision avant du joueur | Respecter PERF-CPU-MASS |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/zonegraph-kinshasa-traffic.md`
- **Modèle Officiel de Livrable** : `templates/traffic-rules-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-traffic-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-traffic-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/traffic-rules-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AI-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le trafic soutient un test d'endurance de 2 heures (`PRD-05`) sur `LOC-MATONGE-VICTOIRE` et `LOC-GOMBE-BD30JUIN` avec 0 deadlock permanent.
- [ ] Les motos IA `VEH-MOTO-WEWA-01` utilisent les couloirs inter-files `>= 130 cm` sans collision fantôme.
- [ ] Aucune apparition ou disparition (pop-in/out) de véhicule n'est visible dans le frustum caméra du joueur.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `PRD-05`, `ENG-07`, `GD-06`.
