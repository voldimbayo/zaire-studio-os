# Paramétrage Simcade des Véhicules Kinois sous UE5 Chaos (`GD-06`)

## 1. Profils Physiques de Référence
| ID Véhicule | Masse (kg) | Gabarit L × l × H (cm) | Vitesse Max (km/h) | 0-60 km/h (s) | Rayon Braquage (m) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `VEH-MOTO-WEWA-01` | `135 kg` (210 avec pilote) | `205 × 80 × 115` | `95 km/h` | `3.2 s` | `2.4 m` |
| `VEH-TAXI-JAUNE-01` | `1 180 kg` | `440 × 180 × 150` | `125 km/h` | `5.8 s` | `5.1 m` |
| `VEH-BUS-TRANSCO-01` | `11 500 kg` | `1200 × 255 × 330` | `80 km/h` | `12.5 s` | `10.8 m` |

## 2. Matrice de Friction par Surface (`ChaosPhysicalMaterial`)
- `PM_Asphalt_Dry` : Friction Latérale = `1.20`, Friction Longitudinale = `1.15`.
- `PM_Asphalt_Wet` (`World.Weather.TropicalStorm`) : Friction Latérale = `0.90`, Longitudinale = `0.88`.
- `PM_Laterite_Dry` (`DST-KALAMU`) : Friction Latérale = `0.95`, Longitudinale = `0.92`.
- `PM_Laterite_Mud` (`World.Weather.TropicalStorm`) : Friction Latérale = `0.78`, Longitudinale = `0.75`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-06` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-03`, `GD-01`, `DIR-05`
- **Audit des Entrées (`inputs`)** :
  - `urban-typology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lead-gd-directives-dir-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `vehicle-handling-spec.md` : Doit respecter le gabarit `templates/vehicle-handling-spec.md` et passer l'audit croisé.
  - `surface-friction-matrix.csv` : Doit respecter le gabarit `templates/vehicle-handling-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `ENG-05`, `AI-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Moto VEH-MOTO-WEWA-01 chutant trop facilement lors des contacts légers à basse vitesse dans le trafic dense | Blocage / Dégradation si ignoré | Activer un couple gyroscopique d'auto-stabilisation assistée sous 35 km/h et relever le seuil d'éjection ragdoll Chaos à un impact frontal > 55 km/h | Escalade vers Privilégier le plaisir de slalom urbain simcade sur la frustration punitive |
| Mode de Défaillance 2: Transition de surface par temps de pluie (World.Weather.TropicalStorm) rendant la moto incontrôlable | Blocage / Dégradation si ignoré | Plafonner la perte d'adhérence latérale à -25 % sur asphalte mouillé et -35 % sur boue latéritique avec retour haptique progressif | Escalade vers Synchroniser avec ENG-05 et AUD-02 (RTPC crissement/éclaboussure) |
| Mode de Défaillance 3: Véhicule lourd (VEH-BUS-TRANSCO-01) incapable de négocier les ronds-points kinois | Blocage / Dégradation si ignoré | Ajuster l'angle de braquage maximal à basse vitesse à 38 degrés sur les voies de 380-400 cm | Escalade vers Valider la trajectoire spline avec AI-03 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-06`)

- [ ] **Contrôle DoD #1** : Chaque véhicule `VEH-*` dispose de ses dimensions en cm, de sa masse en kg, de sa vitesse de pointe et de ses coefficients de friction sur les 4 surfaces.
- [ ] **Contrôle DoD #2** : La différenciation de prise en main entre une moto Wewa agile (`135 kg`) et un bus lourd (`11 500 kg`) est immédiate.
- [ ] **Contrôle DoD #3** : Les seuils d'éjection et de collision sont validés avec `ENG-05` (Chaos Physics).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
