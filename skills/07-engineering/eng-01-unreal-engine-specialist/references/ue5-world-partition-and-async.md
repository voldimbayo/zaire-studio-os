# Architecture C++20 UE5 : World Partition & Streaming Asynchrone (`ENG-01`)

## 1. Configuration des Grilles World Partition (`SYS-WLD-STREAMING`)
| Nom Grille | Taille Cellule (cm) | Rayon Chargement (cm) | Contenu Cible | Stratégie HLOD |
| :--- | :--- | :--- | :--- | :--- |
| `MainGrid_Kinshasa` | `12800 cm (128 m)` | `25600 cm (256 m)` | Architecture modulaire (`ART-02`), Couverts, Routes | `HLOD0_Instanced` -> `HLOD1_MergedMesh` |
| `PropsAndInteriorGrid` | `6400 cm (64 m)` | `12800 cm (128 m)` | Props intérieurs, étals de marché, petits débris | Culled hors rayon (Pas de HLOD) |
| `LandmarkMacroGrid` | `51200 cm (512 m)` | `153600 cm (1.53 km)` | `LOC-LIMETE-ECHANGEUR`, Grues `LOC-GOMBE-PORT` | `HLOD_AlwaysLoaded_LowPoly` |

## 2. Pattern C++20 Obligatoire de Chargement Asynchrone
```cpp
void UZaireStreamingSubsystem::RequestDistrictAssets(const TArray<FSoftObjectPath>& AssetsToLoad, FSimpleDelegate OnLoaded)
{
    FStreamableManager& Streamable = UAssetManager::GetStreamableManager();
    ActiveHandle = Streamable.RequestAsyncLoad(AssetsToLoad, MoveTemp(OnLoaded), FStreamableManager::DefaultAsyncLoadPriority);
}
```

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-01` — Strate DAG 1)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-04`, `WLD-04`, `ART-04`
- **Audit des Entrées (`inputs`)** :
  - `technical-adr-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `open-world-grid-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `3d-pipeline-norms-art-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `ue5-cpp-architecture-spec.md` : Doit respecter le gabarit `templates/ue5-architecture-spec.md` et passer l'audit croisé.
  - `world-partition-streaming-config.md` : Doit respecter le gabarit `templates/ue5-architecture-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-04`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Présence d'un appel LoadSynchronous() ou d'une référence Hard Pointer UPROPERTY() vers un asset lourd dans un Blueprint/C++ | Blocage / Dégradation si ignoré | Remplacer immédiatement le pointeur dur par un TSoftObjectPtr<T> chargé via FStreamableManager avant d'activer l'acteur | Escalade vers Éliminer tout hitch > 2 ms sur le Game Thread |
| Mode de Défaillance 2: Transition rapide en moto Wewa (95 km/h) provoquant un retard de chargement de cellule World Partition | Blocage / Dégradation si ignoré | Activer un Streaming Source secondaire prédictif projeté à +4000 cm en avant du vecteur vitesse du véhicule | Escalade vers Prévenir tout trou géométrique ou pop-in à haute vitesse |
| Mode de Défaillance 3: Conflit de verrouillage de fichiers entre deux level designers travaillant sur la même commune | Blocage / Dégradation si ignoré | Vérifier l'activation obligatoire de One File Per Actor (OFPA) et isoler les acteurs de mission dans un Data Layer dédié | Escalade vers Permettre le travail parallèle sans conflit Git LFS / Perforce |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-01`)

- [ ] **Contrôle DoD #1** : 0 appel `LoadSynchronous()` dans le code runtime ; 100 % des chargements passent par `UAssetManager` / `FStreamableManager`.
- [ ] **Contrôle DoD #2** : Le coût Game Thread global (`PERF-CPU-GAME`) reste `<= 6.5 ms` lors du franchissement de frontière entre deux communes (`DST-GOMBE` -> `DST-KALAMU`).
- [ ] **Contrôle DoD #3** : Configuration World Partition + HLOD validée sur les vitesses de déplacement à pied et en `VEH-MOTO-WEWA-01`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
