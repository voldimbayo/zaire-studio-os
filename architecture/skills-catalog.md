# Catalogue Détaillé des Skills — ZAÏRE STUDIO OS

Ce catalogue définit le contrat d'interface normalisé de chaque skill : **Périmètre**, **Responsabilités**, **Limites**, **Entrées**, **Sorties**, **Méthodes de travail**, **Références**, **Modèles de livrables**, **Critères d'acceptation** et **Règles de validation**.

> **Convention transversale** : Tous les skills lisent et référencent les entités via leurs identifiants normalisés (`CHR-*`, `FAM-*`, `ORG-*`, `DST-*`, `LOC-*`, `MSN-*`, `ITM-*`, `VEH-*`, `SYS-*`) définis dans `knowledge-management.md`.

---

## 0. DIRECTION CENTRALE (`DIR-01` à `DIR-07`)

### `DIR-01` — Studio Orchestrator
- **Périmètre** : Analyse de requêtes, routage multi-agents, séquencement DAG, gestion des handoffs et consolidation des livrables.
- **Responsabilités** : Décomposer toute demande utilisateur en sous-tâches atomiques ; vérifier les prérequis dans le registre de connaissances ; dispatcher vers les skills compétents ; assembler une réponse cohérente.
- **Limites** : Ne rédige jamais directement de contenu métier (code C++, scénario, shader, équilibre économique) à la place d'un spécialiste.
- **Entrées** : Requête utilisateur, état courant du `Knowledge Registry`, matrice des dépendances (`skill-dependencies.md`).
- **Sorties** : Plan d'exécution DAG, ordres de mission typés par skill, synthèse consolidée avec statuts de traçabilité.
- **Méthodes de travail** : Tri topologique des dépendances, vérification systématique des entités `RESEARCH_REQUIRED` ou `BLOCKED` avant lancement.
- **Références** : `architecture/orchestration-protocol.md`, `architecture/skill-dependencies.md`, `research/skills-discovery.md`.
- **Modèles de livrables** : `execution-plan-dag.json`, `consolidated-brief.md`.
- **Critères d'acceptation** : 100 % des sous-tâches assignées à un skill unique sans chevauchement ; aucune dépendance circulaire.
- **Règles de validation** : Vérifier que chaque livrable produit comporte un statut valide (`PROPOSED` ou `CONFIRMED`) et des IDs conformes.

### `DIR-02` à `DIR-07` — Collège de Direction
- **`DIR-02` Executive Producer** : Périmètre = budget, jalons, scope. Limites = n'intervient pas sur les choix techniques bas niveau. Entrées = propositions de features, risques (`PRD-02`). Sorties = arbitrages de scope, validation de jalon. Validation = alignement budget ±5 %.
- **`DIR-03` Creative Director** : Périmètre = piliers créatifs, cohérence tonale/artistique/narrative. Limites = ne modifie pas les spécifications techniques moteur. Entrées = Vision Docs, Art/Narrative Bibles, revues de builds. Sorties = notes de direction créative, validation esthétique. Validation = conformité aux 3 piliers créatifs de ZAÏRE.
- **`DIR-04` Technical Director** : Périmètre = architecture UE5/Houdini, budgets mémoire/CPU/GPU. Limites = n'arbitre pas le design narratif ou ludique hors contrainte technique. Entrées = TDD, profils performance (`ENG-07`). Sorties = ADR techniques, budgets par système. Validation = respect strict des enveloppes VRAM/frametime.
- **`DIR-05` Lead Game Designer** : Périmètre = cohérence ludique globale, métriques spatiales, équilibrage inter-systèmes. Limites = ne code pas l'implémentation C++. Entrées = GDD (`GD-01`..`GD-07`), retours playtests. Sorties = validation mécanique, ajustements d'équilibrage. Validation = absence de contradiction entre systèmes (`SYS-*`).
- **`DIR-06` Documentation Director** : Périmètre = gouvernance documentaire, registre d'entités, promotion de statuts. Limites = ne crée pas le contenu source métier. Entrées = livrables `PROPOSED` des départements, audits `NAR-06` et `PRD-03`. Sorties = promotion en `CONFIRMED`, mise à jour du registre maître. Validation = 100 % des IDs référencés existent et sont non-ambigus.
- **`DIR-07` Quality Director** : Périmètre = seuils qualité studio, certification, accessibilité, Definition of Done. Limites = ne planifie pas les sprints quotidiens (`PRD-01`). Entrées = rapports QA (`PRD-04`), résultats Gauntlet (`PRD-05`), audits XAG (`PRD-06`). Sorties = Go/No-Go de livraison (`CONFIRMED` vs `BLOCKED`). Validation = 0 bug bloquant, conformité XAG.

---

## 1. DÉPARTEMENT NARRATIVE (`NAR-01` à `NAR-06`)

### `NAR-01` — Narrative Architect
- **Périmètre** : Architecture narrative macroscopique, structure en actes, embranchements majeurs et cohérence ludo-narrative.
- **Responsabilités** : Concevoir l'ossature dramatique de ZAÏRE ; relier les arcs narratifs aux systèmes de monde ouvert ; définir les points de convergence/divergence.
- **Limites** : N'écrit pas les dialogues ligne par ligne (`NAR-04`) ni les fiches biographiques détaillées (`NAR-03`).
- **Entrées** : Piliers créatifs (`DIR-03`), World Bible (`WLD-01`), recherche culturelle (`WLD-02`).
- **Sorties** : `narrative-architecture.md`, graphe des actes et embranchements majeurs.
- **Méthodes de travail** : Structuration en actes interactifs, cartographie des conséquences persistantes par quartier (`DST-*`).
- **Références** : `research/technical-reference.md` (`NAR-01`), Heussner et al. (*The Game Narrative Toolbox*).
- **Modèles de livrables** : `act-structure-template.md`, `branching-matrix.csv`.
- **Critères d'acceptation** : Chaque acte possède des enjeux clairs, un ancrage géographique à Kinshasa et une articulation avec le gameplay.
- **Règles de validation** : Audit de continuité par `NAR-06` et validation créative par `DIR-03`.

### `NAR-02` — Screenwriter
- **Périmètre** : Écriture des scénarios de missions principales, cinématiques et scènes dramatiques.
- **Responsabilités** : Rédiger les scripts scénaristiques, didascalies d'action, intentions de mise en scène et beat sheets de quêtes.
- **Limites** : Ne gère pas la logique technique d'embranchement dans Articy/UE5 (`NAR-04`) ni les conditions de déclenchement gameplay (`GD-02`).
- **Entrées** : Architecture narrative (`NAR-01`), fiches personnages (`NAR-03`), structure de mission (`GD-02`).
- **Sorties** : Scripts de scènes (`SCN-*.md`), beat sheets dramatiques.
- **Méthodes de travail** : Écriture format scénario standard, rythme visuel ("Show, don't tell"), intégration naturelle du français kinois.
- **Références** : `research/technical-reference.md` (`NAR-01`), archives culturelles (`WLD-02`).
- **Modèles de livrables** : `mission-script-template.md`.
- **Critères d'acceptation** : Rythme dramatique soutenu, sous-texte présent, durée de scène compatible avec les budgets cinématiques.
- **Règles de validation** : Relecture par `NAR-03` (voix des personnages), `WLD-02` (authenticité culturelle) et `NAR-06` (continuité).

### `NAR-03` — Character Writer
- **Périmètre** : Conception psychologique, biographique et relationnelle des personnages (`CHR-*`) et familles (`FAM-*`).
- **Responsabilités** : Rédiger les bibles de personnages, motivations, failles, tics de langage et graphes relationnels.
- **Limites** : Ne définit pas l'apparence visuelle (`ART-03`) ni les statistiques de combat (`GD-05`).
- **Entrées** : Architecture narrative (`NAR-01`), factions (`WLD-01`), contexte culturel (`WLD-02`).
- **Sorties** : Fiches personnages (`CHR-*.md`), fiches familles (`FAM-*.md`), matrice des relations.
- **Méthodes de travail** : Profilage psychologique, définition du registre linguistique (français soutenu, argot kinois, lingala).
- **Références** : `research/technical-reference.md` (`NAR-01`, `ART-01`).
- **Modèles de livrables** : `character-bible-template.md`.
- **Critères d'acceptation** : Chaque personnage majeur dispose d'un arc clair, d'une voix distincte et d'ancrages sociaux crédibles à Kinshasa.
- **Règles de validation** : Unicité des IDs `CHR-*` et `FAM-*` validée par `NAR-05` et `DIR-06`.

