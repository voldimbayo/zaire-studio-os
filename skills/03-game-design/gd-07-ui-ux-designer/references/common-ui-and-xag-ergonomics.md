# Architecture UE5 Common UI & Ergonomie Accessible (`GD-07`)

## 1. Hiérarchie des Couches (`UCommonActivatableWidget` Stack)
- `UI.Layer.HUD` : Jauge d'endurance/santé contextuelle (masquée à 100 % hors combat), boussole discrète de landmarks (`SYS-WLD-LANDMARKS`), sous-titres enrichis.
- `UI.Layer.DiegeticPhone` : Téléphone portable de Koffi consultable en temps réel sans couper le monde (SMS d'Amina `CHR-ALLY-AMINA`, tuner `ORG-RADIO-KIN`, carte par commune `DST-*`).

## 2. Normes Typographiques & Accessibilité (`PRD-06` / `AUD-04`)
- **Glyphes Obligatoires** : Support natif de `ɛ`, `Ɛ`, `ɔ`, `Ɔ` et des diacritiques tonals (`á`, `é`, `ɛ́`, `ɔ́`).
- **Taille Minimale Police TV/Console (1080p réf)** : `24 px` pour le corps d'interface, `28 px` à `42 px` (réglable) pour les sous-titres avec préfixe locuteur `[KOFFI]` et fond noir opacité `60-85 %`.
- **Tolérance d'Expansion** : `+35 %` de longueur de chaîne sur tous les boutons, notifications et objectifs.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-07` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-01`, `GD-02`, `ART-01`
- **Audit des Entrées (`inputs`)** :
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `mission-design-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `art-bible-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `xag-requirements-prd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `ui-screen-specification.md` : Doit respecter le gabarit `templates/ui-screen-spec-template.md` et passer l'audit croisé.
  - `common-ui-navigation-flow.md` : Doit respecter le gabarit `templates/ui-screen-spec-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `PRD-06`, `AUD-04`, `DIR-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Information transmise uniquement par la couleur (ex: jauge ou icône rouge vs verte) | Blocage / Dégradation si ignoré | Ajouter immédiatement une différenciation géométrique (losange hachuré vs cercle plein) et une option de palette daltonisme (Deutéranopie, Protanopie, Tritanopie) | Escalade vers Respecter l'exigence obligatoire XAG (quality-standards.md) |
| Mode de Défaillance 2: Conteneur UI fixe tronquant une chaîne traduite avec expansion de +35 % | Blocage / Dégradation si ignoré | Remplacer la largeur fixe par un conteneur dynamique Auto-Wrap avec marge de sécurité de +35 % sans défilement horizontal | Escalade vers Synchroniser avec AUD-04 |
| Mode de Défaillance 3: Élément HUD restant affiché en permanence hors combat ou navigation active | Blocage / Dégradation si ignoré | Passer le widget en mode Dynamic Auto-Hide (disparition en fondu après 4 secondes d'inactivité) | Escalade vers Préserver l'immersion visuelle dans Kinshasa (DIR-03 / ART-01) |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-07`)

- [ ] **Contrôle DoD #1** : 100 % des widgets supportent une expansion de texte de `+35 %` et affichent correctement `ɛ` et `ɔ`.
- [ ] **Contrôle DoD #2** : Contraste typographique mesuré `>= 4.5:1` (texte standard) et `>= 7:1` (sous-titres sur fond semi-opaque).
- [ ] **Contrôle DoD #3** : Navigation complète au pavé directionnel/manette et clavier/souris via les Input Action Tables de UE5 Common UI.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
