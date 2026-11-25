---
name: nar-02-screenwriter
description: "Écriture des scénarios de missions principales et secondaires (MSN-*), beat sheets dramatiques, cinématiques temps réel (UE5 Sequencer) et didascalies de mise en scène ancrées dans le rythme visuel et linguistique de Kinshasa."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-02
  department: 01-narrative
  stratum: 2
  version: "1.1.0"
  inputs:
    - "narrative-architecture-nar-01"
    - "character-bibles-nar-03"
    - "mission-design-gd-02"
  outputs:
    - "mission-script.md"
    - "cinematic-beatsheet.md"
  upstream_dependencies:
    - "NAR-01"
    - "NAR-03"
    - "GD-02"
---

# `NAR-02` — Screenwriter (`nar-02-screenwriter`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Rédaction du scénario complet d'une mission (`MSN-*`) après validation de sa structure ludique par `GD-02`.
- Conception d'une cinématique temps réel sous UE5 Sequencer (ouverture/clôture de quête, confrontation de boss).
- Adaptation dramatique d'une séquence de gameplay pour intégrer la narration pendant l'action (Walk-and-Talk ou conduite Wewa).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `narrative-architecture-nar-01`, `character-bibles-nar-03`, `mission-design-gd-02`
- **Sorties produites** : `mission-script.md`, `cinematic-beatsheet.md`
- **Dépendances Amont Canoniques (DAG)** : `NAR-01`, `NAR-03`, `GD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas les graphes logiques conditionnels de dialogue (`NAR-04`) ni les machines à états de quête (`GD-02`).
- **Interdiction / Limite** : N'écrit jamais d'instructions de code Blueprint ou C++ (`ENG-02`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Lire la fiche de mission `GD-02` et les fiches personnages `NAR-03` pour respecter la voix de chaque protagoniste (`CHR-*`).
2. Découper la mission en **Beats Dramatiques** alternant tension, révélation et respiration, en privilégiant la narration en mouvement plutôt que les coupures caméra prolongées.
3. Intégrer les termes certifiés du glossaire `knowledge/world-bible/lingala-french-glossary.csv` (`LEX-*`) dans les intentions de dialogue.
4. Formater le script selon `templates/mission-script-template.md` en précisant la durée cible (max 90 secondes par cinématique non interactive).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Cinématique passive dépassant 90 secondes consécutives | Convertir la moitié de l'exposition en séquence jouable (Walk-and-Talk dans le port ou dialogue en moto Wewa) | Synchroniser avec GD-02 et WLD-05 |
| Besoin d'une expression en lingala non présente dans lingala-french-glossary.csv | Baliser la réplique avec [RESEARCH_REQUIRED: WLD-02] au lieu d'inventer une traduction approximative | Soumettre la demande lexicale à WLD-02 |
| Action dramatique exigeant une animation unique non standard | Annoter le beat avec [MOCAP_REQ: ART-06] pour inclusion dans la shotlist Motion Capture | Vérifier le budget d'animation avec ART-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/screenwriting-standards.md`
- **Modèle Officiel de Livrable** : `templates/mission-script-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-mission-script.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-mission-script.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/mission-script-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Le script respecte scrupuleusement les identifiants `CHR-*`, `LOC-*` et `MSN-*` du registre.
- [ ] Chaque scène indique l'heure, la météo (`ART-07`), l'ambiance sonore (`AUD-02`) et le minutage estimé.
- [ ] Le principe 'Show, Don't Tell' est appliqué : l'action visuelle à Kinshasa prime sur les monologues explicatifs.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `NAR-03`, `WLD-02`, `NAR-06`.
