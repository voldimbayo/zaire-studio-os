---
name: art-01-art-director
description: "Direction artistique globale de ZAÏRE. Définit l'Art Bible, les palettes chromatiques par commune de Kinshasa (DST-*), la charte des matériaux équatoriaux (latérite, béton humide, néons de Matonge) et la lisibilité visuelle gameplay."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-01
  department: 05-art-animation
  stratum: 1
  version: "1.1.0"
  inputs:
    - "creative-pillars-dir-03"
    - "cultural-research-wld-02"
    - "urban-morphology-wld-03"
  outputs:
    - "art-bible-chapter.md"
    - "art-review-scorecard.md"
  upstream_dependencies:
    - "DIR-03"
    - "WLD-02"
    - "WLD-03"
---

# `ART-01` — Art Director (`art-01-art-director`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Définition ou mise à jour de l'identité visuelle d'une commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`).
- Revue de cohérence chromatique et stylistique sur les environnements (`ART-02`), personnages (`ART-03`), éclairages (`ART-07`) ou interfaces (`GD-07`).
- Établissement des règles d'affordance visuelle (couleurs réservées au parkour et aux couverts).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `creative-pillars-dir-03`, `cultural-research-wld-02`, `urban-morphology-wld-03`
- **Sorties produites** : `art-bible-chapter.md`, `art-review-scorecard.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `WLD-02`, `WLD-03`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'outrepasse jamais les budgets GPU (`PERF-GPU-LUMEN`, `PERF-GPU-NANITE`, `PERF-MEM-VRAM`) définis par `DIR-04`.
- **Interdiction / Limite** : Ne modélise pas les assets 3D (`ART-02`/`ART-03`) et n'écrit pas le code des shaders (`ART-08`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Définir pour chaque quartier une **Palette Chromatique Tripartite** : (1) Couleur Dominante (60 % architecture/sol), (2) Couleur Secondaire (30 % signalétique/végétation), (3) Couleur d'Accent/Affordance (10 % guidage joueur).
2. Vérifier la fidélité des références architecturales et vestimentaires avec `WLD-02` et `WLD-03` (`knowledge/world-bible/cultural-guidelines.md`).
3. Garantir une séparation de luminance claire entre le personnage joueur (`CHR-PROTAG-KOFFI`), les menaces (`AI-01`) et l'arrière-plan dense de Kinshasa.
4. Émettre la fiche d'évaluation artistique via `templates/art-bible-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Surcharge visuelle d'un décor de marché masquant les ennemis ou les points d'accroche parkour | Désaturer de 20 % l'arrière-plan haut (> 300 cm) et réserver la teinte jaune ocre haute saturation aux prises d'escalade et sangles de franchissement | Préserver la lisibilité gameplay WLD-05 |
| Teinte de peau d'un personnage paraissant terne ou grise sous l'éclairage de scène | Imposer une recalibration du Subsurface Scattering Profile (ART-03) et de la balance des blancs ACES (ART-07) | Appliquer cultural-guidelines.md Section 3 |
| Même palette chromatique utilisée entre la Gombe et Matonge | Forcer l'opposition : acier/cyan/béton froid pour DST-GOMBE vs ocre latérite/ambre/magenta chaud pour DST-MATONGE | Maintenir l'identité immédiate de chaque commune |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/kinshasa-art-bible-rules.md`
- **Modèle Officiel de Livrable** : `templates/art-bible-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-art-bible-directive.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-art-bible-directive.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/art-bible-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque commune `DST-*` dispose de ses codes couleurs hexadécimaux/linéaires PBR et de ses valeurs d'albédo min/max (`30-240 sRGB`).
- [ ] La couleur d'affordance gameplay est strictement réservée aux éléments interactifs ou franchissables.
- [ ] Validation d'authenticité obtenue auprès de `DIR-03` et `WLD-02`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-03`, `WLD-02`.
