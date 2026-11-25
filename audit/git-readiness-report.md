# Rapport de préparation Git — ZAÏRE STUDIO OS

- **Date :** 2026-11-26
- **Version du framework :** 1.1.0 (`VERSION`)
- **Outil :** Git 2.55.0 (Windows)
- **Livrables :** [`.gitignore`](../.gitignore), [`docs/gitignore-policy.md`](../docs/gitignore-policy.md), ce rapport
- **Verdict :** ✅ **Prêt pour le premier commit**, sous réserve des points de vigilance du § 5.

## 1. État initial

| Constat | Résultat |
|---|---|
| Dépôt Git existant | **Non**. Aucun `.git`, donc **aucun fichier déjà suivi** ni historique à nettoyer. |
| `.gitignore` existant | Aucun. |
| Fichiers dans le projet | 432 (avec le nouveau `.gitignore`), 7,8 Mo. |
| Types de fichiers | 268 `.md`, 70 `.zip`, 29 `.py`, 28 `.json`, 20 `.pyc`, 15 `.csv`, 1 sans extension (`VERSION`), plus `.gitignore`. |
| Contenu Unreal / Houdini | **Aucun pour l'instant.** Les règles correspondantes préparent l'arrivée des projets UE 5.8 et Houdini 22 et ont été testées sur une arborescence simulée (§ 3.2). |

Aucune commande `git init`, `git add`, `git commit`, `git clean` ou `git reset` n'a été exécutée dans le projet. Aucun fichier existant n'a été supprimé ou modifié. Les vérifications ont utilisé un dépôt Git temporaire **placé hors du projet** (`--git-dir` externe, `--work-tree` = projet), qui ne laisse aucune trace dans l'arborescence.

## 2. Analyse de sensibilité

