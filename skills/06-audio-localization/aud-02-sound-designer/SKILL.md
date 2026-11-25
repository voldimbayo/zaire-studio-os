---
name: aud-02-sound-designer
description: "Conception des effets sonores (SFX), bruitages de combat (ITM-WPN-MACHETTE), moteurs de véhicules kinois (VEH-MOTO-WEWA-01), météo équatoriale et architecture acoustique spatiale sous Audiokinetic Wwise (RTPC, Random Containers, Spatial Audio Rooms & Portals) et UE5 MetaSounds."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AUD-02
  department: 06-audio-localization
  stratum: 3
  version: "1.1.0"
  inputs:
    - "audio-bible-aud-01"
    - "combat-design-gd-05"
    - "vehicle-specs-gd-06"
    - "environment-briefs-wld-06"
  outputs:
    - "sfx-asset-catalog.csv"
    - "wwise-rtpc-and-spatial-spec.md"
  upstream_dependencies:
    - "AUD-01"
    - "GD-05"
    - "GD-06"
    - "WLD-06"
---

# `AUD-02` — Sound Designer (`aud-02-sound-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`06-audio-localization`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création des banques d'effets sonores pour un véhicule (`VEH-*`), une arme (`ITM-*`) ou une météo (`World.Weather.TropicalStorm`).
- Paramétrage des courbes RTPC (Real-Time Parameter Controls) reliant la physique UE5 Chaos (`ENG-05`) au moteur Wwise/MetaSounds.
- Configuration des volumes acoustiques `UAkRoomComponent` et `UAkPortalComponent` sur les bâtiments de `WLD-05`/`WLD-06`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `audio-bible-aud-01`, `combat-design-gd-05`, `vehicle-specs-gd-06`, `environment-briefs-wld-06`
- **Sorties produites** : `sfx-asset-catalog.csv`, `wwise-rtpc-and-spatial-spec.md`
- **Dépendances Amont Canoniques (DAG)** : `AUD-01`, `GD-05`, `GD-06`, `WLD-06`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne gère pas la composition musicale (`AUD-03`) ni l'enregistrement des comédiens de doublage (`AUD-04`).
- **Interdiction / Limite** : Interdit tout effet sonore de pas, d'impact ou de moteur reposant sur un échantillon unique sans variation de hauteur (Pitch) et de conteneur aléatoire.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Construire chaque événement SFX fréquent (pas sur latérite/béton, coups de machette, klaxons Wewa) sous forme d'un **Wwise Random/Blend Container** combinant au moins `6 échantillons` distincts avec randomisation de Pitch (`±120 cents`) et de filtre Low-Pass.
2. Relier la pluie tropicale (`World.Weather.TropicalStorm`) à la nature physique du matériau touché (`ChaosPhysicalMaterial` : crépitement métallique aigu sur les toits en tôle `MI_Corrugated_Iron_Rust`, clapotis lourd sur les flaques du port, impact mat sur la boue latéritique).
3. Configurer le moteur de la moto `VEH-MOTO-WEWA-01` via 3 RTPC continus : `RTPC_Veh_RPM` (`1000 - 9500 tr/min`), `RTPC_Veh_Load` (`0.0 - 1.0` couple accélération) et `RTPC_Surface_Wetness` (`0.0 - 1.0` sifflement de pneu sur bitume mouillé).
4. Placer des `AkSpatialAudioVolume` (Rooms & Portals) sur toutes les ouvertures de hangars et de ngandas pour calculer dynamiquement la diffraction et l'occlusion.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Effet sonore répétitif détecté (fatigue auditive sur le moteur Wewa ou la pluie sur tôle) | Ajouter une modulation procédurale granulaire MetaSounds / Wwise LFO sur l'égalisation et croiser 3 couches de boucles asynchrones de longueurs premières entre elles | Éliminer toute périodicité audible |
| Son d'intérieur de hangar traversant un mur plein en béton sans atténuation | Vérifier la fermeture hermétique du UAkRoomComponent et l'assignation du profil d'absorption acoustique Concrete_Heavy sur la géométrie WLD-05 | Corriger la fuite acoustique Spatial Audio |
| Surcharge CPU due à 40 véhicules MassTraffic jouant chacun un synthétiseur moteur complet | Limiter le modèle moteur 4-couches complet au véhicule du joueur et aux 3 véhicules les plus proches (< 25m) ; basculer le reste du trafic sur un bus d'ambiance routière global | Préserver le budget CPU et le plafond de 64 voix AUD-01 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/wwise-rtpc-and-spatial-audio.md`
- **Modèle Officiel de Livrable** : `templates/wwise-rtpc-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-sfx-wwise-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-sfx-wwise-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/wwise-rtpc-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AUD-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des événements SFX récurrents comportent `>= 6 variations` par surface (`PM_Asphalt_Dry`, `PM_Asphalt_Wet`, `PM_Laterite_Dry`, `PM_Laterite_Mud`).
- [ ] Les courbes RTPC sont bornées, lissées (Slew Rate / Interpolation) et reliées aux variables physiques de `GD-06`/`ENG-05`.
- [ ] La propagation intérieure/extérieure via Wwise Rooms & Portals est validée sans coupure brusque.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `AUD-01`, `ENG-07`, `GD-05`, `GD-06`.
