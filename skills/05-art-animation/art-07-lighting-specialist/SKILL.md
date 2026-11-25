---
name: art-07-lighting-specialist
description: "Direction et ingénierie de l'éclairage physique équatorial de Kinshasa sous Unreal Engine 5 (Lumen Global Illumination, Lumen Reflections, Sky Atmosphere, Volumetric Clouds, Virtual Shadow Maps). Gère le cycle jour/nuit, la météo tropicale (World.Weather.TropicalStorm), la mise en valeur des carnations foncées et le budget GPU Lumen <= 4.5 ms."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-07
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "art-bible-art-01"
    - "level-blockouts-wld-05"
    - "environment-art-art-02"
    - "gpu-budgets-dir-04"
  outputs:
    - "lighting-preset-matrix.csv"
    - "equatorial-lighting-spec.md"
  upstream_dependencies:
    - "ART-01"
    - "WLD-05"
    - "ART-02"
    - "DIR-04"
---

# `ART-07` — Lighting Specialist (`art-07-lighting-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Étalonnage des valeurs photométriques physiques (Lux, Kelvin, EV100) du cycle jour/nuit et des orages tropicaux sur Kinshasa.
- Mise en lumière d'un niveau dès la phase de blockout (`WLD-05`, méthodologie Naughty Dog `SRC-011`/`SRC-012`) pour guider naturellement l'œil du joueur.
- Optimisation du budget GPU `PERF-GPU-LUMEN` (`<= 4.5 ms` en mode 60 FPS / `<= 7.0 ms` en mode 30 FPS).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `art-bible-art-01`, `level-blockouts-wld-05`, `environment-art-art-02`, `gpu-budgets-dir-04`
- **Sorties produites** : `lighting-preset-matrix.csv`, `equatorial-lighting-spec.md`
- **Dépendances Amont Canoniques (DAG)** : `ART-01`, `WLD-05`, `ART-02`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie pas le code C++/USF interne du moteur de rendu (`ENG-06`).
- **Interdiction / Limite** : Interdit de placer plus de **3 sources lumineuses dynamiques projetant des ombres Virtual Shadow Maps (VSM) qui se chevauchent** au même endroit.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Configurer l'éclairage en unités photométriques physiques réelles adaptées à la latitude de Kinshasa (`4° Sud`) : Soleil Zénithal à `110 000 Lux` (`5600 K`, `EV100 = 15.0`), Ciel couvert d'orage tropical à `12 000 Lux` (`6800 K`, `EV100 = 11.5`), Nuit urbaine Matonge à `EV100 = 3.5`.
2. Calibrer la courbe d'Auto-Exposure et la LUT colorimétrique **ACES Filmic** en testant systématiquement le rendu sur les shaders de peau de `CHR-PROTAG-KOFFI` et `CHR-ALLY-AMINA` (`ART-03`) pour préserver le détail des tons foncés et l'éclat spéculaire.
3. Utiliser le contraste lumineux (ratio d'éclairement `4:1`) pour mettre en évidence les sorties d'arènes et les points de franchissement du blockout `WLD-05`.
4. Plafonner le rayon d'atténuation (`Attenuation Radius`) et la distance d'ombre (`Shadow Max Draw Distance`) des lampadaires et néons nocturnes pour tenir `PERF-GPU-LUMEN <= 4.5 ms`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Coût GPU Lumen GI + Reflections > 4.5 ms dans une rue nocturne de Matonge | Désactiver la projection d'ombres VSM sur les néons décoratifs secondaires (conserver uniquement l'émission Lumen Surface Cache) et limiter les ombres VSM aux lampadaires directeurs espacés de >= 18m | Respecter strictement PERF-GPU-LUMEN |
| Transition intérieur/extérieur aveuglante lors de la sortie d'un hangar vers le soleil équatorial | Régler la vitesse d'adaptation d'Auto-Exposure (Speed Up = 4.5, Speed Down = 2.5) et utiliser un PostProcessVolume de portail pour pré-adapter l'exposition à 300 cm de la porte | Garantir une lisibilité permanente en combat/poursuite |
| Carnations des personnages apparaissant sous-exposées lors des dialogues nocturnes | Activer une Rim Light / Key Light diégétique subtile calée sur la source locale la plus proche (phare de Wewa, enseigne de nganda, brasero) | Valoriser les visages sans trahir le réalisme |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/equatorial-lumen-lighting.md`
- **Modèle Officiel de Livrable** : `templates/lighting-preset-matrix.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-lighting-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-lighting-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/lighting-preset-matrix.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-07` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le coût GPU combiné `Lumen GI + Lumen Reflections` est `<= 4.5 ms` (60 FPS) / `<= 7.0 ms` (30 FPS).
- [ ] Maximum 3 lumières locales avec ombres VSM superposées en tout point de la carte.
- [ ] Lisibilité validée à 100 % sur les 4 états clés : Aube brumeuse, Zénith équatorial, Orage tropical (`World.Weather.TropicalStorm`), Nuit urbaine.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ART-01`, `ENG-06`, `ENG-07`.
