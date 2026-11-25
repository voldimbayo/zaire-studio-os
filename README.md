# ZAÏRE STUDIO OS | Système Multi-Agents de Production AAA (v1.0.0)

**ZAÏRE STUDIO OS** est un système d'ingénierie logicielle et de production multi-agents conçu pour piloter le développement de **ZAÏRE**, un jeu d'action-aventure en monde ouvert situé à **Kinshasa (République Démocratique du Congo)** sous **Unreal Engine 5**, **SideFX Houdini** et **Audiokinetic Wwise**.

---

## 1. Architecture Globale du Système

Le système repose sur une architecture déterministe à **3 couches** et un **Graphe Orienté Acyclique (DAG)** garantissant zéro dépendance circulaire :

1. **Couche 0 — Direction Centrale (`skills/00-direction/`)** : 7 rôles directeurs (`DIR-01` à `DIR-07`) chargés du routage DAG, de l'arbitrage créatif/technique/budgétaire et de la gouvernance qualité.
2. **Couche 1 — Départements Spécialisés (`skills/01-narrative/` à `skills/08-production-quality/`)** : 50 skills métiers indépendants dotés de contrats d'entrée/sortie stricts, de procédures explicites, de références progressives (`references/`) et de gabarits prêts à l'emploi (`templates/`).
3. **Couche 2 — Single Source of Truth (`knowledge/`)** : Registre maître d'entités (`entities-registry.csv`), journal d'audit des statuts (`CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`), bible urbaine et culturelle de Kinshasa, glossaire Lingala/Français et budgets techniques UE5.

---

## 2. Organisation du Dépôt

```text
zaire-studio-os/
├── README.md                                # Documentation générale et guide d'utilisation
├── CLAUDE.md                                # Instructions d'orchestration pour agents IA
├── CHANGELOG.md                             # Historique des versions
├── VERSION                                  # Version courante du système (1.0.0)
├── research/                                # [Phase 1] Référentiel technique & méthodologies AAA
├── architecture/                            # [Phase 2] Topologie, DAG, catalogue & standards
├── knowledge/                               # [Phase 3] Single Source of Truth (Registre, Bible, Specs)
├── schemas/                                 # [Phase 3] Schémas JSON formels (Frontmatter, Registre, Tâches)
├── templates/                               # [Phase 3] Modèles transversaux (Handoff Packet, ADR)
├── skills/                                  # [Phase 3] 57 Agent Skills indépendants (9 pôles)
│   ├── 00-direction/                        # DIR-01 à DIR-07 (7 skills)
│   ├── 01-narrative/                        # NAR-01 à NAR-06 (6 skills)
│   ├── 02-world-design/                     # WLD-01 à WLD-06 (6 skills)
│   ├── 03-game-design/                      # GD-01 à GD-07   (7 skills)
│   ├── 04-ai-simulation/                    # AI-01 à AI-04   (4 skills)
│   ├── 05-art-animation/                    # ART-01 à ART-09 (9 skills)
│   ├── 06-audio-localization/               # AUD-01 à AUD-04 (4 skills)
│   ├── 07-engineering/                      # ENG-01 à ENG-08 (8 skills)
│   └── 08-production-quality/               # PRD-01 à PRD-06 (6 skills)
├── tools/                                   # [Phase 3] Outillage Python de validation et packaging
├── tests/                                   # [Phase 3] Suite de tests unitaires et d'intégration
├── docs/                                    # [Phase 3] Index des skills, compatibilité et rapports
└── releases/                                # [Phase 3] Archives ZIP (57 skills Claude.ai + bundle global)
```

---

## 3. Exécution des Outils et Tests

L'ensemble de l'outillage est écrit en **Python 3 standard (zéro dépendance externe)** pour garantir une portabilité immédiate sur Windows, macOS et Linux.

```bash
# 1. Valider le registre d'entités et l'intégrité référentielle (knowledge/)
python tools/validate_registry.py

# 2. Vérifier l'absence de cycles dans le graphe de dépendances (DAG)
python tools/check_dag_cycles.py

# 3. Auditer la conformité YAML, les sections, les chemins et références des 57 skills
python tools/lint_skills.py

# 4. Générer les archives ZIP individuelles (Claude.ai) et l'archive globale du système
python tools/package_skills.py

# 5. Exécuter la suite complète de tests unitaires et d'intégration
python -m unittest discover -s tests -v
```

---

## 4. Compatibilité Multi-Environnements

- **Claude.ai (Web / Projects / Custom Skills)** : Importez individuellement les archives ZIP générées dans `releases/skills/<skill-name>.zip`.
- **Claude Code / Antigravity / Cursor** : Utilisez directement le dépôt complet ; `CLAUDE.md` et la découverte automatique des fichiers `SKILL.md` activent le routage via `dir-01-studio-orchestrator`.
- Consultez [docs/compatibility-matrix.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/docs/compatibility-matrix.md) pour les détails complets par environnement.
