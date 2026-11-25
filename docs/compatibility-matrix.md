# Matrice de Compatibilité Multi-Environnements — ZAÏRE STUDIO OS

Ce document décrit les spécificités d'utilisation, d'importation et d'exécution des **57 Agent Skills** de **ZAÏRE STUDIO OS** selon l'environnement cible.

---

## 1. Synthèse Comparative des Environnements

| Fonctionnalité / Contrainte | **Claude.ai (Web / Desktop App)** | **Claude Code (CLI)** | **Google Antigravity (AGY)** | **Cursor / Codex / Autres IDE** |
| :--- | :--- | :--- | :--- | :--- |
| **Mode d'importation** | Upload ZIP individuel (`releases/skills/<skill-name>.zip`) | Découverte native dans le workspace (`skills/**/SKILL.md` + `CLAUDE.md`) | Découverte native des dossiers `SKILL.md` | Référencement via `.cursorrules` ou `AGENTS.md` / `CLAUDE.md` |
| **Frontmatter YAML requis** | `name` (kebab-case <= 64 chars), `description` (<= 1024 chars), `metadata` | `name`, `description`, `metadata` | `name`, `description` | `name`, `description` |
| **Progressive Disclosure** | Chargement automatique de `SKILL.md`, lecture à la demande de `references/` et `templates/` inclus dans le ZIP | Lecture à la demande via outils fichiers (`read_file`) | Lecture à la demande via `read_file` | Lecture à la demande via outils de lecture de fichiers |
| **Exécution des scripts (`scripts/` & `tools/`)** | Dans le bac à sable Code Execution (Analysis Tool / Python sandbox) si activé | Exécution directe locale via terminal Bash/PowerShell | Exécution directe locale via `run_command` | Exécution directe locale via terminal intégré |
| **Accès à `knowledge/` partagé** | Nécessite de joindre les fichiers de `knowledge/` au **Project Knowledge** de Claude.ai | Accès direct sur le disque (`knowledge/entities-registry.csv`) | Accès direct sur le disque (`knowledge/entities-registry.csv`) | Accès direct sur le disque |

---

## 2. Configuration Recommandée pour Claude.ai

Dans **Claude.ai**, chaque skill est importé sous forme d'une archive ZIP autonome :
1. **Structure de l'archive ZIP individuelle (`releases/skills/<skill-name>.zip`)** :
   - La racine du ZIP contient un dossier unique `<skill-name>/` renfermant `SKILL.md`, `references/`, `templates/`, `examples/` (et `scripts/` lorsque applicable).
   - Aucun lien relatif dans un `SKILL.md` ne pointe en dehors de son dossier lors d'une utilisation isolée ; les références au référentiel partagé `knowledge/` indiquent explicitement les fichiers à ajouter dans le *Project Knowledge* de Claude.ai.
2. **Utilisation avec un Projet Claude.ai ("ZAÏRE Production Project")** :
   - Ajoutez les fichiers de `knowledge/` (`entities-registry.csv`, `kinshasa-districts.md`, `cultural-guidelines.md`, `lingala-french-glossary.csv`, `spatial-metrics.md`, `performance-budgets.csv`, `gameplay-tags-taxonomy.csv`) aux fichiers de contexte du Projet.
   - Activez `dir-01-studio-orchestrator.zip` ainsi que les skills du département concerné par votre session de travail.

---

## 3. Configuration pour Claude Code & Google Antigravity

Dans **Claude Code** et **Google Antigravity**, le système fonctionne en mode **Repository-Native** :
1. Le fichier racine `CLAUDE.md` fournit les règles globales d'orchestration, la nomenclature des identifiants uniques et les commandes de vérification.
2. Les agents accèdent directement en lecture/écriture contrôlée à `knowledge/entities-registry.csv` et peuvent exécuter les scripts de validation locale :
   - `python tools/validate_registry.py`
   - `python tools/check_dag_cycles.py`
   - `python tools/lint_skills.py`
3. L'archive complète du système est conservée dans `releases/zaire-studio-os-v1.0.0-full.zip`.
