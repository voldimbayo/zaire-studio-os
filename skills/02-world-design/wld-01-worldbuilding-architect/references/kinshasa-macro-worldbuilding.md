# Principes de Worldbuilding Macroscopique — Kinshasa (`WLD-01`)

## 1. Contraste des Strates Urbaines
- **Axe Fluvial & Institutionnel (`DST-GOMBE`)** : Pouvoir financier, ambassades, port lourd ONATRA (`LOC-GOMBE-PORT`), boulevards à 2x3 voies (`LOC-GOMBE-BD30JUIN`).
- **Cœur Culturel & Commercial (`DST-MATONGE` / `DST-KALAMU`)** : Économie créative, studios, ngandas, marchés denses, ateliers mécaniques (`FAM-KABONGO`).
- **Colonne Vertébrale Industrielle (`DST-LIMETE`)** : Usines, dépôts logistiques, carrefour monumental de la Tour de l'Échangeur (`LOC-LIMETE-ECHANGEUR`).
- **Flancs Fluviaux Occidentaux (`DST-NGALIEMA`)** : Relief prononcé, rapides de Kinsuka, carrières et zones résidentielles.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-01` — Strate DAG 1)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `WLD-02`, `WLD-03`
- **Audit des Entrées (`inputs`)** :
  - `creative-pillars-dir-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-research-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `urban-morphology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `district-profile.md` : Doit respecter le gabarit `templates/district-profile-template.md` et passer l'audit croisé.
  - `kinshasa-world-bible-update.md` : Doit respecter le gabarit `templates/district-profile-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `WLD-02`, `WLD-03`, `DIR-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Commune dont les données SIG secondaires sont incomplètes (ex: DST-MASINA) | Blocage / Dégradation si ignoré | Maintenir explicitement le statut RESEARCH_REQUIRED sur les sous-secteurs non vérifiés | Escalade vers Transmettre une requête ciblée à WLD-03 |
| Mode de Défaillance 2: Deux communes présentent la même densité de foule et la même ambiance visuelle | Blocage / Dégradation si ignoré | Accentuer le contraste structurel (ex: tours administratives et port industriel de Gombe vs galeries musicales et marchés nocturnes de Matonge) | Escalade vers Faire valider la différenciation par DIR-03 et ART-01 |
| Mode de Défaillance 3: Introduction d'une nouvelle faction dans un quartier | Blocage / Dégradation si ignoré | Vérifier la cohérence territoriale avec NAR-05 et mettre à jour les dépendances dans entities-registry.csv | Escalade vers Soumettre à DIR-06 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-01`)

- [ ] **Contrôle DoD #1** : Chaque fiche `DST-*` définit clairement ses communes limitrophes, son landmark directeur (`LOC-*`) et ses densités cibles de foule/trafic.
- [ ] **Contrôle DoD #2** : Alignement total avec `knowledge/world-bible/kinshasa-districts.md` et `cultural-guidelines.md`.
- [ ] **Contrôle DoD #3** : Validation créative obtenue auprès de `DIR-03`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
