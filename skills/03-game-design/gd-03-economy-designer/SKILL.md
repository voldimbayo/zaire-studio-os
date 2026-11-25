---
name: gd-03-economy-designer
description: "Modélisation mathématique et équilibrage de l'économie virtuelle de ZAÏRE (Sources & Puits / Faucets & Sinks). Définit les récompenses de missions, le coût des équipements (ITM-*), la maintenance des véhicules (VEH-*) et prévient l'hyper-inflation sur 40+ heures de jeu."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-03
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "game-systems-gd-01"
    - "missions-list-gd-02"
    - "items-and-vehicles-registry"
  outputs:
    - "economy-balance-sheet.csv"
    - "faucets-sinks-simulation.json"
  upstream_dependencies:
    - "GD-01"
    - "GD-02"
    - "DIR-02"
---

# `GD-03` — Economy Designer (`gd-03-economy-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou tarification d'un nouvel objet (`ITM-*`), véhicule (`VEH-*`) ou service urbain (atelier mécanique, informateur, transport).
- Calibrage des récompenses monétaires (`LEX-010 Mosolo`) des missions principales et secondaires (`MSN-*`).
- Vérification de la stabilité économique long-terme via `scripts/simulate_economy.py`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `game-systems-gd-01`, `missions-list-gd-02`, `items-and-vehicles-registry`
- **Sorties produites** : `economy-balance-sheet.csv`, `faucets-sinks-simulation.json`
- **Dépendances Amont Canoniques (DAG)** : `GD-01`, `GD-02`, `DIR-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne conçoit pas les paliers de points d'expérience ou de compétences (`GD-04`) ni les écrans UI de boutique (`GD-07`).
- **Interdiction / Limite** : N'autorise aucune source de revenu infinie non plafonnée (exploit farming) sans temps de recharge ou coût d'opportunité.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Inventorier toutes les Sources de revenus (**Faucets** : missions `MSN-*`, livraisons Wewa, revente de cargaisons `LEX-012 Bilɔkɔ`) et tous les Puits de dépense (**Sinks** : réparation/customisation `VEH-MOTO-WEWA-01`, équipement `ITM-*`, frais d'informateurs, soutien au réseau citoyen).
2. Lier les multiplicateurs de prix des commerçants de chaque commune (`DST-*`) au niveau de `SYS-WLD-REPUTATION` (`-15 %` en réputation alliée, `+25 %` en zone tendue).
3. Exécuter `scripts/simulate_economy.py` pour vérifier que le ratio moyen `Sink / Faucet` reste compris entre **`0.75` et `0.92`** sur 40 heures de jeu.
4. Exporter la table de prix normalisée dans `templates/economy-balance-sheet.csv`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Ratio Sink / Faucet < 0.75 détecté par simulate_economy.py (excès de liquidités / inflation) | Augmenter le coût des améliorations de palier 2/3 à l'atelier mécanique ou introduire des puits de prestige (tenues Sapeurs, améliorations radio) | Maintenir la valeur perçue du Mosolo jusqu'à l'Acte III |
| Ratio Sink / Faucet > 0.92 ou solde négatif sur le chemin critique | Réduire de 30 % les coûts de réparation obligatoire des véhicules et augmenter la prime des missions principales MSN-MAIN-* | Garantir zéro blocage financier sur la quête principale |
| Activité secondaire répétable générant plus de revenus/minute qu'une mission principale | Appliquer un rendement décroissant (diminishing returns) après 3 exécutions dans la même journée in-game | Protéger le rythme de progression GD-04 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/faucets-and-sinks-math.md`
- **Modèle Officiel de Livrable** : `templates/economy-balance-sheet.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-economy-model.md`
- `scripts/simulate_economy.py` : Script exécutable déterministe associé à `GD-03` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-economy-model.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/economy-balance-sheet.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/03-game-design/gd-03-economy-designer/scripts/simulate_economy.py` retourne un code `0` (`economy_healthy: true`).
- [ ] Aucun achat obligatoire de la quête principale ne bloque la progression du joueur.
- [ ] 100 % des items tarifés utilisent des identifiants `ITM-*` ou `VEH-*` valides.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `GD-04`.
