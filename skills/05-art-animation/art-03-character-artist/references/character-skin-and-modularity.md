# Pipeline Personnages : Shaders de Peau & Modularité PNJ (`ART-03`)

## 1. Calibration PBR des Carnations Foncées sous Lumière Équatoriale
- **BaseColor (Albédo sRGB)** : Plage réaliste calibrée entre `42 sRGB` et `115 sRGB` (jamais de noir pur, saturation riche dans les sous-tons chauds/dorés/acajou).
- **Dual Specular Lobe (UE5 Skin Shading)** : Lobe primaire `Roughness = 0.28` (sébum naturel), Lobe secondaire `Roughness = 0.48` (micro-relief pores via Cavity Map).
- **Subsurface Profile** : Diffusion sub-cutanée ambre-rouge subtil sur les oreilles, narines et contours sous contre-jour solaire équatorial (`EV100 = 15`).

## 2. Budgets Géométriques & LOD Personnages
| Catégorie | LOD 0 (Triangles) | LOD 1 (Triangles) | LOD 2 (Triangles) | LOD 3 VAT Foule |
| :--- | :--- | :--- | :--- | :--- |
| **Héros (`CHR-PROTAG-KOFFI`)** | `85 000 tris` | `42 000 tris` | `18 000 tris` | N/A |
| **PNJ Actif (`AI-01` Garde)** | `35 000 tris` | `16 000 tris` | `7 500 tris` | `2 800 tris` |
| **Citoyen Foule (`AI-02`)** | `22 000 tris` (Hydraté) | `9 500 tris` | `3 200 tris (VAT)` | `1 400 tris (VAT)` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-03` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-03`, `WLD-02`, `ART-01`, `ART-04`
- **Audit des Entrées (`inputs`)** :
  - `character-bibles-nar-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-dress-codes-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `art-bible-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `3d-standards-art-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `character-art-specification.md` : Doit respecter le gabarit `templates/character-art-spec.md` et passer l'audit croisé.
  - `modular-npc-assembly-table.csv` : Doit respecter le gabarit `templates/character-art-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ART-01`, `ART-04`, `WLD-02`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Coiffure Groom Strands dépassant 0.4 ms GPU en phase de gameplay ouvert | Blocage / Dégradation si ignoré | Forcer la bascule automatique vers le mesh Hair Cards dès le retour en caméra gameplay 3e personne (distance > 180 cm) | Escalade vers Préserver le budget GPU global <= 16.6 ms |
| Mode de Défaillance 2: Répétition visuelle de clones dans les marchés de Matonge (600 PNJ AI-02) | Blocage / Dégradation si ignoré | Combiner 12 têtes × 15 hauts × 12 bas × 10 coiffures/chapeaux × 8 palettes de motifs wax/streetwear (plus de 170 000 permutations pour < 768 MB VRAM) | Escalade vers Appliquer le pipeline modulaire Guerrilla Games SRC-009 |
| Mode de Défaillance 3: Vêtement flottant causant du clipping lors des mouvements de combat | Blocage / Dégradation si ignoré | Remplacer la simulation Chaos Cloth par du skinning rigide + Normal Map animée sur les PNJ de foule, et limiter Chaos Cloth à la veste de Koffi (LOD 0) | Escalade vers Respecter le budget PERF-CPU-CHAOS <= 1.5 ms |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-03`)

- [ ] **Contrôle DoD #1** : Tous les personnages partagent le squelette maître standardisé et supportent le retargeting `ART-06`.
- [ ] **Contrôle DoD #2** : Le pool VRAM total des kits modulaires PNJ d'une commune reste `<= 768 MB`.
- [ ] **Contrôle DoD #3** : Les carnations et tenues respectent strictement `knowledge/world-bible/cultural-guidelines.md`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
