# Design Sonore Systémique : RTPC, Surfaces & Spatial Audio (`AUD-02`)

## 1. Mapping `ChaosPhysicalMaterial` -> Switch Group Wwise `SW_Surface_Type`
- `PM_Asphalt_Dry` -> `SW_Surface_Asphalt_Dry`
- `PM_Asphalt_Wet` -> `SW_Surface_Asphalt_Wet` (ajoute la couche d'éclaboussure haute fréquence)
- `PM_Laterite_Dry` -> `SW_Surface_Laterite_Dry` (crissement granuleux de terre sèche)
- `PM_Laterite_Mud` -> `SW_Surface_Laterite_Mud` (succion visqueuse de boue tropicale)
- `PM_Corrugated_Iron` -> `SW_Surface_SheetMetal` (résonance métallique caractéristique des toits kinois sous l'averse)

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AUD-02` — Strate DAG 3)

- **Ingénierie Audio Wwise / MetaSounds & Localisation Unicode (UE 5.8)** (`SRC-018`, `SRC-027`, `SRC-028`, `SRC-029`, `SRC-031`) :
  - **Mixage HDR & Budgets (`AUD-01`, `AUD-02`)** : Cible `-23 LUFS` (`±1 LU`), plafond de `64 voix physiques` simultanées (virtualisation sous `-48 dB`), budget RAM `<= 512 MB`, propagation acoustique par `UAkRoomComponent` & `UAkPortalComponent`, `>= 6 variations` par Random Container SFX.
  - **Musique Interactive & Conformité DMCA (`AUD-03`, `SRC-028`)** : 4 stems verticaux synchronisés au tempo (`Next Beat` / `Next Bar`), bascule instantanée `SW_Music_LicenseMode = STREAMER_SAFE` vers des compositions 100 % originales.
  - **Localisation & Accessibilité XAG 104 (`AUD-04`, `SRC-029`, `SRC-031`)** : Format `[LOCUTEUR] : Texte`, support UTF-8 natif des voyelles lingala `ɛ` et `ɔ`, réserve d'expansion UI `>= +35 %`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `AUD-01`, `GD-05`, `GD-06`, `WLD-06`
- **Audit des Entrées (`inputs`)** :
  - `audio-bible-aud-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-design-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `vehicle-specs-gd-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `environment-briefs-wld-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `sfx-asset-catalog.csv` : Doit respecter le gabarit `templates/wwise-rtpc-spec.md` et passer l'audit croisé.
  - `wwise-rtpc-and-spatial-spec.md` : Doit respecter le gabarit `templates/wwise-rtpc-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `AUD-01`, `ENG-07`, `GD-05`, `GD-06`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Effet sonore répétitif détecté (fatigue auditive sur le moteur Wewa ou la pluie sur tôle) | Blocage / Dégradation si ignoré | Ajouter une modulation procédurale granulaire MetaSounds / Wwise LFO sur l'égalisation et croiser 3 couches de boucles asynchrones de longueurs premières entre elles | Escalade vers Éliminer toute périodicité audible |
| Mode de Défaillance 2: Son d'intérieur de hangar traversant un mur plein en béton sans atténuation | Blocage / Dégradation si ignoré | Vérifier la fermeture hermétique du UAkRoomComponent et l'assignation du profil d'absorption acoustique Concrete_Heavy sur la géométrie WLD-05 | Escalade vers Corriger la fuite acoustique Spatial Audio |
| Mode de Défaillance 3: Surcharge CPU due à 40 véhicules MassTraffic jouant chacun un synthétiseur moteur complet | Blocage / Dégradation si ignoré | Limiter le modèle moteur 4-couches complet au véhicule du joueur et aux 3 véhicules les plus proches (< 25m) ; basculer le reste du trafic sur un bus d'ambiance routière global | Escalade vers Préserver le budget CPU et le plafond de 64 voix AUD-01 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AUD-02`)

- [ ] **Contrôle DoD #1** : 100 % des événements SFX récurrents comportent `>= 6 variations` par surface (`PM_Asphalt_Dry`, `PM_Asphalt_Wet`, `PM_Laterite_Dry`, `PM_Laterite_Mud`).
- [ ] **Contrôle DoD #2** : Les courbes RTPC sont bornées, lissées (Slew Rate / Interpolation) et reliées aux variables physiques de `GD-06`/`ENG-05`.
- [ ] **Contrôle DoD #3** : La propagation intérieure/extérieure via Wwise Rooms & Portals est validée sans coupure brusque.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
