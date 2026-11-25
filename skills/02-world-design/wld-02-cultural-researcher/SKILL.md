---
name: wld-02-cultural-researcher
description: "Recherche culturelle, historique, linguistique, vestimentaire et musicale sur Kinshasa et la République Démocratique du Congo. Maintient le glossaire Lingala/Français Unicode (ɛ, ɔ) et garantit l'absence totale de clichés ou d'anachronismes."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-02
  department: 02-world-design
  stratum: 1
  version: "1.1.0"
  inputs:
    - "research-requests"
    - "knowledge/world-bible/cultural-guidelines.md"
    - "knowledge/world-bible/lingala-french-glossary.csv"
  outputs:
    - "cultural-research-brief.md"
    - "glossary-expansion-entries.csv"
  upstream_dependencies:
    - "DIR-03"
---

# `WLD-02` — Cultural Researcher (`wld-02-cultural-researcher`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Demande de vérification culturelle ou linguistique émise par un skill ayant rencontré un point `RESEARCH_REQUIRED`.
- Validation des expressions en lingala / français kinois utilisées dans les scripts (`NAR-02`), dialogues (`NAR-04`) et doublages (`AUD-04`).
- Documentation des tenues vestimentaires (`ART-03`), genres musicaux (`AUD-03`) et codes sociaux quotidiens de Kinshasa.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `research-requests`, `knowledge/world-bible/cultural-guidelines.md`, `knowledge/world-bible/lingala-french-glossary.csv`
- **Sorties produites** : `cultural-research-brief.md`, `glossary-expansion-entries.csv`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne conçoit pas les règles de gameplay (`GD-01`) ni l'équilibrage mathématique (`GD-03`).
- **Interdiction / Limite** : N'extrapole jamais un fait historique ou linguistique incertain : si une source primaire manque, le point reste marqué `RESEARCH_REQUIRED`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Consulter `knowledge/world-bible/cultural-guidelines.csv`, `lingala-french-glossary.csv` et `research/source-registry.csv`.
2. Fournir des références anthropologiques, linguistiques et urbaines précises (ex: travaux de Filip De Boeck sur Kinshasa, structure de la rumba congolaise, terminologie fluviale).
3. Pour chaque nouveau terme lingala introduit, spécifier sa graphie Unicode exacte (`ɛ`, `ɔ` et tons), son indice phonétique pour les comédiens (`AUD-04`), son registre et son sens en français et anglais.
4. Rédiger le dossier dans `templates/cultural-brief-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Terme argotique ou culturel d'origine incertaine ou non attesté à Kinshasa | Rejeter le terme et proposer une alternative attestée de lingala kinois ou marquer RESEARCH_REQUIRED | Protéger l'authenticité culturelle du jeu |
| Texte en lingala soumis avec des caractères ASCII dégradés ('e'/'o' au lieu de 'ɛ'/'ɔ') | Corriger systématiquement la graphie Unicode et mettre à jour lingala-french-glossary.csv | Synchroniser avec AUD-04 et GD-07 |
| Représentation vestimentaire ou architecturale caricaturale | Émettre une directive corrective immédiate appuyée sur la réalité urbaine contemporaine de Kinshasa | Escalader à DIR-03 en cas de blocage |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/kinshasa-cultural-reference.md`
- **Modèle Officiel de Livrable** : `templates/cultural-brief-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-cultural-brief.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-cultural-brief.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/cultural-brief-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des termes lingala fournis incluent la graphie Unicode (`ɛ`, `ɔ`), la phonétique et le contexte d'usage.
- [ ] Les sources documentaires sont citées et exemptes de tout stéréotype 'Afrique générique'.
- [ ] Le brief culturel est directement exploitable par `NAR-02`, `NAR-04`, `ART-02`, `ART-03` et `AUD-03`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `PRD-03`, `DIR-03`, `DIR-06`.
