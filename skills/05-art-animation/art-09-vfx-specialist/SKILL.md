---
name: art-09-vfx-specialist
description: "Conception des effets visuels temps réel sous UE5 Niagara : averses équatoriales (World.Weather.TropicalStorm), éclaboussures de boue latéritique, poussière ocre soulevée par les motos Wewa, fumées d'échappement et impacts de mêlée dans un budget GPU <= 1.5 ms."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-09
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "art-bible-art-01"
    - "combat-design-gd-05"
    - "lighting-and-weather-art-07"
    - "gpu-budgets-dir-04"
  outputs:
    - "vfx-system-specification.md"
    - "niagara-budget-table.csv"
  upstream_dependencies:
    - "ART-01"
    - "GD-05"
    - "ART-07"
    - "DIR-04"
---

# `ART-09` — VFX Specialist (`art-09-vfx-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création d'un système de particules Niagara atmosphérique (pluie tropicale, brume du fleuve Congo, poussière de rue à Kalamu).
- Conception des effets de combat (`SYS-CMB-MELEE` : étincelles de parade machette `ITM-WPN-MACHETTE`, impacts) et de conduite (`VEH-MOTO-WEWA-01`).
- Optimisation de l'overdraw transparent et du budget GPU `PERF-GPU-NIAGARA` (`<= 1.5 ms` en mode 60 FPS).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `art-bible-art-01`, `combat-design-gd-05`, `lighting-and-weather-art-07`, `gpu-budgets-dir-04`
- **Sorties produites** : `vfx-system-specification.md`, `niagara-budget-table.csv`
- **Dépendances Amont Canoniques (DAG)** : `ART-01`, `GD-05`, `ART-07`, `DIR-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne configure pas l'éclairage global de la scène ni les nuages volumétriques de haute altitude (`ART-07`).
- **Interdiction / Limite** : Interdit de superposer plus de **4 couches d'overdraw transparent** plein écran lors des averses ou explosions.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Exécuter 100 % des systèmes à grand nombre de particules (pluie, poussière, étincelles) en **Simulation GPU Compute Niagara** avec collisions sur le **Global Distance Field** (zéro raycast CPU par particule).
2. Découper tous les sprites transparents (fumée, poussière latérite) avec de la **Cutout Geometry (8 sommets)** afin d'éliminer les pixels vides transparents (réduction de l'overdraw de `-45 %`).
3. Packer les textures de flipbooks en un seul fichier **Channel-Packed** (`R` = Fumée/Densité, `G` = Masque d'érosion, `B` = Émission/Chaleur, `A` = Alpha) limité à `1024x1024` ou `2048x2048`.
4. Configurer les règles de Scalabilité Niagara (`UNiagaraEffectType` : distance de culling strict, plafond d'instances simultanées et réduction automatique de spawn rate si `PERF-GPU-NIAGARA > 1.3 ms`).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Système de pluie tropicale (World.Weather.TropicalStorm) dépassant 1.0 ms GPU à lui seul | Utiliser une boîte d'émission locale attachée à la caméra (rayon 18m) en GPU Compute + un post-process léger de gouttes lointaines plutôt que de simuler des particules sur tout le quartier | Maintenir le budget total Niagara <= 1.5 ms |
| Nuage de poussière derrière 10 motos Wewa saturant l'overdraw transparent | Limiter le nombre d'émetteurs de poussière de roue actifs aux 4 véhicules les plus proches et activer un fondu d'opacité à proximité immédiate de la caméra (< 150 cm) | Préserver le framerate et la visibilité de conduite |
| Effet d'impact de combat masquant l'animation deStartup de la contre-attaque ennemie | Limiter la durée de vie des étincelles de parade machette à 0.18s (11 frames) avec dispersion radiale hors du torse de l'ennemi | Garantir la lisibilité tactique exigée par GD-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/niagara-gpu-and-overdraw.md`
- **Modèle Officiel de Livrable** : `templates/vfx-system-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-vfx-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-vfx-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/vfx-system-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-09` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le coût GPU total de tous les systèmes Niagara actifs est `<= 1.5 ms` (60 FPS) / `<= 2.0 ms` (30 FPS).
- [ ] 100 % des sprites de fumée/poussière utilisent la Cutout Geometry et un plafond de 4 couches d'overdraw.
- [ ] Tous les systèmes Niagara possèdent un `UNiagaraEffectType` avec distance de culling définie.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ENG-07`, `GD-05`, `ART-07`.
