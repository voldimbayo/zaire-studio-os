# Pipeline Procédural Hybride : SideFX Houdini PDG -> UE5 PCG (`ENG-04`)

## 1. Répartition des Responsabilités Houdini (Offline PDG) vs UE5 PCG (In-Engine)
- **SideFX Houdini 20.5+ (HDA / PDG TOP Network)** :
  - Nettoyage topologique des graphes routiers OpenStreetMap et projection sur le MNT (DEM) du bassin du fleuve Congo.
  - Calcul géométrique lourd des carrefours complexes (`LOC-MATONGE-VICTOIRE`, bretelles de `LOC-LIMETE-ECHANGEUR`) et génération des profils `ZoneGraph`.
  - Subdivision des îlots urbains en lots orientés et export de **Point Clouds `.pcg` / Alembics légers** dotés d'attributs (`@kit_id`, `@floor_count`, `@district_tint`).
- **Unreal Engine 5 PCG Framework (Runtime / Editor Graphs)** :
  - Lecture des Point Clouds Houdini et instanciation directe des meshes Nanite (`ART-02`) avec injection de `CustomPrimitiveData`.
  - Adaptation dynamique locale aux volumes d'exclusion `WLD-05` et au matériau RVT du terrain.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-04` — Strate DAG 3)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-03`, `ART-02`, `GD-06`
- **Audit des Entrées (`inputs`)** :
  - `urban-typology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `modular-kits-art-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `traffic-zonegraph-rules-ai-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `hda-pcg-pipeline-spec.md` : Doit respecter le gabarit `templates/hda-pipeline-spec.md` et passer l'audit croisé.
  - `procedural-generation-rules.csv` : Doit respecter le gabarit `templates/hda-pipeline-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `WLD-04`, `ENG-07`, `AI-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Intersection entre un îlot procédural Houdini/PCG et un blockout de mission WLD-05 (ex: LOC-GOMBE-PORT) | Blocage / Dégradation si ignoré | Prioriser à 100 % le volume manuel WLD-05 via un Box Volume taggé PCG_Exclude_ManualArena qui soustrait les points PCG dans son empreinte | Escalade vers Garantir zéro obstacle procédural dans une arène de mission |
| Mode de Défaillance 2: Secteur dont la couverture OSM des ruelles secondaires est incomplète (ex: DST-MASINA en RESEARCH_REQUIRED) | Blocage / Dégradation si ignoré | Appliquer l'algorithme de subdivision L-System / Voronoï orthogonal calibré par WLD-03 uniquement sur un Data Layer de prévisualisation taggé PROPOSED_PROCEDURAL | Escalade vers Séparer clairement la donnée SIG vérifiée du remplissage procédural |
| Mode de Défaillance 3: Génération d'îlot créant plus de 1500 acteurs individuels dans l'Outliner UE5 | Blocage / Dégradation si ignoré | Fusionner les descripteurs d'instances par cellule World Partition (128m) dans des composants Instanced Static Mesh (ISM/HISM) packés | Escalade vers Maintenir un coût d'instanciation minimal en mémoire et en draw calls |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-04`)

- [ ] **Contrôle DoD #1** : Génération 100 % déterministe à seed fixe (`GlobalSeed = 19600630`).
- [ ] **Contrôle DoD #2** : Les splines `ZoneGraph` générées respectent les largeurs de voies (`350-400 cm`) et les couloirs inter-files Wewa (`>= 130 cm`).
- [ ] **Contrôle DoD #3** : Respect absolu des volumes d'exclusion `WLD-05` (zéro prop procédural sur un chemin critique ou un couvert).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
