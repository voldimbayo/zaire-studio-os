---
name: nar-01-narrative-architect
description: "Conception de l'architecture narrative macroscopique de ZAÏRE : structure en 3 actes, arcs thématiques, embranchements majeurs à conséquences persistantes par commune de Kinshasa (DST-*) et alignement ludo-narratif avec les systèmes de monde ouvert."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-01
  department: 01-narrative
  stratum: 1
  version: "1.1.0"
  inputs:
    - "creative-pillars-dir-03"
    - "kinshasa-world-bible-wld-01"
    - "cultural-briefs-wld-02"
  outputs:
    - "narrative-architecture.md"
    - "branching-consequences-matrix.csv"
  upstream_dependencies:
    - "DIR-03"
    - "WLD-01"
    - "WLD-02"
---

# `NAR-01` — Narrative Architect (`nar-01-narrative-architect`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Structuration initiale ou révision des actes principaux du jeu ZAÏRE.
- Conception d'un embranchement narratif majeur modifiant l'état politique, économique ou sécuritaire d'une commune (`DST-*`).
- Alignement entre la progression dramatique de `CHR-PROTAG-KOFFI` et le déblocage des systèmes de gameplay (`GD-01`/`GD-04`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `creative-pillars-dir-03`, `kinshasa-world-bible-wld-01`, `cultural-briefs-wld-02`
- **Sorties produites** : `narrative-architecture.md`, `branching-consequences-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `WLD-01`, `WLD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'écrit jamais les dialogues réplique par réplique (`NAR-04`) ni les scripts de scènes détaillés (`NAR-02`).
- **Interdiction / Limite** : Ne crée pas les profils psychologiques micro-individuels des personnages secondaires (`NAR-03`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Ancrer chaque acte dramatique dans un territoire précis de Kinshasa (`DST-GOMBE`, `DST-KALAMU`, `DST-MATONGE`, `DST-LIMETE`, `DST-NGALIEMA`) en consultant `knowledge/world-bible/kinshasa-districts.md`.
2. Définir les **Points de Pivot (Plot Pivots)** où les choix du joueur modifient durablement les variables d'état du monde (`SYS-WLD-REPUTATION`, Data Layers UE5).
3. Vérifier que chaque arc narratif s'exprime par les boucles de gameplay (infiltration portuaire, courses Wewa, réseaux d'informateurs radio `ORG-RADIO-KIN`) et non uniquement par des cinématiques passives.
4. Documenter la matrice d'embranchements dans `templates/act-structure-template.md` et soumettre à `NAR-06`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Embranchement créant une divergence exponentielle ingérable en production | Appliquer le modèle 'Diamond Branching' (divergence locale forte sur le quartier, reconvergence sur les jalons d'actes avec mémoire d'état persistante) | Faire valider le coût de production par DIR-02 |
| Arc narratif déconnecté de l'environnement urbain de Kinshasa | Rattacher obligatoirement le conflit à une institution ou réalité locale (port ONATRA, transport, coupures réseau, scène musicale) | Consulter WLD-01 et WLD-02 |
| Mort potentielle d'un personnage clé avant sa dernière mission critique | Interdire la létalité hors noeud canonique ou prévoir un remplaçant systémique documenté | Soumettre le graphe d'état à NAR-06 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/macro-narrative-design.md`
- **Modèle Officiel de Livrable** : `templates/act-structure-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-act-architecture.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-act-architecture.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/act-structure-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque acte définit son conflit central, ses communes (`DST-*`), ses factions (`ORG-*`) et son évolution du protagoniste (`CHR-PROTAG-KOFFI`).
- [ ] 100 % des embranchements majeurs produisent un impact mesurable sur `SYS-WLD-REPUTATION` ou sur les Data Layers du quartier.
- [ ] Aucune contradiction avec les 3 piliers créatifs de `DIR-03`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `NAR-06`, `DIR-03`.
