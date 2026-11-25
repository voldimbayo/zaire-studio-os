# Règles de Gouvernance du Registre Maître (`DIR-06`)

## 1. Convention Stricte des 9 Préfixes d'Identifiants
- `CHR-[ROLE]-[SLUG]` : Personnages (`CATEGORY = CHARACTER`, Owner `NAR-03`)
- `FAM-[NOM]` : Familles (`CATEGORY = FAMILY`, Owner `NAR-03`)
- `ORG-[TYPE]-[SLUG]` : Organisations (`CATEGORY = ORGANIZATION`, Owner `NAR-05`)
- `DST-[COMMUNE]` : Quartiers / Communes (`CATEGORY = DISTRICT`, Owner `WLD-01`)
- `LOC-[DST]-[SLUG]` : Lieux / POI (`CATEGORY = LOCATION`, Owner `WLD-04`)
- `MSN-[TYPE]-[NUM]-[SLUG]` : Missions / Quêtes (`CATEGORY = MISSION`, Owner `GD-02`)
- `ITM-[CAT]-[SLUG]` : Objets / Équipements (`CATEGORY = ITEM`, Owner `GD-01`/`GD-03`/`GD-05`)
- `VEH-[CAT]-[SLUG]` : Véhicules (`CATEGORY = VEHICLE`, Owner `GD-06`)
- `SYS-[DOMAINE]-[SLUG]` : Systèmes de Gameplay (`CATEGORY = SYSTEM`, Owner `GD-01`/`ENG-01`/`AI-*`)

## 2. Matrice d'Autorisation des Transitions de Statuts
- `RESEARCH_REQUIRED -> PROPOSED` : Skill propriétaire après fourniture de la recherche `WLD-02`/`WLD-03`/`ENG-*`.
- `PROPOSED -> CONFIRMED` : Signature conjointe obligatoire de `DIR-06` + `DIR-07` (+ Directeur de pôle concerné).
- `* -> BLOCKED` : `DIR-04`, `DIR-07`, `NAR-06`, `ENG-07`, `PRD-04`.
- `* -> DEPRECATED` : `DIR-02`, `DIR-03`, `DIR-06`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`DIR-06` — Strate DAG 5)

- **Gouvernance Moteur & Pipeline (UE 5.8 / Houdini 22.0 / Wwise 2024.1)** (`SRC-001`, `SRC-020`, `SRC-032`..`SRC-035`) :
  - **Unreal Engine 5.8** : Surveillance des budgets cibles P99 (`<= 16.6 ms` à 60 FPS, `<= 33.3 ms` à 30 FPS), grilles `World Partition` (`12800 cm`), `Data Layers`, `One File Per Actor (OFPA)`, `MegaLights` (`SRC-032`), `Mutable` (`SRC-033`) et `AnimNext / UAF` (`SRC-034`, expérimental).
  - **SideFX Houdini 22.0** : Supervision de la chaîne procédurale `PDG TOPs` / `Copernicus` (`SRC-035`, traitement GPU des masques DEM/RVT) et export `ZoneGraph` (`ENG-04` -> `AI-03`).
  - **Audiokinetic Wwise** : Plafond cible de `64 voix physiques`, cible broadcast `-23 LUFS` et mode juridique `STREAMER_SAFE` (`SRC-018`).
  - *[Avertissement d'Audit]* : Toutes les valeurs de frametime/VRAM présentes dans le dépôt sans trace Unreal Insights réelle sont des **cibles budgétaires synthétiques** ; toute compilation C++ (`UBT`), cuisson HDA (`hython`) ou SoundBank (`WwiseConsole`) demeure **`NOT TESTED`** hors moteur.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `PRD-03`, `NAR-06`
- **Audit des Entrées (`inputs`)** :
  - `handoff-packets` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/entities-registry.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/status-audit-log.csv` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `continuity-audits-nar-06` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `registry-promotion-decision.md` : Doit respecter le gabarit `templates/registry-promotion-decision.md` et passer l'audit croisé.
  - `updated-status-audit-entry.csv` : Doit respecter le gabarit `templates/registry-promotion-decision.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-01`, `DIR-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Entité proposée référençant un ID parent ou une dépendance inexistante (Référence Fantôme) | Blocage / Dégradation si ignoré | Rejeter immédiatement la promotion et renvoyer le Handoff Packet au skill émetteur | Escalade vers Maintenir le statut PROPOSED ou passer en BLOCKED |
| Mode de Défaillance 2: Donnée factuelle sur Kinshasa affirmée sans source vérifiée ni validation WLD-02/WLD-03 | Blocage / Dégradation si ignoré | Forcer le statut de l'entité à RESEARCH_REQUIRED | Escalade vers Déclencher une tâche de vérification documentaire via DIR-01 |
| Mode de Défaillance 3: Tous les contrôles DoD, NAR-06, PRD-03 et DIR-07 sont au vert | Blocage / Dégradation si ignoré | Promouvoir l'entité au statut CONFIRMED et inscrire la transition dans status-audit-log.csv | Escalade vers Publier la mise à jour à l'ensemble des départements |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`DIR-06`)

- [ ] **Contrôle DoD #1** : `python tools/validate_registry.py` retourne un code de sortie `0` (zéro erreur).
- [ ] **Contrôle DoD #2** : 100 % des changements de statuts sont tracés dans `knowledge/status-audit-log.csv`.
- [ ] **Contrôle DoD #3** : Aucun ID déprécié (`DEPRECATED`) n'est réutilisé ou référencé comme dépendance active d'une entité `CONFIRMED`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
