# Méthodologie de Planification Hybride Open World (`PRD-01`)

## 1. Chaîne Critique d'un Lieu ou d'une Mission (`LOC-*` / `MSN-*`)
1. **Sprint N-1 (Fondations Strates 1-2)** : Recherche `WLD-02`/`WLD-03` -> Design `GD-02` + Script `NAR-02` -> Blockout `WLD-05` -> Validation Playtest `DIR-05`.
2. **Sprint N (Production Strate 3)** : Environment Brief `WLD-06` -> Kits 3D `ART-02` + IA `AI-01`/`AI-02` + Dialogues/Barks `NAR-04` + SFX `AUD-02`.
3. **Sprint N+1 (Intégration & Gatekeeping Strates 4-5)** : Éclairage `ART-07` + VFX `ART-09` + Profilage P99 `ENG-07` + Tests Gauntlet `PRD-05` + Certification `DIR-06`/`DIR-07`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-01` — Strate DAG 1)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-01`, `DIR-02`
- **Audit des Entrées (`inputs`)** :
  - `orchestration-dag-dir-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `milestone-targets-dir-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `architecture/skill-dependencies.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `sprint-execution-plan.md` : Doit respecter le gabarit `templates/sprint-plan-template.md` et passer l'audit croisé.
  - `department-raci-matrix.csv` : Doit respecter le gabarit `templates/sprint-plan-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-01`, `DIR-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Tâche d'Environment Art (ART-02) planifiée dans le même sprint que le blockout Level Design (WLD-05) du même lieu | Blocage / Dégradation si ignoré | Décaler la production ART-02 au sprint N+1 : le sprint N est consacré au blockout WLD-05 et à sa validation playtest DIR-05 | Escalade vers Appliquer strictement la règle Blockout First |
| Mode de Défaillance 2: Blocage de plus de 24h sur une dépendance RESEARCH_REQUIRED (ex: WLD-02/WLD-03) | Blocage / Dégradation si ignoré | Basculer la capacité du département aval sur une commune CONFIRMED (ex: DST-GOMBE ou DST-MATONGE) pendant que la recherche aboutit | Escalade vers Éviter tout temps mort sur le chemin critique |
| Mode de Défaillance 3: Consommation complète du buffer de 15 % avant la fin de la première semaine du sprint | Blocage / Dégradation si ignoré | Déclencher une alerte précoce vers DIR-02 et PRD-02 pour déprioriser les tâches P2 du sprint | Escalade vers Garantir un taux de complétion des engagements P0 >= 90 % |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-01`)

- [ ] **Contrôle DoD #1** : Chaque tâche du sprint possède un unique skill `Responsible (R)` et respecte l'ordre DAG.
- [ ] **Contrôle DoD #2** : Un buffer de capacité de `15 %` est explicitement provisionné.
- [ ] **Contrôle DoD #3** : Aucun livrable `ART-02` n'est planifié sans un blockout `WLD-05` préalablement validé.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
