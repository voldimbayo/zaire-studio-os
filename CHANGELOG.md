# Changelog — ZAÏRE STUDIO OS

Toutes les modifications notables de **ZAÏRE STUDIO OS** sont documentées dans ce fichier.
Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.1.0] - 2026-11-26 (Phase 5 : Architecture Hardening & Rectification d'Intégrité QA)

### Statut de Livraison
- **Statut Global** : `PARTIAL` — Socle d'architecture, registre DAG et outillage Python validés (`PASS`) ; génération multi-agents autonome et compilation moteur binaire classées `NOT TESTED` (la mention prématurée `RELEASE READY` a été retirée).

### Ajouté & Rectifié
- **Rectification d'Intégrité des Sources (`research/source-registry.csv` : `SRC-001` à `SRC-035`)** :
  - Séparation de `SRC-032` en 4 entrées distinctes vérifiées via recherche web officielle : `SRC-032` (*UE 5.8 MegaLights*), `SRC-033` (*UE Mutable Plugin*), `SRC-034` (*UE AnimNext / UAF* — marqué expérimental) et `SRC-035` (*SideFX Houdini Copernicus (COP) & APEX* — corrigeant l'appellation impropre « Copernicus 2.0 »).
  - Vérification web de `SRC-031` (*Microsoft XAG 101/102/104/107*) et de l'ISBN de `SRC-021` (*Filip De Boeck, Leuven University Press, 9789058679673*).
  - Étiquetage honnête des ouvrages papier `SRC-020` et `SRC-022`..`SRC-030` en *« Référence Bibliographique (Texte intégral non consulté en session) »*.
- **Suppression du Remplissage Artificiel & Balisage des Cibles Synthétiques** :
  - Suppression de la boucle de remplissage (`_TPL_01..09`) dans `tools/skill_builder.py` pour garder des templates CSV authentiques.
  - Marquage explicite des chiffres de performance (`15.70 ms`) comme allocations cibles synthétiques (`SYNTHETIC_TARGET_ALLOCATION_NOT_MEASURED_IN_ENGINE`) dans `production/` et `audit/`.
- **Workstream 1 (Réconciliation DAG Canonique)** :
  - Création de [docs/canonical-dependency-registry.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/docs/canonical-dependency-registry.md) et alignement à 100 % entre `architecture/skill-dependencies.md`, `tools/registry_data.py`, `dir-01-studio-orchestrator/scripts/build_dag_plan.py` (désormais généré dynamiquement depuis `CANONICAL_SKILLS`) et les 57 fichiers `SKILL.md`.
  - Garantie topologique que `ENG-04` (Houdini ZoneGraph) s'exécute toujours en amont d'`AI-03` (Traffic AI) et `WLD-05` (Level Design Blockout) en amont d'`ART-05` (Animation Motion Warping).
- **Workstream 2 (Production Fonctionnelle Réelle dans `production/`)** :
  - Refonte complète de `tools/run_functional_scenarios.py` qui génère et écrit **17 fichiers de production réels** dans `production/scenario-1..5/` et **6 rapports de validation** dans `production/validation-reports/`, validés explicitement via `--file`.
  - Séparation stricte entre artefacts de production (`production/`), fixtures de test (`tests/fixtures/blockout_test_fixtures.json`) et rapports d'audit (`audit/`).
- **Workstream 3 (Approfondissement des 57 Skills)** :
  - Expansion des 57 fichiers `references/*.md` (de 6–18 lignes à **48–62 lignes** chacun) intégrant les matrices FMEA de modes de défaillance, les profils Unreal Engine 5.8 / SideFX Houdini 22.0 / Wwise et les checklists DoD.
  - Expansion des 57 fichiers `templates/*` (`>= 12 lignes` garanties et vérifiées par `tools/lint_skills.py`).
- **Workstream 4 (Complétude Métier & Sources)** :
  - Ajout dans `knowledge/entities-registry.csv` (passé de 33 à **41 entités**) : `DST-BANDAL`, `LOC-BANDAL-LUMUMBA-HUB`, `CHR-ALLY-PAPA-ETIENNE`, `ORG-POLICE-PCR` (Police de Circulation Routière), `ORG-URGENCE-FLUVIALE`, `VEH-POLICE-PICKUP-01`, `SYS-LAW-ESCALATION`, `SYS-TELEMETRY-ANALYTICS`.
  - Ajout des Gameplay Tags d'escalade policière (`State.Law.AlertLevel.1..3`), d'urgence médicale (`State.Emergency.MedicalDispatch`), de véhicule PCR (`Vehicle.Type.PolicePCR`) et de commune (`World.District.Bandal`).
  - Enregistrement des **12 sources bibliographiques et standards industriels** manquants dans `research/source-registry.csv` (`SRC-021` à `SRC-032`, portant le registre de 20 à **32 sources vérifiées**).
- **Workstream 5 & 6 (Vérification Moteur, Durcissement YAML & Packaging Claude.ai)** :
  - Audit technique de compatibilité UE 5.8 / Houdini 22.0 / Wwise dans `audit/phase-5-engine-compatibility.md`.
  - Durcissement de `parse_simple_yaml()` dans `tools/__init__.py` (support des blocs multilignes `|` et `>`, des virgules entre guillemets dans les listes inline et des commentaires inline `#`).
  - Inclusion automatique d'un instantané `references/entities-registry-snapshot.csv` dans chacune des 57 archives ZIP individuelles (`releases/skills/*.zip`) pour garantir leur autonomie dans Claude.ai.
  - Sauvegarde de l'état pré-Phase 5 dans `releases/zaire-studio-os-v1.0.0-backup-pre-phase5.zip`.

---

## [1.0.0] - 2026-11-25

### Ajouté
- Implémentation initiale des Phases 1, 2, 3 et 4 (57 Agent Skills, Knowledge Base, outillage Python et revue indépendante `audit/independent-review.md`).
