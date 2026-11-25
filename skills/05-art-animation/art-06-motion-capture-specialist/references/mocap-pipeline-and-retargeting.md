# Protocole Motion Capture, Praticables & Retargeting UE5 (`ART-06`)

## 1. Alignement Plateau Physique <-> Métriques UE5 (`spatial-metrics.md`)
Tout praticable utilisé sur le volume de capture doit reproduire au centimètre près les cotes moteur :
- **Module Couvert Bas / Vault** : Hauteur `100 cm`, profondeur `100 cm`.
- **Gabarit Moto Wewa (`VEH-MOTO-WEWA-01`)** : Hauteur de selle `78 cm`, largeur guidon `76 cm`, repose-pieds à `32 cm`.
- **Hauteur de Barre d'Accroche (Ledge Grab)** : `280 cm`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ART-06` — Strate DAG 3)

- **Pipeline Visuel Temps Réel : Nanite, Lumen / MegaLights, Mutable & AnimNext (UE 5.8)** (`SRC-003`, `SRC-009`, `SRC-011`, `SRC-015`, `SRC-019`, `SRC-032`..`SRC-034`) :
  - **Standards 3D & Nanite (`ART-02`, `ART-04`)** : Texel Density `10.24 px/cm` (`0-3 m`), pivots alignés sur grille (`10/50/100/400 cm`), interdiction absolue des matériaux `Translucent` sur géométrie Nanite, coupure du `World Position Offset (WPO)` à `<= 3500 cm` (`2500 cm` pour l'invalidation d'ombres VSM).
  - **Personnages Modulaires & Carnations (`ART-03`, `SRC-033`)** : Albédo PBR `42-115 sRGB`, Dual-Lobe Specular (`0.26 / 0.44`), compatibilité avec le plugin **UE 5.8 Mutable (`CustomizableObject`)** pour la fusion runtime des 5 slots modulaires PNJ (`<= 768 MB VRAM` cible).
  - **Animation (`ART-05`, `ART-06`, Budget cible `<= 1.8 ms`, `SRC-034`)** : `Motion Matching (Pose Search)` en production + suivi d'**UE 5.8 AnimNext / UAF** (encore expérimental en C++/Python, à ne pas imposer comme dépendance bloquante sans prototype validé), `Motion Warping` calé sur `100 cm` (Vault) et `280 cm` (Ledge), mapping visèmes lingala (`ɛ`, `ɔ`, `mb`, `nd`, `ng`).
  - **Éclairage Équatorial (`ART-07`, Budget cible Lumen `<= 4.5 ms`, `SRC-032`)** : Soleil Zénithal `110 000 Lux` (`EV100 = 15.0`), maximum `3 lumières VSM superposées` en pipeline VSM sans Ray Tracing matériel, ou utilisation d'**UE 5.8 MegaLights** (passé en statut production en 5.8 sur matériel supportant le Hardware Ray Tracing) pour les scènes nocturnes multi-néons de `DST-MATONGE` et `DST-BANDAL`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-02`, `GD-05`
- **Audit des Entrées (`inputs`)** :
  - `mission-scripts-nar-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-moveset-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `mocap-shotlist.csv` : Doit respecter le gabarit `templates/mocap-shotlist-template.csv` et passer l'audit croisé.
  - `retargeting-and-cleanup-protocol.md` : Doit respecter le gabarit `templates/mocap-shotlist-template.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ART-05`, `NAR-02`, `GD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Accessoire de plateau MoCap dont les dimensions diffèrent des métriques WLD-05 (ex: table à 75 cm au lieu de caisse à 100 cm) | Blocage / Dégradation si ignoré | Interdire la prise tant que le praticable physique du plateau n'est pas réglé exactement à 100 cm (spatial-metrics.md) | Escalade vers Éviter une correction destructive en post-production ART-05 |
| Mode de Défaillance 2: Perte d'occlusion de marqueurs lors d'une prise de mêlée rapide | Blocage / Dégradation si ignoré | Reconstruire la trajectoire cinématique en respectant strictement la durée de Startup/Active de GD-05 sans lisser le pic d'accélération de l'impact | Escalade vers Préserver le punch du Game Feel |
| Mode de Défaillance 3: Décalage de synchronisation labiale > 1 frame entre l'audio lingala/français et la capture faciale | Blocage / Dégradation si ignoré | Réaligner le timecode SMPTE sur la piste audio maîtresse avant l'export des courbes MetaHuman ARKit/Animator | Escalade vers Garantir la qualité cinématique avec AUD-04 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ART-06`)

- [ ] **Contrôle DoD #1** : 100 % des prises de la shotlist indiquent les dimensions exactes des praticables du plateau (`spatial-metrics.md`).
- [ ] **Contrôle DoD #2** : 0 dérive des pieds (foot sliding `< 0.5 mm/frame`) sur les phases d'appui verrouillées.
- [ ] **Contrôle DoD #3** : Synchronisation timecode audio/visage vérifiée à `60 fps`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
