# Méthodologie QA par Quadrillage Open World & Tests Destructifs (`PRD-04`)

## 1. Classification des Sévérités d'Anomalies ZAÏRE STUDIO OS
- **`SEV-A (Blocker / Passage en BLOCKED immédiat)`** : Crash moteur, OOM VRAM (`> 6144 MB`), Soft-Lock de quête principal ou secondaire, perte de sauvegarde, chute à travers le sol.
- **`SEV-B (Critical)`** : Frametime P99 `> 16.6 ms` sur un parcours principal, blocage du trafic `AI-03` non résolu après `8 s`, absence de préfixe locuteur ou troncature UI (`AUD-04`/`PRD-06`).
- **`SEV-C (Major)`** : Artefact visuel Nanite/Lumen, couture de texture visible, bark désynchronisé.
- **`SEV-D (Minor / Polish)`** : Détail cosmétique mineur hors chemin principal.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-04` — Strate DAG 5)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-02`, `WLD-04`, `ENG-02`
- **Audit des Entrées (`inputs`)** :
  - `mission-design-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `open-world-grid-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gameplay-cpp-specs-eng-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `master-qa-test-plan.md` : Doit respecter le gabarit `templates/qa-test-plan-template.md` et passer l'audit croisé.
  - `deterministic-bug-report.json` : Doit respecter le gabarit `templates/qa-test-plan-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-07`, `PRD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Rapport de bug intermittent avec un taux de reproduction < 90 % | Blocage / Dégradation si ignoré | Exiger la capture automatique du Snapshot d'État (Coordonnées X/Y/Z cm, GlobalSeed, GameplayTags actifs, DataLayers chargés) avant validation du ticket | Escalade vers Atteindre le standard de reproductibilité >= 90 % (quality-standards.md) |
| Mode de Défaillance 2: Détection d'un cas où la destruction de la moto Wewa bloque la progression d'une quête sans alternative | Blocage / Dégradation si ignoré | Classer l'anomalie en SEV-A (Blocker), marquer la mission BLOCKED et assigner le correctif de machine à états à GD-02 | Escalade vers Appliquer la tolérance zéro sur les soft-locks |
| Mode de Défaillance 3: Scénario de test répétitif validé manuellement à chaque build (ex: traversée Gombe -> Matonge) | Blocage / Dégradation si ignoré | Transférer le cas de test à PRD-05 pour conversion en test de non-régression nocturne automatisé Gauntlet | Escalade vers Maximiser la couverture automatisée >= 80 % |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-04`)

- [ ] **Contrôle DoD #1** : 100 % des étapes de la machine à états de mission (`GD-02`) sont couvertes par un cas de test nominal ET un cas de test destructif (interruption/fuite/perte véhicule).
- [ ] **Contrôle DoD #2** : Taux de reproductibilité des rapports d'anomalies `>= 90 %`.
- [ ] **Contrôle DoD #3** : Couverture spatiale de 100 % des cellules World Partition actives du jalon.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
