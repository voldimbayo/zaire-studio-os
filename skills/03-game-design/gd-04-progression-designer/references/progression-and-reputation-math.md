# Formules de Progression & Réputation par Quartier (`GD-04`)

## 1. Courbe d'Expérience (Niveaux 1 à 20)
$$XP_{\text{requis}}(L) = 500 \cdot L^2 + 1500 \cdot L$$
- **Niveau 1 -> 5 (Acte I)** : Maîtrise des fondamentaux (contre-attaque machette, slalom Wewa, laissez-passer).
- **Niveau 6 -> 14 (Acte II)** : Synergies urbaines (appel d'attroupement via `ORG-RADIO-KIN`, sabotage de grues/transformateurs).
- **Niveau 15 -> 20 (Acte III)** : Maîtrise complète des 3 branches.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-04` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-01`, `GD-05`, `NAR-01`
- **Audit des Entrées (`inputs`)** :
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `combat-design-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `narrative-architecture-nar-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `progression-curve.csv` : Doit respecter le gabarit `templates/skill-tree-spec.md` et passer l'audit croisé.
  - `skill-tree-specification.md` : Doit respecter le gabarit `templates/skill-tree-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `GD-03`, `GD-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Compétence indispensable au franchissement d'un blockout principal (ex: Ability.Movement.Vault) | Blocage / Dégradation si ignoré | L'inclure dans le kit de base de Koffi dès MSN-MAIN-001-ARRIVEE (ne jamais verrouiller une métrique spatiale de base derrière un arbre d'XP) | Escalade vers Garantir la cohérence avec WLD-05 |
| Mode de Défaillance 2: Branche de compétences choisie par moins de 15 % des profils de jeu simulés | Blocage / Dégradation si ignoré | Ajouter une synergie transversale (ex: l'arbre Réseau débloque aussi des raccourcis de livraison Wewa et des diversions de foule AI-02) | Escalade vers Équilibrer l'attractivité des 3 approches |
| Mode de Défaillance 3: Gain de puissance en fin d'Acte II rendant les affrontements de l'Acte III triviaux | Blocage / Dégradation si ignoré | Plafonner les multiplicateurs de santé/dégâts à +35 % sur l'ensemble du jeu et concentrer la progression sur la variété tactique | Escalade vers Synchroniser avec GD-05 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-04`)

- [ ] **Contrôle DoD #1** : Chaque compétence débloquée correspond à une `UGameplayAbility` ou un `UGameplayEffect` identifié par un `FGameplayTag`.
- [ ] **Contrôle DoD #2** : Les 4 paliers de réputation locale (`SYS-WLD-REPUTATION`) produisent des effets visibles sur les PNJ, le trafic et les commerçants.
- [ ] **Contrôle DoD #3** : Aucune capacité obligatoire pour le chemin critique n'est verrouillée derrière un choix optionnel.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
