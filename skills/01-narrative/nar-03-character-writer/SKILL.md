---
name: nar-03-character-writer
description: "Conception biographique, psychologique, linguistique et relationnelle des personnages (CHR-*) et des familles/dynasties (FAM-*) de ZAÏRE. Définit la voix distinctive, les motivations, les failles et le registre de langue (français soutenu, français kinois, lingala)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-03
  department: 01-narrative
  stratum: 2
  version: "1.1.0"
  inputs:
    - "narrative-architecture-nar-01"
    - "kinshasa-world-bible-wld-01"
    - "cultural-guidelines-wld-02"
  outputs:
    - "character-bible-sheet.md"
    - "family-lineage-dossier.md"
    - "character-relationship-matrix.csv"
  upstream_dependencies:
    - "NAR-01"
    - "WLD-01"
    - "WLD-02"
---

# `NAR-03` — Character Writer (`nar-03-character-writer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création d'un nouveau personnage principal, antagoniste, allié ou figure de quartier (`CHR-*`).
- Structuration d'une famille ou dynastie kinoise (`FAM-*`) et de son ancrage socio-économique.
- Relecture de conformité des voix de personnages sur un script produit par `NAR-02` ou `NAR-04`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `narrative-architecture-nar-01`, `kinshasa-world-bible-wld-01`, `cultural-guidelines-wld-02`
- **Sorties produites** : `character-bible-sheet.md`, `family-lineage-dossier.md`, `character-relationship-matrix.csv`
- **Dépendances Amont Canoniques (DAG)** : `NAR-01`, `WLD-01`, `WLD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne définit pas la topologie 3D, les shaders de peau ou le système modulaire de vêtements (`ART-03`).
- **Interdiction / Limite** : Ne calibre pas les points de vie, dégâts ou arbres de comportement IA de combat (`GD-05`/`AI-01`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Attribuer un identifiant conforme `CHR-[ROLE]-[SLUG]` ou `FAM-[NOM]` et vérifier son unicité dans `knowledge/entities-registry.csv`.
2. Ancrer le personnage dans une commune d'origine (`DST-*`) et une organisation ou famille existante.
3. Définir sa **Signature Linguistique** (ratio français/lingala, rythme des phrases, vocabulaire métier, termes `LEX-*` privilégiés).
4. Documenter son arc psychologique (Désir conscient vs Besoin profond vs Faille) dans `templates/character-bible-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Deux personnages majeurs partagent le même registre de langue et la même posture morale | Différencier immédiatement leur sociolecte (ex: français technocratique de la Gombe vs phrasé imagé et musical de Matonge) | Valider l'authenticité sociolinguistique avec WLD-02 |
| Personnage créé sans lien avec le tissu social ou familial de Kinshasa | Rattacher le personnage à une famille (FAM-*), une faction (ORG-*) ou un lieu de vie (LOC-*) | Interdire les archétypes génériques apatrides |
| Incohérence de ton détectée dans un script NAR-02 | Émettre une demande de réécriture ciblée des répliques hors-caractère | Consigner l'observation pour NAR-06 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/character-psychology-and-voice.md`
- **Modèle Officiel de Livrable** : `templates/character-bible-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-character-bible.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-character-bible.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/character-bible-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque fiche `CHR-*` comporte une voix reconnaissable à l'aveugle sans lire le nom du locuteur.
- [ ] Les relations avec les autres `CHR-*`, `FAM-*` et `ORG-*` sont bidirectionnelles et explicites.
- [ ] Les recommandations vestimentaires et d'attitude fournissent un brief actionnable pour `ART-03` et `ART-06`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `WLD-02`, `NAR-06`, `DIR-06`.
