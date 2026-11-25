# Audit de Compatibilité Moteur : Unreal Engine 5.8, SideFX Houdini 22.0 & Audiokinetic Wwise (`phase-5-engine-compatibility.md`)

- **Date de Révision** : `2026-11-26`
- **Version Système** : `ZAÏRE STUDIO OS v1.1.0`
- **Sources Officielles Vérifiées** : `SRC-001`..`SRC-005`, `SRC-018`, `SRC-019`, `SRC-031`..`SRC-035`
- **Statut d'Exécution Binaire** : **`NOT TESTED`** (aucun exécutable UE 5.8, Houdini 22.0 ou Wwise n'est installé sur la machine d'audit).

---

## 1. Unreal Engine 5.8 — Vérification Documentaire & Rectifications Techniques

| Sous-Système UE 5.8 | Skills Impactés | Constat Vérifié dans la Documentation Epic Games | Alignement Documentaire | Exécution Binaire |
| :--- | :--- | :--- | :--- | :--- |
| **MegaLights (`SRC-032`)** | `ART-07`, `ENG-06` | Passé d'expérimental (UE 5.5) à **production-ready en UE 5.8** pour l'éclairage direct stochastique de centaines de lumières projetant des ombres (nécessite Hardware Ray Tracing). Le plafond de `<= 3` lumières VSM superposées ne s'applique qu'au fallback sans Hardware Ray Tracing. | **`PASS`** | **`NOT TESTED`** |
| **Mutable (`SRC-033`)** | `ART-03`, `AI-02`, `ART-08` | Plugin officiel de personnalisation runtime (`CustomizableObject`) gérant la fusion de maillages/textures et la suppression automatique des faces cachées sous les vêtements superposés. | **`PASS`** | **`NOT TESTED`** |
| **AnimNext / UAF (`SRC-034`)** | `ART-05` | **Rectification** : `AnimNext` (Unreal Animation Framework) repose sur des traits/graphes orientés données mais demeure exposé via des modules **expérimentaux** C++/Python. L'architecture de production de `ZAÏRE` doit donc conserver `Motion Matching (Pose Search)` comme socle principal et traiter `AnimNext` en veille R&D. | **`PASS`** | **`NOT TESTED`** |
| **World Partition, Data Layers & GAS (`SRC-001`, `SRC-002`)** | `ENG-01`, `ENG-02`, `GD-01` | Grilles `12800 cm`, `OFPA`, `FStreamableManager` et Gameplay Tags natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`) pleinement supportés. | **`PASS`** | **`NOT TESTED`** |
| **MassTraffic & Slalom Wewa (`SRC-004`)** | `AI-03`, `ENG-04` | `MassTraffic` (*City Sample*) ne supporte pas nativement la circulation inter-file de deux-roues ni les barrages de `ORG-POLICE-PCR`. Ces comportements sont balisés comme **[Engineering Recommendation — Custom C++ `UMassProcessor` à développer]**. | **`PARTIAL`** | **`NOT TESTED`** |

---

## 2. SideFX Houdini 22.0 — Vérification Documentaire & Rectification Terminologique

| Composant Houdini 22.0 | Skills Impactés | Constat Vérifié dans la Documentation SideFX (`SRC-035`) | Alignement Documentaire | Exécution Binaire |
| :--- | :--- | :--- | :--- | :--- |
| **Copernicus (COP)** | `ENG-04`, `ART-02` | **Rectification terminologique** : La documentation officielle SideFX nomme ce contexte **`Copernicus (COP)`** (lancé en Beta en Houdini 20.5 puis étendu en production dans Houdini 21 et 22 en remplacement de `COP2`), et non « Copernicus 2.0 ». | **`PASS`** | **`NOT TESTED`** |
| **APEX (All-Purpose EXecution)** | `ENG-04`, `ART-08` | Framework d'évaluation procédurale de graphes et de rigging KineFX déployé depuis Houdini 20.0/20.5 et étendu en Houdini 21–22. | **`PASS`** | **`NOT TESTED`** |
| **Pipeline OSM -> ZoneGraph (`SRC-004`, `SRC-005`)** | `ENG-04` -> `AI-03` | Le DAG garantit désormais que `ENG-04` s'exécute en amont d'`AI-03`, mais aucun fichier binaire `.hda` ou `.hip` n'a été créé ou cuit via `hython`. | **`PARTIAL`** | **`NOT TESTED`** |

---

## 3. Audiokinetic Wwise & Valeurs de Performance Synthétiques

- **Wwise (`AUD-01`..`03`, `SRC-018`)** : Architecture de bus HDR (`-23 LUFS`), plafond de `64 voix physiques`, `Rooms & Portals` et switch `SW_Music_LicenseMode = STREAMER_SAFE` cohérents conceptuellement (**`PASS`** documentaire), mais aucun projet `.wproj` n'est compilé (**`NOT TESTED`**).
- **Nature Synthétique des Chiffres de Profilage (`ENG-07`)** : Les valeurs présentes dans `performance-profile-traffic-police.json` (`P99 = 15.70 ms`, `VRAM = 5590 MB`) portent désormais le marqueur explicite `"profile_nature": "SYNTHETIC_TARGET_ALLOCATION_NOT_MEASURED_IN_ENGINE"` afin qu'elles ne soient jamais confondues avec une capture réelle Unreal Insights.
