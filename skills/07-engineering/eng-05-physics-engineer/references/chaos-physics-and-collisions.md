# Architecture UE5 Chaos Physics & Matrice de Collisions (`ENG-05`)

## 1. Matrice de Réponse des Profils de Collision (`SYS-PHYS-CHAOS`)
| Profil Collision | `WorldStatic` | `Pawn (Koffi/PNJ)` | `Vehicle (Wewa/Bus)` | `CombatHitbox` | `ChaosDebris` | `Camera` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`WorldStatic`** | Ignore | **Block** | **Block** | Overlap | **Block** | **Block** |
| **`Pawn`** | **Block** | **Block** | **Block** | **Overlap** | Ignore | Ignore |
| **`Vehicle`** | **Block** | **Block** | **Block** | Overlap | **Block** (Impulse) | **Block** |
| **`ChaosDebris`** | **Block** | Ignore | Ignore (Post-break) | Ignore | **Ignore** | **Ignore** |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-05` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-06`, `ART-02`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `vehicle-handling-specs-gd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `environment-kits-art-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `chaos-physics-specification.md` : Doit respecter le gabarit `templates/chaos-physics-spec.md` et passer l'audit croisé.
  - `collision-channels-matrix.csv` : Doit respecter le gabarit `templates/chaos-physics-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-07`, `PRD-05`, `GD-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Véhicule Wewa traversant un étal de marché à Matonge et provoquant un pic CPU Chaos > 1.5 ms | Blocage / Dégradation si ignoré | Désactiver les collisions inter-fragments (CollisionGroup = Debris_NoSelfCollide) sur les morceaux d'étal brisés et plafonner les corps rigides de débris actifs à 45 simultanés | Escalade vers Maintenir PERF-CPU-CHAOS <= 1.5 ms en toutes circonstances |
| Mode de Défaillance 2: Tremblement (jitter) ou rebond anormal de la moto Wewa à l'arrêt sur une pente en latérite | Blocage / Dégradation si ignoré | Activer le Velocity/Angular Sleep Threshold sur les suspensions au repos et utiliser un Raycast/SphereCast Wheel lissé au lieu d'un cylindre rigide complexe | Escalade vers Garantir une stabilité physique parfaite |
| Mode de Défaillance 3: Static Mesh de décor soumis avec plus de 4 primitives convexes de collision | Blocage / Dégradation si ignoré | Remplacer la collision par 1 à 2 primitives analytiques (Box, Capsule, Sphere) qui coûtent 5x moins cher en Broadphase/Narrowphase | Escalade vers Optimiser les requêtes de balayage (Sweeps) du Game Thread |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-05`)

- [ ] **Contrôle DoD #1** : Le coût CPU Chaos Physics global (`PERF-CPU-CHAOS`) est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).
- [ ] **Contrôle DoD #2** : 0 tremblement (jitter) ni traversée de sol (tunneling) sur `VEH-MOTO-WEWA-01` jusqu'à `95 km/h`.
- [ ] **Contrôle DoD #3** : Tous les débris destructibles passent à l'état `Sleeping` ou sont recyclés en moins de `4.0 secondes`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
