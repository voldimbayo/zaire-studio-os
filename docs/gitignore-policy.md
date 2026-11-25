# Politique `.gitignore` — Projet ZAÏRE

> Fichier de référence : [`.gitignore`](../.gitignore) à la racine.
> Rapport de vérification : [`audit/git-readiness-report.md`](../audit/git-readiness-report.md).

## 1. Principe

Le dépôt ZAÏRE versionne **tout ce qui est source ou livrable** et ignore uniquement :

1. ce qui est **régénérable** (compilation, caches, sorties de simulation, fichiers de projet IDE) ;
2. ce qui est **privé** (secrets, certificats, configurations propres à un poste).

En cas de doute, un fichier est **suivi**. Ajouter une règle d'exclusion exige de pouvoir répondre à la question : *« Comment ce fichier se régénère-t-il, ou pourquoi ne doit-il jamais quitter ce poste ? »*

## 2. Contrainte Windows : sensibilité à la casse

Sous Windows, Git active `core.ignorecase=true`. Un motif s'applique donc **sans tenir compte des majuscules**. Conséquences concrètes :

| Motif écarté | Raison |
|---|---|
| `build/` | Ignorerait `Build/` d'Unreal (icônes, manifestes de plateforme : sources). |
| `dist/` | Nom trop générique ; aucun outil du projet n'en produit. |
| `cache/`, `geo/`, `render/` | Ignoreraient des dossiers de `Content/` (ex. `Content/FX/Cache/`). Les caches Houdini sont exclus **par extension**, pas par nom de dossier. |
| `*token*`, `*secret*` | Ignoreraient des sources réelles, ex. `skills/03-game-design/gd-05-combat-designer/references/frame-data-and-attack-tokens.md`. |

## 3. Règles par domaine

### 3.1 Unreal Engine 5.8

| Ignoré | Pourquoi |
|---|---|
| `Binaries/`, `Intermediate/` | Sorties de compilation C++ / UBT, projet **et** plugins (motif valable à toute profondeur). |
| `DerivedDataCache/` | Cache local de shaders et d'assets dérivés, reconstruit par l'éditeur. |
| `Saved/` | Logs, autosaves, configs utilisateur, crash reports — propres au poste. |
| `ShaderDebugInfo/`, `Packaged/`, `ArchivedBuilds/`, `StagedBuilds/` | Sorties de debug et builds cookés. |
| `*.sln`, `*.vcxproj*`, `*.code-workspace`, `*.xcodeproj/`, `compile_commands.json` | Régénérés par *Generate Project Files*. |
| `.vs/`, `.idea/`, `*.suo`, `*.VC.db`, `*.DotSettings.user` | Caches IDE. |
| `*.uasset.tmp`, `*.umap.tmp` | Écritures d'assets interrompues. |

**Toujours suivis :** `*.uproject`, `*.uplugin`, `Content/`, `Config/`, `Source/`, `Plugins/` (hors leurs `Binaries/` et `Intermediate/`), `Build/`, `.vsconfig`.

### 3.2 Houdini 22

| Ignoré | Pourquoi |
|---|---|
| `*_bak[0-9]*.hip`, `.hiplc`, `.hipnc` | Sauvegardes automatiques (`$HIP/backup/<scène>_bakN.hip`). |
| `crash.*.hip*` | Scènes de récupération après plantage. |
| `*.bgeo`, `*.bgeo.*` (`.sc`, `.gz`…), `*.sim`, `*.simdata`, `*.vdb`, `*.pc` | Caches de géométrie, de simulation et de nuages de points. |
| `*.ifd`, `*.rat` | Scènes de rendu et textures mipmappées générées. |
| `*.abc.tmp`, `*.usd.tmp`, `flipbook/` | Exports intermédiaires et prévisualisations. |

**Toujours suivis :** `*.hip`, `*.hiplc`, `*.hipnc`, `*.hda`, `*.hdalc`, `*.hdanc`, `*.otl`, scripts Python/VEX.

**Convention `SourceArt/`** : un fichier volumineux qui doit être conservé (VDB de référence, bgeo de landmark…) est placé dans un dossier `SourceArt/`, à n'importe quelle profondeur. Les règles `!**/SourceArt/**/*.vdb` (et équivalents) le rendent alors toujours suivi.

