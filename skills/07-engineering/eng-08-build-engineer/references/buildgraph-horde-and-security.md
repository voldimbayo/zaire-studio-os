# Architecture CI/CD BuildGraph, Zen DDC & Sécurité IoStore (`ENG-08`)

## 1. Pipeline CI/CD en 5 Étapes (Budget Incrémental `<= 15 min`)
1. **Pre-Flight & Secret Scan (`< 30 s`)** : Vérifie l'absence de secrets en dur, exécute `tools/validate_registry.py`, `tools/check_dag_cycles.py` et `tools/lint_skills.py`.
2. **Compile C++20 via UnrealBuildAccelerator (UBA) (`<= 4 min`)** : Compilation distribuée avec `/W4` et `IWYU`.
3. **Asset Validation (`ENG-03`, `<= 2 min`)** : Exécution headless du commandlet `ValidateAssets`.
4. **Incremental Cook & IoStore Package via Zen DDC (`<= 7 min`)** : Génération des conteneurs `.utoc`/`.ucas`/`.pak` avec injection de `$ENV{ZAIRE_PAK_AES256_KEY}`.
5. **Automated Gauntlet & PSO Merge (`PRD-05` / `ENG-07`)** : Exécution des tests rapides de fumée (Smoke Tests) et consolidation du cache `.upipelinecache`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-08` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ENG-01`, `ENG-02`, `ENG-03`, `ENG-07`
- **Audit des Entrées (`inputs`)** :
  - `cpp-codebase-eng-01-to-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `perf-pso-specs-eng-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gauntlet-test-suites-prd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `ci-cd-buildgraph-spec.xml` : Doit respecter le gabarit `templates/ci-cd-buildgraph-spec.md` et passer l'audit croisé.
  - `pak-security-and-ddc-protocol.md` : Doit respecter le gabarit `templates/ci-cd-buildgraph-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-04`, `PRD-05`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Temps de build incrémental dépassant 15 minutes sur la ferme CI | Blocage / Dégradation si ignoré | Auditer les inclusions d'en-têtes C++ via Include-What-You-Use (IWYU), activer UnrealBuildAccelerator (UBA) et vérifier le taux de Cache Hit du Zen Server DDC (>= 95 %) | Escalade vers Ramener PERF-CI-BUILD sous le seuil de 15.0 minutes |
| Mode de Défaillance 2: Clé ou secret détecté en dur dans un fichier .ini ou script de build | Blocage / Dégradation si ignoré | Faire échouer immédiatement le pipeline CI (Secret Scanner Fail), révoquer la clé exposée et remplacer par une lecture de variable d'environnement du coffre-fort CI | Escalade vers Respecter la politique Zéro Secret Codé en Dur |
| Mode de Défaillance 3: Échec d'un validateur ENG-03 ou d'un test critique Gauntlet PRD-05 pendant le build | Blocage / Dégradation si ignoré | Stopper la promotion du build vers la branche QA/Stable et notifier automatiquement le skill propriétaire de la régression | Escalade vers Maintenir la branche principale 100 % verte |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-08`)

- [ ] **Contrôle DoD #1** : Temps de build et cooking incrémental `<= 15.0 minutes` (`PERF-CI-BUILD`).
- [ ] **Contrôle DoD #2** : 0 secret ou clé de chiffrement stocké en clair dans les fichiers du dépôt.
- [ ] **Contrôle DoD #3** : Déclenchement automatique des validateurs `ENG-03`, des tests Gauntlet `PRD-05` et de la fusion du cache PSO `ENG-07`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
