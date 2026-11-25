# Architecture ECS UE5 Mass Crowd — Marchés de Kinshasa (`AI-02`)

## 1. Anneaux de Level of Detail (MassRepresentation)
| Anneau LOD | Distance Caméra | Représentation Visuelle (`ART-03`/`ART-05`) | Physique & Navigation | Coût CPU Unitaire |
| :--- | :--- | :--- | :--- | :--- |
| **LOD 0 (Hydraté)** | `0 à 25 m` | `ACharacter` complet + Barks `NAR-04` | Capsule Chaos + Smart Objects | `~0.095 ms` (Pool max 18-24) |
| **LOD 1 (Médian)** | `25 à 80 m` | `USkeletalMeshComponent` partagé (URO 30Hz) | `ZoneGraph` + Évitement RVO | `~0.0045 ms` |
| **LOD 2 (Lointain)** | `80 à 250 m` | `UInstancedStaticMesh` + Vertex Anim Texture (VAT) | `ZoneGraph` cinématique pur | `~0.0018 ms` |
| **LOD 3 (Offscreen)** | `> 250 m` | Culled (0 draw call) | Progression statistique basse fréq. | `< 0.0003 ms` |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AI-02` — Strate DAG 3)

- **Architecture IA Hybride : State Trees, MassEntity & ZoneGraph (UE 5.8)** (`SRC-004`, `SRC-013`, `SRC-015`, `SRC-020`, `SRC-032`) :
  - **IA Individuelle (`AI-01`, Budget `<= 2.5 ms`)** : Plafond strict de `24 acteurs ACharacter` actifs simultanément ; `State Trees` UE 5.8 + time-slicing EQS (`<= 0.35 ms/frame`).
  - **Foule ECS (`AI-02`, Budget `<= 2.0 ms` pour `500-800 entités`)** : Anneau 0 (`0-25 m`, `<= 18` acteurs hydratés), Anneau 1 (`25-80 m`, Skeletal Mesh URO 30Hz + RVO), Anneau 2 (`80-250 m`, ISM animé par Vertex Animation Texture VAT).
  - **Trafic & Escalade Policière PCR (`AI-03`, `AI-04`)** : Réseau `ZoneGraph` généré en amont par `ENG-04` ; sous-voies virtuelles inter-files (`130-150 cm`) pour `VEH-MOTO-WEWA-01` lorsque le flux descend sous `20 km/h` ; Watchdog Anti-Deadlock (`8.0 s`) ; escalade graduée `SYS-LAW-ESCALATION` (`State.Law.AlertLevel.1..3`) avec `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-04`, `ART-03`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `open-world-density-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `modular-npc-kits-art-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cpu-budgets-dir-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `mass-crowd-architecture.md` : Doit respecter le gabarit `templates/mass-crowd-spec.md` et passer l'audit croisé.
  - `district-crowd-density.csv` : Doit respecter le gabarit `templates/mass-crowd-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ENG-07`, `PRD-05`, `DIR-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Budget CPU Mass estimé > 2.0 ms par check_mass_budget.py | Blocage / Dégradation si ignoré | Réduire le rayon d'hydratation de l'Anneau 0 de 25m à 18m et basculer 30 % des entités LOD1 vers la représentation VAT Instanced Static Mesh (LOD2) | Escalade vers Maintenir le frametime global sous 16.6 ms |
| Mode de Défaillance 2: Averse équatoriale déclenchée (World.Weather.TropicalStorm) | Blocage / Dégradation si ignoré | Basculer la vitesse de déplacement des piétons sur ZoneGraph à 1.6x vers les tags d'abris (auvents de 180 cm de WLD-03) et réduire la densité de spawn en plein air de 60 % | Escalade vers Simuler un comportement urbain kinois crédible |
| Mode de Défaillance 3: Collision entre une moto Wewa du joueur et un piéton Mass LOD1 | Blocage / Dégradation si ignoré | Hydrater instantanément l'entité touchée en acteur physique Chaos ragdoll/esquive et déclencher le bark BRK-CROWD-01 | Escalade vers Assurer une continuité physique sans pop visuel |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AI-02`)

- [ ] **Contrôle DoD #1** : `python skills/04-ai-simulation/ai-02-crowd-simulation-specialist/scripts/check_mass_budget.py` retourne un code `0` (`within_budget: true`).
- [ ] **Contrôle DoD #2** : 500+ entités sont simulées simultanément à `DST-MATONGE` pour un coût CPU `<= 2.0 ms`.
- [ ] **Contrôle DoD #3** : L'hydratation/déshydratation entre `MassEntity` et `ACharacter` utilise un pool pré-alloué garantissant 0 hitch d'allocation mémoire.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
