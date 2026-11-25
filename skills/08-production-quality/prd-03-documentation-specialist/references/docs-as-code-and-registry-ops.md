# Procédures Docs-as-Code & Maintenance du Registre (`PRD-03`)

## 1. Les 11 Colonnes Obligatoires de `knowledge/entities-registry.csv`
1. `id` : Identifiant ASCII majuscule (`^(CHR|FAM|ORG|DST|LOC|MSN|ITM|VEH|SYS)-[A-Z0-9-]+$`).
2. `category` : `CHARACTER`, `FAMILY`, `ORGANIZATION`, `DISTRICT`, `LOCATION`, `MISSION`, `ITEM`, `VEHICLE`, `SYSTEM`.
3. `name` : Nom lisible complet.
4. `district_id` : `DST-*` ou `GLOBAL`.
5. `status` : `CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`.
6. `owner_skill` : Code du skill propriétaire (`NAR-03`, `WLD-01`, `GD-02`...).
7. `validated_by` : Liste des valideurs séparés par `|` (`DIR-03|DIR-06`).
8. `dependencies` : Liste des IDs prérequis séparés par `|`.
9. `sources` : Références `SRC-*` issues de `research/source-registry.csv`.
10. `last_updated` : Date ISO `YYYY-MM-DD`.
11. `summary` : Description opérationnelle concise.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-03` — Strate DAG 5)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-05`, `WLD-01`, `GD-01`, `ENG-01`
- **Audit des Entrées (`inputs`)** :
  - `all-department-handoff-packets` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/entities-registry.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `research/source-registry.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `registry-update-patch.csv` : Doit respecter le gabarit `templates/entity-registry-entry.md` et passer l'audit croisé.
  - `documentation-traceability-report.md` : Doit respecter le gabarit `templates/entity-registry-entry.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-06`, `DIR-01`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Handoff Packet mentionnant un lieu 'LOC-PORT-KIN' alors que l'ID officiel du registre est 'LOC-GOMBE-PORT' | Blocage / Dégradation si ignoré | Rejeter le paquet pour Référence Fantôme et imposer l'alignement sur l'ID canonique LOC-GOMBE-PORT de entities-registry.csv | Escalade vers Maintenir l'unicité absolue de la Single Source of Truth |
| Mode de Défaillance 2: Nouvelle entité soumise sans champ summary ou sans owner_skill valide | Blocage / Dégradation si ignoré | Bloquer l'insertion dans entities-registry.csv jusqu'à complétion des 11 colonnes obligatoires du schéma | Escalade vers Garantir que validate_registry.py passe à 100 % |
| Mode de Défaillance 3: Spécification technique s'appuyant sur une méthode GDC ou UE5 | Blocage / Dégradation si ignoré | Vérifier que le code source SRC-001..SRC-020 de research/source-registry.csv est explicitement cité dans la colonne sources | Escalade vers Assurer la traçabilité documentaire de Phase 1 à Phase 3 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-03`)

- [ ] **Contrôle DoD #1** : `python tools/validate_registry.py` s'exécute avec 0 erreur.
- [ ] **Contrôle DoD #2** : 100 % des entités citées dans les livrables sont indexées dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle DoD #3** : Aucun lien relatif cassé dans les fichiers Markdown du dépôt.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
