---
name: prd-02-risk-manager
description: "Identification, quantification (Probabilité x Impact sur 25) et plans de mitigation des risques techniques, culturels, juridiques (licences musicales rumba/ndombolo, marques) et de planning de ZAÏRE STUDIO OS."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: PRD-02
  department: 08-production-quality
  stratum: 1
  version: "1.1.0"
  inputs:
    - "research-gaps-phase-1"
    - "technical-budgets-dir-04"
    - "cultural-briefs-wld-02"
  outputs:
    - "risk-register.csv"
    - "critical-risk-mitigation-plan.md"
  upstream_dependencies:
    - "DIR-02"
    - "DIR-04"
    - "WLD-02"
---

# `PRD-02` — Risk Manager (`prd-02-risk-manager`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`08-production-quality`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Évaluation d'une lacune documentaire ou technique identifiée dans `research/research-gaps.md`.
- Introduction d'une dépendance externe (musique sous licence tiers dans `AUD-03`, données SIG secondaires de Kinshasa dans `WLD-03`/`ENG-04`).
- Apparition d'un blocage récurrent ou d'une dérive de performance menaçant un jalon `DIR-02`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `research-gaps-phase-1`, `technical-budgets-dir-04`, `cultural-briefs-wld-02`
- **Sorties produites** : `risk-register.csv`, `critical-risk-mitigation-plan.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-02`, `DIR-04`, `WLD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne corrige pas lui-même le bug C++ ou le mesh 3D ; impose et suit le plan de contingence assigné au skill propriétaire.
- **Interdiction / Limite** : Interdit de laisser un risque critique (Score `>= 12/25`) sans plan de mitigation actif et sans responsable désigné.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Coter chaque risque selon sa **Probabilité $P \in [1..5]$** et son **Impact $I \in [1..5]$**, produisant un Score de Criticité $S = P \times I \in [1..25]$.
2. Classer les risques en 3 niveaux : `LOW (1-5)`, `MEDIUM (6-11)`, `CRITICAL (12-25)`.
3. Pour tout risque `CRITICAL (>= 12)`, définir obligatoirement : (1) Action Préventive immédiate, (2) Solution de Repli (Fallback technique ou créatif déjà prêt), (3) Skill Propriétaire.
4. Mettre à jour `templates/risk-register-template.csv` et notifier `DIR-02` et `DIR-07`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Risque de strike DMCA / expiration de licence sur les musiques de Radio Lokole (Score 4x4 = 16/25) | Exiger d'AUD-03 qu'un Switch Wwise SW_Music_LicenseMode bascule à 100 % sur des compositions originales du studio en mode Streamer Safe | Neutraliser l'impact juridique et commercial |
| Couverture SIG/OSM hétérogène dans les communes secondaires comme DST-MASINA (Score 4x3 = 12/25) | Isoler DST-MASINA en statut RESEARCH_REQUIRED hors du Vertical Slice et utiliser le générateur de subdivision paramétrique WLD-03/ENG-04 | Protéger le planning du Vertical Slice DIR-02 |
| Risque de dépassement du budget CPU/GPU dans les marchés denses sous la pluie (Score 3x5 = 15/25) | Activer le délestage dynamique : réduction de 40 % de la foule en plein air sous l'averse (AI-02) et bascule automatique des réflexions Lumen sur Surface Cache > 0.40 Roughness (ENG-06) | Garantir le maintien des 60 FPS (16.6 ms) |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/risk-scoring-and-mitigation.md`
- **Modèle Officiel de Livrable** : `templates/risk-register-template.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-risk-register.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-risk-register.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/risk-register-template.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `PRD-02` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] 100 % des lacunes de `research/research-gaps.md` sont couvertes par une entrée dans `risk-register.csv`.
- [ ] 100 % des risques ayant un score `>= 12/25` possèdent un plan de mitigation et un fallback opérationnel.
- [ ] Chaque risque est rattaché à un skill propriétaire unique (`WLD-03`, `AUD-03`, `ENG-07`, etc.).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-02`, `DIR-04`, `DIR-07`.