| Recherche | Résultat |
|---|---|
| Noms de fichiers sensibles (`.env*`, `*.pem`, `*.key`, `*.pfx`, `*.p12`, `id_rsa*`, `*secret*`, `*credential*`, `*token*`) | Un seul résultat : `skills/03-game-design/gd-05-combat-designer/references/frame-data-and-attack-tokens.md`. **Faux positif** : document de game design (jetons d'attaque), pas un secret. Il reste suivi. |
| Motifs de secrets dans le contenu (`api_key=`, `password=`, `sk-…`, `AKIA…`, `ghp_…`, `xox[bp]-`, `-----BEGIN … PRIVATE KEY`) | **Aucune occurrence.** |
| Adresses e-mail | **Aucune occurrence.** |
| Fichiers > 1 Mo | Aucun. |
| Fichiers système/temporaires (`Thumbs.db`, `.DS_Store`, `desktop.ini`, `*.log`, `*.tmp`, `*.bak`) | Aucun. |

**Aucun fichier sensible n'est présent, et aucun n'est suivi par Git puisque le dépôt n'existe pas encore.**

## 3. Vérification des règles

### 3.1 Projet réel

Commandes : `git status --porcelain --ignored -uall` et `git add --dry-run -A .`, avec `core.ignorecase=true` (valeur par défaut sous Windows).

| Mesure | Résultat |
|---|---|
| Fichiers ignorés | **20**, tous des `.pyc` dans 4 dossiers `__pycache__/` (`tools/`, `tools/departments/`, `tests/`, `skills/00-direction/dir-01-studio-orchestrator/scripts/`). |
| Fichiers ajoutables | **412**, soit 100 % des fichiers hors caches Python. |
| `SKILL.md` ajoutables | **57 / 57** |
| ZIP de `releases/` ajoutables | **70 / 70** |
| Fichiers sources ignorés par erreur | **0** |

Répartition des fichiers ajoutables : `skills/` 237 · `releases/` 70 · `production/` 32 · `tools/` 18 · `audit/` 11 · `research/` 9 · `knowledge/` 8 · `architecture/` 8 · `docs/` 6 · `schemas/` 3 · `tests/` 3 · `templates/` 2 · racine 5 (`.gitignore`, `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `VERSION`). Ces chiffres sont antérieurs à l'ajout de `docs/gitignore-policy.md` et de ce rapport, eux aussi ajoutables.

Contrôles nominatifs, tous **ajoutables** : `.gitignore`, `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `VERSION`, `knowledge/entities-registry.csv`, `tests/fixtures/blockout_test_fixtures.json`, `skills/…/frame-data-and-attack-tokens.md`.

### 3.2 Arborescence UE 5.8 / Houdini 22 simulée (`git check-ignore -v`)

Une arborescence fictive, `Zaire/` pour Unreal et `Houdini/`, a été créée hors du projet avec le même `.gitignore`.

**Ignorés comme attendu (36/36)**, par exemple :

| Fichier | Règle |
|---|---|
| `Zaire/Binaries/Win64/UnrealEditor-Zaire.dll` | `Binaries/` |
| `Zaire/Plugins/ZaireMass/Intermediate/x.gen.cpp` | `Intermediate/` |
| `Zaire/Saved/Config/WindowsEditor/EditorPerProjectUserSettings.ini` | `Saved/` |
| `Zaire/DerivedDataCache/a.udd` | `DerivedDataCache/` |
| `Zaire/Zaire.sln`, `Zaire/Zaire.code-workspace`, `Zaire/.vs/…` | `*.sln`, `*.code-workspace`, `.vs/` |
| `Houdini/fx/backup/flood_bak3.hip`, `flood_bak12.hiplc` | `*_bak[0-9]*.hip(lc)` |
| `Houdini/fx/crash.flood.voldi_1234.hip` | `crash.*.hip` |
| `Houdini/fx/geo/river.0001.bgeo.sc`, `…/pyro.0010.sim`, `…/smoke.0010.vdb`, `…/ground.rat` | `*.bgeo.*`, `*.sim`, `*.vdb`, `*.rat` |
| `.venv/…`, `.pytest_cache/…`, `web/node_modules/…` | règles Python / Node |
| `.env`, `.env.production`, `secrets/deploy.pem`, `keys/signing.pfx`, `config/credentials.json`, `tools/settings.local.json`, `.claude/settings.local.json` | règles secrets |

**Suivis comme attendu (24/24)**, par exemple : `Zaire.uproject`, `.vsconfig`, `Content/Maps/Gombe.umap`, `Content/Characters/Koffi/SK_Koffi.uasset`, `Content/Cache/FX_Cache.uasset` (dossier `Cache` dans `Content` : non ignoré), `Config/DefaultEngine.ini`, `Source/…/*.cpp`, `Zaire.Build.cs`, `Plugins/ZaireMass/ZaireMass.uplugin` et ses sources, `Build/Windows/Application.ico` (non touché malgré la casse), `flood.hip`, `flood.hiplc`, `zaire_road.hda`, `scripts/python/export_tools.py`, `SourceArt/volumes/cloud_ref.vdb`, `SourceArt/geo/landmark.bgeo.sc`, `.env.example`, `.vscode/extensions.json`, `docs/token-budget.md`.

### 3.3 Anomalie détectée et corrigée pendant l'audit

La première version des exceptions `!SourceArt/**/*.vdb` ne s'appliquait qu'à un `SourceArt/` **à la racine** : un motif contenant `/` est ancré à l'emplacement du `.gitignore`. `Houdini/SourceArt/volumes/cloud_ref.vdb` était donc ignoré. Correction : `!**/SourceArt/**/*.vdb` (et équivalents). Après revérification, les fichiers de `SourceArt/` sont suivis à toute profondeur, et les caches hors `SourceArt/` restent ignorés.

## 4. Choix délibérés

| Choix | Justification |
|---|---|
| `releases/*.zip` **suivis** | Livrables importables dans Claude (57 skills, 9 départements, archives complètes, plug-in). Exigence explicite de ne pas les ignorer sans raison. |
| Pas de `build/`, `dist/`, `cache/`, `geo/`, `render/` | Collision avec `Build/` ou `Content/…/Cache/` d'Unreal, car `core.ignorecase=true` sous Windows. |
| Pas de `*token*` / `*secret*` | Faux positif réel dans `skills/` (§ 2). |
| `.abc`, `.fbx`, `.usd`, `.exr` **non ignorés** | Souvent sources d'import Unreal ; à gérer par Git LFS, pas par exclusion. |

## 5. Risques et points de vigilance

| # | Risque | Gravité | Recommandation |
|---|---|---|---|
| R1 | **Doublon binaire** : `releases/zaire-studio-os-v1.0.0-backup-pre-phase5.zip` et `releases/zaire-studio-os-v1.0.0-full.zip` sont identiques octet pour octet (MD5 `62ff2e87…`, 657 152 octets). | Faible | Décider avant le premier commit si les deux doivent être versionnés. Aucun fichier n'a été supprimé. |
| R2 | ✅ **Résolu.** Deux archives changeaient à chaque `python tools/package_skills.py` : le plug-in (entrée `plugin.json` horodatée à l'heure courante) et l'archive complète (`docs/skills-index.md` réécrit à chaque exécution, donc nouvelle date de modification). | — | Corrigé dans `tools/package_skills.py` : date fixe pour `plugin.json`, et index réécrit uniquement si son contenu change. Vérification : deux packagings successifs produisent les **70/70 archives identiques** (MD5). |
| R3 | **Binaires dans Git sans LFS** : 70 ZIP (4,2 Mo) aujourd'hui. Ce volume deviendra critique avec les assets Unreal et Houdini, qui pèsent des Go. | Moyenne → Élevée | Mettre en place `.gitattributes` + Git LFS **avant** le premier asset UE/Houdini (voir `docs/gitignore-policy.md` § 5). |
| R4 | **NDA plateformes** : les SDK et dossiers `Platforms/<Console>/` relèvent des accords constructeurs. | Élevée (à venir) | Dépôt privé uniquement ; pas de règle d'exclusion automatique, la décision revient à la production. |
| R5 | **Secrets futurs** : le `.gitignore` ne protège que les noms prévus. | Moyenne | Ajouter un scan de secrets en pre-commit (ex. `gitleaks`) avant d'ouvrir le dépôt à d'autres contributeurs. |

## 6. Étapes suivantes (non exécutées)

```bash
git init
git add -A
git status            # relire la liste avant de valider
git commit -m "Initial commit — ZAÏRE STUDIO OS v1.1.0"
```

Aucun dépôt distant n'a été créé et rien n'a été poussé.
