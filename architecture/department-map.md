# Cartographie des Départements — ZAÏRE STUDIO OS

L'organisation opérationnelle est structurée en **7 départements spécialisés** regroupant **50 skills indépendants**, placés sous la coordination de la **Direction Centrale (7 rôles)**.

---

## Département 1 : NARRATIVE (6 Skills)
*Justification du regroupement* : Couvre toute la chaîne de création dramatique, de l'architecture globale des arcs jusqu'à la vérification de cohérence canonique et l'implémentation des graphes de dialogue multilingues (Français / Lingala / Swahili / Anglais).

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `NAR-01` | **Narrative Architect** | Structure macroscopique des actes, thèmes, embranchements narratifs majeurs et alignement ludo-narratif. |
| `NAR-02` | **Screenwriter** | Écriture des scénarios de missions principales, scènes cinématiques, synopsis et beat sheets dramatiques. |
| `NAR-03` | **Character Writer** | Biographies, psychologie, arcs d'évolution, voix distinctives et relations des personnages (`CHR-*`, `FAM-*`). |
| `NAR-04` | **Dialogue Designer** | Conception des arbres de dialogue interactifs, barks contextuels en monde ouvert, métadonnées émotionnelles et caméra. |
| `NAR-05` | **Lore Manager** | Maintenance de l'encyclopédie canonique de ZAÏRE, chronologie historique, factions (`ORG-*`), médias et archives in-game. |
| `NAR-06` | **Continuity Editor** | Audit éditorial anti-contradiction entre quêtes, dialogues, chronologie et états persistants du monde. |

---

## Département 2 : WORLD DESIGN (6 Skills)
*Justification du regroupement* : Aligne la recherche culturelle et urbaine réelle sur Kinshasa avec la structuration spatiale macroscopique (Open World) et microscopique (Level/Environment Design), garantissant le passage de relais propre du blockout gameplay vers l'habillage artistique.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `WLD-01` | **Worldbuilding Architect** | Conception macroscopique de l'univers de Kinshasa fictif mais ancré, identité des communes (`DST-*`), institutions et sociologie. |
| `WLD-02` | **Cultural Researcher** | Recherche historique, anthropologique, musicale (rumba/ndombolo), vestimentaire et linguistique (français kinois/lingala). |
| `WLD-03` | **Urban Researcher** | Analyse de la morphologie urbaine de Kinshasa (voirie, typologie bâtie Gombe vs Matonge/Kalamu, flux fluviaux, repères). |
| `WLD-04` | **Open World Designer** | Découpage de la carte en régions jouables, densité de POI (règle des 40s), lignes de mire (landmarks) et pacing d'exploration. |
| `WLD-05` | **Level Designer** | Création des espaces jouables en blockout/greyboxing, métriques de déplacement/caméra, couverts et parcours de parkour. |
| `WLD-06` | **Environment Designer** | Direction spatiale des biomes urbains/naturels, spécification des kits architecturaux et narration environnementale par lieu (`LOC-*`). |

*(Note : `Level Designer` a été ajouté au département World Design pour assurer le pont indispensable entre `Open World Designer` et `Environment Artist`.)*

---

## Département 3 : GAME DESIGN (7 Skills)
*Justification du regroupement* : Rassemble toutes les mécaniques interactives, l'équilibrage mathématique et l'ergonomie joueur, pilotés par le `Lead Game Designer` et implémentés sous UE5 via Gameplay Ability System (GAS) et Common UI.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `GD-01` | **Game Systems Designer** | Conception des boucles de gameplay principales (Core Loops), règles systémiques, états et interactions émergentes (`SYS-*`). |
| `GD-02` | **Mission Designer** | Conception détaillée des quêtes principales et secondaires, objectifs, machines à états, embranchements et conditions d'échec (`MSN-*`). |
| `GD-03` | **Economy Designer** | Modélisation mathématique des flux monétaires (devises in-game), coûts, récompenses, boutiques et prévention de l'inflation. |
| `GD-04` | **Progression Designer** | Courbes d'expérience, déblocage de compétences, réputation auprès des factions/quartiers et rythme de montée en puissance. |
| `GD-05` | **Combat Designer** | Mécaniques de mêlée, tir, couverture, timing d'animation (hitstop/frames), archétypes ennemis et système d'Attack Tokens. |
| `GD-06` | **Vehicle Designer** | Comportement et tuning de conduite des véhicules kinois (motos-taxis Wewa, taxis jaunes, bus Transco, 4x4) et physique par surface (`VEH-*`). |
| `GD-07` | **UI/UX Designer** | Architecture de l'information, HUD contextuel minimaliste, carte interactive de Kinshasa, téléphone diégétique et ergonomie Common UI. |