### `NAR-04` — Dialogue Designer
- **Périmètre** : Conception des arbres de dialogue interactifs, répliques contextuelles (barks) et métadonnées de mise en scène procédurale.
- **Responsabilités** : Structurer les graphes de conversation conditionnels, écrire les barks de foule/combat, tagger l'émotion et l'intention caméra par réplique.
- **Limites** : Ne développe pas le code C++ du lecteur de dialogues (`ENG-02`) ni la traduction multilingue (`AUD-04`).
- **Entrées** : Scripts (`NAR-02`), bibles personnages (`NAR-03`), états de quêtes (`GD-02`).
- **Sorties** : Graphes de dialogue structurés (JSON/Markdown), banques de barks taggées.
- **Méthodes de travail** : Conception modulaire inspirée d'Ubisoft Quebec (`SRC-014` : métadonnées émotionnelles et cadrage automatique), gestion des interruptions.
- **Références** : `research/industry-methodologies.md` (Ubisoft GDC 2019), `research/technical-reference.md` (`NAR-03`).
- **Modèles de livrables** : `dialogue-tree-schema.json`, `barks-table-template.csv`.
- **Critères d'acceptation** : Zéro impasse dans les graphes, répliques concises (< 20 mots par bulle UI), tags émotionnels complets.
- **Règles de validation** : Vérification des conditions de variables par `GD-02` et compatibilité localisation par `AUD-04`.

### `NAR-05` — Lore Manager
- **Périmètre** : Encyclopédie du monde, chronologie canonique, médias in-game (radios, journaux, affiches) et organisations (`ORG-*`).
- **Responsabilités** : Maintenir la cohérence historique et fictionnelle du monde de ZAÏRE ; rédiger les textes d'ambiance (codex, journaux, slogans).
- **Limites** : N'invente pas de faits historiques réels contredisant les recherches de `WLD-02`.
- **Entrées** : Worldbuilding (`WLD-01`), recherche historique/culturelle (`WLD-02`), arcs narratifs (`NAR-01`).
- **Sorties** : `lore-encyclopedia.md`, chronologie maître, textes diégétiques urbains.
- **Méthodes de travail** : Indexation encyclopédique par entité (`ORG-*`, `DST-*`, `LOC-*`).
- **Références** : `research/technical-reference.md` (`NAR-02`).
- **Modèles de livrables** : `organization-dossier-template.md`, `timeline-master.csv`.
- **Critères d'acceptation** : Cohérence chronologique totale et richesse diégétique exploitable par l'Environment Art (`ART-02`).
- **Règles de validation** : Validation historique par `WLD-02` et enregistrement par `PRD-03`.

### `NAR-06` — Continuity Editor
- **Périmètre** : Contrôle qualité éditorial, détection des incohérences narratives, temporelles et d'état du monde.
- **Responsabilités** : Auditer tous les livrables narratifs et de mission avant passage au statut `CONFIRMED` ; signaler les contradictions de lore ou de chronologie.
- **Limites** : Ne réécrit pas intégralement les scènes ; émet des rapports d'anomalies et correctifs ciblés.
- **Entrées** : Tous les livrables `NAR-01`..`NAR-05` et `GD-02` (missions).
- **Sorties** : Rapports d'audit de continuité (`continuity-audit.md`), statut de validation éditoriale.
- **Méthodes de travail** : Vérification croisée des états de personnages (vivant/mort/allié/hostile) à chaque étape du graphe de quêtes.
- **Références** : `architecture/knowledge-management.md`.
- **Modèles de livrables** : `continuity-checklist.md`.
- **Critères d'acceptation** : 0 contradiction majeure détectée entre deux quêtes ou fiches d'entités.
- **Règles de validation** : Prérequis obligatoire avant toute promotion d'un asset narratif en `CONFIRMED`.

---

## 2. DÉPARTEMENT WORLD DESIGN (`WLD-01` à `WLD-06`)

### `WLD-01` — Worldbuilding Architect
- **Périmètre** : Vision macroscopique de Kinshasa dans ZAÏRE, découpage administratif fictif/réel (`DST-*`), dynamique socio-économique.
- **Responsabilités** : Définir l'identité de chaque commune/quartier (Gombe, Matonge, Kalamu, Limete, Masina, Ngaliema, fleuve Congo) et leurs interactions.
- **Limites** : Ne réalise pas le blockout 3D (`WLD-05`) ni la modélisation (`ART-02`).
- **Entrées** : Piliers créatifs (`DIR-03`), recherches culturelle (`WLD-02`) et urbaine (`WLD-03`).
- **Sorties** : `kinshasa-world-bible.md`, fiches de quartiers (`DST-*.md`).
- **Méthodes de travail** : Cartographie thématique multicouche (économie, sécurité, culture, architecture).
- **Références** : `research/technical-reference.md` (`NAR-02`), `SRC-019` (Epic World Building Guide).
- **Modèles de livrables** : `district-profile-template.md`.
- **Critères d'acceptation** : Chaque quartier possède une signature visuelle, sonore, économique et ludique distincte.
- **Règles de validation** : Cohérence avec `WLD-02` et `WLD-03` ; validation par `DIR-03`.

### `WLD-02` — Cultural Researcher
- **Périmètre** : Authenticité culturelle, historique, linguistique, musicale et sociale de Kinshasa et de la RDC.
- **Responsabilités** : Documenter les usages sociaux, codes vestimentaires (Sape, tenues quotidiennes), expressions en lingala/français kinois, histoire urbaine et patrimoine musical.
- **Limites** : Ne conçoit pas les mécaniques de jeu (`GD-01`) ; fournit des faits et références vérifiés.
- **Entrées** : Demandes de recherche de tous les départements, sources documentaires primaires.
- **Sorties** : Dossiers thématiques culturels, lexique Français/Lingala normalisé, notes d'authenticité.
- **Méthodes de travail** : Vérification documentaire rigoureuse ; marquage explicite en `RESEARCH_REQUIRED` de toute zone d'ombre.
- **Références** : `research/technical-reference.md` (`NAR-04`), Filip De Boeck (*Kinshasa: Tales of the Invisible City*).
- **Modèles de livrables** : `cultural-brief-template.md`, `lingala-glossary.csv`.
- **Critères d'acceptation** : Sources vérifiables, absence de clichés externes, utilisabilité directe par les équipes Narrative, Art et Audio.
- **Règles de validation** : Audit de traçabilité par `PRD-03` et `DIR-06`.

### `WLD-03` — Urban Researcher
- **Périmètre** : Morphologie urbaine, réseaux viaires, typologies architecturales, infrastructures et topographie de Kinshasa.
- **Responsabilités** : Analyser les axes routiers majeurs (Boulevard du 30 Juin, Lumumba, Poids Lourds), carrefours (Rond-point Victoire), habitats, marchés et berges du fleuve.
- **Limites** : Ne crée pas les graphes Houdini (`ENG-04`) ; fournit les spécifications urbaines et règles d'implantation.
- **Entrées** : Données SIG/OSM disponibles, cartographies urbaines, objectifs de gameplay (`WLD-04`).
- **Sorties** : Spécifications morphologiques par commune, règles de voirie et densité bâtie.
- **Méthodes de travail** : Classification typologique des îlots urbains (grille coloniale orthogonale vs tissu organique dense).
- **Références** : `research/research-gaps.md` (Section 2), `SRC-005` (SideFX OSM City).
- **Modèles de livrables** : `urban-typology-spec.md`.
- **Critères d'acceptation** : Règles géométriques exploitables par `WLD-04`, `ENG-04` (Houdini) et `AI-03` (Traffic).
- **Règles de validation** : Faisabilité procédurale validée par `ENG-04`.

### `WLD-04` — Open World Designer
- **Périmètre** : Macro-design de la carte jouable, répartition des Points d'Intérêt (POI), lignes de mire (landmarks) et pacing d'exploration.
- **Responsabilités** : Structurer la carte de Kinshasa en zones de progression, placer les repères visuels majeurs et calibrer la densité d'activités.
- **Limites** : Ne conçoit pas l'architecture intérieure détaillée des bâtiments (`WLD-05`).
- **Entrées** : World Bible (`WLD-01`), typologie urbaine (`WLD-03`), systèmes de jeu (`GD-01`), budgets streaming (`DIR-04`).
- **Sorties** : Carte maîtresse des POI (`LOC-*.md`), plan de pacing spatial, grille World Partition logique.
- **Méthodes de travail** : Règle des 40 secondes d'intérêt visuel, hiérarchie des landmarks (Tour de l'Échangeur, Palais du Peuple, Fleuve).
- **Références** : `research/technical-reference.md` (`GD-02`), Totten (*An Architectural Approach to Level Design*).
- **Modèles de livrables** : `poi-specification-template.md`, `world-pacing-matrix.csv`.
- **Critères d'acceptation** : Orientation intuitive sans mini-carte, temps de traversée équilibré, respect des contraintes de streaming UE5.
- **Règles de validation** : Validation ludique par `DIR-05` et technique par `ENG-01`.

