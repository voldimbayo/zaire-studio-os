# Photométrie Équatoriale (Kinshasa 4°S) & Budgets Lumen (`ART-07`)

## 1. Matrice Photométrique de Référence (PBR Physical Units)
| État Horaire / Météo | Directional Light (Lux) | Température (K) | Sky Light / Rayleigh | Cible EV100 | Budget GPU Lumen |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Aube Fluviale (06h15)** | `18 000 Lux` | `3800 K` (Ambre doux) | Brume Exponential Height Fog dense | `11.8` | `<= 4.2 ms` |
| **Zénith Équatorial (12h30)** | `110 000 Lux` | `5600 K` (Blanc pur) | Ombres verticales très franches | `15.0` | `<= 4.0 ms` |
| **Orage (`TropicalStorm`)** | `9 500 Lux` | `7000 K` (Ardoise froid) | Nuages volumétriques bas + éclairs | `11.0` | `<= 4.5 ms` |
| **Nuit Matonge (21h30)** | `0.25 Lux` (Lune) | `4200 K` + Néons `2200-3200K` | Réflexions Lumen sur bitume humide | `3.5` | `<= 4.5 ms` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-07` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ART-01`, `WLD-05`, `ART-02`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `art-bible-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `level-blockouts-wld-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `environment-art-art-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `lighting-preset-matrix.csv` : Doit respecter le gabarit `templates/lighting-preset-matrix.csv` et passer l'audit croisé.
  - `equatorial-lighting-spec.md` : Doit respecter le gabarit `templates/lighting-preset-matrix.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ART-01`, `ENG-06`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Coût GPU Lumen GI + Reflections > 4.5 ms dans une rue nocturne de Matonge | Blocage / Dégradation si ignoré | Désactiver la projection d'ombres VSM sur les néons décoratifs secondaires (conserver uniquement l'émission Lumen Surface Cache) et limiter les ombres VSM aux lampadaires directeurs espacés de >= 18m | Escalade vers Respecter strictement PERF-GPU-LUMEN |
| Mode de Défaillance 2: Transition intérieur/extérieur aveuglante lors de la sortie d'un hangar vers le soleil équatorial | Blocage / Dégradation si ignoré | Régler la vitesse d'adaptation d'Auto-Exposure (Speed Up = 4.5, Speed Down = 2.5) et utiliser un PostProcessVolume de portail pour pré-adapter l'exposition à 300 cm de la porte | Escalade vers Garantir une lisibilité permanente en combat/poursuite |
| Mode de Défaillance 3: Carnations des personnages apparaissant sous-exposées lors des dialogues nocturnes | Blocage / Dégradation si ignoré | Activer une Rim Light / Key Light diégétique subtile calée sur la source locale la plus proche (phare de Wewa, enseigne de nganda, brasero) | Escalade vers Valoriser les visages sans trahir le réalisme |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-07`)

- [ ] **Contrôle DoD #1** : Le coût GPU combiné `Lumen GI + Lumen Reflections` est `<= 4.5 ms` (60 FPS) / `<= 7.0 ms` (30 FPS).
- [ ] **Contrôle DoD #2** : Maximum 3 lumières locales avec ombres VSM superposées en tout point de la carte.
- [ ] **Contrôle DoD #3** : Lisibilité validée à 100 % sur les 4 états clés : Aube brumeuse, Zénith équatorial, Orage tropical (`World.Weather.TropicalStorm`), Nuit urbaine.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
