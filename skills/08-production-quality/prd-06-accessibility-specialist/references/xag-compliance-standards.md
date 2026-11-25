# Référentiel de Conformité Xbox Accessibility Guidelines — XAG (`PRD-06`)

## 1. Grille des Exigences XAG Obligatoires pour ZAÏRE
| Code XAG | Domaine | Exigence Technique Impérative dans ZAÏRE STUDIO OS | Skills Impliqués |
| :--- | :--- | :--- | :--- |
| **XAG 101** | Contraste & Texte | Ratio de contraste `>= 4.5:1` (UI) et `>= 7.0:1` (Sous-titres), tolérance expansion `+35 %`, police Unicode (`ɛ`, `ɔ`). | `GD-07`, `AUD-04` |
| **XAG 102** | Daltonisme & Couleur | Zéro information codée par la couleur seule (Double codage Couleur + Forme/Icône + Filtres Deutéranopie/Protanopie/Tritanopie). | `GD-07`, `ART-01` |
| **XAG 104** | Sous-titres & Audio | Préfixe locuteur `[KOFFI]`, fond réglable (`50-100 %`), taille police `28-42 px`, radar visuel des sons critiques (`BUS_SFX_CombatTelegraph`). | `AUD-04`, `AUD-01`, `GD-07` |
| **XAG 107** | Accessibilité Motrice | Remapping complet `Enhanced Input`, bascule `Hold / Toggle` pour la course/visée, remplacement des QTE par maintien continu ou auto-succès. | `ENG-02`, `GD-05`, `GD-06` |
| **XAG 108** | Cognitif & Navigation | Rappel permanent de l'objectif `MSN-*` sur le téléphone diégétique et guidage visuel optionnel par les landmarks (`SYS-WLD-LANDMARKS`). | `GD-02`, `WLD-04`, `GD-07` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`PRD-06` — Strate DAG 5)

- **Gouvernance Production, QA, Télémétrie & Accessibilité XAG (UE 5.8)** (`SRC-020`, `SRC-030`, `SRC-031`) :
  - **Planification & Risques (`PRD-01`, `PRD-02`)** : Buffer d'aléas Open World de `15 %`, verrou *Blockout First*, cotation des risques $S = P \times I$ avec fallback obligatoire dès $S \ge 12/25$.
  - **Docs-as-Code (`PRD-03`) & QA Open World (`PRD-04`)** : Vérification automatisée du registre (`validate_registry.py`), tests destructifs anti-soft-lock par cellule `World Partition (128 m)`, reproductibilité `>= 90 %`.
  - **Tests Gauntlet & Télémétrie (`PRD-05`, `SYS-TELEMETRY-ANALYTICS`)** : Synchronisation 100 % événementielle (zéro `Sleep` fixe, faux positifs `< 2 %`), couverture des systèmes critiques `>= 80 %`, capture asynchrone (`< 0.1 ms CPU`) des heatmaps de FPS P99, blocages et flux économiques.
  - **Accessibilité Universelle (`PRD-06`, `SRC-031`)** : Conformité XAG 101/102/104/107/108 (contraste `>= 4.5:1` UI / `>= 7:1` sous-titres, double codage forme+couleur, maintien `Hold` remplaçant les QTE).

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-07`, `GD-05`, `AUD-04`
- **Audit des Entrées (`inputs`)** :
  - `ui-screen-specs-gd-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-design-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `localization-tables-aud-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `xag-compliance-matrix.csv` : Doit respecter le gabarit `templates/xag-compliance-matrix.csv` et passer l'audit croisé.
  - `accessibility-audit-report.md` : Doit respecter le gabarit `templates/xag-compliance-matrix.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-07`, `GD-07`, `AUD-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Séquence de lutte au corps-à-corps ou de crochetage exigeant un martèlement rapide de bouton (Button Mashing) | Blocage / Dégradation si ignoré | Imposer l'intégration native de l'option 'QTE Input Mode : Tap / Hold / Auto-Complete' dans Enhanced Input (ENG-02) | Escalade vers Respecter XAG 107 et quality-standards.md Section 2.D |
| Mode de Défaillance 2: Alarme d'attaque lourde ennemie transmise uniquement par un signal sonore (AUD-02) | Blocage / Dégradation si ignoré | Ajouter un indicateur visuel radial directionnel à fort contraste autour de Koffi synchronisé sur le Startup de l'attaque (>= 22 frames) | Escalade vers Assurer une jouabilité complète pour les joueurs sourds ou malentendants |
| Mode de Défaillance 3: Sous-titre dépourvu du nom du locuteur ou fond transparent illisible sous le soleil équatorial de midi | Blocage / Dégradation si ignoré | Forcer le format '[LOCUTEUR] : Texte' et un fond sombre semi-opaque par défaut à 78 % d'opacité (ratio contraste >= 7:1) | Escalade vers Garantir la validation de check_xag_compliance.py |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`PRD-06`)

- [ ] **Contrôle DoD #1** : `python skills/08-production-quality/prd-06-accessibility-specialist/scripts/check_xag_compliance.py` retourne un code `0`.
- [ ] **Contrôle DoD #2** : Les 4 piliers XAG (Visuel, Auditif, Moteur, Cognitif) sont couverts et validés sans exception.
- [ ] **Contrôle DoD #3** : L'écran de configuration d'accessibilité est présenté dès le premier démarrage du jeu (*First-Boot Flow*).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
