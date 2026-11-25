---
name: wld-01-worldbuilding-architect
description: "Conception macroscopique du monde de Kinshasa dans ZAÏRE. Définit l'identité socio-économique, architecturale, sécuritaire et sensorielle de chaque commune (DST-*), leurs frontières et leurs interactions systémiques dans la World Bible."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: WLD-01
  department: 02-world-design
  stratum: 1
  version: "1.1.0"
  inputs:
    - "creative-pillars-dir-03"
    - "cultural-research-wld-02"
    - "urban-morphology-wld-03"
  outputs:
    - "district-profile.md"
    - "kinshasa-world-bible-update.md"
  upstream_dependencies:
    - "DIR-03"
    - "WLD-02"
    - "WLD-03"
---

# `WLD-01` — Worldbuilding Architect (`wld-01-worldbuilding-architect`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`02-world-design`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Création ou mise à jour du profil d'une commune de Kinshasa (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`, `DST-NGALIEMA`, `DST-MASINA`).
- Définition des contrastes sociaux, économiques et de présence des factions (`ORG-*`) entre deux quartiers.
- Cadrage initial avant le découpage spatial Open World (`WLD-04`) et l'écriture des arcs d'actes (`NAR-01`).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `creative-pillars-dir-03`, `cultural-research-wld-02`, `urban-morphology-wld-03`
- **Sorties produites** : `district-profile.md`, `kinshasa-world-bible-update.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `WLD-02`, `WLD-03`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne réalise pas le placement précis des Points d'Intérêt sur la grille World Partition (`WLD-04`) ni le blockout 3D (`WLD-05`).
- **Interdiction / Limite** : N'invente aucune donnée démographique ou topographique sans validation préalable par `WLD-02` et `WLD-03`.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Enregistrer ou vérifier l'identifiant `DST-[COMMUNE]` dans `knowledge/entities-registry.csv` et `knowledge/world-bible/kinshasa-districts.md`.
2. Spécifier les 4 couches identitaires de la commune : (1) Sociologie & Économie, (2) Morphologie & Verticalité, (3) Signature Visuelle & Sonore, (4) Factions & Gameplay dominant.
3. Associer le Gameplay Tag de territoire (`World.District.*` dans `knowledge/technical-specs/gameplay-tags-taxonomy.csv`).
4. Générer la fiche complète selon `templates/district-profile-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Commune dont les données SIG secondaires sont incomplètes (ex: DST-MASINA) | Maintenir explicitement le statut RESEARCH_REQUIRED sur les sous-secteurs non vérifiés | Transmettre une requête ciblée à WLD-03 |
| Deux communes présentent la même densité de foule et la même ambiance visuelle | Accentuer le contraste structurel (ex: tours administratives et port industriel de Gombe vs galeries musicales et marchés nocturnes de Matonge) | Faire valider la différenciation par DIR-03 et ART-01 |
| Introduction d'une nouvelle faction dans un quartier | Vérifier la cohérence territoriale avec NAR-05 et mettre à jour les dépendances dans entities-registry.csv | Soumettre à DIR-06 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/kinshasa-macro-worldbuilding.md`
- **Modèle Officiel de Livrable** : `templates/district-profile-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-district-profile.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-district-profile.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/district-profile-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `WLD-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque fiche `DST-*` définit clairement ses communes limitrophes, son landmark directeur (`LOC-*`) et ses densités cibles de foule/trafic.
- [ ] Alignement total avec `knowledge/world-bible/kinshasa-districts.md` et `cultural-guidelines.md`.
- [ ] Validation créative obtenue auprès de `DIR-03`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `WLD-02`, `WLD-03`, `DIR-03`.
