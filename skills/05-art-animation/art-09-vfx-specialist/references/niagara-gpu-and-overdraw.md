# Architecture UE5 Niagara GPU & Contrôle d'Overdraw (`ART-09`)

## 1. Répartition du Budget GPU VFX (`PERF-GPU-NIAGARA <= 1.5 ms`)
| Catégorie VFX | Budget GPU Max | Simulation | Culling Distance | Max Instances Simultanées |
| :--- | :--- | :--- | :--- | :--- |
| **Météo (`NS_Weather_TropicalRain`)** | `<= 0.65 ms` | GPU Compute + Distance Field | Attaché Caméra (`18 m`) | `1 (Global)` |
| **Véhicules (`NS_Veh_LateriteDust`)** | `<= 0.40 ms` | GPU Compute + Cutout 8-verts | `4500 cm (45 m)` | `4 véhicules max` |
| **Combat (`NS_Cmb_MacheteParrySparks`)** | `<= 0.25 ms` | GPU / CPU Burst léger | `2500 cm (25 m)` | `4 impacts max` |
| **Ambiance (`NS_Env_StreetSteam_Smoke`)** | `<= 0.20 ms` | GPU Compute | `3500 cm (35 m)` | `12 sources locales` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-09` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ART-01`, `GD-05`, `ART-07`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `art-bible-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-design-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lighting-and-weather-art-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `vfx-system-specification.md` : Doit respecter le gabarit `templates/vfx-system-spec.md` et passer l'audit croisé.
  - `niagara-budget-table.csv` : Doit respecter le gabarit `templates/vfx-system-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-07`, `GD-05`, `ART-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Système de pluie tropicale (World.Weather.TropicalStorm) dépassant 1.0 ms GPU à lui seul | Blocage / Dégradation si ignoré | Utiliser une boîte d'émission locale attachée à la caméra (rayon 18m) en GPU Compute + un post-process léger de gouttes lointaines plutôt que de simuler des particules sur tout le quartier | Escalade vers Maintenir le budget total Niagara <= 1.5 ms |
| Mode de Défaillance 2: Nuage de poussière derrière 10 motos Wewa saturant l'overdraw transparent | Blocage / Dégradation si ignoré | Limiter le nombre d'émetteurs de poussière de roue actifs aux 4 véhicules les plus proches et activer un fondu d'opacité à proximité immédiate de la caméra (< 150 cm) | Escalade vers Préserver le framerate et la visibilité de conduite |
| Mode de Défaillance 3: Effet d'impact de combat masquant l'animation deStartup de la contre-attaque ennemie | Blocage / Dégradation si ignoré | Limiter la durée de vie des étincelles de parade machette à 0.18s (11 frames) avec dispersion radiale hors du torse de l'ennemi | Escalade vers Garantir la lisibilité tactique exigée par GD-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-09`)

- [ ] **Contrôle DoD #1** : Le coût GPU total de tous les systèmes Niagara actifs est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).
- [ ] **Contrôle DoD #2** : 100 % des sprites de fumée/poussière utilisent la Cutout Geometry et un plafond de 4 couches d'overdraw.
- [ ] **Contrôle DoD #3** : Tous les systèmes Niagara possèdent un `UNiagaraEffectType` avec distance de culling définie.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