### `WLD-05` — Level Designer
- **Périmètre** : Conception spatiale détaillée des lieux jouables (`LOC-*`), blockout/greyboxing, métriques de déplacement/caméra, couverts et parcours.
- **Responsabilités** : Produire les plans et spécifications de blockout pour missions et intérieurs ; garantir la lisibilité spatiale et la fluidité des déplacements.
- **Limites** : N'applique pas les matériaux finaux ni le set dressing décoratif (`ART-02`).
- **Entrées** : Spécifications de POI (`WLD-04`), briefs de mission (`GD-02`), métriques personnage/combat (`GD-05`, `ART-05`).
- **Sorties** : Spécifications de blockout (`BLK-*.md`), schémas d'arènes et parcours, exigences NavMesh/Smart Links.
- **Méthodes de travail** : Méthodologie Naughty Dog (`SRC-012`) : validation complète du gameplay en volumes gris avant passage à l'art.
- **Références** : `research/industry-methodologies.md` (Naughty Dog GDC 2018), `research/technical-reference.md` (`GD-04`).
- **Modèles de livrables** : `level-blockout-brief.md`, `spatial-metrics-checklist.md`.
- **Critères d'acceptation** : Respect strict des gabarits caméra/joueur, zéro cul-de-sac involontaire, lignes de tir et couverts équilibrés.
- **Règles de validation** : Playtest validation par `DIR-05` et handoff formel vers `WLD-06` / `ART-02`.

### `WLD-06` — Environment Designer
- **Périmètre** : Direction environnementale par lieu (`LOC-*`), spécification des biomes urbains/naturels, kits architecturaux et narration visuelle.
- **Responsabilités** : Traduire les blockouts validés (`WLD-05`) et la recherche urbaine (`WLD-03`) en briefs de production détaillés pour les artistes 3D et Houdini.
- **Limites** : Ne modélise pas les assets finaux (`ART-02`) et ne programme pas les outils HDA (`ENG-04`).
- **Entrées** : Blockouts (`WLD-05`), Art Bible (`ART-01`), recherche culturelle/urbaine (`WLD-02`, `WLD-03`).
- **Sorties** : Environment Design Briefs par quartier/lieu, listes de kits modulaires requis, plans d'usure/météo locale.
- **Méthodes de travail** : Découpage modulaire sur grille, storytelling environnemental par couches (structure -> habillage -> vie quotidienne).
- **Références** : `research/technical-reference.md` (`ART-03`), `SRC-019` (Epic World Building Guide).
- **Modèles de livrables** : `environment-brief-template.md`, `asset-kit-manifest.csv`.
- **Critères d'acceptation** : Cohérence architecturale kinoise, réutilisation maximale des kits modulaires, préservation des lignes de lisibilité du Level Design.
- **Règles de validation** : Validation artistique par `ART-01` et budgétaire par `ART-08`.

---

## 3. DÉPARTEMENT GAME DESIGN (`GD-01` à `GD-07`)

### `GD-01` — Game Systems Designer
- **Périmètre** : Conception des boucles de gameplay fondamentales (Core Loops) et des systèmes transversaux (`SYS-*`).
- **Responsabilités** : Spécifier les règles d'interaction (furtivité, exploration, réputation, inventaire, interactions sociales) et leur mapping vers UE5 GAS / Gameplay Tags.
- **Limites** : Ne conçoit pas les quêtes individuelles (`GD-02`) ni le code C++ (`ENG-02`).
- **Entrées** : Piliers créatifs (`DIR-03`), direction ludique (`DIR-05`).
- **Sorties** : Spécifications de systèmes (`SYS-*.md`), taxonomie des Gameplay Tags, diagrammes d'états.
- **Méthodes de travail** : Pensée systémique, conception par composants découplés communiquant via Gameplay Tags.
- **Références** : `research/technical-reference.md` (`GD-01`), `SRC-002` (UE5 GAS Documentation).
- **Modèles de livrables** : `system-design-doc-template.md`, `gameplay-tags-registry.csv`.
- **Critères d'acceptation** : Systèmes composables sans effets de bord destructeurs, règles claires et testables.
- **Règles de validation** : Validation par `DIR-05` et revue d'architecture par `ENG-02`.

### `GD-02` — Mission Designer
- **Périmètre** : Conception ludique des missions principales, secondaires et activités dynamiques (`MSN-*`).
- **Responsabilités** : Définir les objectifs, étapes, conditions de victoire/échec, approches multiples (action/infiltration/dialogue) et récompenses.
- **Limites** : N'écrit pas les dialogues littéraires (`NAR-02`/`NAR-04`) et ne sculpte pas les décors (`ART-02`).
- **Entrées** : Architecture narrative (`NAR-01`), carte des POI (`WLD-04`), systèmes de jeu (`GD-01`).
- **Sorties** : Mission Design Documents (`MSN-*.md`), machines à états de quête, besoins en blockout (`WLD-05`).
- **Méthodes de travail** : Graphes d'états tolérants aux interruptions en monde ouvert, checkpoints atomiques.
- **Références** : `research/technical-reference.md` (`GD-03`).
- **Modèles de livrables** : `mission-design-template.md`, `quest-state-machine.json`.
- **Critères d'acceptation** : Zéro soft-lock possible, au moins 2 approches tactiques sur les missions majeures, intégration fluide dans le monde ouvert.
- **Règles de validation** : Audit de continuité (`NAR-06`), revue de faisabilité IA (`AI-01`) et QA (`PRD-04`).

### `GD-03` — Economy Designer
- **Périmètre** : Modélisation et équilibrage de l'économie virtuelle de ZAÏRE (sources de revenus, dépenses, objets `ITM-*`, tarifs).
- **Responsabilités** : Définir les tables de prix, récompenses de missions, coûts d'équipement/véhicules et mécanismes anti-inflation.
- **Limites** : Ne conçoit pas l'arbre de compétences (`GD-04`) ni l'interface des boutiques (`GD-07`).
- **Entrées** : Liste des objets (`ITM-*`), véhicules (`VEH-*`), structure des missions (`GD-02`), télémétrie (`DIR-02`).
- **Sorties** : Modèle économique mathématique, tables de données (`economy-tables.csv`).
- **Méthodes de travail** : Modélisation Sources & Puits (Faucets & Sinks), simulations de progression sur 30 à 60 heures de jeu.
- **Références** : `research/technical-reference.md` (`GD-07`), Adams & Dormans (*Game Mechanics*).
- **Modèles de livrables** : `economy-balance-sheet.csv`, `faucets-sinks-model.md`.
- **Critères d'acceptation** : Absence de blocage financier sur la quête principale, pertinence des achats jusqu'en fin de jeu.
- **Règles de validation** : Validation mathématique et approbation par `DIR-05`.

### `GD-04` — Progression Designer
- **Périmètre** : Systèmes d'évolution du personnage, déblocage de capacités, réputation par quartier/faction et courbe de difficulté.
- **Responsabilités** : Structurer les paliers de progression, arbres de compétences/talents et récompenses d'exploration.
- **Limites** : Ne définit pas les prix monétaires (`GD-03`) ni les frames d'animation de combat (`GD-05`).
- **Entrées** : Systèmes de jeu (`GD-01`), combat (`GD-05`), structure narrative (`NAR-01`).
- **Sorties** : Courbes d'XP/réputation, arbre de compétences, matrice de déblocage.
- **Méthodes de travail** : Équilibrage des courbes exponentielles/logarithmiques, validation du rythme de récompense par heure de jeu.
- **Références** : `research/technical-reference.md` (`GD-01`, `GD-07`).
- **Modèles de livrables** : `progression-curve.csv`, `skill-tree-spec.md`.
- **Critères d'acceptation** : Sentiment constant de montée en puissance sans déséquilibrer le combat tardif.
- **Règles de validation** : Cohérence avec `GD-03` et `GD-05`, validation par `DIR-05`.

### `GD-05` — Combat Designer
- **Périmètre** : Conception des systèmes d'affrontement (corps-à-corps, armes blanches, armes à feu, couverture, dégâts, game feel).
- **Responsabilités** : Spécifier les combos, fenêtres de parade/esquive, hitstop, recul d'armes, archétypes ennemis et règles d'Attack Tokens.
- **Limites** : Ne réalise pas les animations (`ART-05`) ni les effets particules (`ART-09`).
- **Entrées** : Systèmes de jeu (`GD-01`), objets/armes (`ITM-*`), métriques d'animation (`ART-05`).
- **Sorties** : Combat Design Bible, matrices de dégâts/stamina, spécifications d'archétypes ennemis.
- **Méthodes de travail** : Calibrage image par image (Anticipation / Active / Recovery), prototypage en Combat Gym.
- **Références** : `research/technical-reference.md` (`GD-05`), Swink (*Game Feel*).
- **Modèles de livrables** : `combat-archetype-template.md`, `weapon-balance-matrix.csv`.
- **Critères d'acceptation** : Réactivité immédiate des commandes, attaques ennemies lisibles, caméra stable en mêlée urbaine.
- **Règles de validation** : Validation technique avec `ENG-02` (GAS) et `AI-01` (IA combat).

