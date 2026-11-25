# Normes Géométriques, UV & Nomenclature UE5 (`ART-04`)

## 1. Convention de Nommage Officielle ZAÏRE STUDIO OS
- `SM_[Kit/District]_[AssetName]_[Variant]` (ex: `SM_Port_HangarWall_400a`)
- `SK_[Category]_[CharacterName]` (ex: `SK_Hero_Koffi`, `SK_Veh_MotoWewa01`)
- `T_[AssetName]_[D|N|ORM]` (`_D` = BaseColor sRGB, `_N` = Normal BC5 Linear, `_ORM` = Occlusion/Roughness/Metallic Linear)

## 2. Contraintes Techniques Nanite & Textures
- **Texel Density** : `10.24 px/cm` (0-3m), `5.12 px/cm` (3-15m), `1.28 px/cm` (HLOD).
- **Taille Max Texture** : `2048 × 2048` en standard environnement ; `4096 × 4096` réservé aux visages héros LOD 0 et trim sheets maîtresses.
- **WPO Cull Distance** : `<= 3500 cm` (`35 m`) obligatoire sur tout matériau utilisant World Position Offset.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-04` — Strate DAG 1)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-04`, `ART-01`
- **Audit des Entrées (`inputs`)** :
  - `hardware-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `art-direction-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `3d-modeling-standards.md` : Doit respecter le gabarit `templates/asset-validation-rules.json` et passer l'audit croisé.
  - `asset-validation-rules.json` : Doit respecter le gabarit `templates/asset-validation-rules.json` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-03`, `ART-08`, `DIR-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Static Mesh architectural soumis avec Nanite activé ET un matériau Blend Mode = Translucent | Blocage / Dégradation si ignoré | Bloquer immédiatement l'asset : séparer les vitres translucides dans un sous-mesh distinct non-Nanite (LOD standard) | Escalade vers Respecter les contraintes matérielles du rasterizer Nanite UE5 |
| Mode de Défaillance 2: Texture soumise avec une dimension non puissance de 2 (ex: 1500x1500) | Blocage / Dégradation si ignoré | Rejeter l'import : imposer des dimensions puissances de 2 (512, 1024, 2048, 4096) pour permettre la génération de MipMaps et la compression BC7 | Escalade vers Éviter tout gaspillage VRAM non streamable |
| Mode de Défaillance 3: Asset modulaire dont le pivot est centré au milieu de la géométrie au lieu du coin de grille | Blocage / Dégradation si ignoré | Renvoyer l'asset en correction DCC (Blender/Maya) pour replacer le pivot sur la grille 10/50/100 cm | Escalade vers Garantir la compatibilité avec le snapping WLD-05/WLD-06 et Houdini ENG-04 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-04`)

- [ ] **Contrôle DoD #1** : `python skills/05-art-animation/art-04-3d-pipeline-specialist/scripts/check_3d_standards.py` retourne un code `0`.
- [ ] **Contrôle DoD #2** : 100 % des règles de `asset-validation-rules.json` sont déterministes et vérifiables par `ENG-03`.
- [ ] **Contrôle DoD #3** : Zéro texture non compressée ou sans MipMaps dans le pipeline.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
