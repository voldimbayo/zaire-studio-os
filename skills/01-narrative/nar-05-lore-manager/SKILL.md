---
name: nar-05-lore-manager
description: "Gouvernance de l'encyclopédie canonique (Lore) de ZAÏRE, de la chronologie historique et fictionnelle, des dossiers d'organisations/factions (ORG-*) et des textes diégétiques urbains (émissions de Radio Lokole, enseignes peintes, presse, archives portuaires)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: NAR-05
  department: 01-narrative
  stratum: 2
  version: "1.1.0"
  inputs:
    - "kinshasa-world-bible-wld-01"
    - "cultural-research-wld-02"
    - "narrative-architecture-nar-01"
  outputs:
    - "organization-dossier.md"
    - "diegetic-media-pack.md"
    - "master-timeline.csv"
  upstream_dependencies:
    - "WLD-01"
    - "WLD-02"
    - "NAR-01"
---

# `NAR-05` — Lore Manager (`nar-05-lore-manager`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`01-narrative`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou enrichissement d'une faction, entreprise, syndicat ou média in-game (`ORG-*`).
- Rédaction de contenus diégétiques pour habiller l'environnement (`ART-02` : affiches, graffitis, enseignes) ou alimenter `ORG-RADIO-KIN` (`AUD-03`) et le téléphone de Koffi (`GD-07`).
- Vérification de la chronologie des événements précédant le début de l'Acte I.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `kinshasa-world-bible-wld-01`, `cultural-research-wld-02`, `narrative-architecture-nar-01`
- **Sorties produites** : `organization-dossier.md`, `diegetic-media-pack.md`, `master-timeline.csv`
- **Dépendances Amont Canoniques (DAG)** : `WLD-01`, `WLD-02`, `NAR-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : N'invente jamais de faits historiques réels sur la RDC qui contrediraient les dossiers documentaires de `WLD-02`.
- **Interdiction / Limite** : Ne modifie pas la structure des quêtes principales (`GD-02`/`NAR-01`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Enregistrer toute nouvelle faction sous un identifiant `ORG-[TYPE]-[SLUG]` dans `knowledge/entities-registry.csv` au statut `PROPOSED`.
2. Définir pour chaque organisation son territoire d'influence (`DST-*`), ses dirigeants (`CHR-*`), ses ressources économiques et son identité visuelle/sonore.
3. Produire des textes diégétiques courts et percutants (bulletins flash de `ORG-RADIO-KIN` réagissant aux missions terminées, slogans d'enseignes pour `WLD-06`/`ART-02`).
4. Vérifier l'alignement chronologique de chaque événement dans la ligne du temps maître.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Besoin d'une référence à une institution réelle de Kinshasa | Utiliser un équivalent fictionnel respectueux ou le statut RESEARCH_REQUIRED pour validation juridique PRD-02 et culturelle WLD-02 | Éviter tout risque de diffamation ou d'inexactitude |
| Mission principale terminée par le joueur | Générer systématiquement 2 variantes de bulletin radio (ORG-RADIO-KIN) correspondant aux 2 approches possibles du joueur | Renforcer la réactivité du monde ouvert |
| Texte d'enseigne urbaine destiné aux textures 3D (ART-02) | Fournir le texte exact avec vérification orthographique française/lingala Unicode | Empêcher toute faute de frappe gravée dans les textures PBR |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/lore-and-diegetic-media.md`
- **Modèle Officiel de Livrable** : `templates/organization-dossier-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-organization-dossier.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-organization-dossier.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/organization-dossier-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `NAR-05` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque dossier `ORG-*` est relié à au moins un quartier `DST-*` et un personnage `CHR-*`.
- [ ] La chronologie ne comporte aucun chevauchement ou paradoxe temporel.
- [ ] Les textes diégétiques respectent la charte linguistique (`cultural-guidelines.md`).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `WLD-02`, `NAR-06`, `PRD-03`.
