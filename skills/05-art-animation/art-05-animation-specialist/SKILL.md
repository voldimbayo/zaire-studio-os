---
name: art-05-animation-specialist
description: "Architecture des systèmes d'animation temps réel sous Unreal Engine 5 : locomotion réactive par Motion Matching (Pose Search), franchissements parkour par Motion Warping (couverts 100 cm, accroches 260-300 cm), montages de combat (GD-05) et Control Rig IK dans un budget CPU <= 1.8 ms."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-05
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "spatial-metrics-wld-05"
    - "combat-frame-data-gd-05"
    - "cleaned-mocap-art-06"
  outputs:
    - "animation-graph-specification.md"
    - "locomotion-and-warping-metrics.csv"
  upstream_dependencies:
    - "WLD-05"
    - "GD-05"
    - "ART-06"
---

# `ART-05` — Animation Specialist (`art-05-animation-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception ou optimisation de l'Animation Blueprint de `CHR-PROTAG-KOFFI` ou des gardes `AI-01`.
- Paramétrage des fenêtres `Motion Warping` pour aligner les mains et les pieds sur les obstacles de Kinshasa (`100 cm` vault, `280 cm` ledge grab).
- Synchronisation des `AnimNotifies` de combat avec la Frame Data à 60 FPS définie par `GD-05`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `spatial-metrics-wld-05`, `combat-frame-data-gd-05`, `cleaned-mocap-art-06`
- **Sorties produites** : `animation-graph-specification.md`, `locomotion-and-warping-metrics.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-05`, `GD-05`, `ART-06`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne dirige pas l'acquisition sur le plateau Motion Capture ni le nettoyage brut des marqueurs optiques (`ART-06`).
- **Interdiction / Limite** : Interdit tout calcul d'IK complet (`Control Rig Full Body IK`) sur les PNJ situés à plus de `25 mètres` de la caméra.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Configurer la base de données **UE5 Motion Matching (`UPoseSearchDatabase`)** de Koffi avec les canaux de trajectoire future (`+0.2s`, `+0.4s`, `+0.6s`) et de vélocité des pieds pour éliminer tout glissement (*foot sliding*, méthode Rockstar `SRC-015`).
2. Associer les fenêtres `UMotionWarpingComponent` aux capacités GAS (`Ability.Movement.Vault` à `100 cm`, `LedgeGrab` à `260-300 cm`) définies dans `knowledge/technical-specs/spatial-metrics.md`.
3. Placer les `UAnimNotifyState` de combat (`ANS_MeleeHitbox`, `ANS_ParryWindow`, `ANS_CancelWindow`) aux frames exactes spécifiées par `GD-05`.
4. Activer l'**Update Rate Optimization (URO)** et l'évaluation sur Worker Threads (`bUseMultiThreadedAnimationUpdate = true`) pour tenir le budget `PERF-CPU-ANIM <= 1.8 ms`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Latence ressentie (> 100 ms) lors d'un demi-tour brusque en sprint ou en combat | Augmenter le poids de la réactivité d'input (Trajectory Weight) dans le Pose Search Schema et déclencher un Pivot Transition Montage | Concilier inertie réaliste et contrôle nerveux DIR-05 |
| Dépassement du budget CPU Animation (> 1.8 ms) dans une scène dense | Désactiver le Foot Placement Control Rig au-delà de 15m, passer les PNJ entre 15m et 30m à 30Hz (URO) et figer l'évaluation squelettique au-delà de 80m (bascule VAT AI-02) | Respecter PERF-CPU-ANIM |
| Obstacle de blockout situé à 105 cm au lieu de 100 cm | Autoriser le Motion Warping vertical dans la plage de tolérance [90 cm, 110 cm] sans déformer la vitesse d'animation | Garantir un franchissement sans accroc géométrique |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/motion-matching-and-warping.md`
- **Modèle Officiel de Livrable** : `templates/animation-graph-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-animation-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-animation-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/animation-graph-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Coût CPU Animation total `<= 1.8 ms` (60 FPS) / `<= 2.5 ms` (30 FPS) avec 100 % des mises à jour sur Worker Threads.
- [ ] Alignement exact à la frame près entre les `AnimNotifies` et la table Frame Data de `GD-05`.
- [ ] Zéro glissement des pieds sur les pentes en latérite de `DST-NGALIEMA` grâce au Control Rig Foot IK.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `GD-05`, `WLD-05`, `ENG-07`.
