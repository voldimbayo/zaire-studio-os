---
name: ai-02-crowd-simulation-specialist
description: "Simulation de foules urbaines denses (marchés de Kinshasa, Rond-Point Victoire, boulevards) sous UE5 Mass Entity / Mass Crowd et ZoneGraph. Gère 500 à 800+ citoyens simultanés dans un budget CPU <= 2.0 ms avec évitement RVO et hydratation dynamique sans hitch en acteurs complets."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AI-02
  department: 04-ai-simulation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "open-world-density-wld-04"
    - "modular-npc-kits-art-03"
    - "cpu-budgets-dir-04"
  outputs:
    - "mass-crowd-architecture.md"
    - "district-crowd-density.csv"
  upstream_dependencies:
    - "WLD-04"
    - "ART-03"
    - "DIR-04"
---

# `AI-02` — Crowd Simulation Specialist (`ai-02-crowd-simulation-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`04-ai-simulation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Configuration de la densité piétonne d'une commune (`DST-MATONGE`, `DST-GOMBE`, `DST-KALAMU`, `DST-LIMETE`) selon l'heure et la météo.
- Conception des Fragments et Processors ECS (`UMassProcessor`) et des règles d'hydratation (`MassRepresentation` -> `ACharacter` `AI-01`).
- Vérification du budget CPU `PERF-CPU-MASS` (`<= 2.0 ms` à 60 FPS) via `scripts/check_mass_budget.py`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `open-world-density-wld-04`, `modular-npc-kits-art-03`, `cpu-budgets-dir-04`
- **Sorties produites** : `mass-crowd-architecture.md`, `district-crowd-density.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-04`, `ART-03`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne sculpte pas les vêtements modulaires 3D des passants (`ART-03`) et ne gère pas la logique de combat individuel (`AI-01`).
- **Interdiction / Limite** : Interdit toute instanciation de `UCharacterMovementComponent` sur les entités Mass de niveau LOD 1 et LOD 2 (usage exclusif de `ZoneGraph` + Vertex Animation Textures).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Définir l'archétype ECS `MassCrowd` avec ses Fragments minimaux (`FTransformFragment`, `FMassZoneGraphLaneLocationFragment`, `FMassLookAtFragment`, `FZaireDistrictCultureFragment`).
2. Configurer les **3 Anneaux de Représentation LOD** : Anneau 0 (`0 - 25 m` : jusqu'à 18 acteurs hydratés interactifs), Anneau 1 (`25 - 80 m` : Skeletal Mesh simplifié avec URO), Anneau 2 (`80 - 250 m` : Instanced Static Mesh animé par VAT).
3. Programmer la réaction collective aux événements systémiques (`World.Weather.TropicalStorm` -> repli sous les auvents de `DST-MATONGE` ; combat ou coup de feu -> onde de panique directionnelle).
4. Valider l'enveloppe CPU en exécutant `scripts/check_mass_budget.py`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Budget CPU Mass estimé > 2.0 ms par check_mass_budget.py | Réduire le rayon d'hydratation de l'Anneau 0 de 25m à 18m et basculer 30 % des entités LOD1 vers la représentation VAT Instanced Static Mesh (LOD2) | Maintenir le frametime global sous 16.6 ms |
| Averse équatoriale déclenchée (World.Weather.TropicalStorm) | Basculer la vitesse de déplacement des piétons sur ZoneGraph à 1.6x vers les tags d'abris (auvents de 180 cm de WLD-03) et réduire la densité de spawn en plein air de 60 % | Simuler un comportement urbain kinois crédible |
| Collision entre une moto Wewa du joueur et un piéton Mass LOD1 | Hydrater instantanément l'entité touchée en acteur physique Chaos ragdoll/esquive et déclencher le bark BRK-CROWD-01 | Assurer une continuité physique sans pop visuel |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/ue5-mass-crowd-ecs.md`
- **Modèle Officiel de Livrable** : `templates/mass-crowd-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-mass-crowd-spec.md`
- `scripts/check_mass_budget.py` : Script exécutable déterministe associé à `AI-02` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-mass-crowd-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/mass-crowd-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AI-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/04-ai-simulation/ai-02-crowd-simulation-specialist/scripts/check_mass_budget.py` retourne un code `0` (`within_budget: true`).
- [ ] 500+ entités sont simulées simultanément à `DST-MATONGE` pour un coût CPU `<= 2.0 ms`.
- [ ] L'hydratation/déshydratation entre `MassEntity` et `ACharacter` utilise un pool pré-alloué garantissant 0 hitch d'allocation mémoire.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-07`, `PRD-05`, `DIR-04`.