### `GD-06` — Vehicle Designer
- **Périmètre** : Conception ludique et physique de la conduite des véhicules de Kinshasa (`VEH-*` : motos Wewa, taxis jaunes, bus, 4x4, bateaux fluviaux).
- **Responsabilités** : Définir les profils de maniabilité (arcade/simcade), courbes de couple, adhérence par surface (asphalte, latérite, boue), dégâts et caméras véhicule.
- **Limites** : Ne modélise pas les carrosseries 3D (`ART-02`) et n'implémente pas les solveurs Chaos (`ENG-05`).
- **Entrées** : Typologie urbaine (`WLD-03`), physique Chaos (`ENG-05`), audio moteur (`AUD-02`).
- **Sorties** : Fiches techniques véhicules (`VEH-*.md`), matrices de tuning physique par surface.
- **Méthodes de travail** : Tests comparatifs par catégorie de véhicule, stabilisation assistée des deux-roues.
- **Références** : `research/technical-reference.md` (`GD-06`), Epic *Chaos Vehicles User Guide*.
- **Modèles de livrables** : `vehicle-handling-spec.md`, `surface-friction-table.csv`.
- **Critères d'acceptation** : Contrôle fluide au clavier et à la manette, comportement distinct et crédible entre une moto Wewa et un bus lourd.
- **Règles de validation** : Validation physique avec `ENG-05` et compatibilité trafic avec `AI-03`.

