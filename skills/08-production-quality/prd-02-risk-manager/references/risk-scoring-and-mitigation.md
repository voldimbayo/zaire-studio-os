# Méthodologie de Cotation & Mitigation des Risques AAA (`PRD-02`)

## 1. Grille de Criticité ($S = P 	imes I$)
- **Probabilité ($1..5$)** : `1` = Rare (<10%), `3` = Possible (40-60%), `5` = Quasi-certain (>85%).
- **Impact ($1..5$)** : `1` = Mineur, `3` = Retard de sprint / Dégradation FPS locale, `5` = Blocage Jalon / Crash / Litige juridique ou rejet culturel.
- **Seuil d'Action Obligatoire** : Tout score **`>= 12`** déclenche une mesure de contingence immédiate intégrée au DAG de `DIR-01`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-02` — Strate DAG 1)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-02`, `DIR-04`, `WLD-02`
- **Audit des Entrées (`inputs`)** :
  - `research-gaps-phase-1` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `technical-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-briefs-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `risk-register.csv` : Doit respecter le gabarit `templates/risk-register-template.csv` et passer l'audit croisé.
  - `critical-risk-mitigation-plan.md` : Doit respecter le gabarit `templates/risk-register-template.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-02`, `DIR-04`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Risque de strike DMCA / expiration de licence sur les musiques de Radio Lokole (Score 4x4 = 16/25) | Blocage / Dégradation si ignoré | Exiger d'AUD-03 qu'un Switch Wwise SW_Music_LicenseMode bascule à 100 % sur des compositions originales du studio en mode Streamer Safe | Escalade vers Neutraliser l'impact juridique et commercial |
| Mode de Défaillance 2: Couverture SIG/OSM hétérogène dans les communes secondaires comme DST-MASINA (Score 4x3 = 12/25) | Blocage / Dégradation si ignoré | Isoler DST-MASINA en statut RESEARCH_REQUIRED hors du Vertical Slice et utiliser le générateur de subdivision paramétrique WLD-03/ENG-04 | Escalade vers Protéger le planning du Vertical Slice DIR-02 |
| Mode de Défaillance 3: Risque de dépassement du budget CPU/GPU dans les marchés denses sous la pluie (Score 3x5 = 15/25) | Blocage / Dégradation si ignoré | Activer le délestage dynamique : réduction de 40 % de la foule en plein air sous l'averse (AI-02) et bascule automatique des réflexions Lumen sur Surface Cache > 0.40 Roughness (ENG-06) | Escalade vers Garantir le maintien des 60 FPS (16.6 ms) |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-02`)

- [ ] **Contrôle DoD #1** : 100 % des lacunes de `research/research-gaps.md` sont couvertes par une entrée dans `risk-register.csv`.
- [ ] **Contrôle DoD #2** : 100 % des risques ayant un score `>= 12/25` possèdent un plan de mitigation et un fallback opérationnel.
- [ ] **Contrôle DoD #3** : Chaque risque est rattaché à un skill propriétaire unique (`WLD-03`, `AUD-03`, `ENG-07`, etc.).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
