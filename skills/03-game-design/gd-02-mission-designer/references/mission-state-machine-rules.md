# Architecture de Quêtes Tolérantes aux Interruptions (`GD-02`)

## 1. Protocole Anti-Soft-Lock en Monde Ouvert
Dans un monde ouvert systémique comme Kinshasa, toute étape de mission doit survivre à 4 événements imprévus :
1. `EVENT_VEHICLE_LOST` : Destruction ou perte de `VEH-MOTO-WEWA-01` -> activation d'un point de récupération secondaire ou continuation en parkour.
2. `EVENT_STEALTH_BROKEN` : Échec de l'infiltration `SYS-STEALTH` -> transition dynamique de l'objectif "Infiltrer sans alerte" vers "Arracher les registres sous le feu et s'exfiltrer" (pas d'écran d'échec punitif).
3. `EVENT_AREA_ABANDONED` : Sortie du rayon de `300 m` -> suspension propre de la mission au dernier checkpoint atomique.
4. `EVENT_WEATHER_SHIFT` : Déclenchement de `World.Weather.TropicalStorm` -> adaptation des cônes de détection `AI-01` et de l'adhérence `GD-06`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-02` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-01`, `WLD-04`, `GD-01`
- **Audit des Entrées (`inputs`)** :
  - `narrative-architecture-nar-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `poi-specs-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `mission-design-document.md` : Doit respecter le gabarit `templates/mission-design-template.md` et passer l'audit croisé.
  - `quest-state-machine.json` : Doit respecter le gabarit `templates/mission-design-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `NAR-06`, `AI-01`, `PRD-04`, `DIR-05`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Véhicule de mission (ex: VEH-MOTO-WEWA-01) détruit ou coincé pendant une poursuite | Blocage / Dégradation si ignoré | Ne jamais afficher un Game Over brutal s'il existe un repli : faire apparaître une Wewa de secours ou basculer l'objectif en fuite à pied/parkour | Escalade vers Garantir la règle Zéro Soft-Lock (quality-standards.md) |
| Mode de Défaillance 2: Nombre de gardes demandé > 24 dans l'arène de mission | Blocage / Dégradation si ignoré | Plafonner les gardes AI-01 à 20-24 et compléter l'ambiance par des travailleurs civils AI-02 Mass Crowd | Escalade vers Respecter le budget CPU AI-01 <= 2.5 ms |
| Mode de Défaillance 3: Joueur quitte le périmètre de la mission en plein dialogue | Blocage / Dégradation si ignoré | Sauvegarder le dernier checkpoint atomique et déclencher le handler ON_INTERRUPT_LEAVE de NAR-04 | Escalade vers Permettre la reprise fluide de la quête ultérieurement |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-02`)

- [ ] **Contrôle DoD #1** : Chaque étape de la machine à états possède un handler explicite contre les soft-locks (fuite, destruction véhicule, alerte).
- [ ] **Contrôle DoD #2** : Au moins 2 approches tactiques distinctes sont documentées et reliées aux systèmes `GD-01`/`GD-05`/`GD-06`.
- [ ] **Contrôle DoD #3** : Le nombre maximal de PNJ `AI-01` simultanés est `<= 24`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
