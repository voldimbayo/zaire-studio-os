# Gouvernance des Jalons AAA (`DIR-02`)

## 1. Grille des Jalons de Production ZAÏRE
- **Vertical Slice (VS)** : 1 quartier complet (`DST-GOMBE` -> `LOC-GOMBE-PORT` + `DST-MATONGE` -> `LOC-MATONGE-VICTOIRE`), 1 mission principale (`MSN-MAIN-001-ARRIVEE`), boucle complète combat/infiltration/conduite Wewa à 60 FPS (`<= 16.6 ms`).
- **Feature Complete (Alpha)** : 100 % des systèmes (`SYS-*`) et quêtes principales jouables de bout en bout en blockout/art intermédiaire.
- **Content Complete (Beta)** : 100 % des assets artistiques, doublages multilingues (`fr-CD`, `ln-CD`) et optimisation PSO/VRAM intégrés.
- **Gold Master** : 0 bug Sévérité A/B, conformité XAG validée par `DIR-07`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-02` — Strate DAG 0)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-01`
- **Audit des Entrées (`inputs`)** :
  - `execution-plan-dag.json` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `risk-register.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `sprint-velocity-metrics` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `milestone-gate-review.md` : Doit respecter le gabarit `templates/milestone-gate-review.md` et passer l'audit croisé.
  - `scope-arbitration-decision.md` : Doit respecter le gabarit `templates/milestone-gate-review.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-01`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Dérive de charge estimée > +10 % sur un jalon | Blocage / Dégradation si ignoré | Activer le Feature Gating : déprioriser les éléments P2 ou restreindre la densité aux communes P0 (Gombe, Matonge, Kalamu, Limete) | Escalade vers Marquer les entités coupées au statut DEPRECATED via DIR-06 |
| Mode de Défaillance 2: Commune en statut RESEARCH_REQUIRED (ex: DST-MASINA) sur le chemin critique | Blocage / Dégradation si ignoré | Isoler la commune hors du Vertical Slice et maintenir le focus sur DST-GOMBE et DST-MATONGE | Escalade vers Assigner une tâche prioritaire d'acquisition SIG à WLD-03 |
| Mode de Défaillance 3: Risque juridique sur licences musicales (AUD-03) | Blocage / Dégradation si ignoré | Exiger l'activation par défaut du fallback Streamer Safe composé en interne | Escalade vers Bloquer l'intégration de la piste jusqu'à validation contractuelle |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-02`)

- [ ] **Contrôle DoD #1** : Écart budgétaire et capacitaire maintenu dans l'enveloppe de tolérance de ±5 %.
- [ ] **Contrôle DoD #2** : 100 % des coupes de périmètre (Scope Cuts) identifient les IDs d'entités à passer en `DEPRECATED`.
- [ ] **Contrôle DoD #3** : Chaque jalon dispose de critères d'entrée et de sortie mesurables validés avec `DIR-04` et `DIR-07`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
