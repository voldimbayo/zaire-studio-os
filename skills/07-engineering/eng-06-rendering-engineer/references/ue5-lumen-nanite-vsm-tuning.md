# Optimisation Bas Niveau du Pipeline Graphique UE5 (`ENG-06`)

## 1. Matrice des CVar de Référence (Mode Performance 60 FPS vs Mode Qualité 30 FPS)
| Sous-Système / CVar UE5 | Mode Performance (60 FPS / `<= 16.6 ms`) | Mode Qualité (30 FPS / `<= 33.3 ms`) | Impact GPU |
| :--- | :--- | :--- | :--- |
| **Résolution Interne -> TSR Output** | `1080p..1440p -> 4K TSR` | `1440p..1800p -> 4K TSR` | Gain `-3.2 ms` |
| `r.Lumen.HardwareRayTracing` | `0 (Software SDF + Surface Cache)` | `1 (Hardware RT Reflections)` | Gain `-2.4 ms` |
| `r.Lumen.Reflections.MaxRoughnessToTrace` | `0.40` (Au-delà : Surface Cache) | `0.55` | Gain `-0.8 ms` |
| `r.Shadow.Virtual.ResolutionLodBiasDirectional` | `-0.5` | `-1.0` | Gain `-0.7 ms` |
| **WPO Shadow Invalidation Distance** | `2500 cm (25 m)` | `3500 cm (35 m)` | Préserve le cache VSM |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-06` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-04`, `ART-07`, `ART-08`
- **Audit des Entrées (`inputs`)** :
  - `gpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lighting-specs-art-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `master-materials-art-08` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `rendering-pipeline-spec.md` : Doit respecter le gabarit `templates/rendering-pipeline-spec.md` et passer l'audit croisé.
  - `scalability-presets-matrix.csv` : Doit respecter le gabarit `templates/rendering-pipeline-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-04`, `ENG-07`, `ART-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Invalidation massive des pages Virtual Shadow Maps (> 2.0 ms GPU) causée par les palmiers agités par le vent ou les foules Mass | Blocage / Dégradation si ignoré | Forcer r.Shadow.Virtual.NonNanite.IncludeInCachedPage et couper l'invalidation WPO des ombres du feuillage à 2500 cm | Escalade vers Stopper l'effondrement du cache VSM |
| Mode de Défaillance 2: Réflexions Lumen sur les flaques de pluie de Matonge dépassant 2.2 ms à elles seules | Blocage / Dégradation si ignoré | Utiliser un seuil de Roughness de réflexion stricte (MaxRoughnessToTrace = 0.40) afin que le bitume rugueux (> 0.40) réutilise directement l'irradiance du Lumen Surface Cache sans lancer de rayons de réflexion dédiés | Escalade vers Maintenir Lumen GI + Reflections <= 4.5 ms |
| Mode de Défaillance 3: Scintillement temporel (ghosting/shimmering) sur les câbles électriques aériens et les grilles en TSR | Blocage / Dégradation si ignoré | Activer le matériau Responsive AA / Translucency Mask sur les câbles fins et ajuster r.TSR.History.ScreenPercentage | Escalade vers Garantir la stabilité temporelle de l'image |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-06`)

- [ ] **Contrôle DoD #1** : Les passes GPU cumulées respectent `PERF-GPU-LUMEN <= 4.5 ms` et `PERF-GPU-NANITE <= 2.5 ms` en Mode Performance 60 FPS.
- [ ] **Contrôle DoD #2** : Le taux de hit du cache de pages statiques VSM est `>= 92 %` lors des déplacements normaux.
- [ ] **Contrôle DoD #3** : La matrice de scalabilité distingue explicitement les CVar du Mode Performance (`16.6 ms`) et du Mode Qualité (`33.3 ms`).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
