# Frame Data (60 FPS) & Régulation par Attack Tokens (`GD-05`)

## 1. Standards de Frame Data à 60 FPS (`1 frame = 16.66 ms`)
| Action (`FGameplayTag`) | Startup (Frames) | Active (Frames) | Recovery (Frames) | Hitstop (ms) | Cancel Window |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `Ability.Melee.LightAttack` (Mains nues) | `9 f (150 ms)` | `4 f (66 ms)` | `11 f (183 ms)` | `40 ms` | Frame 16 -> Parade/Esquive |
| `Ability.Melee.LightAttack` (`ITM-WPN-MACHETTE`) | `12 f (200 ms)` | `5 f (83 ms)` | `14 f (233 ms)` | `55 ms` | Frame 20 -> Parade/Esquive |
| `Ability.Melee.HeavyAttack` (`ITM-WPN-MACHETTE`) | `24 f (400 ms)` | `6 f (100 ms)` | `20 f (333 ms)` | `90 ms` | Non annulable pendant Active |
| `State.Character.Combat.Parrying` | `3 f (50 ms)` | `12 f (200 ms)` | `10 f (166 ms)` | `85 ms` | Contre-attaque immédiate sur succès |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-05` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-01`, `DIR-05`
- **Audit des Entrées (`inputs`)** :
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lead-gd-directives-dir-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `animation-metrics-art-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `combat-design-bible.md` : Doit respecter le gabarit `templates/combat-archetype-template.md` et passer l'audit croisé.
  - `weapon-and-archetype-matrix.csv` : Doit respecter le gabarit `templates/combat-archetype-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `ENG-02`, `AI-01`, `ART-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Attaque ennemie avec un Startup < 18 frames (300 ms à 60 FPS) | Blocage / Dégradation si ignoré | Allonger l'animation d'anticipation à >= 22 frames (366 ms) avec un indice sonore clair (AUD-02) et visuel | Escalade vers Garantir une réaction humaine équitable et conforme à l'accessibilité PRD-06 |
| Mode de Défaillance 2: Combat déclenché dans un espace de largeur < 500 cm | Blocage / Dégradation si ignoré | Restreindre dynamiquement le plafond d'Attack Tokens à 1 seul assaillant actif et activer les animations de combat rapproché mural | Escalade vers Prévenir toute désorientation caméra |
| Mode de Défaillance 3: Latence mesurée entre l'input joueur et la première frame d'esquive/parade > 100 ms | Blocage / Dégradation si ignoré | Autoriser l'annulation (Animation Cancel) des 6 dernières frames de Recovery des attaques légères par la parade ou l'esquive | Escalade vers Maintenir la réactivité nerveuse exigée par DIR-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-05`)

- [ ] **Contrôle DoD #1** : Toutes les attaques spécifient leurs frames Startup / Active / Recovery à 60 FPS et leur durée de Hitstop en ms.
- [ ] **Contrôle DoD #2** : La règle des Attack Tokens (max 2 jetons simultanés) est explicitement paramétrée pour `AI-01`.
- [ ] **Contrôle DoD #3** : Chaque arme ou capacité est reliée à un identifiant `ITM-*` et un tag `Ability.Melee.*` ou `State.Character.Combat.*`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
