---
name: gd-01-game-systems-designer
description: "Conception des boucles de gameplay fondamentales (Core Loops) et des systèmes transversaux (SYS-* : infiltration urbaine/sociale, réputation par commune, interactions systémiques) mappés sur l'architecture UE5 Gameplay Ability System (GAS) et les Gameplay Tags."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-01
  department: 03-game-design
  stratum: 1
  version: "1.1.0"
  inputs:
    - "creative-pillars-dir-03"
    - "lead-gd-directives-dir-05"
    - "open-world-structure-wld-04"
  outputs:
    - "system-design-document.md"
    - "gameplay-tags-mapping.csv"
  upstream_dependencies:
    - "DIR-03"
    - "DIR-05"
---

# `GD-01` — Game Systems Designer (`gd-01-game-systems-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou mise à jour d'un système de jeu transversal (`SYS-STEALTH`, `SYS-WLD-REPUTATION`, inventaire, interactions PNJ).
- Définition des contrats d'interaction émergente entre deux systèmes via `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.
- Cadrage fonctionnel d'une mécanique avant son implémentation C++ GAS par `ENG-02`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `creative-pillars-dir-03`, `lead-gd-directives-dir-05`, `open-world-structure-wld-04`
- **Sorties produites** : `system-design-document.md`, `gameplay-tags-mapping.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `DIR-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne conçoit pas le déroulé spécifique d'une mission (`GD-02`) ni le code C++ des `UGameplayAbility` (`ENG-02`).
- **Interdiction / Limite** : N'introduit aucun état booléen isolé hors de la taxonomie des `FGameplayTag`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Enregistrer le système sous un identifiant `SYS-[DOMAINE]-[SLUG]` dans `knowledge/entities-registry.csv`.
2. Décomposer le système en Entrées Joueur (Enhanced Input), États (`FGameplayTag`), Attributs (`UAttributeSet`) et Effets (`UGameplayEffect`).
3. Définir la matrice d'interactions émergentes avec la météo (`World.Weather.TropicalStorm`), la foule (`AI-02`) et la réputation de quartier (`World.District.*`).
4. Rédiger la spécification complète suivant `templates/system-design-doc-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Deux systèmes doivent communiquer (ex: météo pluie -> bruit de pas infiltration) | Interdire le couplage direct entre classes et passer exclusivement par un Gameplay Tag partagé (World.Weather.TropicalStorm) | Maintenir la modularité GAS validée avec ENG-02 |
| Mécanique complexe nécessitant plus de 3 minutes de tutoriel texte | Simplifier la règle d'activation contextuelle à un seul input et enseigner par l'affordance spatiale en jeu (WLD-05) | Appliquer le standard d'onboarding DIR-05 |
| Système impactant le budget CPU par un polling frame-by-frame | Remplacer le polling par des callbacks événementiels sur changement de Gameplay Tag | Respecter l'enveloppe Game Thread <= 6.5 ms |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/gas-systemic-design.md`
- **Modèle Officiel de Livrable** : `templates/system-design-doc-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-system-design.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-system-design.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/system-design-doc-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des états et déclencheurs du système sont mappés sur des Gameplay Tags enregistrés.
- [ ] Le document définit clairement les règles d'activation, d'annulation (Cancel Tags) et de blocage (Block Tags) sous UE5 GAS.
- [ ] Les cas limites (interruption par combat, entrée dans un véhicule, transition de quartier) sont couverts.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `ENG-02`.
