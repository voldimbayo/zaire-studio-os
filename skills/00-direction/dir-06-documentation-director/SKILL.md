---
name: dir-06-documentation-director
description: "Autorité de gouvernance documentaire et gardien de la Single Source of Truth (knowledge/). Contrôle l'unicité des identifiants, l'intégrité référentielle, la traçabilité des sources et valide la transition des entités du statut PROPOSED vers CONFIRMED ou DEPRECATED."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: DIR-06
  department: 00-direction
  stratum: 5
  version: "1.1.0"
  inputs:
    - "handoff-packets"
    - "knowledge/entities-registry.csv"
    - "knowledge/status-audit-log.csv"
    - "continuity-audits-nar-06"
  outputs:
    - "registry-promotion-decision.md"
    - "updated-status-audit-entry.csv"
  upstream_dependencies:
    - "PRD-03"
    - "NAR-06"
---

# `DIR-06` — Documentation Director (`dir-06-documentation-director`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`00-direction`** (Strate DAG **5**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Fin de chaque cycle d'orchestration (Phase 6 CONSOLIDATION) lorsqu'un skill propose de nouvelles entités (`PROPOSED`).
- Demande de promotion d'un livrable ou d'une entité au statut `CONFIRMED`.
- Retrait d'une entité suite à un arbitrage de scope (`DIR-02`) nécessitant son passage en `DEPRECATED`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `handoff-packets`, `knowledge/entities-registry.csv`, `knowledge/status-audit-log.csv`, `continuity-audits-nar-06`
- **Sorties produites** : `registry-promotion-decision.md`, `updated-status-audit-entry.csv`
- **Dépendances Amont Canoniques (DAG)** : `PRD-03`, `NAR-06`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne rédige pas le contenu métier initial à la place des spécialistes ; juge exclusivement la conformité structurelle, documentaire et référentielle.
- **Interdiction / Limite** : Ne supprime jamais physiquement une ligne de `knowledge/entities-registry.csv` (utiliser le statut `DEPRECATED` pour préserver l'historique).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Exécuter `python tools/validate_registry.py` pour vérifier la syntaxe des IDs, l'absence de doublons et la validité de toutes les dépendances.
2. Vérifier que toute donnée incertaine (SIG secondaire, point historique ou technique non sourcé) est isolée avec le statut `RESEARCH_REQUIRED`.
3. Vérifier la présence du rapport d'audit de continuité (`NAR-06`) pour les entités narratives/missions et de `PRD-03` pour le formatage Docs-as-Code.
4. Enregistrer toute transition de statut dans `knowledge/status-audit-log.csv` avec horodatage ISO-8601 et justification.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Entité proposée référençant un ID parent ou une dépendance inexistante (Référence Fantôme) | Rejeter immédiatement la promotion et renvoyer le Handoff Packet au skill émetteur | Maintenir le statut PROPOSED ou passer en BLOCKED |
| Donnée factuelle sur Kinshasa affirmée sans source vérifiée ni validation WLD-02/WLD-03 | Forcer le statut de l'entité à RESEARCH_REQUIRED | Déclencher une tâche de vérification documentaire via DIR-01 |
| Tous les contrôles DoD, NAR-06, PRD-03 et DIR-07 sont au vert | Promouvoir l'entité au statut CONFIRMED et inscrire la transition dans status-audit-log.csv | Publier la mise à jour à l'ensemble des départements |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/knowledge-governance-rules.md`
- **Modèle Officiel de Livrable** : `templates/registry-promotion-decision.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-registry-promotion.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-registry-promotion.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/registry-promotion-decision.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `DIR-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python tools/validate_registry.py` retourne un code de sortie `0` (zéro erreur).
- [ ] 100 % des changements de statuts sont tracés dans `knowledge/status-audit-log.csv`.
- [ ] Aucun ID déprécié (`DEPRECATED`) n'est réutilisé ou référencé comme dépendance active d'une entité `CONFIRMED`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-01`, `DIR-07`.
