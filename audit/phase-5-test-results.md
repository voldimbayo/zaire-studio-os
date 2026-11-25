# Résultats des Tests & Limites Méthodologiques — Phase 5 (`phase-5-test-results.md`)

- **Date de Révision** : `2026-11-26`
- **Version Testée** : `ZAÏRE STUDIO OS v1.1.0`
- **Environnement** : Windows / PowerShell — `Python 3.14.7` (0 dépendance tierce)
- **Statut Global Système** : **`PARTIAL` (Outillage, DAG et schémas `PASS` ; génération multi-agents autonome et exécution moteur `NOT TESTED`)**

---

## 1. Tableau Récapitulatif Honnête des Vérifications

| Suite / Vérification | Cible Réellement Testée | Résultat | Classification |
| :--- | :--- | :--- | :--- |
| `python tools/validate_registry.py` | Syntaxe et intégrité référentielle des 41 entités de `knowledge/entities-registry.csv` et correspondance des IDs `SRC-001`..`SRC-035`. | `0 erreur` | **`PASS`** |
| `python tools/check_dag_cycles.py` | Absence de cycles (algorithme de Kahn) sur les 57 skills du catalogue canonique et sur les 57 fichiers `SKILL.md` sur disque. | `0 cycle sur 57 skills` | **`PASS`** |
| `python tools/lint_skills.py --require-all` | Conformité YAML frontmatter, présence des 7 sections SOP, sécurité des chemins locaux, intégrité des templates CSV (sans remplissage artificiel) et Markdown. | `57/57 skills vérifiés (0 erreur)` | **`PASS`** |
| `python -m unittest discover -s tests -v` | 14 tests unitaires et d'intégration (parseur YAML, parité `build_dag_plan.py` == `CANONICAL_SKILLS`, ordre `ENG-04 -> AI-03`, fixtures positives/négatives `--file`, structure ZIP Claude.ai). | `Ran 14 tests — OK` | **`PASS`** |
| `python tools/run_functional_scenarios.py` | **Portée exacte** : Génère de manière déterministe en Python 17 fichiers de spécification de référence dans `production/scenario-1..5/` et vérifie qu'ils franchissent les validateurs CLI (`--file`). **Limite** : Ces fichiers sont écrits par le script Python et non par 57 agents LLM indépendants ; les profils de performance sont des allocations cibles synthétiques. | Validateurs CLI OK, mais génération scriptée | **`PARTIAL`** |
| Exécution autonome des 57 Skills par un orchestrateur LLM multi-agents | Évaluation de la qualité des livrables produits à froid par Claude / un LLM en lisant uniquement les `SKILL.md` sur de nouveaux briefs inédits. | Non exécuté par `run_functional_scenarios.py` | **`NOT TESTED`** |
| Compilation & Profilage Moteur (UE 5.8, Houdini 22.0, Wwise) | Compilation C++ `UBT`, cuisson HDA `hython`, SoundBanks `WwiseConsole` et captures GPU `Unreal Insights` / `RenderDoc`. | Logiciels absents de l'hôte | **`NOT TESTED`** |
