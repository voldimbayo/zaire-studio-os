# Architecture des Fichiers & Répertoires — ZAÏRE STUDIO OS (`file-structure.md`)

Cette arborescence définit l'organisation complète et réconciliée du dépôt **ZAÏRE STUDIO OS (v1.1.0)**.

```text
zaire-studio-os/
├── README.md                                # Point d'entrée global du système
├── CLAUDE.md                                # Instructions globales d'orchestration pour les agents IA
├── CHANGELOG.md                             # Journal des versions (v1.0.0 -> v1.1.0)
├── VERSION                                  # Version courante du système (1.1.0)
│
├── research/                                # [PHASE 1] Base documentaire vérifiée (SRC-001 à SRC-032)
│   ├── README.md
│   ├── research-index.md
│   ├── industry-methodologies.md
│   ├── technical-reference.md
│   ├── skills-discovery.md
│   ├── skills-coverage-matrix.md
│   ├── research-gaps.md
│   ├── source-registry.csv
│   └── source-registry.md
│
├── architecture/                            # [PHASE 2 & 5] Architecture système & contrats réconciliés
│   ├── system-architecture.md
│   ├── department-map.md
│   ├── skills-catalog.md
│   ├── skill-dependencies.md
│   ├── orchestration-protocol.md
│   ├── knowledge-management.md
│   ├── quality-standards.md
│   └── file-structure.md
│
├── knowledge/                               # [COUCHE 2] Single Source of Truth (Registre, Bible, Specs)
│   ├── entities-registry.csv                # Registre maître (CHR, FAM, ORG, DST, LOC, MSN, ITM, VEH, SYS)
│   ├── status-audit-log.csv                 # Historique des transitions (PROPOSED -> CONFIRMED / BLOCKED)
│   ├── world-bible/
│   │   ├── kinshasa-districts.md            # Référentiel des communes (Gombe, Matonge, Limete, Kalamu, Bandal...)
│   │   ├── cultural-guidelines.md           # Codes sociaux, musique, architecture, authenticité RDC
│   │   └── lingala-french-glossary.csv      # Lexique normalisé multilingue (support Unicode ɛ, ɔ)
│   └── technical-specs/
│       ├── spatial-metrics.md               # Gabarits personnage, caméra, couverts (100/200cm), voirie (>=350cm)
│       ├── performance-budgets.csv          # Budgets CPU/GPU/RAM/VRAM par sous-système UE 5.8
│       └── gameplay-tags-taxonomy.csv       # Arborescence officielle des Gameplay Tags UE 5.8
│
├── schemas/                                 # Schémas JSON formels (Frontmatter, Registre, Task Envelope)
├── templates/                               # Modèles transversaux (Handoff Packet, ADR)
│
├── skills/                                  # [COUCHE 0 & 1] 57 Agent Skills (7 Direction + 50 Métiers)
│   ├── 00-direction/                        # dir-01 à dir-07
│   ├── 01-narrative/                        # nar-01 à nar-06
│   ├── 02-world-design/                     # wld-01 à wld-06
│   ├── 03-game-design/                      # gd-01 à gd-07
│   ├── 04-ai-simulation/                    # ai-01 à ai-04
│   ├── 05-art-animation/                    # art-01 à art-09
│   ├── 06-audio-localization/               # aud-01 à aud-04
│   ├── 07-engineering/                      # eng-01 à eng-08
│   └── 08-production-quality/               # prd-01 à prd-06
│
├── production/                              # [PHASE 5] Artefacts réels générés par les 5 scénarios fonctionnels
│   ├── scenario-1-district-bandal/          # Spécification MD/JSON, blockout, registre bâtiments, économie
│   ├── scenario-2-protagonist-koffi/        # Biographie, graphe relationnel JSON, progression
│   ├── scenario-3-mission-onatra/           # Spécification mission, dialogue JSON, table L10n, audit XAG
│   ├── scenario-4-traffic-and-police/       # Configuration ZoneGraph, intervention PCR, rapport perf JSON
│   ├── scenario-5-crowd-simulation/         # Configuration MassCrowd UE 5.8, budget CPU/VRAM
│   └── validation-reports/                  # Rapports de validation produits sur les fichiers réels
│
├── tools/                                   # Outillage Python de compilation, validation et packaging
├── tests/                                   # Suite de tests unitaires, d'intégration et de parité
│   └── fixtures/                            # Jeux de données de test isolés des artefacts de production
├── docs/                                    # Index des skills, registre DAG canonique, guides Claude.ai
├── audit/                                   # Rapports d'audit Phase 4, Revue Indépendante & Phase 5
└── releases/                                # Archives ZIP (57 individuelles, 9 départements, bundle global, backup)
```

---

## Structure Interne Standardisée d'un Répertoire Skill
Chaque dossier de skill sous `skills/<department>/<skill-slug>/` suit strictement cette anatomie :
```text
<skill-slug>/
├── SKILL.md                  # Frontmatter YAML (name, description, metadata) + Instructions opérationnelles
├── references/               # Référentiel technique approfondi, tables de paramètres, checklists et sources SRC-*
│   └── <domain-reference>.md
├── templates/                # Modèles de livrables prêts à l'emploi (Markdown, CSV ou JSON)
│   └── <deliverable-template>
├── examples/                 # Exemple concret d'exécution appliqué à Kinshasa
│   └── <sample-deliverable>.md
└── scripts/                  # (Optionnel) Validateurs et simulateurs Python déterministes acceptant --file
    └── <validator>.py
```
*(Note de réconciliation Phase 5 : L'ancien nom provisoire `assets/` mentionné en Phase 2 a été unifié en `templates/` et `examples/` dans l'ensemble du système.)*
