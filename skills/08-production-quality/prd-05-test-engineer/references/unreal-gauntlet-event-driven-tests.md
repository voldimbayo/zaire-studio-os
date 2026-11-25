# Architecture des Tests Automatisés Gauntlet Sans Faux Positifs (`PRD-05`)

## 1. Règle d'Or Anti-Flakiness : Synchronisation Événementielle Pure
- **Interdit** : `AddCommand(new FDelayedFunctionLatentCommand(..., 3.0f));` (échoue si le disque ou le shader cache met 3.2s).
- **Obligatoire** : `AddCommand(new FZaireWaitForWorldPartitionIdleCommand(World));` suivi de `FZaireWaitForGameplayTagCommand(Actor, Tag)`.

## 2. Suite Nocturne Gauntlet (`ZaireNightlyAutomationSuite`)
| Suite ID | Type Gauntlet | Durée | Systèmes Couverts (`>= 80 %`) | Critère de Succès Bloquant |
| :--- | :--- | :--- | :--- | :--- |
| `GT_Smoke_BootAndPort` | `FunctionalTest` | `3.5 min` | `SYS-WLD-STREAMING`, `SYS-STEALTH`, `SYS-CMB-MELEE` | 100 % des assertions vertes, 0 crash. |
| `GT_Perf_KinshasaLoop` | `GauntletController` | `30 min` | `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS` | `P99 <= 16.6 ms` (`ENG-07`), `VRAM <= 6144 MB`. |
| `GT_Soak_2Hours_Traffic` | `EnduranceSoak` | `120 min` | Stabilité mémoire & Watchdog Anti-Deadlock `AI-03` | 0 deadlock routier `> 8s`, dérive RAM `< 1 %`. |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-05` — Strate DAG 5)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `PRD-04`, `ENG-07`, `ENG-08`
- **Audit des Entrées (`inputs`)** :
  - `qa-test-plans-prd-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `performance-budgets-eng-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `ci-cd-pipelines-eng-08` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `gauntlet-automation-spec.md` : Doit respecter le gabarit `templates/gauntlet-test-spec.md` et passer l'audit croisé.
  - `automated-test-suite-summary.csv` : Doit respecter le gabarit `templates/gauntlet-test-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `PRD-04`, `ENG-08`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Test automatisé échouant de manière aléatoire (Flaky Test > 2 % de faux positifs) sur la ferme CI | Blocage / Dégradation si ignoré | Remplacer immédiatement toute attente temporelle fixe par un abonnement au delegate d'achèvement du sous-système (ex: UWorldPartitionSubsystem::OnStreamingStateUpdated) | Escalade vers Ramener le taux de faux positifs sous la barre des 2 % |
| Mode de Défaillance 2: Couverture automatisée d'un nouveau système SYS-* inférieure à 80 % | Blocage / Dégradation si ignoré | Refuser le passage du système au jalon Beta/Gold et ajouter les AFunctionalTest manquants dans la map de test dédiée | Escalade vers Respecter le seuil obligatoire >= 80 % (quality-standards.md) |
| Mode de Défaillance 3: Bot Gauntlet détectant une hausse de consommation RAM/VRAM monotone (+50 MB/heure) pendant le test d'endurance de 2h | Blocage / Dégradation si ignoré | Émettre une alerte automatique de fuite mémoire (Memory Leak) vers ENG-01 et ENG-07 avec le diff d'allocations Unreal Insights | Escalade vers Bloquer le build nocturne |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-05`)

- [ ] **Contrôle DoD #1** : Couverture des systèmes critiques `SYS-*` par tests automatisés `>= 80 %`.
- [ ] **Contrôle DoD #2** : Taux de faux positifs (flakiness) `< 2 %` sur 50 exécutions CI consécutives (0 `Sleep` fixe).
- [ ] **Contrôle DoD #3** : Exécution automatique intégrée à l'étape 4 du BuildGraph `ENG-08`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
