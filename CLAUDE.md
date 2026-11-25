# ZAÏRE STUDIO OS — Instructions d'Orchestration Agents (`CLAUDE.md`)

Ce dépôt contient **ZAÏRE STUDIO OS (v1.0.0)**, le système multi-agents d'ingénierie et de production AAA conçu pour le développement du jeu d'action-aventure en monde ouvert **ZAÏRE** (situé à Kinshasa, République Démocratique du Congo).

## 1. Architecture Opérationnelle (3 Couches)
1. **Couche 0 — Direction Centrale (`skills/00-direction/`)** : 7 skills de gouvernance (`dir-01-studio-orchestrator` à `dir-07-quality-director`). Toute requête complexe ou multi-départements doit être routée via `dir-01-studio-orchestrator`.
2. **Couche 1 — Départements Spécialisés (`skills/01-narrative/` à `skills/08-production-quality/`)** : 50 skills métiers indépendants organisés en 8 départements selon un graphe orienté acyclique (DAG) strict.
3. **Couche 2 — Single Source of Truth (`knowledge/`)** :
   - `knowledge/entities-registry.csv` : Registre maître des identifiants uniques (`CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*`, `ITM-*`, `VEH-*`, `SYS-*`).
   - Machine à 5 statuts obligatoires : `CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`.

## 2. Règles Impératives pour Tout Agent Actif
- **Chargement Progressif (Progressive Disclosure)** : Ne chargez les fichiers `references/`, `templates/` et `examples/` d'un skill que lorsque ce skill est activé.
- **Intégrité Référentielle** : N'inventez jamais d'entité sans lui attribuer un ID normalisé conforme à `architecture/knowledge-management.md` et le statut `PROPOSED` (ou `RESEARCH_REQUIRED` si une vérification factuelle sur Kinshasa ou UE5 est requise).
- **Respect des Budgets UE5** : Tout livrable doit respecter les seuils définis dans `knowledge/technical-specs/performance-budgets.csv` (16.6 ms à 60 FPS en mode Performance, 33.3 ms à 30 FPS en mode Qualité) et `knowledge/technical-specs/spatial-metrics.md` (1 unité UE = 1 cm, couloir minimal 350 cm).
- **Zéro Dépendance Circulaire** : Les skills suivent l'ordre topologique de `architecture/skill-dependencies.md`. Tout blocage aval émet un ticket `BLOCKED` ou `REVISION_REQUEST` vers `dir-01-studio-orchestrator`.

## 3. Commandes de Vérification et Packaging
Exécutez toujours la suite de validation après toute modification d'un skill ou du registre :
```bash
python -m unittest discover -s tests -v
python tools/lint_skills.py
python tools/validate_registry.py
python tools/check_dag_cycles.py
python tools/package_skills.py
```
