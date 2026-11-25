# Boucles de Gameplay & Règles d'Arbitrage Ludique (`DIR-05`)

## 1. Boucle Principale (Core Loop) de ZAÏRE
1. **Reconnaissance Urbaine (Minute-to-Minute)** : Explorer Kinshasa sans mini-carte invasive grâce aux landmarks (`SYS-WLD-LANDMARKS`), écouter les rumeurs dans les ngandas (`DST-MATONGE`) et observer les routines PNJ (`AI-04`).
2. **Action & Approche Tactique** : Aborder chaque objectif (`MSN-*`) via un spectre fluide entre **Infiltration Sociale/Urbaine** (`SYS-STEALTH`), **Combat Corps-à-Corps Nerveux** (`SYS-CMB-MELEE`) et **Exfiltration Véhiculaire** (`VEH-MOTO-WEWA-01`).
3. **Impact & Réputation Locale (Hour-to-Hour)** : Faire évoluer la réputation par commune (`SYS-WLD-REPUTATION`), débloquer des raccourcis, des informateurs et des améliorations mécaniques (`GD-03`/`GD-04`).

## 2. Règles Non-Négociables de Playtest Blockout
- **Latence d'input combat** : `< 100 ms`.
- **Attack Tokens (`GD-05`)** : Maximum 2 assaillants au corps-à-corps simultanés contre Koffi en difficulté standard.
- **Règle des 40 secondes (`WLD-04`)** : Un point d'intérêt ou micro-événement systémique toutes les 40 secondes de déplacement à pied.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-05` — Strate DAG 0)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-01`, `DIR-03`
- **Audit des Entrées (`inputs`)** :
  - `game-design-specs-gd-01-to-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `level-blockouts-wld-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/technical-specs/spatial-metrics.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `gameplay-coherence-review.md` : Doit respecter le gabarit `templates/gameplay-coherence-review.md` et passer l'audit croisé.
  - `systemic-balance-directive.md` : Doit respecter le gabarit `templates/gameplay-coherence-review.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-03`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Blockout WLD-05 comportant un couloir jouable < 350 cm ou une impasse non intentionnelle | Blocage / Dégradation si ignoré | Rejeter le handoff vers WLD-06/ART-02 et exiger une reprise géométrique du blockout | Escalade vers Appliquer strictement la règle Blockout First |
| Mode de Défaillance 2: Mission GD-02 n'offrant qu'une seule approche linéaire ou vulnérable au soft-lock | Blocage / Dégradation si ignoré | Exiger au moins 2 approches distinctes (ex: infiltration sociale ITM-DOC-PASSEPORT + parcours parkour/mêlée) et une gestion de fuite | Escalade vers Bloquer le passage en CONFIRMED |
| Mode de Défaillance 3: Mécanique introduisant un tag absent de gameplay-tags-taxonomy.csv | Blocage / Dégradation si ignoré | Valider la pertinence systémique du tag et ordonner son ajout normalisé dans la taxonomie | Escalade vers Interdire les variables booléennes ad-hoc non composables |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-05`)

- [ ] **Contrôle DoD #1** : 100 % des interactions inter-systèmes passent par des `FGameplayTag` répertoriés.
- [ ] **Contrôle DoD #2** : 100 % des espaces de mission respectent les gabarits de caméra, de couvert et de circulation véhicule.
- [ ] **Contrôle DoD #3** : L'équilibrage numérique évite à la fois l'inflation monétaire (`GD-03`) et la trivialisation du combat (`GD-05`).
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
