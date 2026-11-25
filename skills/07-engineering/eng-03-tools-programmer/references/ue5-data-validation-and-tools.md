# Architecture des Validateurs Pré-Commit UE5 (`ENG-03`)

## 1. Liste des Validateurs Automatisés (`UDataValidationSubsystem`)
1. `UZaireAssetNamingValidator` : Vérifie les préfixes `SM_`, `SK_`, `M_`, `MI_`, `T_`, `NS_`, `BP_`.
2. `UZaireNaniteAndMaterialValidator` : Interdit `BLEND_Translucent` sur Nanite et vérifie que `WPO Disable Distance <= 3500 cm`.
3. `UZaireTextureORMValidator` : Vérifie les dimensions puissances de 2 et force `sRGB = false` + `TC_Masks` sur le suffixe `_ORM`.
4. `UZaireHardReferenceValidator` : Scanne les Blueprints de quête/monde pour interdire les références dures vers des acteurs hors Data Layer courant.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`ENG-03` — Strate DAG 4)

- **Ingénierie Moteur C++20, Houdini 22.0 & Pipeline Graphique (UE 5.8)** (`SRC-001`..`SRC-008`, `SRC-016`, `SRC-020`, `SRC-032`, `SRC-035`) :
  - **C++20 & Streaming (`ENG-01`, `ENG-02`, `ENG-03`, Budget cible Game Thread `<= 6.5 ms`)** : Zéro `LoadSynchronous()` runtime (usage exclusif de `FStreamableManager` et `TSoftObjectPtr`), tags GAS natifs (`UE_DECLARE_GAMEPLAY_TAG_EXTERN`), validateurs pré-commit `UEditorValidatorBase`.
  - **Houdini 22.0 & UE 5.8 PCG (`ENG-04`, `SRC-035`)** : Génération déterministe (`GlobalSeed = 19600630`) des splines `ZoneGraph` en amont d'`AI-03` ; support du framework **Houdini Copernicus (COP)** (introduit en Beta en 20.5 et étendu en 21–22 en remplacement de COP2) pour le traitement GPU des masques RVT/DEM, et d'**APEX** pour l'évaluation procédurale de graphes.
  - **Chaos Physics (`ENG-05`, cible `<= 1.5 ms`), Rendu (`ENG-06`), Perf (`ENG-07`) & Build (`ENG-08`, cible `<= 15 min`)** : Async Physics Tick `60 Hz`, cache de pages statiques VSM (`>= 92 % hit rate` cible), collecte automatisée du cache PSO (`0 hitch > 5 ms`), chiffrement IoStore `.utoc` AES-256 par variable d'environnement `$ENV{ZAIRE_PAK_AES256_KEY}`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `ART-04`, `ENG-01`
- **Audit des Entrées (`inputs`)** :
  - `3d-validation-rules-art-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `ue5-architecture-eng-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `editor-validator-spec.md` : Doit respecter le gabarit `templates/editor-tool-spec.md` et passer l'audit croisé.
  - `ue5-python-automation-script.py` : Doit respecter le gabarit `templates/editor-tool-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-04`, `ART-04`, `ENG-01`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Artiste tentant de soumettre un Static Mesh Nanite avec un matériau Translucide ou une texture non puissance de 2 | Blocage / Dégradation si ignoré | Faire échouer le DataValidationSubsystem (EDataValidationResult::Invalid) et afficher un message explicite indiquant l'asset, la règle ART-04 violée et la procédure de correction | Escalade vers Bloquer 100 % des régressions avant le commit |
| Mode de Défaillance 2: Opération manuelle répétitive identifiée sur plus de 20 assets (ex: assignation des ChaosPhysicalMaterial sur les kits routiers) | Blocage / Dégradation si ignoré | Écrire un script Python UE5 idempotent utilisant unreal.EditorAssetLibrary avec support --dry-run | Escalade vers Réduire le temps d'itération de l'équipe Art/World |
| Mode de Défaillance 3: Outil éditeur introduisant une dépendance dans le module Runtime du jeu | Blocage / Dégradation si ignoré | Déplacer immédiatement le code dans le module ZaireEditor (TargetType::Editor uniquement) | Escalade vers Empêcher tout alourdissement ou échec de compilation du build client ENG-08 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`ENG-03`)

- [ ] **Contrôle DoD #1** : Les validateurs `UEditorValidatorBase` interceptent 100 % des violations définies par `ART-04` et `ENG-01`.
- [ ] **Contrôle DoD #2** : Tous les modules d'outils sont strictement bornés à l'environnement `Editor`.
- [ ] **Contrôle DoD #3** : Chaque erreur retournée à l'utilisateur contient le code de la règle et la solution actionnable.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
