# Modèle Mathématique Sources & Puits (`GD-03`)

## 1. Équation d'Équilibre Monétaire (`Mosolo`)
Pour chaque heure de jeu $t \in [1, 40]$, le flux net $\Delta M(t) = F(t) - S(t)$ doit vérifier :
$$0.75 \le \frac{S(t)}{F(t)} \le 0.92$$
- **Faucets $F(t)$** : $12\,000 + 2\,500 \cdot t$ (Missions principales, courses urgentes `MSN-SIDE-014-WEWA`, contrats d'atelier).
- **Sinks $S(t)$** : $9\,500 + 2\,150 \cdot t$ (Pièces moteur Wewa, outils d'infiltration, corruption/accréditations portuaires, équipement de mêlée).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-03` — Strate DAG 2)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `GD-01`, `GD-02`, `DIR-02`
- **Audit des Entrées (`inputs`)** :
  - `game-systems-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `missions-list-gd-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `items-and-vehicles-registry` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `economy-balance-sheet.csv` : Doit respecter le gabarit `templates/economy-balance-sheet.csv` et passer l'audit croisé.
  - `faucets-sinks-simulation.json` : Doit respecter le gabarit `templates/economy-balance-sheet.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `GD-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Ratio Sink / Faucet < 0.75 détecté par simulate_economy.py (excès de liquidités / inflation) | Blocage / Dégradation si ignoré | Augmenter le coût des améliorations de palier 2/3 à l'atelier mécanique ou introduire des puits de prestige (tenues Sapeurs, améliorations radio) | Escalade vers Maintenir la valeur perçue du Mosolo jusqu'à l'Acte III |
| Mode de Défaillance 2: Ratio Sink / Faucet > 0.92 ou solde négatif sur le chemin critique | Blocage / Dégradation si ignoré | Réduire de 30 % les coûts de réparation obligatoire des véhicules et augmenter la prime des missions principales MSN-MAIN-* | Escalade vers Garantir zéro blocage financier sur la quête principale |
| Mode de Défaillance 3: Activité secondaire répétable générant plus de revenus/minute qu'une mission principale | Blocage / Dégradation si ignoré | Appliquer un rendement décroissant (diminishing returns) après 3 exécutions dans la même journée in-game | Escalade vers Protéger le rythme de progression GD-04 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-03`)

- [ ] **Contrôle DoD #1** : `python skills/03-game-design/gd-03-economy-designer/scripts/simulate_economy.py` retourne un code `0` (`economy_healthy: true`).
- [ ] **Contrôle DoD #2** : Aucun achat obligatoire de la quête principale ne bloque la progression du joueur.
- [ ] **Contrôle DoD #3** : 100 % des items tarifés utilisent des identifiants `ITM-*` ou `VEH-*` valides.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
