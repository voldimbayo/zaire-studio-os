---
name: art-06-motion-capture-specialist
description: "Planification et pipeline d'acquisition Motion Capture corporelle et faciale (MetaHuman Animator) de ZAÏRE. Produit les shotlists de capture, les protocoles de nettoyage des courbes (zéro patinage des pieds, préservation des contacts) et le retargeting IK Rig vers le squelette maître SK_Zaire_Master_Humanoid."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-06
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "mission-scripts-nar-02"
    - "combat-moveset-gd-05"
  outputs:
    - "mocap-shotlist.csv"
    - "retargeting-and-cleanup-protocol.md"
  upstream_dependencies:
    - "NAR-02"
    - "GD-05"
---

# `ART-06` — Motion Capture Specialist (`art-06-motion-capture-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Préparation d'une session de capture de mouvement pour les cinématiques (`NAR-02`), le combat (`GD-05`) ou les attitudes quotidiennes des habitants de Kinshasa (`WLD-02`).
- Nettoyage (solving & cleaning) des prises optiques/inertielles et faciales avant livraison à `ART-05`.
- Configuration des chaînes `UIKRigDefinition` et `UIKRetargeter` sous UE5.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `mission-scripts-nar-02`, `combat-moveset-gd-05`
- **Sorties produites** : `mocap-shotlist.csv`, `retargeting-and-cleanup-protocol.md`
- **Dépendances Amont Canoniques (DAG)** : `NAR-02`, `GD-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas la logique d'état des Animation Blueprints (`ART-05`).
- **Interdiction / Limite** : Ne livre jamais une prise brute non nettoyée ou dont la pose de départ/fin rompt les boucles de Motion Matching.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Extraire des scripts `NAR-02` et des matrices `GD-05` la liste exhaustive des prises requises et les codifier sous le format `MCP_[CAT]_[CHR]_[ACTION]_[TAKE]`.
2. Renseigner pour chaque prise de la shotlist les accessoires physiques requis sur le plateau (gabarit bois de `VEH-MOTO-WEWA-01`, caisse de `100 cm` exacte pour le vault, machette factice `ITM-WPN-MACHETTE`).
3. Appliquer le protocole de nettoyage en 4 étapes : (1) Stabilisation des contacts plantaires (0 dérive sur les frames d'appui), (2) Filtrage du bruit haute fréquence sans écraser les impacts de combat, (3) Résolution faciale MetaHuman Animator synchronisée au timecode audio (`AUD-04`), (4) Retargeting IK Rig vers `SK_Zaire_Master_Humanoid`.
4. Exporter la shotlist et le rapport de contrôle qualité dans `templates/mocap-shotlist-template.csv`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Accessoire de plateau MoCap dont les dimensions diffèrent des métriques WLD-05 (ex: table à 75 cm au lieu de caisse à 100 cm) | Interdire la prise tant que le praticable physique du plateau n'est pas réglé exactement à 100 cm (spatial-metrics.md) | Éviter une correction destructive en post-production ART-05 |
| Perte d'occlusion de marqueurs lors d'une prise de mêlée rapide | Reconstruire la trajectoire cinématique en respectant strictement la durée de Startup/Active de GD-05 sans lisser le pic d'accélération de l'impact | Préserver le punch du Game Feel |
| Décalage de synchronisation labiale > 1 frame entre l'audio lingala/français et la capture faciale | Réaligner le timecode SMPTE sur la piste audio maîtresse avant l'export des courbes MetaHuman ARKit/Animator | Garantir la qualité cinématique avec AUD-04 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/mocap-pipeline-and-retargeting.md`
- **Modèle Officiel de Livrable** : `templates/mocap-shotlist-template.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-mocap-shotlist.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-mocap-shotlist.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/mocap-shotlist-template.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des prises de la shotlist indiquent les dimensions exactes des praticables du plateau (`spatial-metrics.md`).
- [ ] 0 dérive des pieds (foot sliding `< 0.5 mm/frame`) sur les phases d'appui verrouillées.
- [ ] Synchronisation timecode audio/visage vérifiée à `60 fps`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ART-05`, `NAR-02`, `GD-05`.