Les fichiers `.abc`, `.fbx`, `.usd` ne sont **pas** ignorés : ce sont souvent des sources d'import Unreal. Voir § 5 pour leur stockage.

### 3.3 Développement logiciel

| Ignoré | Détail |
|---|---|
| Python | `__pycache__/`, `*.py[cod]`, `*.egg-info/`, `.venv/`, `venv/`, `env/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.tox/`, `.coverage*`, `htmlcov/` |
| Node | `node_modules/`, `npm-debug.log*`, `yarn-error.log*`, `.pnpm-store/` |
| Logs / temporaires | `*.log`, `logs/`, `*.tmp`, `*.temp`, `*.swp`, `*.swo`, `*~`, `~$*` (verrous Office) |
| Éditeurs | `.vscode/*` sauf `.vscode/extensions.json` (recommandations partagées) |
| Systèmes | `Thumbs.db`, `ehthumbs.db`, `desktop.ini`, `$RECYCLE.BIN/`, `.DS_Store`, `._*`, `.Spotlight-V100`, `.Trashes` |

### 3.4 ZAÏRE STUDIO OS

**Aucun dossier du framework n'est ignoré.** Sont suivis :

- `skills/` : les 57 `SKILL.md`, avec leurs `references/`, `templates/`, `examples/` et `scripts/` ;
- `knowledge/` : `entities-registry.csv`, `technical-specs/`, `world-bible/` ;
- `architecture/`, `research/`, `schemas/`, `templates/` ;
- `production/` : livrables de référence des scénarios ;
- `tools/`, `tests/` (avec `tests/fixtures/`) ;
- `audit/`, `docs/` ;
- `releases/` : les 70 archives ZIP (57 skills, 9 départements, archives complètes et plug-in). Ce sont des livrables importables dans Claude ; elles restent versionnées.

Seuls les caches Python (`__pycache__/`) de `tools/`, `tests/` et `skills/*/scripts/` sont exclus.

### 3.5 Secrets et configurations locales

| Ignoré | Exemples |
|---|---|
| Variables d'environnement | `.env`, `.env.*` — **sauf** `.env.example` (modèle partagé, sans valeurs réelles) |
| Clés et certificats | `*.pem`, `*.key`, `*.pfx`, `*.p12`, `*.keystore`, `*.jks`, `*.ppk`, `id_rsa*`, `id_ed25519*` |
| Identifiants | `credentials.json`, `service-account*.json`, `secrets.json`, `secrets.y(a)ml`, `*.secret` |
| Configs par poste | `*.local.json`, `*.local.ini`, `*.local.y(a)ml`, `.claude/settings.local.json`, `CLAUDE.local.md` |

Un `.gitignore` **n'efface pas** un fichier déjà commité. Si un secret a été commité, il faut le révoquer et le remplacer, puis le retirer de l'historique (`git filter-repo`) — l'exclure ne suffit pas.

## 4. Vérifier une règle

```bash
# Pourquoi ce fichier est-il ignoré ? (affiche la ligne du .gitignore responsable)
git check-ignore -v chemin/vers/fichier

# Lister tout ce qui est ignoré dans l'arbre de travail
git status --ignored

# Vérifier ce qui serait ajouté, sans rien ajouter
git add --dry-run -A .
```

Note : avec `-v`, `check-ignore` affiche aussi les règles de négation (`!…`). Une ligne qui commence par `!` signifie que le fichier est **suivi**.

## 5. Recommandations pour la suite

1. **Git LFS dès le premier asset binaire Unreal ou Houdini.** `*.uasset`, `*.umap`, `*.hip`, `*.hda`, `*.fbx`, `*.abc`, `*.usd`, `*.exr`, `*.png`, `*.wav`, `*.bnk`, `*.zip` doivent être suivis via un fichier `.gitattributes` LFS **avant** leur premier commit. Ce choix relève de l'hébergeur (quotas LFS) et doit être validé par la production.
2. **Fichiers sous NDA de plateforme** (SDK consoles, `Platforms/<Console>/`) : à ne versionner que dans un dépôt privé dont l'accès est conforme aux accords constructeurs.
3. **Tout nouvel outil** qui produit des fichiers dans le dépôt doit soit les ranger dans un dossier déjà ignoré, soit ajouter sa règle ici **et** dans `.gitignore`.
