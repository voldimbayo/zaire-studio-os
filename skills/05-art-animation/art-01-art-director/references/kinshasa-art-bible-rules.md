# Charte Chromatique & PBR de Kinshasa (`ART-01`)

## 1. Palettes Officielles par Commune (`DST-*`)
| Commune | Dominante (60 %) | Secondaire (30 %) | Accent & Lumière (10 %) | Contraste & Humeur |
| :--- | :--- | :--- | :--- | :--- |
| `DST-GOMBE` | Béton Brut & Verre (`#7A8288`) | Acier Portuaire & Vert Fluvial (`#2F4F4F`) | LED Froide & Sangles Jaunes (`#F2C94C`) | Vertical, institutionnel, reflets humides. |
| `DST-MATONGE` | Ocre Latérite & Crépi Chaud (`#B85D3B`) | Turquoise & Enseignes Peintes (`#1B998B`) | Néons Ambre/Magenta (`#FF3366`, `#FF9F1C`) | Vibrante, polyphonique, nocturne électrique. |
| `DST-LIMETE` | Béton Monumental Patiné (`#6E6A66`) | Tôle Rouillée & Verdure (`#8C4A27`) | Sodium Industriel (`#FFB347`) | Massif, industriel, silhouettes sur ciel équatorial. |

## 2. Plage de Calibration PBR Obligatoire
- **BaseColor (Albédo sRGB)** : Interdiction de descendre sous `30 sRGB` (charbon/pneu = `35-45 sRGB`) ou de dépasser `240 sRGB` pour laisser travailler Lumen GI (`ART-07`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-01` — Strate DAG 1)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `WLD-02`, `WLD-03`
- **Audit des Entrées (`inputs`)** :
  - `creative-pillars-dir-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-research-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `urban-morphology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `art-bible-chapter.md` : Doit respecter le gabarit `templates/art-bible-template.md` et passer l'audit croisé.
  - `art-review-scorecard.md` : Doit respecter le gabarit `templates/art-bible-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-03`, `WLD-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Surcharge visuelle d'un décor de marché masquant les ennemis ou les points d'accroche parkour | Blocage / Dégradation si ignoré | Désaturer de 20 % l'arrière-plan haut (> 300 cm) et réserver la teinte jaune ocre haute saturation aux prises d'escalade et sangles de franchissement | Escalade vers Préserver la lisibilité gameplay WLD-05 |
| Mode de Défaillance 2: Teinte de peau d'un personnage paraissant terne ou grise sous l'éclairage de scène | Blocage / Dégradation si ignoré | Imposer une recalibration du Subsurface Scattering Profile (ART-03) et de la balance des blancs ACES (ART-07) | Escalade vers Appliquer cultural-guidelines.md Section 3 |
| Mode de Défaillance 3: Même palette chromatique utilisée entre la Gombe et Matonge | Blocage / Dégradation si ignoré | Forcer l'opposition : acier/cyan/béton froid pour DST-GOMBE vs ocre latérite/ambre/magenta chaud pour DST-MATONGE | Escalade vers Maintenir l'identité immédiate de chaque commune |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-01`)

- [ ] **Contrôle DoD #1** : Chaque commune `DST-*` dispose de ses codes couleurs hexadécimaux/linéaires PBR et de ses valeurs d'albédo min/max (`30-240 sRGB`).
- [ ] **Contrôle DoD #2** : La couleur d'affordance gameplay est strictement réservée aux éléments interactifs ou franchissables.
- [ ] **Contrôle DoD #3** : Validation d'authenticité obtenue auprès de `DIR-03` et `WLD-02`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
