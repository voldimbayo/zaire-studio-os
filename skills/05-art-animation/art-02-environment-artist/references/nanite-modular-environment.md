# Production Environnementale Modulaire Nanite & RVT (`ART-02`)

## 1. Standards de Kits Modulaires Kinois
- **Grille de Snapping** : `100 cm`, `200 cm`, `400 cm` (hauteur d'étage standard = `400 cm` RDC commercial, `350 cm` étages).
- **Texel Density** : `10.24 px/cm` (0 à 3 m) -> `2048 × 2048` couvre exactement `200 × 200 cm`.
- **Channel Packing Obligatoire (`ORM`)** :
  - Canal **R** = Ambient Occlusion
  - Canal **G** = Roughness
  - Canal **B** = Metallic
  (Compression UE5 : `Masks (no sRGB)`, BC7/BC5 pour les normales).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-02` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-06`, `ART-04`
- **Audit des Entrées (`inputs`)** :
  - `environment-briefs-wld-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `3d-pipeline-standards-art-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `modular-kit-specification.md` : Doit respecter le gabarit `templates/modular-kit-spec.md` et passer l'audit croisé.
  - `pbr-material-library.csv` : Doit respecter le gabarit `templates/modular-kit-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ART-04`, `ART-08`, `ART-01`, `WLD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Besoin de varier la couleur de 50 conteneurs ou façades commerciales dans le même quartier | Blocage / Dégradation si ignoré | Interdire la création de 50 textures BaseColor distinctes : utiliser un seul matériau maître piloté par Per-Instance Custom Data | Escalade vers Économiser la VRAM (budget <= 6144 MB) |
| Mode de Défaillance 2: Végétation tropicale (palmiers, manguiers, herbes hautes) causant un surcoût GPU dans Nanite/VSM | Blocage / Dégradation si ignoré | Utiliser de la géométrie opaque/masked découplée au plus près de la feuille et couper le World Position Offset (vent) à 3500 cm (35m) | Escalade vers Respecter PERF-GPU-NANITE <= 2.5 ms |
| Mode de Défaillance 3: Écart constaté entre le mesh artistique et la boîte de collision du blockout WLD-05 | Blocage / Dégradation si ignoré | Conserver la boîte de collision exacte du blockout comme Simple Collision du Static Mesh | Escalade vers Garantir zéro régression sur le NavMesh et le parkour |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-02`)

- [ ] **Contrôle DoD #1** : 100 % des modules architecturaux s'assemblent sans couture (watertight) sur la grille `100/200/400 cm`.
- [ ] **Contrôle DoD #2** : Les valeurs PBR respectent la charte `ART-01` (`Albédo 30-240 sRGB`) et la Texel Density `10.24 px/cm`.
- [ ] **Contrôle DoD #3** : Les collisions gameplay sont strictement identiques au blockout `WLD-05` approuvé.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
