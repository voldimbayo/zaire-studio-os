# Méthodologie Blockout First & Gabarits UE5 (`WLD-05`)

## 1. Tableau Récapitulatif des Cotes Obligatoires (`spatial-metrics.md`)
| Élément Géométrique | Cote Cible (cm) | Seuil Minimal Absolu | Justification Gameplay / Caméra |
| :--- | :--- | :--- | :--- |
| Largeur Couloir Jouable | `400 cm` | `350 cm` | Croisement 2 PNJ + rotation caméra SpringArm sans clipping. |
| Largeur Arène Mêlée (`GD-05`) | `600 cm` | `500 cm` | Espace requis pour esquives et gestion de 2 Attack Tokens. |
| Hauteur Sous Plafond | `360 cm` | `320 cm` | Évite l'écrasement vertical de la caméra 3e personne. |
| Couvert Bas (Vault / Crouch) | `100 cm` | `90 - 110 cm` | Alignement exact avec `Ability.Movement.Vault` (`ART-05`). |
| Couvert Haut (Full Cover) | `220 cm` | `200 cm` | Occultation complète de la capsule `180 cm`. |
| Inter-file Moto Wewa | `150 cm` | `130 cm` | Passage fluide de `VEH-MOTO-WEWA-01` (largeur 80 cm). |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-05` — Strate DAG 2)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-04`, `GD-02`, `GD-05`, `DIR-05`
- **Audit des Entrées (`inputs`)** :
  - `poi-specs-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `mission-design-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-metrics-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/technical-specs/spatial-metrics.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `level-blockout-brief.md` : Doit respecter le gabarit `templates/level-blockout-brief.md` et passer l'audit croisé.
  - `blockout-metrics-validation.json` : Doit respecter le gabarit `templates/level-blockout-brief.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `AI-01`, `WLD-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Couloir ou passage intérieur < 350 cm détecté par check_spatial_metrics.py | Blocage / Dégradation si ignoré | Élargir immédiatement le volume géométrique à >= 350 cm avant toute validation | Escalade vers Éliminer les collisions de SpringArm caméra 3e personne |
| Mode de Défaillance 2: Arène de combat dépourvue d'options de flanquement ou de verticalité | Blocage / Dégradation si ignoré | Ajouter au moins une boucle de circulation latérale et un point d'élévation accessible en vault (100 cm) ou ledge grab (280 cm) | Escalade vers Synchroniser avec GD-05 et AI-01 (requêtes EQS) |
| Mode de Défaillance 3: Demande d'habillage artistique anticipé par ART-02 sur un blockout non validé | Blocage / Dégradation si ignoré | Refuser le handoff en vertu de la règle Blockout First (quality-standards.md) | Escalade vers Maintenir le verrou jusqu'au feu vert DIR-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-05`)

- [ ] **Contrôle DoD #1** : `python skills/02-world-design/wld-05-level-designer/scripts/check_spatial_metrics.py` retourne un code `0`.
- [ ] **Contrôle DoD #2** : Chaque arène supporte les approches prévues par `GD-02` (infiltration, mêlée/tir, fuite) sans cul-de-sac involontaire.
- [ ] **Contrôle DoD #3** : Les volumes NavMesh, Smart Links et zones d'occlusion sont explicitement balisés.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
