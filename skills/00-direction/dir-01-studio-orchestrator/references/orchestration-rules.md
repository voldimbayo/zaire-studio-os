# Règles d'Orchestration & Tri Topologique (`DIR-01`)

## 1. Protocole en 6 Phases
1. **INTAKE** : Lecture de `knowledge/entities-registry.csv`. Vérification des préfixes (`CHR-`, `FAM-`, `ORG-`, `DST-`, `LOC-`, `MSN-`, `ITM-`, `VEH-`, `SYS-`).
2. **PLANNING** : Calcul des strates 0 à 5. Aucun skill de Strate $N$ ne peut s'exécuter avant la complétion de ses dépendances amont de Strate $< N$.
3. **DISPATCH** : Envoi de la `Task Envelope` JSON.
4. **HANDOFF** : Réception du `Handoff Packet` Markdown.
5. **GATEKEEPING** : Contrôle par `NAR-06` (Continuité), `ENG-07` (Performance), `PRD-04` (QA) et `PRD-06` (Accessibilité XAG).
6. **CONSOLIDATION** : Mise à jour de `knowledge/entities-registry.csv` via `PRD-03` et validation finale `DIR-06`/`DIR-07`.

## 2. Plafonds Techniques Impératifs à Injecter dans `constraints`
- `target_frametime_ms` : `16.6` (Mode Performance 60 FPS) ou `33.3` (Mode Qualité 30 FPS).
- `max_npc_active` : `24` acteurs `AI-01` (au-delà, utiliser `AI-02` Mass Crowd jusqu'à 600+ entités).
- `min_corridor_width_cm` : `350` cm.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-01` — Strate DAG 0)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : Aucune (Racine Strate 0)
- **Audit des Entrées (`inputs`)** :
  - `user-request` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/entities-registry.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `architecture/skill-dependencies.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `execution-plan-dag.json` : Doit respecter le gabarit `templates/execution-plan-dag.json` et passer l'audit croisé.
  - `task-envelopes.json` : Doit respecter le gabarit `templates/execution-plan-dag.json` et passer l'audit croisé.
  - `consolidated-brief.md` : Doit respecter le gabarit `templates/execution-plan-dag.json` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-06`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Entité requise absente du registre | Blocage / Dégradation si ignoré | Créer un ID provisoire au statut PROPOSED ou RESEARCH_REQUIRED et router vers le skill propriétaire (WLD-01, NAR-03, GD-02...) | Escalade vers Refuser toute génération avec un nom libre sans ID normalisé |
| Mode de Défaillance 2: Entité critique au statut BLOCKED ou DEPRECATED | Blocage / Dégradation si ignoré | Suspendre la branche dépendante du DAG et notifier immédiatement l'utilisateur | Escalade vers Convoquer le collège de direction (DIR-02, DIR-03, DIR-04) |
| Mode de Défaillance 3: Dépassement de budget CPU/GPU détecté en Vague 3/4 | Blocage / Dégradation si ignoré | Ouvrir une boucle d'arbitrage DIR-04 + DIR-05 (ex: basculer le surplus de PNJ AI-01 vers AI-02 Mass Crowd) | Escalade vers Marquer le livrable BLOCKED tant que P99 > 16.6 ms |
| Mode de Défaillance 4: Un skill génère une section hors de son périmètre (Scope Violation) | Blocage / Dégradation si ignoré | Tronquer la section hors périmètre et émettre une Task Envelope vers le skill légitime | Escalade vers Consigner l'alerte SCOPE_GUARD dans le rapport d'orchestration |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-01`)

- [ ] **Contrôle DoD #1** : 100 % des sous-tâches sont assignées à un skill unique identifié par son code (`NAR-01`..`PRD-06`).
- [ ] **Contrôle DoD #2** : Le graphe d'exécution en vagues est un DAG strict (0 cycle vérifié par `scripts/build_dag_plan.py`).
- [ ] **Contrôle DoD #3** : Chaque Task Envelope inclut explicitement les entités du registre et l'enveloppe frametime UE5.
- [ ] **Contrôle DoD #4** : La synthèse finale distingue clairement les éléments `CONFIRMED`, `PROPOSED` et `RESEARCH_REQUIRED`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
