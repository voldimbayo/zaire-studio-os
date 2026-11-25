# Gouvernance des Master Materials, PSO & Rigging (`ART-08`)

## 1. Catalogue des 8 Master Materials Officiels ZAÏRE
| Master Material | Domaine | Max Instructions PS | Max Static Switches | Custom Primitive Data |
| :--- | :--- | :--- | :--- | :--- |
| `M_Zaire_Env_Standard` | Architecture & Props Nanite | `<= 135` | `2` (RVT Blend, Triplanar) | `[0-3]` Tint RGB + Wetness |
| `M_Zaire_Env_Decal` | Signalétique, flaques, graffitis | `<= 95` | `1` | `[0]` Opacity / Wear |
| `M_Zaire_Foliage_Masked` | Végétation tropicale (WPO `<= 35m`) | `<= 140` | `1` | `[0]` Phase vent |
| `M_Zaire_Char_Skin` | Peau humaine Dual-Specular SSS | `<= 215` | `1` | `[0]` Sweat / Rain factor |
| `M_Zaire_Char_Cloth` | Vêtements wax / streetwear / cuir | `<= 150` | `2` | `[0-3]` Pattern Index + Tint |
| `M_Zaire_Hair_Cards` | Coiffures africaines Hair Cards | `<= 165` | `0` | `[0-2]` Melanin / Roughness |
| `M_Zaire_Vehicle_Master` | Carrosseries Wewa, Taxis, Bus | `<= 155` | `1` | `[0-4]` Couleur + Boue latérite |
| `M_Zaire_Water_River` | Fleuve Congo & Bassins portuaires | `<= 190` | `1` | Courant & Turbidité limon |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-08` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ART-02`, `ART-03`, `ART-04`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `environment-art-art-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `character-art-art-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `3d-standards-art-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `master-material-specification.md` : Doit respecter le gabarit `templates/master-material-spec.md` et passer l'audit croisé.
  - `shader-pso-budget-guidelines.md` : Doit respecter le gabarit `templates/master-material-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-06`, `ENG-07`, `DIR-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Artiste demandant un Static Switch supplémentaire doublant le nombre de permutations PSO d'un Master Material | Blocage / Dégradation si ignoré | Refuser le Static Switch et implémenter l'effet via un masque de canal ou un float CustomPrimitiveData évalué dynamiquement | Escalade vers Éviter l'explosion combinatoire des PSO ($2^N$) |
| Mode de Défaillance 2: Shader d'environnement dépassant 140 instructions Pixel Shader | Blocage / Dégradation si ignoré | Pré-cuire les opérations mathématiques procédurales lourdes dans une texture ORM/Masque 2K ou basculer le calcul sur les Vertex/Interpolants | Escalade vers Tenir le budget GPU de rendu ENG-06 |
| Mode de Défaillance 3: Rig de véhicule (ex: VEH-MOTO-WEWA-01) comportant plus de 35 os actifs | Blocage / Dégradation si ignoré | Simplifier la hiérarchie osseuse à <= 24 os (châssis, fourche, guidon, bras oscillant, 2 roues, béquille, suspension) | Escalade vers Optimiser le coût CPU Chaos Vehicles ENG-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-08`)

- [ ] **Contrôle DoD #1** : Le nombre total de Master Materials du studio reste `<= 10` et le nombre de `StaticSwitch` par Master Material est `<= 3`.
- [ ] **Contrôle DoD #2** : Tous les shaders d'environnement standard respectent le plafond de `140 instructions` Pixel Shader.
- [ ] **Contrôle DoD #3** : Les rigs de véhicules et de personnages passent le test de déformation extrême sans artefact.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
