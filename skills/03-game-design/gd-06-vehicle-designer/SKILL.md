---
name: gd-06-vehicle-designer
description: "Conception ludique et tuning de conduite des véhicules de Kinshasa (VEH-MOTO-WEWA-01, VEH-TAXI-JAUNE-01, VEH-BUS-TRANSCO-01) sous UE5 Chaos Vehicles. Calibre les courbes de couple, la maniabilité simcade, la stabilisation deux-roues et l'adhérence par surface (asphalte, latérite sèche, boue d'averse équatoriale)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-06
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "urban-typology-wld-03"
    - "game-systems-gd-01"
    - "lead-gd-directives-dir-05"
  outputs:
    - "vehicle-handling-spec.md"
    - "surface-friction-matrix.csv"
  upstream_dependencies:
    - "WLD-03"
    - "GD-01"
    - "DIR-05"
---

# `GD-06` — Vehicle Designer (`gd-06-vehicle-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou réglage d'un véhicule jouable ou IA (`VEH-*`).
- Équilibrage de l'impact de la météo (`World.Weather.TropicalStorm`) et de la nature des sols kinois (béton portuaire, asphalte du Boulevard du 30 Juin, latérite de Kalamu) sur le freinage et la dérive.
- Paramétrage du comportement d'inter-file (slalom trafic `130 cm`) de la moto `VEH-MOTO-WEWA-01`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `urban-typology-wld-03`, `game-systems-gd-01`, `lead-gd-directives-dir-05`
- **Sorties produites** : `vehicle-handling-spec.md`, `surface-friction-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-03`, `GD-01`, `DIR-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modélise pas le maillage 3D ni le rig squelettique du véhicule (`ART-02`/`ART-08`).
- **Interdiction / Limite** : Ne programme pas le solveur bas niveau C++ Chaos (`ENG-05`), mais fournit les valeurs cibles exactes de suspension, masse, centre de gravité et friction.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Enregistrer le véhicule sous un identifiant `VEH-[CAT]-[SLUG]` dans `knowledge/entities-registry.csv` et lui associer son Gameplay Tag (`Vehicle.Type.*`).
2. Vérifier la compatibilité du gabarit géométrique du véhicule avec `knowledge/technical-specs/spatial-metrics.md` (ex: largeur `80 cm` pour `VEH-MOTO-WEWA-01` dans un couloir inter-file de `130 cm`).
3. Définir la matrice des multiplicateurs d'adhérence (`Friction Scale`) sur les 4 surfaces de Kinshasa : Asphalte Sec, Asphalte Mouillé, Latérite Compactée, Boue Tropicale.
4. Rédiger la fiche technique dans `templates/vehicle-handling-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Moto VEH-MOTO-WEWA-01 chutant trop facilement lors des contacts légers à basse vitesse dans le trafic dense | Activer un couple gyroscopique d'auto-stabilisation assistée sous 35 km/h et relever le seuil d'éjection ragdoll Chaos à un impact frontal > 55 km/h | Privilégier le plaisir de slalom urbain simcade sur la frustration punitive |
| Transition de surface par temps de pluie (World.Weather.TropicalStorm) rendant la moto incontrôlable | Plafonner la perte d'adhérence latérale à -25 % sur asphalte mouillé et -35 % sur boue latéritique avec retour haptique progressif | Synchroniser avec ENG-05 et AUD-02 (RTPC crissement/éclaboussure) |
| Véhicule lourd (VEH-BUS-TRANSCO-01) incapable de négocier les ronds-points kinois | Ajuster l'angle de braquage maximal à basse vitesse à 38 degrés sur les voies de 380-400 cm | Valider la trajectoire spline avec AI-03 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/chaos-vehicle-tuning-guide.md`
- **Modèle Officiel de Livrable** : `templates/vehicle-handling-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-vehicle-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-vehicle-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/vehicle-handling-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque véhicule `VEH-*` dispose de ses dimensions en cm, de sa masse en kg, de sa vitesse de pointe et de ses coefficients de friction sur les 4 surfaces.
- [ ] La différenciation de prise en main entre une moto Wewa agile (`135 kg`) et un bus lourd (`11 500 kg`) est immédiate.
- [ ] Les seuils d'éjection et de collision sont validés avec `ENG-05` (Chaos Physics).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `ENG-05`, `AI-03`.
