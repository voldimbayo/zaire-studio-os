---
name: art-02-environment-artist
description: "Production des kits architecturaux modulaires de Kinshasa, de la bibliothèque de matériaux PBR (latérite, béton tropicalisé, tôle ondulée), de la végétation équatoriale et de l'habillage (set dressing) sous UE5 Nanite et Runtime Virtual Texturing (RVT)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-02
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "environment-briefs-wld-06"
    - "3d-pipeline-standards-art-04"
  outputs:
    - "modular-kit-specification.md"
    - "pbr-material-library.csv"
  upstream_dependencies:
    - "WLD-06"
    - "ART-04"
---

# `ART-02` — Environment Artist (`art-02-environment-artist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création des meshes architecturaux modulaires et des matériaux PBR d'un lieu `LOC-*` dont le blockout `WLD-05` est validé.
- Configuration de la fusion terrain/bâtiments (poussière de latérite, humidité) via Runtime Virtual Texturing (RVT).
- Fourniture des pièces modulaires standardisées au générateur procédural Houdini (`ENG-04`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `environment-briefs-wld-06`, `3d-pipeline-standards-art-04`
- **Sorties produites** : `modular-kit-specification.md`, `pbr-material-library.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-06`, `ART-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie jamais l'enveloppe de collision ni les cotes de couverture validées par `WLD-05` (règle Blockout First).
- **Interdiction / Limite** : N'utilise jamais de matériaux Translucides sur des géométries Nanite et désactive le WPO du feuillage au-delà de `35 mètres`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Modéliser chaque pièce du kit architectural sur la grille métrique (`100`, `200`, `400 cm`) avec le point de pivot placé au coin inférieur gauche arrière (`ART-04`).
2. Appliquer une Texel Density de **`10.24 px/cm`** sur tous les modules situés entre `0` et `300 cm` de hauteur d'œil (`5.12 px/cm` sur les étages supérieurs).
3. Utiliser des **Trim Sheets** et le **Vertex Color / Custom Primitive Data** pour générer des dizaines de variations de façades kinoises sans dupliquer les textures en VRAM.
4. Intégrer un blend RVT sur les `50 premiers centimètres` à la base des murs pour fondre la poussière latéritique ou les éclaboussures de pluie.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Besoin de varier la couleur de 50 conteneurs ou façades commerciales dans le même quartier | Interdire la création de 50 textures BaseColor distinctes : utiliser un seul matériau maître piloté par Per-Instance Custom Data | Économiser la VRAM (budget <= 6144 MB) |
| Végétation tropicale (palmiers, manguiers, herbes hautes) causant un surcoût GPU dans Nanite/VSM | Utiliser de la géométrie opaque/masked découplée au plus près de la feuille et couper le World Position Offset (vent) à 3500 cm (35m) | Respecter PERF-GPU-NANITE <= 2.5 ms |
| Écart constaté entre le mesh artistique et la boîte de collision du blockout WLD-05 | Conserver la boîte de collision exacte du blockout comme Simple Collision du Static Mesh | Garantir zéro régression sur le NavMesh et le parkour |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/nanite-modular-environment.md`
- **Modèle Officiel de Livrable** : `templates/modular-kit-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-modular-kit-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-modular-kit-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/modular-kit-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des modules architecturaux s'assemblent sans couture (watertight) sur la grille `100/200/400 cm`.
- [ ] Les valeurs PBR respectent la charte `ART-01` (`Albédo 30-240 sRGB`) et la Texel Density `10.24 px/cm`.
- [ ] Les collisions gameplay sont strictement identiques au blockout `WLD-05` approuvé.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ART-04`, `ART-08`, `ART-01`, `WLD-05`.
