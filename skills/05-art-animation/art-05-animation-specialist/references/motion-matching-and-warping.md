# Architecture UE5 Motion Matching, Motion Warping & URO (`ART-05`)

## 1. Seuils de Synchronisation Spatiale (`WLD-05` <-> `ART-05`)
| Action (`FGameplayTag`) | Hauteur Cible | Fenêtre Tolérance Motion Warping | Durée Animation |
| :--- | :--- | :--- | :--- |
| `Ability.Movement.Vault` (Franchissement bas) | `100 cm` | `90 cm à 110 cm` (Distance d'appel `<= 180 cm`) | `0.55 s (33 frames)` |
| `Ability.Movement.ClimbHigh` (Mur / Conteneur) | `220 - 240 cm` | `200 cm à 250 cm` | `1.10 s (66 frames)` |
| `Ability.Movement.LedgeGrab` (Saut d'accroche) | `280 cm` | `260 cm à 300 cm` | `0.85 s (51 frames)` |

## 2. Paliers d'Optimisation CPU (`PERF-CPU-ANIM <= 1.8 ms`)
- **0 à 15 m** : Tick `60 Hz`, Motion Matching complet + Control Rig Foot/Hand IK actif.
- **15 à 35 m** : Tick `30 Hz` (URO Skip 1 frame), IK désactivé.
- **35 à 80 m** : Tick `15 Hz` (URO Skip 3 frames), State Machine simplifiée.
- **> 80 m** : Vertex Animation Texture (VAT) sur Static Mesh (`AI-02`), `0.0 ms` CPU squelettique.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-05` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-05`, `GD-05`, `ART-06`
- **Audit des Entrées (`inputs`)** :
  - `spatial-metrics-wld-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-frame-data-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cleaned-mocap-art-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `animation-graph-specification.md` : Doit respecter le gabarit `templates/animation-graph-spec.md` et passer l'audit croisé.
  - `locomotion-and-warping-metrics.csv` : Doit respecter le gabarit `templates/animation-graph-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `GD-05`, `WLD-05`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Latence ressentie (> 100 ms) lors d'un demi-tour brusque en sprint ou en combat | Blocage / Dégradation si ignoré | Augmenter le poids de la réactivité d'input (Trajectory Weight) dans le Pose Search Schema et déclencher un Pivot Transition Montage | Escalade vers Concilier inertie réaliste et contrôle nerveux DIR-05 |
| Mode de Défaillance 2: Dépassement du budget CPU Animation (> 1.8 ms) dans une scène dense | Blocage / Dégradation si ignoré | Désactiver le Foot Placement Control Rig au-delà de 15m, passer les PNJ entre 15m et 30m à 30Hz (URO) et figer l'évaluation squelettique au-delà de 80m (bascule VAT AI-02) | Escalade vers Respecter PERF-CPU-ANIM |
| Mode de Défaillance 3: Obstacle de blockout situé à 105 cm au lieu de 100 cm | Blocage / Dégradation si ignoré | Autoriser le Motion Warping vertical dans la plage de tolérance [90 cm, 110 cm] sans déformer la vitesse d'animation | Escalade vers Garantir un franchissement sans accroc géométrique |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-05`)

- [ ] **Contrôle DoD #1** : Coût CPU Animation total `<= 1.8 ms` (60 FPS) / `<= 2.5 ms` (30 FPS) avec 100 % des mises à jour sur Worker Threads.
- [ ] **Contrôle DoD #2** : Alignement exact à la frame près entre les `AnimNotifies` et la table Frame Data de `GD-05`.
- [ ] **Contrôle DoD #3** : Zéro glissement des pieds sur les pentes en latérite de `DST-NGALIEMA` grâce au Control Rig Foot IK.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
