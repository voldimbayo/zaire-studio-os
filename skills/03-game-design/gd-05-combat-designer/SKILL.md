---
name: gd-05-combat-designer
description: "Conception du système de combat urbain de ZAÏRE (SYS-CMB-MELEE) : affrontements à mains nues et à l'arme blanche (ITM-WPN-MACHETTE), timing image par image (Startup/Active/Recovery), hitstop, archétypes ennemis et régulation des assauts par Attack Tokens."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-05
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "game-systems-gd-01"
    - "lead-gd-directives-dir-05"
    - "animation-metrics-art-05"
  outputs:
    - "combat-design-bible.md"
    - "weapon-and-archetype-matrix.csv"
  upstream_dependencies:
    - "GD-01"
    - "DIR-05"
---

# `GD-05` — Combat Designer (`gd-05-combat-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Calibrage des coups, parades, esquives et sensations d'impact (Game Feel) de `CHR-PROTAG-KOFFI`.
- Conception d'un nouvel archétype d'ennemi (vigile portuaire, homme de main de `ORG-CARTEL-FLEUVE`, élite) pour `AI-01`.
- Réglage du système d'Attack Tokens et du comportement caméra dans les espaces urbains de Kinshasa.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `game-systems-gd-01`, `lead-gd-directives-dir-05`, `animation-metrics-art-05`
- **Sorties produites** : `combat-design-bible.md`, `weapon-and-archetype-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `GD-01`, `DIR-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne produit pas les fichiers d'animation `.fbx` (`ART-05`/`ART-06`) ni les systèmes de particules Niagara d'impact (`ART-09`).
- **Interdiction / Limite** : Interdit que plus de **2 ennemis au corps-à-corps** n'attaquent simultanément Koffi hors champ caméra (règle Attack Tokens).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Définir chaque attaque à 60 FPS en 3 phases exactes : **Startup (Anticipation lisible)**, **Active (Frames de collision hitbox)** et **Recovery (Fenêtre de punition/annulation)**.
2. Spécifier les paramètres de **Game Feel** : durée de Hitstop (`40 ms` sur coup léger, `85 ms` sur parade parfaite ou coup lourd), amplitude du Camera Shake et déclencheur `FGameplayTag`.
3. Configurer le budget d'**Attack Tokens** par archétype ennemi (`1 jeton` pour assaillant standard, `2 jetons` pour élite lourd, plafond global de l'escouade = `2 jetons` actifs simultanément).
4. Documenter la matrice complète dans `templates/combat-archetype-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Attaque ennemie avec un Startup < 18 frames (300 ms à 60 FPS) | Allonger l'animation d'anticipation à >= 22 frames (366 ms) avec un indice sonore clair (AUD-02) et visuel | Garantir une réaction humaine équitable et conforme à l'accessibilité PRD-06 |
| Combat déclenché dans un espace de largeur < 500 cm | Restreindre dynamiquement le plafond d'Attack Tokens à 1 seul assaillant actif et activer les animations de combat rapproché mural | Prévenir toute désorientation caméra |
| Latence mesurée entre l'input joueur et la première frame d'esquive/parade > 100 ms | Autoriser l'annulation (Animation Cancel) des 6 dernières frames de Recovery des attaques légères par la parade ou l'esquive | Maintenir la réactivité nerveuse exigée par DIR-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/frame-data-and-attack-tokens.md`
- **Modèle Officiel de Livrable** : `templates/combat-archetype-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-combat-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-combat-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/combat-archetype-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Toutes les attaques spécifient leurs frames Startup / Active / Recovery à 60 FPS et leur durée de Hitstop en ms.
- [ ] La règle des Attack Tokens (max 2 jetons simultanés) est explicitement paramétrée pour `AI-01`.
- [ ] Chaque arme ou capacité est reliée à un identifiant `ITM-*` et un tag `Ability.Melee.*` ou `State.Character.Combat.*`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `ENG-02`, `AI-01`, `ART-05`.
