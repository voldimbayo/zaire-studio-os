---
name: gd-07-ui-ux-designer
description: "Architecture de l'information, conception du HUD contextuel minimaliste, du téléphone diégétique de Koffi, de la carte interactive de Kinshasa et des parcours utilisateurs (UX) sous UE5 Common UI. Garantit le support Unicode Lingala (ɛ, ɔ), l'expansion de texte (+35 %) et la conformité native aux normes d'accessibilité XAG (PRD-06)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-07
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "game-systems-gd-01"
    - "mission-design-gd-02"
    - "art-bible-art-01"
    - "xag-requirements-prd-06"
  outputs:
    - "ui-screen-specification.md"
    - "common-ui-navigation-flow.md"
  upstream_dependencies:
    - "GD-01"
    - "GD-02"
    - "ART-01"
---

# `GD-07` — UI/UX Designer (`gd-07-ui-ux-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception ou modification d'un écran d'interface, d'un composant HUD, de la carte de Kinshasa ou du téléphone diégétique (`UI.Layer.*`).
- Vérification de la tenue des conteneurs de texte face à l'expansion linguistique (+35 %) et aux caractères spéciaux du lingala (`ɛ`, `ɔ`).
- Intégration des exigences d'accessibilité visuelle et cognitive (`PRD-06` : double codage forme+couleur, contraste >= 4.5:1, taille des sous-titres).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `game-systems-gd-01`, `mission-design-gd-02`, `art-bible-art-01`, `xag-requirements-prd-06`
- **Sorties produites** : `ui-screen-specification.md`, `common-ui-navigation-flow.md`
- **Dépendances Amont Canoniques (DAG)** : `GD-01`, `GD-02`, `ART-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas le code C++ des `UCommonActivatableWidget` (`ENG-02`).
- **Interdiction / Limite** : Interdit tout encombrement permanent de l'écran (pas de mini-carte intrusive verrouillée si le joueur navigue via `SYS-WLD-LANDMARKS`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Rattacher chaque widget à sa couche Common UI (`UI.Layer.HUD` ou `UI.Layer.DiegeticPhone` dans `knowledge/technical-specs/gameplay-tags-taxonomy.csv`).
2. Appliquer la règle de **Navigation en 3 Actions Maximum** : toute fonction principale (carte de Kinshasa, journal de mission `MSN-*`, station radio `ORG-RADIO-KIN`, inventaire) doit être atteignable en `<= 3` pressions manette ou clavier.
3. Dimensionner tous les conteneurs de chaînes dynamiques avec une réserve d'expansion horizontale/verticale de **`+35 %`** et imposer une police supportant la plage Unicode Latin Étendu B (`ɛ` U+025B, `ɔ` U+0254).
4. Appliquer le **Double Codage XAG** : associer systématiquement une icône distincte et une variation de forme à chaque couleur d'état (ennemi, allié, objectif, danger).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Information transmise uniquement par la couleur (ex: jauge ou icône rouge vs verte) | Ajouter immédiatement une différenciation géométrique (losange hachuré vs cercle plein) et une option de palette daltonisme (Deutéranopie, Protanopie, Tritanopie) | Respecter l'exigence obligatoire XAG (quality-standards.md) |
| Conteneur UI fixe tronquant une chaîne traduite avec expansion de +35 % | Remplacer la largeur fixe par un conteneur dynamique Auto-Wrap avec marge de sécurité de +35 % sans défilement horizontal | Synchroniser avec AUD-04 |
| Élément HUD restant affiché en permanence hors combat ou navigation active | Passer le widget en mode Dynamic Auto-Hide (disparition en fondu après 4 secondes d'inactivité) | Préserver l'immersion visuelle dans Kinshasa (DIR-03 / ART-01) |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/common-ui-and-xag-ergonomics.md`
- **Modèle Officiel de Livrable** : `templates/ui-screen-spec-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-ui-screen-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-ui-screen-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/ui-screen-spec-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-07` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des widgets supportent une expansion de texte de `+35 %` et affichent correctement `ɛ` et `ɔ`.
- [ ] Contraste typographique mesuré `>= 4.5:1` (texte standard) et `>= 7:1` (sous-titres sur fond semi-opaque).
- [ ] Navigation complète au pavé directionnel/manette et clavier/souris via les Input Action Tables de UE5 Common UI.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `PRD-06`, `AUD-04`, `DIR-05`.
