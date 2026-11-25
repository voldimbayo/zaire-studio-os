# Guide d'Installation dans Claude.ai — ZAÏRE STUDIO OS v1.1.0 (`claude-ai-installation-guide.md`)

Ce guide explique comment importer et utiliser les **57 Agent Skills** et la **Single Source of Truth (`knowledge/`)** de **ZAÏRE STUDIO OS (v1.1.0)** dans **Claude.ai** (Web et application Desktop).

---

## 1. Distinction Cruciale entre les Types d'Archives ZIP (`releases/`)

| Répertoire / Archive | Format Interne | Usage dans Claude.ai |
| :--- | :--- | :--- |
| **`releases/skills/<skill-name>.zip`** (57 fichiers) | Dossier racine unique `<skill-name>/SKILL.md` + `references/` (incluant `entities-registry-snapshot.csv`) + `templates/` + `examples/` (+ `scripts/`). | **DIRECTEMENT IMPORTABLE** dans l'interface *Settings > Capabilities > Upload Skill* de Claude.ai. |
| **`releases/departments/<00..08>.zip`** (9 fichiers) | Contient plusieurs sous-dossiers de skills (`00-direction/dir-01-...`, `00-direction/dir-02-...`). | **BUNDLE D'ARCHIVAGE** : Ne pas téléverser tel quel dans l'importateur de Skill unitaire de Claude.ai (qui exige un seul `SKILL.md` à la racine). Décompressez d'abord l'archive départementale si vous souhaitez accéder à ses skills. |
| **`releases/zaire-studio-os-v1.1.0-full.zip`** | Dépôt complet (`research/`, `architecture/`, `knowledge/`, `skills/`, `production/`, `tools/`, `tests/`, `docs/`, `audit/`). | **ARCHIVE SYSTÈME COMPLÈTE** pour Claude Code, Google Antigravity, Cursor et archivage Git. |

---

## 2. Étape 1 : Configurer le Projet Claude.ai ("ZAÏRE STUDIO OS — Knowledge Base")

Pour que tous les skills partagent la même **Single Source of Truth (Couche 2)** :
1. Ouvrez **Claude.ai** et créez un Projet intitulé **`ZAÏRE STUDIO OS v1.1.0`**.
2. Dans **Project Knowledge (Connaissances du projet)**, ajoutez les fichiers de `knowledge/` et la racine :
   - `CLAUDE.md` & `docs/canonical-dependency-registry.md`
   - `knowledge/entities-registry.csv` (41 entités incluant `DST-BANDAL`, `ORG-POLICE-PCR`, `SYS-LAW-ESCALATION`, `SYS-TELEMETRY-ANALYTICS`)
   - `knowledge/status-audit-log.csv`
   - `knowledge/world-bible/kinshasa-districts.md`, `cultural-guidelines.md`, `lingala-french-glossary.csv`
   - `knowledge/technical-specs/spatial-metrics.md`, `performance-budgets.csv`, `gameplay-tags-taxonomy.csv`

*(Note d'autonomie v1.1.0 : Chaque archive individuelle `releases/skills/<skill-name>.zip` embarque également une copie locale `references/entities-registry-snapshot.csv` afin de fonctionner sans erreur même hors d'un Projet Claude.ai).*

---

## 3. Étape 2 : Importer les Agent Skills (`releases/skills/*.zip`)

1. Dans Claude.ai, activez **Code Execution / Analysis Tool** pour permettre l'exécution des scripts Python (`scripts/*.py`).
2. Cliquez sur **Upload Skill** et sélectionnez les archives individuelles depuis `releases/skills/`.
3. Importez en priorité le socle de direction (`dir-01-studio-orchestrator.zip` à `dir-07-quality-director.zip`) puis les skills des départements requis par votre session de production.
