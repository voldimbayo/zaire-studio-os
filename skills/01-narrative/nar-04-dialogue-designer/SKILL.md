---
name: nar-04-dialogue-designer
description: "Conception des arbres de dialogue interactifs, banques de répliques systémiques (barks de combat, foule, trafic) et métadonnées de mise en scène procédurale (tags d'émotion, cadrage caméra automatique, conditions Gameplay Tags)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-04
  department: 01-narrative
  stratum: 2
  version: "1.1.0"
  inputs:
    - "mission-scripts-nar-02"
    - "character-bibles-nar-03"
    - "quest-states-gd-02"
    - "lingala-french-glossary.csv"
  outputs:
    - "dialogue-tree.json"
    - "contextual-barks-table.csv"
  upstream_dependencies:
    - "NAR-02"
    - "NAR-03"
    - "GD-02"
---

# `NAR-04` — Dialogue Designer (`nar-04-dialogue-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Implémentation des dialogues à choix multiples d'une mission (`MSN-*`) ou d'un commerçant/informateur.
- Création des banques de barks réactifs pour l'IA de combat (`AI-01`), la foule de Kinshasa (`AI-02`) ou le trafic (`AI-03`).
- Génération des métadonnées de caméra procédurale (méthodologie Ubisoft Quebec `SRC-014`) pour les quêtes secondaires.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `mission-scripts-nar-02`, `character-bibles-nar-03`, `quest-states-gd-02`, `lingala-french-glossary.csv`
- **Sorties produites** : `dialogue-tree.json`, `contextual-barks-table.csv`
- **Dépendances Amont Canoniques (DAG)** : `NAR-02`, `NAR-03`, `GD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne code pas le sous-système C++ de lecture de dialogues (`ENG-02`) ni la compilation binaire `.locres` (`AUD-04`).
- **Interdiction / Limite** : N'autorise aucune réplique dépassant **20 mots par bulle UI** afin de garantir la lisibilité et la tolérance d'expansion de +35 % (`AUD-04`/`PRD-06`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer la conversation en noeuds atomiques identifiés (`node_id`), reliés par des conditions basées sur `knowledge/technical-specs/gameplay-tags-taxonomy.csv`.
2. Attacher à chaque noeud un tag d'émotion (`NEUTRAL`, `TENSE`, `ANGRY`, `WARM`, `URGENT`, `IRONIC`) et une directive de caméra procédurale (`OTS_LEFT`, `OTS_RIGHT`, `CLOSE_UP`, `TWO_SHOT`, `WIDE_ESTABLISHING`).
3. Prévoir systématiquement des répliques d'interruption et de reprise (`ON_INTERRUPT_COMBAT`, `ON_INTERRUPT_LEAVE`, `ON_RESUME`) pour éviter tout soft-lock en monde ouvert.
4. Valider le fichier JSON généré en exécutant `scripts/validate_dialogue_json.py`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Réplique dépassant 20 mots dans un noeud de dialogue | Scinder la réplique en 2 noeuds consécutifs ou condenser le texte | Garantir la conformité au validateur validate_dialogue_json.py et aux normes XAG |
| Noeud non terminal dépourvu de transition sortante (impasse) | Relier le noeud à une sortie de repli valide ou marquer explicitement is_terminal: true | Corriger avant tout handoff vers AUD-04 et ENG-02 |
| Dialogue de mission susceptible d'être interrompu par une averse ou une collision routière | Ajouter les hooks système ON_INTERRUPT et ON_RESUME reliés à la machine à états GD-02 | Empêcher toute perte de progression narrative |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/procedural-dialogue-staging.md`
- **Modèle Officiel de Livrable** : `templates/dialogue-tree-schema.json`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-dialogue-and-barks.md`
- `scripts/validate_dialogue_json.py` : Script exécutable déterministe associé à `NAR-04` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-dialogue-and-barks.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/dialogue-tree-schema.json` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/01-narrative/nar-04-dialogue-designer/scripts/validate_dialogue_json.py` valide le graphe avec 0 erreur.
- [ ] 100 % des répliques font `<= 20 mots` et identifient le locuteur via un ID `CHR-*` valide.
- [ ] Les barks contextuels couvrent au moins 4 variations par déclencheur pour éviter la répétition auditive.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `GD-02`, `AUD-04`, `NAR-06`.