*(Note : `UI/UX Designer` a été ajouté au département Game Design pour couvrir l'interface joueur et la navigation urbaine.)*

---

## Département 4 : AI & SIMULATION (4 Skills)
*Justification du regroupement* : Regroupe l'intelligence artificielle individuelle et les simulations de masse orientées données (UE5 Mass Entity / ZoneGraph) indispensables pour donner vie à une mégapole africaine dense sans saturer le budget CPU.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `AI-01` | **NPC AI Architect** | Architecture des IA individuelles (State Trees, Behavior Trees, EQS, AI Perception, Smart Objects) pour alliés, civils et ennemis. |
| `AI-02` | **Crowd Simulation Specialist** | Simulation de foules denses (marchés de Kinshasa) via UE5 Mass Entity / Mass Crowd, RVO avoidance et hydratation dynamique d'acteurs. |
| `AI-03` | **Traffic AI Specialist** | Graphes routiers ZoneGraph, gestion des intersections complexes (ronds-points kinois), comportement des conducteurs et déblocage de trafic. |
| `AI-04` | **Decision Systems Designer** | Conception des modèles Utility AI, systèmes de réputation dynamique, routines quotidiennes des PNJ et événements systémiques émergents. |

---

## Département 5 : ART & ANIMATION (9 Skills)
*Justification du regroupement* : Couvre l'intégralité de la production visuelle temps réel, du concept art jusqu'aux shaders, à l'éclairage équatorial Lumen et aux effets visuels Niagara.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `ART-01` | **Art Director** | Définition de la charte visuelle globale (Art Bible), palettes chromatiques par quartier, cohérence stylistique et revues artistiques. |
| `ART-02` | **Environment Artist** | Production des kits architecturaux kinois, matériaux PBR (latérite, béton humide, tôle), végétation tropicale et set dressing. |
| `ART-03` | **Character Artist** | Sculpture anatomique, vêtements réalistes (Marvelous Designer), système modulaire de PNJ, Groom cheveux et shaders de peau. |
| `ART-04` | **3D Pipeline Specialist** | Standards de modélisation modulaire, topologie Nanite, densité de texels, UV mapping, baking et validation d'export FBX/USD. |
| `ART-05` | **Animation Specialist** | Locomotion temps réel (Motion Matching UE5), Control Rig, Motion Warping, IK procédural et graphes d'animation. |
| `ART-06` | **Motion Capture Specialist** | Planification des sessions MoCap corporelles/faciales, nettoyage des courbes, retargeting squelettique et pipeline MetaHuman Animator. |
| `ART-07` | **Lighting Specialist** | Éclairage physique équatorial (Lumen GI, Sky Atmosphere, Volumetric Clouds), cycle jour/nuit, météo tropicale et color grading ACES. |
| `ART-08` | **Technical Artist** | Master Materials HLSL/Substrate, optimisation draw calls/PSO, rigging complexe et passerelles outils DCC -> UE5. |
| `ART-09` | **VFX Specialist** | Effets visuels temps réel sous Niagara (pluies diluviennes, poussière rouge, fumée d'échappement, impacts) et contrôle de l'overdraw GPU. |

*(Note : `Motion Capture Specialist` et `VFX Specialist` ont été ajoutés pour couvrir respectivement l'acquisition de mouvement réaliste et les effets atmosphériques/combat sous Niagara.)*

---

## Département 6 : AUDIO & LOCALIZATION (4 Skills)
*Justification du regroupement* : Centralise l'identité sonore de Kinshasa (spatialisation acoustique Wwise, captation terrain, musique congolaise interactive) et l'adaptation linguistique/doublage multilingue.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `AUD-01` | **Audio Director** | Vision sonore globale (Audio Bible), hiérarchie de mixage HDR, cohérence acoustique entre quartiers et direction artistique audio. |
| `AUD-02` | **Sound Designer** | Design sonore des ambiances urbaines kinoises, véhicules, armes, folies et architecture middleware Wwise / MetaSounds (Rooms & Portals). |
| `AUD-03` | **Music Designer** | Composition interactive adaptative (stems synchronisés au tempo) et programmation des radios locales (rumba, ndombolo, rap kinois). |
| `AUD-04` | **Voice and Localization Specialist** | Pipeline d'internationalisation (UE5 Localization Dashboard, `.locres`), casting/direction de doublage, support Unicode lingala (`ɛ`, `ɔ`) et LQA. |

---

## Département 7 : ENGINEERING (8 Skills)
*Justification du regroupement* : Regroupe l'ingénierie logicielle C++ UE5, la génération procédurale Houdini/PCG, la simulation physique, le rendu bas niveau et l'infrastructure CI/CD.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `ENG-01` | **Unreal Engine Specialist** | Architecture C++20 sous UE5, World Partition, Data Layers, OFPA, Subsystems, gestion mémoire et streaming asynchrone. |
| `ENG-02` | **Gameplay Programmer** | Implémentation C++ des mécaniques joueur via Gameplay Ability System (GAS), Enhanced Input, composants modulaires et caméras. |
| `ENG-03` | **Tools Programmer** | Développement de plugins éditeur UE5 (Slate, Editor Utility Widgets, Python API), validateurs d'assets pré-commit et automatisation. |
| `ENG-04` | **Houdini Specialist** | Création d'outils procéduraux HDA/PDG exploitant OpenStreetMap/DEM pour générer routes, îlots urbains, câblages et végétation via UE5 PCG. |
| `ENG-05` | **Physics Engineer** | Configuration et optimisation de Chaos Physics, Chaos Destruction, Chaos Cloth, profils de collision et stabilité des solveurs. |
| `ENG-06` | **Rendering Engineer** | Customisation et optimisation du pipeline graphique DX12/Vulkan (Nanite, Lumen, Virtual Shadow Maps, shaders d'eau du fleuve Congo, TSR). |
| `ENG-07` | **Performance Engineer** | Profilage CPU/GPU (Unreal Insights, RenderDoc), élimination des hitches PSO/streaming, respect des budgets frametime (16.6ms / 33.3ms) et VRAM. |
| `ENG-08` | **Build Engineer** | Infrastructure CI/CD (Horde, BuildGraph, UAT, Perforce/Git LFS, Zen Server DDC), cooking automatisé et packaging chiffré. |

*(Note : `Rendering Engineer` a été ajouté pour couvrir l'optimisation graphique bas niveau RHI/VSM/Lumen identifiée en Phase 1.)*

---

## Département 8 : PRODUCTION & QUALITY (6 Skills)
*Justification du regroupement* : Assure la planification opérationnelle, la traçabilité documentaire, la gestion des risques, l'assurance qualité manuelle/automatisée et la conformité d'accessibilité.

| ID | Skill | Rôle Principal |
| :--- | :--- | :--- |
| `PRD-01` | **Production Planner** | Découpage en sprints, estimation de charge, suivi des dépendances inter-départements (Jira/ShotGrid) et orchestration des jalons. |
| `PRD-02` | **Risk Manager** | Identification, quantification et mitigation des risques techniques, culturels, juridiques et de planning tout au long de la production. |
| `PRD-03` | **Documentation Specialist** | Rédaction technique (Docs-as-Code), maintien des wikis, mise à jour du registre d'entités et indexation des livrables validés. |
| `PRD-04` | **QA Architect** | Stratégie globale d'assurance qualité open world, plans de test par quadrillage géographique de Kinshasa et protocoles de certification. |
| `PRD-05` | **Test Engineer** | Développement et maintenance des tests automatisés (Unreal Gauntlet, Functional Tests, bots d'exploration mémoire/FPS) et triage de bugs. |
| `PRD-06` | **Accessibility Specialist** | Conformité aux normes Xbox Accessibility Guidelines (XAG), options daltonisme, sous-titres enrichis, remapping et assistance motrice/cognitive. |

*(Note : `Accessibility Specialist` a été ajouté pour garantir l'intégration native de l'accessibilité dès la conception.)*