### `GD-07` — UI/UX Designer
- **Périmètre** : Ergonomie de l'expérience utilisateur, HUD contextuel, carte de Kinshasa, menus, téléphone in-game et flux d'interaction.
- **Responsabilités** : Concevoir les wireframes, parcours utilisateurs (user flows), règles d'affichage diégétique et spécifications UE5 Common UI.
- **Limites** : Ne programme pas les widgets C++/UMG (`ENG-02`) ni les polices localisées (`AUD-04`).
- **Entrées** : Tous les systèmes exposés au joueur (`GD-01`..`GD-06`), contraintes d'accessibilité (`PRD-06`).
- **Sorties** : UI/UX Wireframes, UI Style Guide, spécifications de navigation manette/clavier.
- **Méthodes de travail** : Conception centrée utilisateur, HUD minimaliste laissant respirer la direction artistique de Kinshasa.
- **Références** : `research/technical-reference.md` (`GD-08`), Hodent (*The Gamer's Brain*).
- **Modèles de livrables** : `ui-screen-spec-template.md`, `ux-flow-diagram.md`.
- **Critères d'acceptation** : Navigation en 3 actions maximum, lisibilité parfaite sur TV et moniteur, compatibilité daltonisme/taille de police.
- **Règles de validation** : Audit d'accessibilité obligatoire par `PRD-06` (XAG).

---

## 4. DÉPARTEMENT AI & SIMULATION (`AI-01` à `AI-04`)

### `AI-01` — NPC AI Architect
- **Périmètre** : Architecture des comportements individuels des PNJ (combattants, forces de l'ordre, alliés, commerçants).
- **Responsabilités** : Concevoir les State Trees / Behavior Trees, requêtes EQS (couverture, ligne de vue, flanquement), perception sensorielle et Smart Objects.
- **Limites** : Ne gère pas les foules de masse de centaines d'entités légères (`AI-02`) ni le trafic routier (`AI-03`).
- **Entrées** : Archétypes de combat (`GD-05`), métriques de niveau (`WLD-05`), budgets CPU (`DIR-04`).
- **Sorties** : Architecture IA PNJ, graphes State Tree, spécifications EQS et Smart Objects.
- **Méthodes de travail** : Tests en AI Gym, time-slicing des mises à jour sensorielles pour maîtriser le budget CPU (< 2.5 ms).
- **Références** : `research/technical-reference.md` (`AI-01`), Rabin (*Game AI Pro*).
- **Modèles de livrables** : `npc-ai-architecture.md`, `eqs-query-spec.md`.
- **Critères d'acceptation** : Réactions tactiques crédibles, zéro blocage sur le NavMesh, respect strict du budget CPU.
- **Règles de validation** : Profilage par `ENG-07` et validation combat par `GD-05`.

### `AI-02` — Crowd Simulation Specialist
- **Périmètre** : Simulation de foules urbaines denses (marchés de Kinshasa, artères commerçantes) sous UE5 Mass Entity / Mass Crowd.
- **Responsabilités** : Définir les archétypes ECS (Fragments/Processors), voies piétonnes ZoneGraph, évitement RVO et seuils d'hydratation en acteurs complets.
- **Limites** : Ne modélise pas les vêtements modulaires des PNJ (`ART-03`) ni les comportements de combat complexes (`AI-01`).
- **Entrées** : Densité par quartier (`WLD-04`), kits modulaires PNJ (`ART-03`), budget CPU/GPU (`DIR-04`).
- **Sorties** : Architecture Mass Crowd, règles de densité horaire (jour/nuit/marché), pipeline d'hydratation.
- **Méthodes de travail** : Architecture orientée données (ECS) inspirée d'Epic *City Sample* (`SRC-004`) et événements de foule Ubisoft (`SRC-013`).
- **Références** : `research/technical-reference.md` (`AI-02`), `SRC-004`, `SRC-013`.
- **Modèles de livrables** : `mass-crowd-spec.md`, `district-crowd-density.csv`.
- **Critères d'acceptation** : 500+ PNJ simultanés pour < 2.0 ms CPU, transition imperceptible entre entité légère et acteur interactif.
- **Règles de validation** : Stress test automatisé par `PRD-05` et validation performance par `ENG-07`.

### `AI-03` — Traffic AI Specialist
- **Périmètre** : Simulation du trafic routier et fluvial de Kinshasa sous UE5 ZoneGraph et Mass Traffic.
- **Responsabilités** : Concevoir les règles de voies, priorités aux ronds-points, comportements spécifiques (motos Wewa slalomant, arrêts taxis), prévention des deadlocks.
- **Limites** : Ne tune pas la physique fine de suspension des véhicules (`GD-06`).
- **Entrées** : Réseau routier Houdini (`ENG-04`), fiches véhicules (`GD-06`), morphologie urbaine (`WLD-03`).
- **Sorties** : Spécifications ZoneGraph / Mass Traffic, algorithmes de résolution d'interblocages aux carrefours.
- **Méthodes de travail** : Suivi cinématique sur splines avec bascule instantanée vers Chaos Physics lors d'une collision ou proximité joueur.
- **Références** : `research/technical-reference.md` (`AI-03`), `research/research-gaps.md` (Section 1).
- **Modèles de livrables** : `traffic-rules-spec.md`, `intersection-priority-matrix.csv`.
- **Critères d'acceptation** : Trafic vivant et dense sans embouteillage infini bloqué, disparition/apparition invisible hors champ caméra.
- **Règles de validation** : Tests de charge routière de 2 heures par `PRD-05`.

### `AI-04` — Decision Systems Designer
- **Périmètre** : Systèmes de décision de haut niveau, Utility AI, routines quotidiennes des citoyens et générateur d'événements systémiques émergents.
- **Responsabilités** : Concevoir les matrices d'utilité gouvernant les réactions collectives (panique, attroupement, commerce, météo) et les micro-scènes de rue.
- **Limites** : N'implémente pas les arbres de navigation bas niveau (`AI-01`).
- **Entrées** : Worldbuilding (`WLD-01`), systèmes de réputation (`GD-01`), barks (`NAR-04`).
- **Sorties** : Courbes d'utilité, catalogue des événements systémiques urbains, plannings quotidiens PNJ.
- **Méthodes de travail** : Architecture systémique inspirée de Rockstar (`SRC-015`) et Ubisoft (`SRC-013`).
- **Références** : `research/industry-methodologies.md` (Rockstar & Ubisoft).
- **Modèles de livrables** : `utility-ai-matrix.csv`, `systemic-events-catalog.md`.
- **Critères d'acceptation** : Réactivité cohérente du monde aux actions du joueur et aux changements météo/horaires.
- **Règles de validation** : Cohérence narrative avec `NAR-06` et ludique avec `DIR-05`.

---

## 5. DÉPARTEMENT ART & ANIMATION (`ART-01` à `ART-09`)

### `ART-01` — Art Director
- **Périmètre** : Direction artistique globale, Art Bible, identité visuelle des quartiers, personnages et interfaces.
- **Responsabilités** : Définir les palettes couleurs, matériaux de référence, proportions et règles de lisibilité visuelle de ZAÏRE.
- **Limites** : N'arbitre pas les budgets techniques CPU/GPU (`DIR-04`), mais adapte la direction visuelle pour les respecter.
- **Entrées** : Piliers créatifs (`DIR-03`), recherche culturelle/urbaine (`WLD-02`, `WLD-03`).
- **Sorties** : `art-bible.md`, planches de direction visuelle par commune, notes de revue artistique.
- **Méthodes de travail** : Direction par références photographiques et architecturales réelles de Kinshasa, hiérarchie de contraste.
- **Références** : `research/technical-reference.md` (`PROD-03`, `ART-01`).
- **Modèles de livrables** : `art-bible-template.md`, `art-review-scorecard.md`.
- **Critères d'acceptation** : Identité visuelle forte, originale et immédiatement reconnaissable comme Kinshasa.
- **Règles de validation** : Approbation par `DIR-03`.

### `ART-02` — Environment Artist
- **Périmètre** : Production des assets architecturaux modulaires, matériaux PBR, végétation tropicale et habillage des quartiers (set dressing).
- **Responsabilités** : Créer les kits de bâtiments kinois, shaders de matériaux (latérite, béton patiné, tôle ondulée), feuillage et habillage des blockouts.
- **Limites** : Ne modifie pas les collisions gameplay ou métriques validées par le `Level Designer` (`WLD-05`).
- **Entrées** : Environment Design Briefs (`WLD-06`), blockouts (`WLD-05`), standards pipeline (`ART-04`).
- **Sorties** : Spécifications de kits modulaires, bibliothèques de matériaux PBR, plans de set dressing.
- **Méthodes de travail** : Assemblage modulaire UE5 Nanite, Runtime Virtual Texturing (RVT) pour fondre les transitions sol/bâtiments.
- **Références** : `research/technical-reference.md` (`ART-03`), `SRC-019`.
- **Modèles de livrables** : `modular-kit-spec.md`, `pbr-material-library.csv`.
- **Critères d'acceptation** : Zéro répétition visuelle flagrante, respect des métriques de collision et des budgets mémoire texture.
- **Règles de validation** : Validation technique par `ART-04` / `ART-08` et artistique par `ART-01`.

### `ART-03` — Character Artist
- **Périmètre** : Création des modèles 3D des protagonistes, PNJ modulaires, vêtements, coiffures (Groom) et shaders de peau.
- **Responsabilités** : Spécifier les base meshes, le système d'assemblage modulaire des foules kinoises, les matériaux textiles et la calibration des peaux foncées sous lumière équatoriale.
- **Limites** : Ne rige pas les squelettes complexes (`ART-08`) et n'anime pas les personnages (`ART-05`).
- **Entrées** : Bibles personnages (`NAR-03`), recherche vestimentaire (`WLD-02`), Art Bible (`ART-01`).
- **Sorties** : Spécifications personnages héros (`CHR-*`), matrice d'assemblage modulaire PNJ, guidelines shaders peau/cheveux.
- **Méthodes de travail** : Pipeline modulaire inspiré de Guerrilla Games (`SRC-009`), bascule Groom Strands (héros) -> Hair Cards (PNJ).
- **Références** : `research/industry-methodologies.md` (Guerrilla Games GDC 2018), `research/technical-reference.md` (`ART-04`).
- **Modèles de livrables** : `character-art-spec.md`, `modular-npc-parts.csv`.
- **Critères d'acceptation** : Rendu réaliste des carnations et textures capillaires, haute diversité visuelle pour un coût mémoire maîtrisé.
- **Règles de validation** : Validation pipeline par `ART-04` et performance foule par `ENG-07`.

### `ART-04` — 3D Pipeline Specialist
- **Périmètre** : Normes techniques de production 3D (topologie Nanite, UV, Texel Density, pivots, collisions, formats FBX/USD).
- **Responsabilités** : Établir les standards géométriques du studio et les règles de validation automatique à l'import dans UE5.
- **Limites** : Ne développe pas les plugins C++ éditeur (`ENG-03`), mais fournit leurs spécifications métier.
- **Entrées** : Budgets techniques (`DIR-04`), besoins Environment/Character Art (`ART-02`, `ART-03`).
- **Sorties** : `3d-modeling-standards.md`, grilles de Texel Density, spécifications de validateurs d'assets.
- **Méthodes de travail** : Standardisation stricte sur grille métrique (1 unité UE = 1 cm), optimisation Nanite vs LOD classiques.
- **Références** : `research/technical-reference.md` (`ART-02`), Epic *Nanite Virtualized Geometry*.
- **Modèles de livrables** : `asset-validation-rules.json`.
- **Critères d'acceptation** : 100 % des assets conformes aux règles de pivot, d'échelle et de collision avant intégration.
- **Règles de validation** : Implémentation vérifiée avec `ENG-03` (Tools Programmer).

### `ART-05` — Animation Specialist
- **Périmètre** : Systèmes d'animation temps réel, locomotion (Motion Matching), parkour urbain, combat et animation procédurale (Control Rig / IK).
- **Responsabilités** : Concevoir l'architecture des Animation Blueprints, bases de données Pose Search (Motion Matching), Motion Warping et Foot Placement IK.
- **Limites** : Ne gère pas les plateaux de capture optique/inertielle (`ART-06`).
- **Entrées** : Métriques de déplacement (`WLD-05`), spécifications combat (`GD-05`), données MoCap nettoyées (`ART-06`).
- **Sorties** : Architecture d'animation UE5, spécifications Motion Matching et Control Rig.
- **Méthodes de travail** : Locomotion physique réactive inspirée de Rockstar (`SRC-015`) et Epic Motion Matching UE5.
- **Références** : `research/industry-methodologies.md` (Rockstar GDC 2020), `research/technical-reference.md` (`ART-05`).
- **Modèles de livrables** : `animation-graph-spec.md`, `locomotion-metrics.csv`.
- **Critères d'acceptation** : Zéro glissement des pieds, transitions fluides sans latence d'input perçue.
- **Règles de validation** : Validation réactivité par `GD-05` et budget CPU animation par `ENG-07`.

### `ART-06` — Motion Capture Specialist
- **Périmètre** : Capture de mouvement corporel et facial, nettoyage de courbes, retargeting squelettique et pipeline MetaHuman Animator.
- **Responsabilités** : Rédiger les shot lists de capture, protocoles de calibration, règles de retargeting IK Rig et nomenclature des prises.
- **Limites** : N'intègre pas la logique des Animation Blueprints (`ART-05`).
- **Entrées** : Scripts de scènes (`NAR-02`), listes d'actions combat/locomotion (`GD-05`, `ART-05`).
- **Sorties** : Shot lists MoCap, spécifications de retargeting FBX/BVH, pipeline facial.
- **Méthodes de travail** : Pré-visualisation Live Link, séparation propre corps/mains/visage.
- **Références** : `research/technical-reference.md` (`ART-06`), Menache (*Understanding Motion Capture*).
- **Modèles de livrables** : `mocap-shotlist-template.csv`, `retargeting-protocol.md`.
- **Critères d'acceptation** : Données propres sans bruit haute fréquence, alignement squelettique exact sur les rigs UE5.
- **Règles de validation** : Contrôle qualité à la réception par `ART-05`.

### `ART-07` — Lighting Specialist
- **Périmètre** : Éclairage artistique et technique de Kinshasa, cycle jour/nuit, météo tropicale (pluies, brume) et color grading ACES.
- **Responsabilités** : Calibrer les valeurs physiques (EV100, lux, Kelvin) pour le soleil équatorial, configurer Lumen GI, Sky Atmosphere, Volumetric Clouds et Post Process.
- **Limites** : Ne modifie pas le code source du moteur de rendu (`ENG-06`).
- **Entrées** : Art Bible (`ART-01`), blockouts/environnements (`WLD-05`, `ART-02`), budgets GPU (`DIR-04`).
- **Sorties** : Lighting Bible, presets atmosphériques par heure/météo, LUTs de colorimétrie.
- **Méthodes de travail** : Guidage visuel par la lumière dès le blockmesh (méthode Naughty Dog `SRC-011`/`SRC-012`), contrôle de l'auto-exposition.
- **Références** : `research/technical-reference.md` (`ART-08`), `SRC-003` (Lumen Technical Details), `SRC-011`.
- **Modèles de livrables** : `lighting-preset-matrix.csv`, `time-of-day-spec.md`.
- **Critères d'acceptation** : Lisibilité optimale en intérieur comme en plein soleil équatorial, respect du budget GPU Lumen.
- **Règles de validation** : Validation artistique (`ART-01`) et profilage GPU (`ENG-06`/`ENG-07`).

### `ART-08` — Technical Artist
- **Périmètre** : Master Materials HLSL/Substrate, optimisation des permutations shaders (PSO), rigging avancé et passerelles techniques Art -> UE5.
- **Responsabilités** : Concevoir les shaders maîtres paramétrables, réduire l'explosion des PSO, rigger les véhicules/armes/vêtements et profiler les scènes artistiques.
- **Limites** : Ne développe pas le C++ gameplay (`ENG-02`) ni les pipelines CI/CD (`ENG-08`).
- **Entrées** : Besoins shaders/rigs (`ART-02`, `ART-03`, `GD-06`), budgets GPU (`DIR-04`).
- **Sorties** : Spécifications Master Materials, guidelines PSO, architectures de rigs complexes.
- **Méthodes de travail** : Remplacement des Static Switches par des paramètres dynamiques / Custom Primitive Data.
- **Références** : `research/technical-reference.md` (`ART-07`).
- **Modèles de livrables** : `master-material-spec.md`, `shader-budget-guidelines.md`.
- **Critères d'acceptation** : Temps de compilation shaders maîtrisé, zéro hitch PSO en jeu, respect des budgets d'instructions GPU.
- **Règles de validation** : Audit technique par `ENG-06` et `ENG-07`.

### `ART-09` — VFX Specialist
- **Périmètre** : Effets visuels temps réel sous UE5 Niagara (météo tropicale, poussière latérite, fumées urbaines, combats, impacts).
- **Responsabilités** : Concevoir les systèmes de particules GPU Niagara, flipbooks/VAT issus de simulations fluides et règles de LOD/overdraw.
- **Limites** : Ne gère pas l'éclairage global de scène (`ART-07`).
- **Entrées** : Art Bible (`ART-01`), spécifications combat (`GD-05`), météo (`ART-07`), budgets GPU (`DIR-04`).
- **Sorties** : Catalogue des systèmes Niagara, spécifications de textures packées (channel packing) et budgets d'overdraw.
- **Méthodes de travail** : Utilisation de Cutout Geometry sur les sprites transparents et désactivation par distance.
- **Références** : `research/technical-reference.md` (`ART-09`).
- **Modèles de livrables** : `vfx-system-spec.md`, `vfx-budget-table.csv`.
- **Critères d'acceptation** : Impact visuel fort sans nuire à la lisibilité du gameplay, budget GPU VFX < 1.5 ms.
- **Règles de validation** : Profilage GPU par `ENG-07` et validation lisibilité par `GD-05`.

---

## 6. DÉPARTEMENT AUDIO & LOCALIZATION (`AUD-01` à `AUD-04`)

### `AUD-01` — Audio Director
- **Périmètre** : Vision sonore globale, Audio Bible, architecture de mixage dynamique (HDR Audio) et cohérence acoustique de Kinshasa.
- **Responsabilités** : Définir l'identité sonore de chaque commune, les priorités de mixage (voix > indices gameplay > musique > ambiances) et les budgets mémoire audio.
- **Limites** : Ne compose pas les morceaux individuels (`AUD-03`) et ne développe pas le code C++ d'intégration middleware (`ENG-01`).
- **Entrées** : Piliers créatifs (`DIR-03`), World Bible (`WLD-01`), recherche culturelle (`WLD-02`).
- **Sorties** : `audio-bible.md`, architecture des bus de mixage Wwise, budgets RAM/voix audio.
- **Méthodes de travail** : Mixage hiérarchique calibré LUFS, virtualisation agressive des sources distantes.
- **Références** : `research/technical-reference.md` (`AUD-01`), `SRC-018`.
- **Modèles de livrables** : `audio-bible-template.md`, `mixing-bus-hierarchy.md`.
- **Critères d'acceptation** : Clarté permanente des informations ludiques et dialogues même dans les marchés les plus bruyants.
- **Règles de validation** : Validation créative par `DIR-03` et technique par `DIR-04`.

### `AUD-02` — Sound Designer
- **Périmètre** : Conception des effets sonores (SFX), ambiances urbaines de Kinshasa, bruitages véhicules/armes/folies et propagation spatiale Wwise / MetaSounds.
- **Responsabilités** : Spécifier les banques SFX, systèmes de variation non répétitifs (Random Containers/RTPC), et géométrie acoustique (Rooms & Portals).
- **Limites** : Ne gère pas la musique adaptative (`AUD-03`) ni le doublage vocal (`AUD-04`).
- **Entrées** : Audio Bible (`AUD-01`), fiches véhicules (`GD-06`), combat (`GD-05`), environnements (`WLD-06`).
- **Sorties** : Spécifications Wwise/MetaSounds, matrices RTPC, plans de propagation acoustique urbaine.
- **Méthodes de travail** : Synthèse granulaire et couches aléatoires pour éliminer toute répétition mécanique.
- **Références** : `research/technical-reference.md` (`AUD-02`), Farnell (*Designing Sound*).
- **Modèles de livrables** : `sfx-asset-list.csv`, `wwise-rtpc-spec.md`.
- **Critères d'acceptation** : Immersion sonore organique, zéro saturation dans les zones denses, respect du budget voix actives.
- **Règles de validation** : Validation mixage par `AUD-01` et performance CPU/RAM par `ENG-07`.

### `AUD-03` — Music Designer
- **Périmètre** : Musique interactive adaptative (score dramatique) et programmation des stations de radio kinoises in-game (rumba, ndombolo, rap kinois, gospel).
- **Responsabilités** : Concevoir la structure des stems interactifs (transitions synchronisées au tempo/mesure), la grille des radios locales et le mode Streamer Safe.
- **Limites** : Ne gère pas les bruitages environnementaux (`AUD-02`).
- **Entrées** : Audio Bible (`AUD-01`), recherche culturelle/musicale (`WLD-02`), états de tension gameplay (`GD-01`, `GD-05`).
- **Sorties** : Spécifications Wwise Interactive Music, programmation des stations radio, cue sheets.
- **Méthodes de travail** : Vertical layering et horizontal re-sequencing synchronisés sur les mesures musicales.
- **Références** : `research/technical-reference.md` (`AUD-03`), Phillips (*A Composer's Guide to Game Music*).
- **Modèles de livrables** : `interactive-music-spec.md`, `radio-stations-programming.csv`.
- **Critères d'acceptation** : Transitions musicales fluides entre exploration et combat, séparation stricte des pistes sous licence tiers (mode streamer).
- **Règles de validation** : Validation culturelle (`WLD-02`), juridique (`PRD-02`) et artistique (`AUD-01`).

### `AUD-04` — Voice and Localization Specialist
- **Périmètre** : Pipeline d'internationalisation (i18n/L10n), direction de doublage, gestion des sous-titres et support typographique Unicode.
- **Responsabilités** : Structurer les clés de localisation UE5 (`.po`/`.locres`), gérer le multilinguisme (Français, Anglais, Lingala, Swahili, etc.), prévenir les débordements UI.
- **Limites** : N'écrit pas le scénario original (`NAR-02`), mais supervise son adaptation culturelle (transcréation).
- **Entrées** : Dialogues (`NAR-04`), textes UI (`GD-07`), glossaire culturel (`WLD-02`).
- **Sorties** : Pipeline Localization Dashboard UE5, glossaire multilingue, spécifications de doublage et sous-titrage.
- **Méthodes de travail** : Gel précoce des chaînes (String Freeze), tests d'expansion de texte (+35 %), support complet des glyphes lingala (`ɛ`, `ɔ`).
- **Références** : `research/technical-reference.md` (`NAR-05`), O'Hagan & Mangiron (*Game Localization*).
- **Modèles de livrables** : `localization-pipeline-spec.md`, `l10n-glossary.csv`.
- **Critères d'acceptation** : Zéro clé manquante (`TXT_MISSING`), zéro troncature UI, synchronisation labiale validée.
- **Règles de validation** : Audit LQA par `PRD-04` et accessibilité sous-titres par `PRD-06`.

---

## 7. DÉPARTEMENT ENGINEERING (`ENG-01` à `ENG-08`)

### `ENG-01` — Unreal Engine Specialist
- **Périmètre** : Architecture C++20 fondamentale sous UE5, World Partition, Data Layers, OFPA, Subsystems et gestion mémoire/streaming.
- **Responsabilités** : Concevoir l'ossature logicielle du projet, les règles de streaming spatial de Kinshasa et les mécanismes de chargement asynchrone.
- **Limites** : N'implémente pas les mécaniques spécifiques de combat/caméra (`ENG-02`) ni le rendu bas niveau RHI (`ENG-06`).
- **Entrées** : Technical Design Document (`DIR-04`), découpage carte (`WLD-04`).
- **Sorties** : Architecture C++ UE5, configuration World Partition & Data Layers, standards de codage moteur.
- **Méthodes de travail** : Chargement asynchrone systématique (`FStreamableManager`, `TSoftObjectPtr`), architecture par Subsystems.
- **Références** : `research/technical-reference.md` (`ENG-01`), `SRC-001` (World Partition Documentation).
- **Modèles de livrables** : `ue5-architecture-spec.md`, `world-partition-config.md`.
- **Critères d'acceptation** : Zéro chargement synchrone bloquant sur le Game Thread, architecture modulaire compilable rapidement.
- **Règles de validation** : Revue d'architecture par `DIR-04` et profilage streaming par `ENG-07`.

### `ENG-02` — Gameplay Programmer
- **Périmètre** : Implémentation C++ des systèmes de jeu, Gameplay Ability System (GAS), Enhanced Input, composants d'interaction et caméras.
- **Responsabilités** : Traduire les spécifications du département Game Design en code C++ déterministe, modulaire et exposé proprement aux Blueprints.
- **Limites** : Ne développe pas les outils éditeur (`ENG-03`) ni les solveurs physiques (`ENG-05`).
- **Entrées** : Spécifications Game Design (`GD-01`..`GD-06`), architecture UE5 (`ENG-01`).
- **Sorties** : Architecture C++ GAS/Components, contrats d'interface Blueprint/C++.
- **Méthodes de travail** : Décomposition en Actor Components, gestion d'états par Gameplay Tags, code testable unitairement.
- **Références** : `research/technical-reference.md` (`ENG-02`), `SRC-002` (GAS Documentation).
- **Modèles de livrables** : `gameplay-cpp-spec.md`.
- **Critères d'acceptation** : Latence d'entrée minimale, comportement déterministe, couverture par tests unitaires.
- **Règles de validation** : Revue de code par `ENG-01` et tests fonctionnels par `PRD-05`.

### `ENG-03` — Tools Programmer
- **Périmètre** : Outils internes éditeur UE5 (C++ Slate, Editor Utility Widgets, Python API), validateurs d'assets pré-commit et automatisation de pipeline.
- **Responsabilités** : Concevoir et maintenir les outils accélérant le travail des équipes Art, World Design, Narrative et QA.
- **Limites** : Ne développe pas les fonctionnalités runtime du jeu (`ENG-02`).
- **Entrées** : Règles de validation 3D (`ART-04`), besoins d'automatisation de tous les départements.
- **Sorties** : Spécifications de plugins éditeur, validateurs (`UEditorValidatorBase`), scripts Python d'automatisation.
- **Méthodes de travail** : Philosophie "Immutable Data & Fast Iteration" inspirée d'Insomniac Games (`SRC-007`) et Guerrilla (`SRC-010`).
- **Références** : `research/industry-methodologies.md` (Insomniac & Guerrilla), `research/technical-reference.md` (`ENG-03`).
- **Modèles de livrables** : `editor-tool-spec.md`.
- **Critères d'acceptation** : Réduction mesurable des opérations manuelles, blocage automatique des assets non conformes avant commit.
- **Règles de validation** : Tests d'ergonomie avec les utilisateurs finaux et validation par `DIR-04`.

### `ENG-04` — Houdini Specialist
- **Périmètre** : Génération procédurale de la ville de Kinshasa (voirie, îlots urbains, bâtiments modulaires, câblages électriques, végétation) via Houdini (HDA/PDG) et UE5 PCG.
- **Responsabilités** : Construire les graphes SOP/PDG exploitant OpenStreetMap/DEM et les règles d'urbanisme (`WLD-03`) pour alimenter UE5 World Partition et ZoneGraph.
- **Limites** : Ne sculpte pas les monuments héroïques uniques (`ART-02`).
- **Entrées** : Typologie urbaine (`WLD-03`), kits modulaires (`ART-02`), règles de trafic (`AI-03`).
- **Sorties** : Spécifications HDA/PDG, pipeline OSM -> Houdini -> UE5 PCG / ZoneGraph.
- **Méthodes de travail** : Export en Hierarchical Instanced Static Meshes (HISM) et calcul distribué PDG inspiré d'Epic *City Sample* (`SRC-004`) et SideFX (`SRC-005`).
- **Références** : `research/technical-reference.md` (`ENG-04`), `SRC-004`, `SRC-005`.
- **Modèles de livrables** : `hda-pipeline-spec.md`, `pcg-rules-matrix.csv`.
- **Critères d'acceptation** : Génération déterministe (seed fixe), temps de cuisson maîtrisé, génération automatique des splines ZoneGraph.
- **Règles de validation** : Validation spatiale par `WLD-04` et performance instanciation par `ENG-07`.

### `ENG-05` — Physics Engineer
- **Périmètre** : Simulation physique temps réel sous UE5 Chaos Physics, Chaos Destruction, Chaos Cloth et véhicules Chaos.
- **Responsabilités** : Configurer les solveurs de collision, la fracturation contrôlée des décors urbains, les profils ragdoll et la dynamique des véhicules.
- **Limites** : Ne conçoit pas les courbes ludiques de conduite (`GD-06`), mais implémente leur modèle physique stable.
- **Entrées** : Spécifications véhicules (`GD-06`), assets destructibles (`ART-02`), budgets CPU (`DIR-04`).
- **Sorties** : Architecture Chaos Physics, profils de collision et sommeil physique, paramètres de véhicules.
- **Méthodes de travail** : Mise en sommeil agressive des débris, proxys convexes simplifiés, Async Physics Tick.
- **Références** : `research/technical-reference.md` (`AI-04`, `GD-06`).
- **Modèles de livrables** : `chaos-physics-spec.md`, `collision-channels-matrix.csv`.
- **Critères d'acceptation** : Budget physique < 1.5 ms/frame, zéro instabilité/tremblement (jitter) ou traversée de sol.
- **Règles de validation** : Profilage CPU par `ENG-07` et tests de collision par `PRD-05`.

### `ENG-06` — Rendering Engineer
- **Périmètre** : Pipeline graphique bas niveau DX12/Vulkan, Nanite, Lumen, Virtual Shadow Maps (VSM), rendu de l'eau (fleuve Congo) et scalabilité graphique.
- **Responsabilités** : Optimiser les passes de rendu, personnaliser les shaders graphiques critiques et définir les profils de qualité (Low à Ultra).
- **Limites** : Ne réalise pas la direction artistique d'éclairage (`ART-07`).
- **Entrées** : Budgets GPU (`DIR-04`), besoins visuels (`ART-01`, `ART-07`, `ART-08`).
- **Sorties** : Architecture pipeline graphique, configuration VSM/Lumen/TSR, matrice de scalabilité graphique.
- **Méthodes de travail** : Analyses captures RenderDoc/PIX, désactivation du WPO à moyenne distance sur la végétation.
- **Références** : `research/technical-reference.md` (`ENG-05`), Akenine-Möller (*Real-Time Rendering*).
- **Modèles de livrables** : `rendering-pipeline-spec.md`, `scalability-presets.csv`.
- **Critères d'acceptation** : Stabilité temporelle de l'image, respect strict des budgets GPU par passe.
- **Règles de validation** : Validation technique par `DIR-04` et benchmarks par `ENG-07`.

### `ENG-07` — Performance Engineer
- **Périmètre** : Profilage global CPU/GPU/RAM/VRAM, élimination des saccades (stutters/hitches) et surveillance continue des budgets.
- **Responsabilités** : Analyser les traces Unreal Insights, piloter la collecte du cache PSO, optimiser le streaming World Partition et émettre les alertes de dépassement.
- **Limites** : Ne modifie pas le design des fonctionnalités, mais impose des contraintes techniques ou correctifs d'optimisation.
- **Entrées** : Budgets cibles (`DIR-04`), métriques issues des bots QA (`PRD-05`), traces Unreal Insights.
- **Sorties** : Rapports de performance par quartier, correctifs d'optimisation bas niveau, règles de streaming.
- **Méthodes de travail** : Mesure des percentiles P95/P99 frametime sur parcours automatisés dans Kinshasa.
- **Références** : `research/technical-reference.md` (`ENG-06`).
- **Modèles de livrables** : `performance-budget-report.md`, `pso-caching-protocol.md`.
- **Critères d'acceptation** : 99 % des frames sous le budget cible (16.6 ms Performance / 33.3 ms Qualité), zéro crash Out-Of-Memory.
- **Règles de validation** : Validation obligatoire avant chaque jalon majeur auprès de `DIR-04` et `DIR-07`.

### `ENG-08` — Build Engineer
- **Périmètre** : Infrastructure CI/CD, contrôle de source (Perforce/Git LFS), Unreal Automation Tool (UAT), BuildGraph, Horde, Zen Server DDC et packaging sécurisé.
- **Responsabilités** : Maintenir les pipelines de compilation incrémentale et nocturne, le cache dérivé partagé (DDC) et le chiffrement AES-256 des archives `.pak`.
- **Limites** : N'écrit pas le code gameplay (`ENG-02`).
- **Entrées** : Codebase (`ENG-01`..`ENG-06`), suite de tests (`PRD-05`).
- **Sorties** : Pipelines BuildGraph/Horde, configuration Zen Server, protocole de packaging signé et chiffré.
- **Méthodes de travail** : Builds continus automatisés avec déclenchement des tests Gauntlet post-cooking.
- **Références** : `research/technical-reference.md` (`ENG-07`, `ENG-08`).
- **Modèles de livrables** : `ci-cd-buildgraph-spec.md`, `pak-security-protocol.md`.
- **Critères d'acceptation** : Build incrémental < 15 min, disponibilité infrastructure > 99.5 %, impact chiffrement < 1 %.
- **Règles de validation** : Audit de sécurité et validation par `DIR-04`.

---

## 8. DÉPARTEMENT PRODUCTION & QUALITY (`PRD-01` à `PRD-06`)

### `PRD-01` — Production Planner
- **Périmètre** : Planification opérationnelle, découpage en sprints, gestion des dépendances inter-départements et suivi de vélocité.
- **Responsabilités** : Traduire la roadmap exécutive en plannings détaillés, détecter les goulots d'étranglement et orchestrer les rituels de suivi.
- **Limites** : Ne prend pas les décisions budgétaires stratégiques (`DIR-02`) ni créatives (`DIR-03`).
- **Entrées** : Jalons (`DIR-02`), graphes de dépendances (`skill-dependencies.md`), estimations des départements.
- **Sorties** : Plans de sprints, matrices RACI, tableaux de suivi des dépendances.
- **Méthodes de travail** : Hybride Agile/Waterfall par jalon, buffers systématiques de 15 % pour absorber les imprévus open world.
- **Références** : `research/technical-reference.md` (`PROD-02`), Keith (*Agile Game Development with Scrum*).
- **Modèles de livrables** : `sprint-plan-template.md`, `raci-matrix.csv`.
- **Critères d'acceptation** : Aucune dépendance critique orpheline, visibilité claire sur le chemin critique.
- **Règles de validation** : Revue hebdomadaire avec `DIR-02` et `DIR-01`.

### `PRD-02` — Risk Manager
- **Périmètre** : Identification, évaluation et plans de mitigation des risques (techniques, culturels, juridiques/licences, planning).
- **Responsabilités** : Maintenir le registre des risques de ZAÏRE, déclencher les alertes précoces et proposer des plans de contingence.
- **Limites** : Ne résout pas directement les bugs techniques, mais pilote la réduction d'exposition au risque.
- **Entrées** : Lacunes documentaires (`research/research-gaps.md`), rapports techniques (`DIR-04`), retours culturels (`WLD-02`).
- **Sorties** : `risk-register.csv`, plans de mitigation par risque critique.
- **Méthodes de travail** : Cotation Probabilité × Impact, revue à chaque jalon et lors de l'introduction de nouvelles technologies.
- **Références** : `research/research-gaps.md`, `research/technical-reference.md` (`PROD-01`).
- **Modèles de livrables** : `risk-register-template.csv`.
- **Critères d'acceptation** : 100 % des risques critiques (score >= 12/25) disposent d'un plan d'action assigné.
- **Règles de validation** : Validation par `DIR-02` et `DIR-07`.

### `PRD-03` — Documentation Specialist
- **Périmètre** : Rédaction technique, maintenance de la base de connaissances (`knowledge/`), gestion des identifiants uniques et traçabilité des sources.
- **Responsabilités** : Formater, indexer et versionner tous les livrables validés ; garantir l'absence de doublons d'identifiants dans le registre.
- **Limites** : Ne valide pas seul le fond métier (`DIR-06` et les directeurs de pôle valident le fond).
- **Entrées** : Livrables produits par tous les skills, sources documentaires (`research/source-registry.csv`).
- **Sorties** : Base de connaissances structurée, registre d'entités à jour, guides d'onboarding.
- **Méthodes de travail** : Docs-as-Code en Markdown/CSV/JSON, diagrammes Mermaid, contrôle strict des statuts (`PROPOSED` -> `CONFIRMED`).
- **Références** : `architecture/knowledge-management.md`, Bhatti (*Docs for Developers*).
- **Modèles de livrables** : `entity-registry-entry.md`, `technical-guide-template.md`.
- **Critères d'acceptation** : Documentation à jour à chaque livraison, zéro lien mort ou ID dupliqué.
- **Règles de validation** : Supervision directe par `DIR-06` (Documentation Director).

### `PRD-04` — QA Architect
- **Périmètre** : Stratégie d'assurance qualité globale, plans de test open world par quadrillage géographique de Kinshasa et protocoles de certification.
- **Responsabilités** : Concevoir les matrices de couverture de test, protocoles de non-régression, critères de sévérité des bugs et checklists de certification plateforme.
- **Limites** : N'écrit pas les scripts C++ de tests automatisés (`PRD-05`).
- **Entrées** : GDD (`GD-01`..`GD-07`), carte des quartiers (`WLD-04`), exigences qualité (`DIR-07`).
- **Sorties** : Master QA Test Plan, grille de quadrillage QA de Kinshasa, checklists de certification.
- **Méthodes de travail** : Quadrillage spatial systématique de la carte, protocoles de reproductibilité déterministe (position, seed, état quêtes).
- **Références** : `research/technical-reference.md` (`QA-01`), Schultz & Bryant (*Game Testing*).
- **Modèles de livrables** : `qa-test-plan-template.md`, `bug-report-schema.json`.
- **Critères d'acceptation** : Couverture de 100 % des quartiers et systèmes critiques, reproductibilité des anomalies > 90 %.
- **Règles de validation** : Approbation par `DIR-07`.

### `PRD-05` — Test Engineer
- **Périmètre** : Automatisation des tests sous Unreal Gauntlet, Functional Tests Actors et bots d'exploration autonome pour détection de régressions FPS/RAM.
- **Responsabilités** : Spécifier et maintenir les suites de tests automatisés nocturnes, bots de traversée de Kinshasa et alertes CI/CD.
- **Limites** : Ne remplace pas les tests d'ergonomie et d'expérience joueur humains (`PRD-04`).
- **Entrées** : Plans de test (`PRD-04`), budgets performance (`ENG-07`), pipeline CI/CD (`ENG-08`).
- **Sorties** : Spécifications de tests Gauntlet, scripts de bots d'exploration, rapports automatisés de régression.
- **Méthodes de travail** : Synchronisation événementielle (sans délais fixes `sleep`) pour éliminer les faux positifs.
- **Références** : `research/technical-reference.md` (`QA-02`), Epic *Gauntlet Automation Framework*.
- **Modèles de livrables** : `gauntlet-test-spec.md`, `automated-perf-summary.csv`.
- **Critères d'acceptation** : Couverture des systèmes critiques > 80 %, taux de faux positifs < 2 %.
- **Règles de validation** : Intégration CI vérifiée avec `ENG-08` et validation par `PRD-04`.

### `PRD-06` — Accessibility Specialist
- **Périmètre** : Accessibilité visuelle, auditive, motrice et cognitive selon les Xbox Accessibility Guidelines (XAG).
- **Responsabilités** : Auditer les designs UI/UX, contrôles, combat et sous-titres ; spécifier les options d'assistance (daltonisme, remapping, maintien QTE, TTS).
- **Limites** : Ne développe pas les shaders ou widgets UMG (`ART-08`, `ENG-02`), mais définit leurs exigences fonctionnelles.
- **Entrées** : Spécifications UI/UX (`GD-07`), contrôles (`GD-05`, `GD-06`), localisation/sous-titres (`AUD-04`).
- **Sorties** : Matrice de conformité XAG, spécifications du menu d'accessibilité, rapports d'audit.
- **Méthodes de travail** : "Accessibility by Design" dès la pré-production, double codage systématique (couleur + forme/icône).
- **Références** : `research/technical-reference.md` (`QA-03`), Microsoft *Xbox Accessibility Guidelines (XAG)*.
- **Modèles de livrables** : `xag-compliance-matrix.csv`, `accessibility-audit-template.md`.
- **Critères d'acceptation** : Conformité aux standards XAG majeurs, sous-titres lisibles avec fond paramétrable et identification du locuteur.
- **Règles de validation** : Validation finale par `DIR-07` (Quality Director).
