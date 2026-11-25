---
name: eng-06-rendering-engineer
description: "Ingénierie du pipeline de rendu bas niveau DX12/Vulkan sous Unreal Engine 5 : optimisation de Lumen (Surface Cache / Reflections), Nanite (VisBuffer / WPO culling), Virtual Shadow Maps (VSM page caching), shader du fleuve Congo (Single Layer Water) et Temporal Super Resolution (TSR)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ENG-06
  department: 07-engineering
  stratum: 4
  version: "1.1.0"
  inputs:
    - "gpu-budgets-dir-04"
    - "lighting-specs-art-07"
    - "master-materials-art-08"
  outputs:
    - "rendering-pipeline-spec.md"
    - "scalability-presets-matrix.csv"
  upstream_dependencies:
    - "DIR-04"
    - "ART-07"
    - "ART-08"
---

# `ENG-06` — Rendering Engineer (`eng-06-rendering-engineer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`07-engineering`** (Strate DAG **4**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Optimisation des passes GPU (`Lumen <= 4.5 ms`, `Nanite <= 2.5 ms`, `VSM`) suite à une capture RenderDoc ou PIX.
- Définition des profils de scalabilité graphique (`Mode Performance 60 FPS` vs `Mode Qualité 30 FPS` / PC Low -> Epic).
- Implémentation et optimisation du rendu de l'eau turbide du fleuve Congo (`LOC-GOMBE-PORT`, rapides de `DST-NGALIEMA`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `gpu-budgets-dir-04`, `lighting-specs-art-07`, `master-materials-art-08`
- **Sorties produites** : `rendering-pipeline-spec.md`, `scalability-presets-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-04`, `ART-07`, `ART-08`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie pas l'intention artistique des palettes de couleurs ou de l'ambiance d'éclairage (`ART-01`/`ART-07`).
- **Interdiction / Limite** : Interdit l'activation du Hardware Ray Tracing lourd en Mode Performance 60 FPS lorsque le Software Ray Tracing Lumen (Global Distance Field + Surface Cache) respecte le budget de `4.5 ms`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Optimiser les **Virtual Shadow Maps (VSM)** en activant le cache de pages statiques (`r.Shadow.Virtual.Cache = 1`) et en désactivant l'invalidation dynamique des pages d'ombre par le WPO de la végétation au-delà de `3500 cm` (`35 m`).
2. Configurer **Lumen** en Mode Performance 60 FPS sur `Software Ray Tracing` (`r.Lumen.TraceMeshSDFs = 0` au-delà de `40 m`, `Final Gather Quality = 1.0`, `Reflection Downsample Factor = 2`) et réserver le `Hardware Ray Tracing (Hit Lighting)` au Mode Qualité 30 FPS.
3. Implémenter le shader du fleuve Congo (`M_Zaire_Water_River`) sous **UE5 Single Layer Water** avec coefficients d'absorption/diffusion du limon brun-ocre équatorial et réflexions hybrides Screen-Space + Lumen Sky.
4. Définir les CVar exactes de chaque mode dans `templates/rendering-pipeline-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Invalidation massive des pages Virtual Shadow Maps (> 2.0 ms GPU) causée par les palmiers agités par le vent ou les foules Mass | Forcer r.Shadow.Virtual.NonNanite.IncludeInCachedPage et couper l'invalidation WPO des ombres du feuillage à 2500 cm | Stopper l'effondrement du cache VSM |
| Réflexions Lumen sur les flaques de pluie de Matonge dépassant 2.2 ms à elles seules | Utiliser un seuil de Roughness de réflexion stricte (MaxRoughnessToTrace = 0.40) afin que le bitume rugueux (> 0.40) réutilise directement l'irradiance du Lumen Surface Cache sans lancer de rayons de réflexion dédiés | Maintenir Lumen GI + Reflections <= 4.5 ms |
| Scintillement temporel (ghosting/shimmering) sur les câbles électriques aériens et les grilles en TSR | Activer le matériau Responsive AA / Translucency Mask sur les câbles fins et ajuster r.TSR.History.ScreenPercentage | Garantir la stabilité temporelle de l'image |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/ue5-lumen-nanite-vsm-tuning.md`
- **Modèle Officiel de Livrable** : `templates/rendering-pipeline-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-rendering-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-rendering-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/rendering-pipeline-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ENG-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Les passes GPU cumulées respectent `PERF-GPU-LUMEN <= 4.5 ms` et `PERF-GPU-NANITE <= 2.5 ms` en Mode Performance 60 FPS.
- [ ] Le taux de hit du cache de pages statiques VSM est `>= 92 %` lors des déplacements normaux.
- [ ] La matrice de scalabilité distingue explicitement les CVar du Mode Performance (`16.6 ms`) et du Mode Qualité (`33.3 ms`).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-04`, `ENG-07`, `ART-07`.
