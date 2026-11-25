# Référentiel Technique Exhaustif — ZAÏRE STUDIO OS (46 Domaines)

Chaque domaine est analysé selon les **12 axes standardisés** requis pour la spécification future des Agent Skills.

---

## PÔLE 1 : DIRECTION, PRODUCTION & GOUVERNANCE

### 1. Executive Production (`PROD-01`)
1. **Responsabilités** : Définition de la vision commerciale et budgétaire, gestion des relations éditeurs/investisseurs, validation des jalons majeurs (Vertical Slice, Alpha, Beta, Gold).
2. **Compétences requises** : Finance de production vidéoludique, négociation contractuelle, gestion des risques stratégiques, leadership exécutif.
3. **Méthodes de travail** : Revues trimestrielles de portefeuille, gouvernance par comités de pilotage (SteerCo), gestion de scénarios budgétaires.
4. **Outils professionnels** : Excel/Google Sheets financiers, ShotGrid, Jira Align, PowerBI/Tableau.
5. **Technologies utilisées** : Modèles prévisionnels de ROI, pipelines de télémétrie exécutive.
6. **Processus de production** : Pré-production (Greenlight) -> Production -> Post-production -> Certification -> Exploitation Live.
7. **Livrables attendus** : P&L prévisionnel, roadmap exécutive, contrats de prestation/édition, rapports de risques.
8. **Problèmes courants** : Dérive des coûts (scope creep), retards sur le chemin critique, sous-estimation des coûts de localisation et QA.
9. **Solutions techniques** : Découpage modulaire des fonctionnalités (feature gating), suivi hebdomadaire de la vélocité et du burn rate.
10. **Critères de qualité** : Respect du budget à ±5 %, respect des jalons de certification plateforme, rentabilité projetée.
11. **Ressources de formation** : GDC Production Track, *The Game Production Toolbox* (Heather Maxwell Chandler).
12. **Références documentaires** : Chandler, H. M. (2019), *The Game Production Toolbox*, CRC Press.

### 2. Production Management (`PROD-02`)
1. **Responsabilités** : Coordination quotidienne des équipes pluridisciplinaires, planification des sprints, déblocage des dépendances inter-départements.
2. **Compétences requises** : Méthodes Agiles (Scrum/Kanban), gestion de dépendances complexes, communication interpersonnelle, estimation de charge.
3. **Méthodes de travail** : Stand-ups quotidiens, sprint planning, rétrospectives, triages de bugs hebdomadaires.
4. **Outils professionnels** : Jira, ShotGrid (Autodesk Flow Production Tracking), Confluence, Miro, Slack/Discord.
5. **Technologies utilisées** : Automatisations Jira/Perforce, webhooks de suivi de builds.
6. **Processus de production** : Décomposition des Epics en User Stories -> Estimation en points -> Suivi burndown -> Validation QA.
7. **Livrables attendus** : Plannings de sprints, matrices RACI, comptes-rendus de triage, bilans de vélocité.
8. **Problèmes courants** : Goulots d'étranglement entre Art et Tech Art, dépendances non détectées sur les niveaux open world.
9. **Solutions techniques** : Visualisation des graphes de dépendances dans ShotGrid, buffers systématiques de 15 % par sprint.
10. **Critères de qualité** : Taux de complétion de sprint > 85 %, zéro blocage critique non assigné > 24h.
11. **Ressources de formation** : GDC Producer Bootcamp, Atlassian Agile Coach.
12. **Références documentaires** : Keith, C. (2010), *Agile Game Development with Scrum*, Addison-Wesley.

### 3. Creative Direction (`PROD-03`)
1. **Responsabilités** : Maintien de l'unité esthétique, narrative et ludique de ZAÏRE ; arbitrage final sur les choix d'expérience joueur.
2. **Compétences requises** : Vision artistique et ludique holistique, narration visuelle, critique constructive, direction d'équipes créatives.
3. **Méthodes de travail** : Revues créatives hebdomadaires, validation des Bibles (Art Bible, Narrative Bible, Gameplay Pillars).
4. **Outils professionnels** : PureRef, Miro, Figma, Unreal Engine Editor (revues in-engine).
5. **Technologies utilisées** : Sequencer UE5, outils de capture vidéo/captures d'écran annotées.
6. **Processus de production** : Définition des piliers -> Prototypage Vertical Slice -> Revues par quartier/mission -> Polish final.
7. **Livrables attendus** : Vision Document, Piliers Créatifs, Notes de revue de builds.
8. **Problèmes courants** : Fragmentation tonale entre quartiers ou missions, sur-accumulation de mécaniques incohérentes.
9. **Solutions techniques** : Grille d'évaluation systématique de chaque fonctionnalité face aux 3 piliers créatifs de ZAÏRE.
10. **Critères de qualité** : Cohérence sensorielle immédiate, identité kinoise authentique et reconnaissable.
11. **Ressources de formation** : GDC Art & Design Keynotes, *The Art of Game Design* (Jesse Schell).
12. **Références documentaires** : Schell, J. (2019), *The Art of Game Design: A Book of Lenses*, CRC Press.

### 4. Technical Direction (`PROD-04`)
1. **Responsabilités** : Choix de l'architecture logicielle et graphique, définition des budgets matériels cibles (PC/Consoles), gouvernance de la dette technique.
2. **Compétences requises** : Architecture moteur C++, rendu temps réel, gestion mémoire, pipelines de données à grande échelle.
3. **Méthodes de travail** : Architecture Decision Records (ADR), audits techniques mensuels, revues de code critiques.
4. **Outils professionnels** : Visual Studio, Rider, Unreal Insights, RenderDoc, Perforce Helix Core.
5. **Technologies utilisées** : Unreal Engine 5.x, C++20, HLSL, Houdini Engine, Python.
6. **Processus de production** : Spécification d'architecture -> Proof of Concept -> Établissement des budgets -> Surveillance continue.
7. **Livrables attendus** : Technical Design Document (TDD), budgets mémoire/GPU par système, standards de codage.
8. **Problèmes courants** : Explosion de la VRAM avec les textures 4K et Nanite/Lumen, temps de chargement excessifs.
9. **Solutions techniques** : Virtual Texturing, pools mémoire stricts, validation automatique des assets avant commit.
10. **Critères de qualité** : Stabilité (0 crash bloquant), respect strict des budgets mémoire par plateforme.
11. **Ressources de formation** : GDC Technical Direction Track, Epic Developer Community.
12. **Références documentaires** : Gregory, J. (2018), *Game Engine Architecture* (3rd ed.), CRC Press.

### 5. LiveOps & Telemetry Analytics (`PROD-05`)
1. **Responsabilités** : Instrumentation du jeu pour collecter les données comportementales anonymisées, analyse de rétention, difficulté et bugs en conditions réelles.
2. **Compétences requises** : Data science appliquée au jeu vidéo, SQL/Python, statistiques, respect RGPD/vie privée.
3. **Méthodes de travail** : Définition des plans de marquage (tracking plans), analyse post-playtest, A/B testing d'équilibrage.
4. **Outils professionnels** : Python (Pandas), Grafana/Tableau, ElasticSearch, Unreal Analytics.
5. **Technologies utilisées** : REST APIs asynchrones, sérialisation JSON/Protobuf, bases de données orientées séries temporelles.
6. **Processus de production** : Spécification des événements -> Implémentation C++ -> Playtests -> Tableaux de bord -> Ajustements design.
7. **Livrables attendus** : Schéma d'événements télémétriques, heatmaps de morts/blocages dans Kinshasa, rapports d'équilibrage.
8. **Problèmes courants** : Surcharge réseau par trop d'événements, biais d'interprétation des données brutes.
9. **Solutions techniques** : Batching local des événements, corrélation systématique avec les retours qualitatifs QA.
10. **Critères de qualité** : Impact CPU < 0.1 ms, conformité stricte aux règles de confidentialité.
11. **Ressources de formation** : GDC Game Analytics talks, *Game Data Science* (El-Nasr et al.).
12. **Références documentaires** : El-Nasr, M. S. et al. (2021), *Game Data Science*, Oxford University Press.

---

## PÔLE 2 : GAME DESIGN & SYSTÈMES DE JEU

### 6. Game Design (`GD-01`)
1. **Responsabilités** : Conception des règles fondamentales, des systèmes d'interaction et de la boucle de progression du joueur.
2. **Compétences requises** : Pensée systémique, prototypage rapide, mathématiques d'équilibrage, psychologie de l'engagement.
3. **Méthodes de travail** : Prototypage papier et Blueprint, itération par playtests hebdomadaires, documentation modulaire.
4. **Outils professionnels** : Unreal Engine Blueprints, Machinations.io, Notion/Confluence, Excel.
5. **Technologies utilisées** : UE5 Gameplay Ability System (GAS), DataAssets, Gameplay Tags.
6. **Processus de production** : Concept -> Prototype gris -> Playtest interne -> Équilibrage numérique -> Production finale.
7. **Livrables attendus** : Game Design Documents (GDD) systémiques, tableaux d'équilibrage, prototypes jouables.
8. **Problèmes courants** : Systèmes isolés qui n'interagissent pas entre eux, courbe d'apprentissage trop abrupte.
9. **Solutions techniques** : Utilisation unifiée des Gameplay Tags UE5 pour permettre des interactions émergentes entre systèmes.
10. **Critères de qualité** : Prise en main intuitive en moins de 3 minutes, profondeur tactique durable.
11. **Ressources de formation** : GDC Game Design Workshop, *Rules of Play* (Salen & Zimmerman).
12. **Références documentaires** : Salen, K., & Zimmerman, E. (2003), *Rules of Play*, MIT Press.

### 7. Open World Design (`GD-02`)
1. **Responsabilités** : Structuration macroscopique de la carte de Kinshasa, répartition des points d'intérêt (POI), gestion du rythme entre tension et exploration.
2. **Compétences requises** : Urbanisme ludique, gestion des lignes de mire (weenies), pacing spatial, narration environnementale.
3. **Méthodes de travail** : Cartographie topographique, règle des "40 secondes" d'intérêt visuel, zonage par identité de quartier.
4. **Outils professionnels** : Unreal Engine World Partition, Houdini, QGIS/OpenStreetMap, Miro.
5. **Technologies utilisées** : UE5 World Partition, Hierarchical LOD (HLOD), Streaming Sources.
6. **Processus de production** : Carte 2D -> Blockout macroscopique -> Implantation des landmarks -> Densification des POI -> Tests de traversée.
7. **Livrables attendus** : Carte maîtresse de Kinshasa zonée, grille de densité d'activités, spécifications de landmarks.
8. **Problèmes courants** : Zones vides ennuyeuses, fatigue de répétition (syndrome checklist), désorientation du joueur.
9. **Solutions techniques** : Repères verticaux distincts par commune (ex. Tour de l'Échangeur, Fleuve Congo), rencontres dynamiques non scriptées.
10. **Critères de qualité** : Navigation possible sans mini-carte grâce aux repères visuels, temps de traversée équilibré.
11. **Ressources de formation** : GDC Open World Design talks (Sucker Punch, CDPR, Ubisoft).
12. **Références documentaires** : Totten, C. W. (2019), *An Architectural Approach to Level Design* (2nd ed.), CRC Press.

### 8. Mission Design (`GD-03`)
1. **Responsabilités** : Conception des missions principales et secondaires, objectifs, conditions de réussite/échec, intégration narrative et ludique.
2. **Compétences requises** : Scénarisation interactive, gestion d'états complexes, rythme dramatique, scripting.
3. **Méthodes de travail** : Diagrammes d'états (flowcharts), greyboxing de mission, revues de rythme.
4. **Outils professionnels** : Unreal Engine Blueprints, Articy:draft, Twine, State Trees.
5. **Technologies utilisées** : UE5 Subsystems de quêtes, Data Layers pour les états persistants du monde.
6. **Processus de production** : Pitch mission -> Beat sheet -> Greybox jouable -> Intégration dialogues/cinématiques -> Polish & Debug.
7. **Livrables attendus** : Mission Design Documents, graphes d'états de quête, scripts de mission fonctionnels.
8. **Problèmes courants** : Blocages de progression (soft-locks) si le joueur quitte la zone ou tue un PNJ clé, linéarité excessive.
9. **Solutions techniques** : Machines à états tolérantes aux interruptions, sauvegardes par checkpoints atomiques, approches multiples (furtivité/action/social).
10. **Critères de qualité** : Zéro soft-lock, variété des situations de jeu, impact visible sur le monde.
11. **Ressources de formation** : GDC Narrative & Quest Design talks.
12. **Références documentaires** : Kremers, R. (2009), *Level Design: Concept, Theory, and Practice*, CRC Press.

### 9. Level Design (`GD-04`)
1. **Responsabilités** : Création détaillée des espaces jouables (bâtiments, ruelles, intérieurs, arènes de combat), placement des couverts et chemins de parkour.
2. **Compétences requises** : Maîtrise des métriques personnage (hauteur de saut, largeur de couloir), composition spatiale, affordance.
3. **Méthodes de travail** : Blockout/Greyboxing strict avant habillage artistique, tests de lisibilité sans textures.
4. **Outils professionnels** : Unreal Engine Modeling Tools, CubeGrid, Blender, Maya.
5. **Technologies utilisées** : NavMesh UE5, Smart Links, volumes de couverture et d'escalade.
6. **Processus de production** : Schéma 2D -> Gym de métriques -> Blockout 3D -> Playtest gameplay -> Passage de relais à l'Environment Art.
7. **Livrables attendus** : Niveaux blockout validés, document des métriques spatiales du studio.
8. **Problèmes courants** : Caméra bloquée dans les intérieurs exigus, collisions invisibles frustrantes, perte d'orientation.
9. **Solutions techniques** : Respect strict des gabarits minimaux de caméra (ex. largeur couloir >= 3.5m), guidage par éclairage et lignes directrices.
10. **Critères de qualité** : Fluidité de déplacement sans accroc géométrique, lisibilité immédiate des sorties et couverts.
11. **Ressources de formation** : Naughty Dog GDC 2018 (*Blockmesh and Lighting Tips*), World of Level Design.
12. **Références documentaires** : Rogers, S. (2014), *Level Up! The Guide to Great Video Game Design* (2nd ed.), Wiley.

### 10. Combat Design (`GD-05`)
1. **Responsabilités** : Conception des affrontements à mains nues, armes blanches et armes à feu, comportements d'attaque ennemis, sensation d'impact (game feel).
2. **Compétences requises** : Timing d'animation (frames d'anticipation, d'action, de récupération), équilibrage des dégâts, ergonomie des contrôles.
3. **Méthodes de travail** : Prototypage en salle de test (Combat Gym), analyse image par image des hitboxes.
4. **Outils professionnels** : Unreal Engine Animation Montage, Gameplay Ability System, Sequencer.
5. **Technologies utilisées** : AnimNotifies, Motion Warping, Hitstop, Camera Shakes, Niagara VFX.
6. **Processus de production** : Prototypage des coups -> Calibrage des frames -> IA d'archétypes ennemis -> Tests de foule -> Polish sensoriel.
7. **Livrables attendus** : Combat Gym, matrices de dégâts/stamina, spécifications des archétypes ennemis.
8. **Problèmes courants** : Caméra désorientante en mêlée urbaine, ennemis qui attaquent simultanément hors champ.
9. **Solutions techniques** : Système de jetons d'attaque (Attack Tokens) limitant les assauts simultanés, ciblage contextuel intelligent.
10. **Critères de qualité** : Réactivité des inputs < 100 ms, lisibilité claire des attaques ennemies télégraphiées.
11. **Ressources de formation** : GDC Combat Design talks (*God of War*, *Ghost of Tsushima*, *Marvel's Spider-Man*).
12. **Références documentaires** : Swink, S. (2008), *Game Feel: A Game Designer's Guide to Virtual Sensation*, CRC Press.

### 11. Vehicle Systems (`GD-06`)
1. **Responsabilités** : Modélisation de la conduite et du comportement physique des véhicules emblématiques de Kinshasa (taxis jaunes, motos Wewa, bus Transco, 4x4).
2. **Compétences requises** : Dynamique du véhicule (adhérence, suspension, transfert de masse), tuning arcade/simcade, gestion des dégâts.
3. **Méthodes de travail** : Tests sur circuits d'essai (asphalte, boue, nids-de-poule), télémétrie de vitesse et freinage.
4. **Outils professionnels** : Unreal Engine Chaos Vehicles, Houdini, courbe de couple moteur.
5. **Technologies utilisées** : Chaos Vehicle Movement Component, Physical Materials (asphalte, latérite, eau), Force Feedback.
6. **Processus de production** : Rig squelettique véhicule -> Paramétrage Chaos -> Tuning maniabilité -> Audio moteur -> Intégration trafic.
7. **Livrables attendus** : Classes de véhicules configurées, profils physiques par surface, système de déformation.
8. **Problèmes courants** : Tonneaux incontrôlables sur les trottoirs, motos instables à basse vitesse, collisions bloquantes.
9. **Solutions techniques** : Abaissement artificiel du centre de gravité, stabilisation gyroscopique assistée pour les deux-roues.
10. **Critères de qualité** : Prise en main immédiate au clavier et à la manette, sensations distinctes par catégorie de véhicule.
11. **Ressources de formation** : Unreal Engine Chaos Vehicles Documentation, GDC Vehicle Physics talks.
12. **Références documentaires** : Epic Games, *Chaos Vehicles User Guide*, Unreal Engine 5 Documentation.

### 12. Economy Design (`GD-07`)
1. **Responsabilités** : Équilibrage des flux monétaires (Franc Congolais / devises in-game), coût des équipements, véhicules, propriétés et récompenses de mission.
2. **Compétences requises** : Modélisation mathématique, théorie des jeux, lutte contre l'inflation virtuelle, psychologie de la progression.
3. **Méthodes de travail** : Simulations Monte-Carlo sur tableurs, modélisation de puits et sources (Faucets & Sinks).
4. **Outils professionnels** : Machinations.io, Excel/Python (simulations économiques), DataTables UE5.
5. **Technologies utilisées** : DataTables, Gameplay Effects (GAS) pour les modificateurs de prix/réputation.
6. **Processus de production** : Modèle théorique -> Simulation 100 heures de jeu -> Intégration DataTables -> Ajustement post-playtest.
7. **Livrables attendus** : Modèle mathématique de l'économie, grilles tarifaires, courbes de progression.
8. **Problèmes courants** : Accumulation excessive d'argent en milieu de jeu rendant les récompenses obsolètes, ou manque frustrant de ressources.
9. **Solutions techniques** : Création de puits économiques récurrents et aspirationnels (personnalisation, gestion d'affaires locales, équipements rares).
10. **Critères de qualité** : Tension économique maintenue sur toute la durée de la campagne sans grind obligatoire.
11. **Ressources de formation** : GDC Game Economy talks, Machinations Academy.
12. **Références documentaires** : Adams, E., & Dormans, J. (2012), *Game Mechanics: Advanced Game Design*, New Riders.

### 13. UI/UX Design (`GD-08`)
1. **Responsabilités** : Conception de l'interface utilisateur (HUD, carte interactive de Kinshasa, téléphone in-game, inventaire) et de l'expérience utilisateur globale.
2. **Compétences requises** : Ergonomie cognitive, architecture de l'information, design graphique, motion design UI, accessibilité visuelle.
3. **Méthodes de travail** : Wireframing, prototypage interactif, tests utilisateurs avec suivi oculaire/ergonomique.
4. **Outils professionnels** : Figma, Adobe Illustrator/After Effects, Unreal Motion Graphics (UMG), Common UI.
5. **Technologies utilisées** : UE5 Common UI Plugin (support manette/clavier fluide), Material UI shaders, SVG/SDF icons.
6. **Processus de production** : Wireframes -> Maquettes Figma -> Prototypes interactifs -> Implémentation UMG -> Tests d'accessibilité.
7. **Livrables attendus** : UI Style Guide, maquettes haute fidélité, widgets UMG/Common UI optimisés.
8. **Problèmes courants** : Surcharge visuelle masquant la richesse de Kinshasa, navigation lente à la manette.
9. **Solutions techniques** : HUD contextuel dynamique (masquage automatique hors combat/navigation), utilisation du smartphone in-game pour les fonctions diégétiques.
10. **Critères de qualité** : Lisibilité parfaite à 3 mètres sur TV comme sur moniteur PC, navigation en 3 clics maximum.
11. **Ressources de formation** : Game UI Database, GDC UX Summit.
12. **Références documentaires** : Hodent, C. (2017), *The Gamer's Brain: How Neuroscience and UX Can Impact Video Game Design*, CRC Press.

---

## PÔLE 3 : NARRATION, CULTURE & MONDE

### 14. Narrative Design (`NAR-01`)
1. **Responsabilités** : Fusion entre l'histoire et les mécaniques de jeu, écriture des quêtes, barks contextuels et narration environnementale.
2. **Compétences requises** : Dramaturgie interactive, dialogue naturel, narration non linéaire, collaboration étroite avec le Level/Mission Design.
3. **Méthodes de travail** : Écriture itérative en parallèle du greyboxing, tables de lecture (table reads) avec acteurs.
4. **Outils professionnels** : Articy:draft, Final Draft, Celtx, Confluence, Unreal Engine Sequencer.
5. **Technologies utilisées** : Systèmes de déclencheurs narratifs, bases de données de répliques conditionnelles (barks).
6. **Processus de production** : Synopsis -> Structure en actes -> Dialogues premier jet -> Intégration moteur -> Réécriture post-playtest.
7. **Livrables attendus** : Bible narrative, scripts de missions, banque de barks contextuels.
8. **Problèmes courants** : Dissonance ludo-narrative (actions du joueur en monde ouvert contredisant le héros des cinématiques).
9. **Solutions techniques** : Système de réputation et commentaires dynamiques des PNJ réagissant au comportement réel du joueur.
10. **Critères de qualité** : Rythme soutenu, personnages nuancés, absence d'exposition artificielle.
11. **Ressources de formation** : GDC Narrative Summit, *Interactive Storytelling for Video Games* (Josiah Lebowitz).
12. **Références documentaires** : Heussner, T. et al. (2015), *The Game Narrative Toolbox*, CRC Press.

### 15. Worldbuilding (`NAR-02`)
1. **Responsabilités** : Construction de la cohérence historique, géographique, économique et sociale de la version fictive mais ancrée de Kinshasa.
2. **Compétences requises** : Sociologie urbaine, géographie, écriture encyclopédique, création d'identité visuelle de marques et institutions fictives.
3. **Méthodes de travail** : Cartographie thématique par commune, création de fiches de factions, chronologies historiques.
4. **Outils professionnels** : World Anvil, Notion/Confluence, Miro, QGIS.
5. **Technologies utilisées** : Bases de données structurées (JSON/CSV) alimentant les journaux in-game, radios et affiches.
6. **Processus de production** : Recherche terrain -> Définition des districts -> Factions & médias locaux -> Signalétique urbaine.
7. **Livrables attendus** : World Bible complète, guide des communes de Kinshasa, chartes des factions et médias fictifs.
8. **Problèmes courants** : Caricatures culturelles ou manque d'épaisseur historique des quartiers.
9. **Solutions techniques** : Collaboration directe avec des consultants culturels kinois et ancrage dans l'architecture et l'histoire réelles.
10. **Critères de qualité** : Chaque quartier possède une identité sonore, visuelle et sociale immédiatement identifiable.
11. **Ressources de formation** : GDC Worldbuilding lectures, archives urbaines de Kinshasa.
12. **Références documentaires** : Wolf, M. J. P. (2012), *Building Imaginary Worlds*, Routledge.

### 16. Dialogue Systems (`NAR-03`)
1. **Responsabilités** : Conception technique et éditoriale des conversations interactives, gestion des interruptions, caméras de dialogue et mémoire conversationnelle.
2. **Compétences requises** : Architecture de graphes conditionnels, mise en scène procédurale, gestion du multilinguisme (code-switching Français/Lingala).
3. **Méthodes de travail** : Standardisation des métadonnées émotionnelles et gestuelles par réplique.
4. **Outils professionnels** : Articy:draft, Yarn Spinner, Unreal Engine Dialogue Voice/Wave, FaceFX/Audio2Face.
5. **Technologies utilisées** : Graphes de nœuds C++, synchronisation labiale automatique (Lip-Sync), métadonnées de caméra.
6. **Processus de production** : Écriture structurée -> Export JSON/XML -> Import UE5 -> Génération Lip-Sync -> Validation en jeu.
7. **Livrables attendus** : Pipeline d'import de dialogues, outil de prévisualisation de conversations, spécifications de mise en scène.
8. **Problèmes courants** : Dialogues rigides ("têtes parlantes" statiques), coupures audio lors des interruptions en monde ouvert.
9. **Solutions techniques** : Système de reprise intelligente ("Où en étais-je ?") inspiré des standards AAA modernes et caméras dynamiques procédurales.
10. **Critères de qualité** : Transitions naturelles entre exploration et conversation, synchronisation labiale crédible.
11. **Ressources de formation** : GDC 2019 Ubisoft (*Procedural Generation of Cinematic Dialogues*).
12. **Références documentaires** : Epic Games, *Dialogue System & Audio Localization Documentation*, UE5.

### 17. Cultural and Historical Research (`NAR-04`)
1. **Responsabilités** : Vérification de l'exactitude culturelle, linguistique, musicale, vestimentaire et architecturale liée à Kinshasa et à la RDC.
2. **Compétences requises** : Recherche documentaire et archivistique, anthropologie urbaine, maîtrise des registres du lingala et du français kinois.
3. **Méthodes de travail** : Constitution de dossiers iconographiques, entretiens avec des natifs, relecture culturelle des scripts et assets.
4. **Outils professionnels** : PureRef, bases d'archives numériques, glossaires collaboratifs.
5. **Technologies utilisées** : Bibliothèques de référence visuelle et sonore taguées par époque et quartier.
6. **Processus de production** : Collecte documentaire -> Synthèse par thème -> Revue des concepts -> Audit des niveaux avant validation.
7. **Livrables attendus** : Dossiers de référence culturelle, lexique argotique kinois (langue de la rue), guide d'authenticité.
8. **Problèmes courants** : Anachronismes architecturaux, erreurs de traduction en lingala, stéréotypes externes.
9. **Solutions techniques** : Boucle de validation obligatoire par des référents culturels à chaque jalon majeur.
10. **Critères de qualité** : Reconnaissance authentique par le public congolais et pertinence universelle pour les joueurs internationaux.
11. **Ressources de formation** : Archives musicales (Rumba congolaise - patrimoine UNESCO), études urbaines sur Kinshasa (Filip De Boeck).
12. **Références documentaires** : De Boeck, F., & Plissart, M.-F. (2004), *Kinshasa: Tales of the Invisible City*, Ludion.

### 18. Localization (`NAR-05`)
1. **Responsabilités** : Adaptation linguistique et culturelle complète du jeu (textes, UI, sous-titres, doublages) vers les marchés cibles (Français, Anglais, Lingala/Swahili en VO/ST, Espagnol, Portugais, etc.).
2. **Compétences requises** : Internationalisation logicielle (i18n), gestion des chaînes de caractères, direction de doublage, contrôle qualité linguistique (LQA).
3. **Méthodes de travail** : Gel précoce des chaînes (String Freeze), fourniture de contexte visuel aux traducteurs.
4. **Outils professionnels** : Unreal Engine Localization Dashboard, Crowdin/MemoQ, Gridly, Excel.
5. **Technologies utilisées** : Formats `.po` / `.locres`, polices Unicode complètes (support des caractères spéciaux du lingala : ɛ, ɔ).
6. **Processus de production** : Extraction des clés -> Traduction/Transcréation -> Enregistrement voix -> Intégration `.locres` -> LQA en jeu.
7. **Livrables attendus** : Glossaire terminologique, fichiers localisés compilés, rapports LQA.
8. **Problèmes courants** : Débordement de texte dans l'UI (text expansion de +30 % en français/allemand), caractères manquants dans les polices.
9. **Solutions techniques** : Design UI élastique avec marges de 35 %, tests automatisés de troncature de texte.
10. **Critères de qualité** : Zéro clé brute affichée (`TXT_MISSING`), cohérence des registres de langue.
11. **Ressources de formation** : GDC Localization Summit, IGDA Localization SIG.
12. **Références documentaires** : O'Hagan, M., & Mangiron, C. (2013), *Game Localization*, John Benjamins Publishing.

---

## PÔLE 4 : INTELLIGENCE ARTIFICIELLE & SIMULATION VIVANTE

### 19. NPC AI (`AI-01`)
1. **Responsabilités** : Conception des comportements individuels des PNJ (combattants, policiers, civils, commerçants), perception, navigation et prise de décision.
2. **Compétences requises** : Architecture IA (Behavior Trees, State Trees, Utility AI), algorithmes de pathfinding, programmation C++ temps réel.
3. **Méthodes de travail** : Tests en environnements contrôlés (AI Gyms), débogage visuel temps réel.
4. **Outils professionnels** : Unreal Engine State Trees, Behavior Trees, Environment Query System (EQS), Gameplay Debugger.
5. **Technologies utilisées** : UE5 AI Perception Component, Recast NavMesh, Smart Objects.
6. **Processus de production** : Définition des archétypes -> Arbres de décision -> Intégration Smart Objects -> Optimisation CPU -> Tests en foule.
7. **Livrables attendus** : Systèmes IA modulaires, requêtes EQS de couverture/flanquement, profils de perception.
8. **Problèmes courants** : PNJ bloqués contre des obstacles dynamiques, réactions identiques et prévisibles, coût CPU élevé en combat urbain.
9. **Solutions techniques** : Utilisation d'EQS asynchrone, étalement des mises à jour IA (Time-Slicing) et Smart Objects pour les interactions contextuelles.
10. **Critères de qualité** : Budget CPU IA < 2.5 ms/frame, comportements crédibles et réactifs aux actions du joueur.
11. **Ressources de formation** : GDC AI Summit, *Game AI Pro* (Steve Rabin).
12. **Références documentaires** : Rabin, S. (Ed.) (2013–2017), *Game AI Pro* (Vol. 1–3), CRC Press.

### 20. Crowd Simulation (`AI-02`)
1. **Responsabilités** : Simulation de centaines à milliers de citoyens dans les artères commerçantes et marchés de Kinshasa sans effondrement des performances.
2. **Compétences requises** : Architecture orientée données (ECS / Data-Oriented Design), évitement de foule, systèmes de LOD visuels et logiques.
3. **Méthodes de travail** : Profilage massif par densité de zone, transition transparente entre entité légère et personnage complet.
4. **Outils professionnels** : Unreal Engine Mass Entity, Mass Crowd, Vertex Animation Textures (VAT), Houdini.
5. **Technologies utilisées** : UE5 Mass Framework (Archetypes, Fragments, Processors), ZoneGraph, RVO Avoidance.
6. **Processus de production** : Définition des voies piétonnes (ZoneGraph) -> Configuration Mass Entity -> Spawning dynamique -> Hydratation en acteurs complets à proximité.
7. **Livrables attendus** : Graphes de circulation piétonne de Kinshasa, processeurs Mass Crowd, système d'hydratation/déshydratation d'acteurs.
8. **Problèmes courants** : Clones visuels évidents dans la foule, piétons traversant les véhicules, chute drastique de FPS.
9. **Solutions techniques** : Randomisation des matériaux par instance (Per-Instance Custom Data), transition vers des acteurs complets uniquement dans un rayon de 15–20 m autour du joueur.
10. **Critères de qualité** : 500+ PNJ simultanés à l'écran pour un coût CPU < 2.0 ms.
11. **Ressources de formation** : Epic Games *City Sample* Documentation (Mass AI), GDC Crowd Simulation talks.
12. **Références documentaires** : Epic Games, *Mass Entity & Mass Crowd Overview*, Unreal Engine 5 Documentation.

### 21. Traffic Simulation (`AI-03`)
1. **Responsabilités** : Gestion de la circulation routière urbaine (voies, intersections, feux, dépassements, réactions aux sirènes et accidents).
2. **Compétences requises** : Théorie des graphes routiers, cinématique de suivi de splines, résolution d'interblocages (deadlocks) aux carrefours.
3. **Méthodes de travail** : Modélisation des réseaux via splines, simulation d'heures de pointe vs trafic nocturne.
4. **Outils professionnels** : Unreal Engine ZoneGraph, Mass Traffic, Houdini (génération de réseaux routiers).
5. **Technologies utilisées** : ZoneGraph Lanes, réservations d'intersections, interpolation cinématique avec bascule physique Chaos lors d'une collision.
6. **Processus de production** : Tracé du réseau routier -> Règles de priorité -> Simulation Mass Traffic -> Bascule physique sur impact -> Profilage.
7. **Livrables attendus** : Réseau ZoneGraph complet de Kinshasa, système de gestion des carrefours, profils de conduite par type de véhicule.
8. **Problèmes courants** : Embouteillages permanents bloqués aux grands ronds-points, véhicules disparaissant dans le champ de vision du joueur.
9. **Solutions techniques** : Timeouts de déblocage automatique aux intersections, règles strictes d'apparition/disparition hors frustum caméra et derrière occlusion.
10. **Critères de qualité** : Fluidité du trafic réaliste sans blocage infini, transition imperceptible entre mode rail et physique complète.
11. **Ressources de formation** : Epic Games *Matrix Awakens / City Sample* Mass Traffic architecture.
12. **Références documentaires** : Epic Games, *City Sample Quick Start & ZoneGraph Documentation*, UE5.

### 22. Physics Simulation (`AI-04`)
1. **Responsabilités** : Gestion des corps rigides, destruction d'éléments urbains (étals, palissades, mobilier), ragdolls réalistes et simulation de câbles/tissus.
2. **Compétences requises** : Mécanique des corps rigides, contraintes physiques, optimisation des solveurs de collision.
3. **Méthodes de travail** : Hiérarchisation des collisions (canaux dédiés), fracturation pré-calculée contrôlée.
4. **Outils professionnels** : Unreal Engine Chaos Physics, Chaos Destruction, Chaos Cloth, Houdini RBD.
5. **Technologies utilisées** : Geometry Collections, Physical Animation Component, Async Physics Tick.
6. **Processus de production** : Création des proxys de collision -> Fracturation Chaos -> Configuration des seuils de rupture -> Optimisation sommeil physique.
7. **Livrables attendus** : Bibliothèque d'objets destructibles urbains, profils ragdoll actifs, configurations Chaos Cloth.
8. **Problèmes courants** : Effondrement des FPS lors de destructions multiples, objets tremblants (jitter) au sol.
9. **Solutions techniques** : Mise en sommeil agressive des débris, limitation du nombre maximal de corps actifs simultanés, proxys convexes simplifiés.
10. **Critères de qualité** : Budget physique < 1.5 ms/frame, aucune interpénétration majeure du joueur.
11. **Ressources de formation** : Unreal Engine Chaos Physics & Destruction Documentation.
12. **Références documentaires** : Millington, I. (2010), *Game Physics Engine Development* (2nd ed.), CRC Press.

---

## PÔLE 5 : ARTS VISUELS, PERSONNAGES & ANIMATION

### 23. Character Design (`ART-01`)
1. **Responsabilités** : Création de l'identité visuelle des personnages principaux, secondaires et archétypes de foule (silhouettes, costumes, accessoires).
2. **Compétences requises** : Anatomie, design vestimentaire contemporain africain/kinois, narration par le costume, théorie des couleurs.
3. **Méthodes de travail** : Recherches de silhouettes, planches d'expression, feuilles de modèle (turnarounds) annotées techniquement.
4. **Outils professionnels** : Adobe Photoshop, Procreate, ZBrush (concept sculpt), PureRef.
5. **Technologies utilisées** : Rendu de concept 2D/3D hybride, nuanciers calibrés PBR.
6. **Processus de production** : Brief narratif -> Vignettes de silhouettes -> Exploration couleurs -> Turnaround orthographique + détails matériaux.
7. **Livrables attendus** : Character Concept Sheets (face/profil/dos), callouts matériaux et coutures.
8. **Problèmes courants** : Designs magnifiques en 2D mais impossibles à rigger ou trop coûteux en simulation de tissu temps réel.
9. **Solutions techniques** : Validation précoce avec le Lead Character Artist et le Technical Animator avant finalisation du concept.
10. **Critères de qualité** : Silhouette reconnaissable instantanément, fidélité culturelle aux styles vestimentaires de Kinshasa.
11. **Ressources de formation** : GDC Visual Arts Track, *Character Design Quarterly*.
12. **Références documentaires** : Bancroft, T. (2006), *Creating Characters with Personality*, Watson-Guptill.

### 24. 3D Modeling (`ART-02`)
1. **Responsabilités** : Production des modèles 3D d'objets (props), véhicules, mobilier urbain et éléments architecturaux modulaires.
2. **Compétences requises** : Modélisation polygonale et subdivision, maîtrise de la topologie, dépliage UV propre, baking de maps.
3. **Méthodes de travail** : Modélisation modulaire sur grille stricte, workflow High-to-Low poly ou Nanite-ready.
4. **Outils professionnels** : Blender, Autodesk Maya, ZBrush, Marmoset Toolbag, Substance 3D Painter.
5. **Technologies utilisées** : Formats FBX/USD, Nanite Static Meshes, Texel Density standardisée (ex. 10.24 px/cm).
6. **Processus de production** : Blockout métrique -> High Poly -> Low Poly / Nanite mesh -> UV & Baking -> Texturing PBR -> Export UE5.
7. **Livrables attendus** : Assets 3D modulaires propres (pivots cohérents, collisions, LODs/Nanite).
8. **Problèmes courants** : Pivots mal placés cassant l'assemblage modulaire, densité de texels incohérente entre objets voisins.
9. **Solutions techniques** : Scripts de vérification automatique des pivots, échelles et densité de texels avant export.
10. **Critères de qualité** : Zéro face non-manifold, respect strict de la grille modulaire et des budgets mémoire texture.
11. **Ressources de formation** : Epic Games *Nanite Virtualized Geometry Documentation*, Beyond Extent.
12. **Références documentaires** : Epic Games, *Nanite Virtualized Geometry*, Unreal Engine 5 Documentation.

### 25. Environment Art (`ART-03`)
1. **Responsabilités** : Assemblage des quartiers de Kinshasa, création des biomes urbains et naturels (bords du fleuve Congo), matériaux et set dressing.
2. **Compétences requises** : Composition architecturale, narration environnementale, création de matériaux procéduraux PBR, feuillage temps réel.
3. **Méthodes de travail** : Assemblage par kits modulaires, mélange de textures par vertex painting / Runtime Virtual Texturing (RVT).
4. **Outils professionnels** : Unreal Engine 5, Substance 3D Designer, Quixel Megascans, SpeedTree, Houdini.
5. **Technologies utilisées** : UE5 Nanite, World Partition, Runtime Virtual Texturing (RVT), Foliage Instancing.
6. **Processus de production** : Habillage du blockout LD -> Kits architecturaux -> Matériaux d'usure tropicale (humidité, poussière rouge) -> Set dressing.
7. **Livrables attendus** : Quartiers complets habillés, bibliothèques de matériaux maîtres PBR, kits architecturaux kinois.
8. **Problèmes courants** : Répétition visible des textures sur les façades et routes, perte de lisibilité gameplay sous trop de détails.
9. **Solutions techniques** : World-Aligned Textures, Decals d'usure/affiches locales, hiérarchie de contraste respectant le blockout initial.
10. **Critères de qualité** : Crédibilité photographique de l'environnement, maintien des performances cible.
11. **Ressources de formation** : GDC Environment Art talks, 80 Level breakdowns.
12. **Références documentaires** : Epic Games, *World Building Guide*, Epic Developer Community.

### 26. Character Art (`ART-04`)
1. **Responsabilités** : Création des modèles 3D haute fidélité des personnages principaux et modulaires des PNJ (anatomie, visages, cheveux, vêtements).
2. **Compétences requises** : Sculpture anatomique réaliste, topologie faciale compatible FACS/ARKit, grooming capillaire (cheveux crépus/tresses), shaders de peau.
3. **Méthodes de travail** : Base meshes standardisés pour partager les rigs et animations entre tous les PNJ.
4. **Outils professionnels** : ZBrush, Marvelous Designer, Substance 3D Painter, MetaHuman Creator, Blender/Maya.
5. **Technologies utilisées** : UE5 Groom System (strands/cards), Subsurface Profile Shaders, Mutable Character Customization.
6. **Processus de production** : Sculpt anatomique -> Simulation vêtements Marvelous -> Retopologie & UV -> Textures PBR -> Groom cheveux -> Intégration UE5.
7. **Livrables attendus** : Personnages héros complets, système modulaire de PNJ kinois, shaders de peau et cheveux calibrés.
8. **Problèmes courants** : Coût GPU prohibitif des cheveux Groom sur une foule entière, déformations faciales non naturelles.
9. **Solutions techniques** : Utilisation de Groom Strands uniquement sur les héros en gros plan et bascule vers des Hair Cards optimisées pour les PNJ.
10. **Critères de qualité** : Rendu réaliste des peaux foncées sous éclairage équatorial (spécularité et subsurface scattering maîtrisés).
11. **Ressources de formation** : Guerrilla Games GDC 2018 (*Character Production on Horizon Zero Dawn*), MetaHuman Documentation.
12. **Références documentaires** : Epic Games, *MetaHuman & Groom Rendering Documentation*, UE5.

### 27. Animation (`ART-05`)
1. **Responsabilités** : Création des mouvements des personnages (locomotion, parkour urbain, combat, gestuelle sociale) et systèmes d'animation temps réel.
2. **Compétences requises** : Principes de l'animation, mécanique corporelle, graphes d'animation complexes, Motion Matching.
3. **Méthodes de travail** : Séparation stricte entre locomotion réactive et actions scriptées, tests de réactivité manette.
4. **Outils professionnels** : Autodesk Maya, Blender, Unreal Engine Control Rig, Motion Matching (Pose Search).
5. **Technologies utilisées** : UE5 Motion Matching, Motion Warping, Full Body IK, Linked Anim Layers.
6. **Processus de production** : Capture/Keyframe -> Nettoyage -> Tagging des bases de données Motion Matching -> Configuration Control Rig -> Tests terrain.
7. **Livrables attendus** : Bases de données de locomotion, Animation Blueprints modulaires, rigs d'interaction.
8. **Problèmes courants** : Transitions brusques entre marche/course/virage, pieds flottants dans les escaliers ou terrains accidentés.
9. **Solutions techniques** : Motion Matching couplé au Foot Placement IK procédural et au Motion Warping pour l'escalade d'obstacles.
10. **Critères de qualité** : Fluidité organique sans latence perçue par le joueur.
11. **Ressources de formation** : Rockstar GDC 2020 (*RDR2 Locomotion*), Epic Games *Motion Matching in UE5*.
12. **Références documentaires** : Epic Games, *Motion Matching in Unreal Engine*, Unreal Engine 5 Documentation.

### 28. Motion Capture (`ART-06`)
1. **Responsabilités** : Planification des sessions de capture de mouvement corporel et facial, direction d'acteurs sur plateau, nettoyage et retargeting des données.
2. **Compétences requises** : Gestion de plateau MoCap, résolution de marqueurs/capteurs inertiels, nettoyage de courbes d'animation, retargeting.
3. **Méthodes de travail** : Pré-visualisation temps réel sur plateau (Live Link), nomenclature stricte des prises (takes).
4. **Outils professionnels** : Vicon Shogun / OptiTrack Motive / Xsens MVN, MotionBuilder, Unreal Engine Live Link, Live Link Face.
5. **Technologies utilisées** : Formats FBX/BVH, IK Rig & IK Retargeter UE5, MetaHuman Animator.
6. **Processus de production** : Shot list -> Calibration plateau -> Capture -> Solve & Clean -> Retargeting vers squelette UE5 -> Livraison Animation.
7. **Livrables attendus** : Clips MoCap nettoyés, données faciales résolues, rapports de session.
8. **Problèmes courants** : Bruit haute fréquence sur les mains/doigts, décalage d'échelle entre l'acteur et le personnage 3D.
9. **Solutions techniques** : Gants de capture dédiés ou pose libraries manuelles, calibration précise des chaînes IK Retargeter.
10. **Critères de qualité** : Absence de tremblement articulaire, fidélité aux intentions de jeu d'acteur.
11. **Ressources de formation** : GDC Motion Capture Bootcamps, Epic Games *MetaHuman Animator Guide*.
12. **Références documentaires** : Menache, A. (2011), *Understanding Motion Capture for Computer Animation* (2nd ed.), Morgan Kaufmann.

### 29. Technical Art (`ART-07`)
1. **Responsabilités** : Pont entre artistes et programmeurs ; création de shaders maîtres, outils de validation, rigging complexe et optimisation des pipelines visuels.
2. **Compétences requises** : Mathématiques vectorielles/matricielles, HLSL/GLSL, Python/C++ éditeur, rigging, profilage GPU.
3. **Méthodes de travail** : Développement de shaders maîtres paramétrables pour éviter la prolifération de compilations.
4. **Outils professionnels** : Unreal Material Editor, HLSL, Houdini, Maya/Blender Python API, RenderDoc.
5. **Technologies utilisées** : Material Layers, Substrate (UE5), Custom Primitive Data, Control Rig.
6. **Processus de production** : Analyse des besoins artistiques -> Prototypage shader/rig -> Packaging outil -> Documentation -> Support production.
7. **Livrables attendus** : Bibliothèques de Master Materials, scripts d'export automatisés, rigs d'armes/véhicules.
8. **Problèmes courants** : Explosion du nombre de permutations de shaders (PSO hitches), matériaux trop coûteux en instructions pixel.
9. **Solutions techniques** : Réduction des commutateurs statiques (Static Switches) au profit de paramètres dynamiques, collecte PSO automatisée.
10. **Critères de qualité** : Temps de compilation shaders maîtrisé, zéro asset non conforme entrant dans le moteur.
11. **Ressources de formation** : GDC Technical Artist Bootcamp, Ben Cloward Shader Tutorials.
12. **Références documentaires** : Epic Games, *Material Best Practices & PSO Caching*, Unreal Engine 5 Documentation.

### 30. Lighting (`ART-08`)
1. **Responsabilités** : Éclairage artistique et technique de Kinshasa (cycle jour/nuit complet, intérieurs, conditions météo tropicales, cinématiques).
2. **Compétences requises** : Photographie et cinématographie, colorimétrie (ACES), compréhension physique de la lumière (lux, candela, température Kelvin).
3. **Méthodes de travail** : Éclairage basé sur des valeurs physiques réelles (EV100), passes de contraste pour la lisibilité gameplay.
4. **Outils professionnels** : Unreal Engine Lumen, Sky Atmosphere, Volumetric Clouds, Post Process Volumes, DaVinci Resolve (LUTs).
5. **Technologies utilisées** : Lumen Global Illumination & Reflections, MegaLights (UE5.5+), Exponential Height Fog, Exposure Metering.
6. **Processus de production** : Calibrage ciel/soleil physique -> Éclairage macro quartiers -> Éclairage intérieurs -> Cycle météo -> Color grading.
7. **Livrables attendus** : Presets atmosphériques par heure/météo, LUTs de colorimétrie, passes d'éclairage par quartier.
8. **Problèmes courants** : Intérieurs trop sombres ou surexposés lors du passage extérieur/intérieur (auto-exposure lente), bruit Lumen dans les zones étroites.
9. **Solutions techniques** : Courbes d'exposition manuelles calibrées par zone, ajustement de la Lumen Surface Cache et des Cards sur les meshes modulaires.
10. **Critères de qualité** : Contraste lisible à toute heure du jour et de la nuit, atmosphère tropicale vibrante.
11. **Ressources de formation** : Naughty Dog GDC 2014 (*Lighting of The Last of Us*), Epic Games *Lumen Technical Details*.
12. **Références documentaires** : Epic Games, *Lumen Technical Details in Unreal Engine*, UE5 Documentation.

### 31. VFX / Real-Time Visual Effects (`ART-09`)
1. **Responsabilités** : Conception des effets visuels temps réel (pluies torrentielles tropicales, poussière soulevée par les véhicules, étincelles, fumée, impacts).
2. **Compétences requises** : Dynamique des fluides simplifiée, shaders animés, timing visuel, optimisation de l'overdraw GPU.
3. **Méthodes de travail** : Réutilisation de textures packées (channel packing), hiérarchie visuelle des effets en combat.
4. **Outils professionnels** : Unreal Engine Niagara, Houdini (simulations Pyro/Flip -> VAT/Flipbooks), EmberGen, Substance Designer.
5. **Technologies utilisées** : Niagara GPU Particles, Data Interfaces, Flipbooks, Distance Field Collisions.
6. **Processus de production** : Référence vidéo -> Simulation Houdini/EmberGen -> Baking texture -> Assemblage Niagara -> Optimisation overdraw.
7. **Livrables attendus** : Systèmes Niagara modulaires, bibliothèques de textures VFX packées, événements météo dynamiques.
8. **Problèmes courants** : Chute massive de FPS causée par l'overdraw des particules transparentes (fumée, pluie dense).
9. **Solutions techniques** : Découpage précis des maillages de particules (Cutout Geometry), LOD de distance désactivant les particules secondaires.
10. **Critères de qualité** : Impact visuel fort sans masquer l'action du joueur, budget GPU VFX < 1.5 ms.
11. **Ressources de formation** : GDC Real-Time VFX Bootcamp, RealtimeVFX.com.
12. **Références documentaires** : Epic Games, *Niagara Visual Effects Documentation*, Unreal Engine 5.

---

## PÔLE 6 : AUDIO & MUSIQUE

### 32. Audio Engineering (`AUD-01`)
1. **Responsabilités** : Architecture du moteur audio, gestion de la propagation acoustique urbaine (écho entre immeubles, occlusion intérieurs), optimisation mémoire.
2. **Compétences requises** : Acoustique architecturale, DSP temps réel, intégration C++/Blueprint de middleware audio.
3. **Méthodes de travail** : Profilage continu des voix actives (virtualisation des sons distants), bus de mixage hiérarchiques.
4. **Outils professionnels** : Audiokinetic Wwise, Unreal Engine MetaSounds, Steam Audio / Project Acoustics.
5. **Technologies utilisées** : Spatial Audio (Portals & Rooms), HRTF binaural, compression Vorbis/Opus, streaming audio.
6. **Processus de production** : Architecture des bus Wwise -> Intégration Rooms/Portals -> Profilage voix -> Mixage dynamique (HDR Audio).
7. **Livrables attendus** : Projet Wwise structuré, système de propagation acoustique, budgets mémoire audio.
8. **Problèmes courants** : Saturation sonore dans les marchés denses de Kinshasa, coupures de voix par dépassement de limite matérielle.
9. **Solutions techniques** : Priorisation dynamique des voix (HDR Audio), virtualisation des sources au-delà du rayon audible.
10. **Critères de qualité** : Spatialisation précise, zéro craquement audio (buffer underrun), mémoire RAM audio < budget défini.
11. **Ressources de formation** : Audiokinetic Wwise Certification (Wwise-101/201/301), GDC Audio Track.
12. **Références documentaires** : Audiokinetic, *Wwise Spatial Audio Documentation*.

### 33. Sound Design (`AUD-02`)
1. **Responsabilités** : Création de l'identité sonore de Kinshasa (klaxons, vendeurs ambulants, générateurs électriques, moteurs, pas sur latérite, armes).
2. **Compétences requises** : Prise de son terrain (field recording), synthèse sonore, montage multipiste, design procédural non répétitif.
3. **Méthodes de travail** : Construction de variations multiples (random containers, modulation de pitch/filtre) pour éviter toute fatigue auditive.
4. **Outils professionnels** : REAPER, Pro Tools, iZotope RX, Wwise, enregistreurs terrain (Zoom F6 / Sound Devices).
5. **Technologies utilisées** : Synthèse granulaire pour moteurs de véhicules, convolution reverbs urbaines.
6. **Processus de production** : Enregistrement/Synthèse -> Édition/Nettoyage -> Intégration Wwise -> Réglage courbes d'atténuation in-game.
7. **Livrables attendus** : Banques d'effets sonores calibrées LUFS, systèmes sonores de véhicules et d'ambiances par quartier.
8. **Problèmes courants** : Répétition mécanique audible sur les bruits de pas ou les ambiances de foule.
9. **Solutions techniques** : Combinaison de couches aléatoires de micro-échantillons et variation continue liée à la vitesse/surface.
10. **Critères de qualité** : Immersion sonore immédiate, clarté du mixage (les indices gameplay restent toujours audibles).
11. **Ressources de formation** : Designing Sound, GDC Audio Bootcamp.
12. **Références documentaires** : Farnell, A. (2010), *Designing Sound*, MIT Press.

### 34. Music Direction (`AUD-03`)
1. **Responsabilités** : Direction artistique musicale, composition interactive adaptative et intégration des radios locales (rumba, ndombolo, rap kinois, gospel).
2. **Compétences requises** : Composition musicale, orchestration adaptative (vertical layering / horizontal re-sequencing), gestion des licences musicales.
3. **Méthodes de travail** : Découpage des compositions en stems interactifs pilotés par l'intensité du gameplay.
4. **Outils professionnels** : Cubase / Logic Pro / Ableton Live, Wwise Interactive Music Hierarchy, MetaSounds.
5. **Technologies utilisées** : Transitions synchronisées au tempo/mesure (beat/bar sync), streaming radio multi-stations dans les véhicules.
6. **Processus de production** : Direction musicale -> Composition/Licensing -> Export stems -> Intégration interactive -> Mixage final.
7. **Livrables attendus** : Bande originale interactive, programmation des stations de radio kinoises in-game, cue sheets.
8. **Problèmes courants** : Transitions musicales abruptes entre exploration et combat, conflits de droits d'auteur (streamer mode).
9. **Solutions techniques** : Transitions sur stingers musicaux calibrés, mode "Streamer Safe" séparant les musiques sous licence tierce.
10. **Critères de qualité** : Cohérence émotionnelle parfaite avec l'action, authenticité musicale congolaise.
11. **Ressources de formation** : GDC Music Track, *A Composer's Guide to Game Music* (Winifred Phillips).
12. **Références documentaires** : Phillips, W. (2014), *A Composer's Guide to Game Music*, MIT Press.

---

## PÔLE 7 : INGÉNIERIE LOGICIELLE, MOTEUR & OUTILS

### 35. Unreal Engine Development (`ENG-01`)
1. **Responsabilités** : Architecture C++ principale du jeu sous UE5, gestion du cycle de vie des acteurs, streaming World Partition, intégration des sous-systèmes.
2. **Compétences requises** : C++ moderne (C++20), macros et réflexion UE (`UCLASS`, `UPROPERTY`), gestion mémoire (Garbage Collection), multithreading (`TaskGraph`).
3. **Méthodes de travail** : Séparation stricte C++ (systèmes critiques, données) et Blueprints (exposition design, prototypage).
4. **Outils professionnels** : Visual Studio 2022, JetBrains Rider, Unreal Build Tool (UBT), Perforce.
5. **Technologies utilisées** : UE5 World Partition, Data Layers, One File Per Actor (OFPA), GameInstance/World Subsystems.
6. **Processus de production** : Architecture modules C++ -> Implémentation Subsystems -> Exposition Blueprint -> Revues de code -> Profilage.
7. **Livrables attendus** : Codebase C++ modulaire et documentée, architecture World Partition configurée pour Kinshasa.
8. **Problèmes courants** : Dépendances circulaires entre classes, chargement synchrone bloquant le Game Thread (`LoadSynchronous`).
9. **Solutions techniques** : Chargement asynchrone systématique via `FStreamableManager` et `TSoftObjectPtr`, architecture orientée interfaces et sous-systèmes.
10. **Critères de qualité** : Zéro fuite mémoire, compilation modulaire rapide, respect des conventions de nommage Epic.
11. **Ressources de formation** : Epic Developer Community, *Unreal Engine C++ Programming* (Tom Looman).
12. **Références documentaires** : Epic Games, *Unreal Engine 5 C++ Programming & World Partition Documentation*.

### 36. Gameplay Programming (`ENG-02`)
1. **Responsabilités** : Implémentation des mécaniques de joueur (déplacement, combat, interactions, inventaire, quêtes) avec une réactivité irréprochable.
2. **Compétences requises** : Gameplay Ability System (GAS), machines à états, algorithmes de caméra, mathématiques 3D (quaternions, vecteurs).
3. **Méthodes de travail** : Itération rapide en binôme avec les Game/Combat Designers.
4. **Outils professionnels** : Rider/Visual Studio, Unreal Engine Gameplay Debugger, Visual Logger.
5. **Technologies utilisées** : UE5 Gameplay Ability System (GAS), Enhanced Input System, Motion Warping, Camera Modes.
6. **Processus de production** : Prototypage mécanique -> Refactoring C++ GAS -> Exposition paramètres DataAsset -> Tests QA.
7. **Livrables attendus** : Systèmes de personnage, capacités GAS, gestionnaire de caméras contextuelles.
8. **Problèmes courants** : Logique gameplay monolithique concentrée dans la classe `Character`, bugs d'états concurrents.
9. **Solutions techniques** : Décomposition en Actor Components modulaires et gestion des états exclusifs via Gameplay Tags.
10. **Critères de qualité** : Code testable unitairement, latence d'entrée minimale, comportement déterministe.
11. **Ressources de formation** : Tranek's *GASDocumentation* (GitHub), Epic Developer Community.
12. **Références documentaires** : Epic Games, *Gameplay Ability System for Unreal Engine*, UE5 Documentation.

### 37. Tools Programming (`ENG-03`)
1. **Responsabilités** : Création d'outils internes pour accélérer la production (validateurs d'assets, générateurs de quartiers, éditeurs de quêtes, batch processors).
2. **Compétences requises** : C++ éditeur UE5, Slate / Editor Utility Widgets, Python UE5, ergonomie d'outils (UX interne).
3. **Méthodes de travail** : Observation directe des flux de travail des artistes/designers pour éliminer les tâches répétitives.
4. **Outils professionnels** : Unreal Editor Python API, Slate UI Framework, Data Validation Plugin.
5. **Technologies utilisées** : `UEditorValidatorBase`, Blutilities, JSON/CSV importers, Perforce Python API (`P4Python`).
6. **Processus de production** : Identification d'un goulot -> Prototype Python/EUW -> Déploiement équipe -> Collecte retours -> Maintenance.
7. **Livrables attendus** : Plugins éditeur internes, règles de validation automatiques pré-commit, documentation d'utilisation.
8. **Problèmes courants** : Outils puissants mais ergonomiquement complexes abandonnés par les artistes.
9. **Solutions techniques** : Co-conception avec les utilisateurs finaux et intégration transparente dans les menus contextuels de l'éditeur.
10. **Critères de qualité** : Réduction mesurable du temps de production par asset, zéro corruption de données.
11. **Ressources de formation** : Insomniac GDC 2019 (*Tools for Marvel's Spider-Man*), The Toolsmiths community.
12. **Références documentaires** : Epic Games, *Scripting the Unreal Editor Using Python*, UE5 Documentation.

### 38. Houdini Procedural Generation (`ENG-04`)
1. **Responsabilités** : Création de générateurs procéduraux (HDA) pour la voirie de Kinshasa, les bâtiments modulaires, les réseaux électriques aériens et la végétation.
2. **Compétences requises** : VEX, graphes SOP/PDG (TOPs), traitement de données SIG/OpenStreetMap, intégration Houdini Engine pour UE5.
3. **Méthodes de travail** : Génération non destructive pilotée par courbes et attributs, instanciation géométrique légère.
4. **Outils professionnels** : SideFX Houdini FX, Houdini Engine for Unreal, SideFX Labs (OSM Importer).
5. **Technologies utilisées** : VEX, PDG (Procedural Dependency Graph), UE5 PCG (Procedural Content Generation) Framework.
6. **Processus de production** : Analyse données réelles (OSM/DEM Kinshasa) -> Graphe Houdini -> Export HDA -> Génération dans UE5 World Partition.
7. **Livrables attendus** : Bibliothèque de HDA (routes, immeubles, câbles, clôtures), pipelines PDG de génération massive.
8. **Problèmes courants** : Temps de cuisson (cook time) trop longs dans UE5, création de milliers d'acteurs individuels saturant l'éditeur.
9. **Solutions techniques** : Export sous forme d'Hierarchical Instanced Static Meshes (HISM) et utilisation de PDG pour le calcul distribué hors ligne.
10. **Critères de qualité** : Génération reproductible (seed déterministe), respect des règles d'occlusion et de collision.
11. **Ressources de formation** : SideFX *Project Titan* & *City Sample* tutorials.
12. **Références documentaires** : SideFX, *Houdini Engine for Unreal Documentation* & *SideFX Labs OSM Tools*.

### 39. Rendering (`ENG-05`)
1. **Responsabilités** : Optimisation et personnalisation du pipeline de rendu temps réel (Lumen, Nanite, Virtual Shadow Maps, eau du fleuve Congo, post-traitement).
2. **Compétences requises** : Architecture GPU moderne (DX12/Vulkan), HLSL, algorithmes d'illumination globale, anti-aliasing temporel.
3. **Méthodes de travail** : Captures GPU régulières sur scènes de référence, analyse des passes de rendu.
4. **Outils professionnels** : RenderDoc, NVIDIA Nsight Graphics, AMD Radeon GPU Profiler (RGP), PIX for Windows.
5. **Technologies utilisées** : DirectX 12, Vulkan, HLSL, Nanite, Lumen, Virtual Shadow Maps (VSM), TSR / DLSS / FSR.
6. **Processus de production** : Définition du budget GPU par passe -> Customisation shaders/water -> Profilage captures -> Optimisation.
7. **Livrables attendus** : Shaders de rendu optimisés (eau, atmosphère), configuration de scalabilité graphique (Low à Ultra).
8. **Problèmes courants** : Coût élevé des Virtual Shadow Maps sur la végétation animée par le vent (World Position Offset), ghosting TSR.
9. **Solutions techniques** : Désactivation du WPO à moyenne distance sur les feuillages, réglage fin des vecteurs de mouvement et du cache VSM.
10. **Critères de qualité** : Image stable sans scintillement temporel, respect strict du budget GPU (ex. < 14 ms en 60 FPS).
11. **Ressources de formation** : SIGGRAPH *Advances in Real-Time Rendering*, Epic Games Rendering Docs.
12. **Références documentaires** : Akenine-Möller, T. et al. (2018), *Real-Time Rendering* (4th ed.), CRC Press.

### 40. Performance Engineering (`ENG-06`)
1. **Responsabilités** : Garantie de la fluidité globale (FPS stables, élimination des micro-saccades/stutters, respect des empreintes RAM et VRAM).
2. **Compétences requises** : Profilage bas niveau CPU/GPU, gestion du cache CPU, multithreading, streaming d'assets.
3. **Méthodes de travail** : Tests automatisés quotidiens de survol de Kinshasa avec relevé des percentiles (P95, P99 frametime).
4. **Outils professionnels** : Unreal Insights, Stat Unit/GPU, MemReport, Superluminal / VTune.
5. **Technologies utilisées** : Async Loading Thread, PSO Precaching, HLOD streaming, Memory Pools.
6. **Processus de production** : Établissement des budgets -> Surveillance continue -> Chasse aux pics (spikes) -> Validation pré-jalon.
7. **Livrables attendus** : Rapports hebdomadaires de performance par quartier, correctifs d'optimisation bas niveau.
8. **Problèmes courants** : Hitches lors de la compilation de shaders (PSO) ou lors du streaming de cellules denses en véhicule rapide.
9. **Solutions techniques** : Bundled PSO Cache généré par bots QA, ajustement des rayons de grille World Partition et pré-chargement prédictif.
10. **Critères de qualité** : 99 % des frames sous le budget cible (16.6 ms en mode Performance / 33.3 ms en mode Qualité), zéro crash Out-Of-Memory.
11. **Ressources de formation** : Epic Games *Unreal Insights & Performance Optimization Guides*, GDC Performance talks.
12. **Références documentaires** : Epic Games, *Performance and Profiling Documentation*, Unreal Engine 5.

### 41. Build Engineering (`ENG-07`)
1. **Responsabilités** : Maintenance de l'infrastructure de contrôle de source, compilation automatisée des binaires et données (cooking), distribution des builds.
2. **Compétences requises** : Administration Perforce/Git LFS, pipelines CI/CD, scripting PowerShell/Python, gestion de fermes de build.
3. **Méthodes de travail** : Intégration continue (builds incrémentaux à chaque commit critique, builds complets nocturnes).
4. **Outils professionnels** : Perforce Helix Core, Horde (UE5), Jenkins / TeamCity, Unreal Automation Tool (UAT), BuildGraph.
5. **Technologies utilisées** : Derived Data Cache (DDC) partagé, Zen Server (UE5), conteneurs Docker.
6. **Processus de production** : Commit code/assets -> Pré-flight check -> Compilation C++ -> Cooking données -> Packaging -> Déploiement QA.
7. **Livrables attendus** : Pipelines BuildGraph fonctionnels, serveur DDC partagé, installeurs de builds quotidiens.
8. **Problèmes courants** : Temps de cooking de plusieurs heures bloquant les tests QA, corruption du DDC partagé.
9. **Solutions techniques** : Déploiement d'Unreal Zen Server et distribution multi-machines via Horde BuildGraph.
10. **Critères de qualité** : Temps de build incrémental < 15 minutes, disponibilité de l'infrastructure > 99.5 %.
11. **Ressources de formation** : Epic Games *Unreal Horde & BuildGraph Documentation*.
12. **Références documentaires** : Epic Games, *BuildGraph & Automation Tool Documentation*, UE5.

### 42. Security & Anti-Tamper Engineering (`ENG-08`)
1. **Responsabilités** : Protection des fichiers du jeu (`.pak`/`.utoc`), sécurisation des sauvegardes locales, prévention de la triche sur l'économie/classements.
2. **Compétences requises** : Cryptographie appliquée, sécurité logicielle, ingénierie inverse défensive.
3. **Méthodes de travail** : Audits de sécurité avant mise en production, chiffrement des clés de signature.
4. **Outils professionnels** : UnrealPak (chiffrement AES), outils d'analyse binaire, certificats de signature de code.
5. **Technologies utilisées** : Chiffrement AES-256 des archives Pak, signature RSA, validation d'intégrité des sauvegardes (HMAC).
6. **Processus de production** : Définition des menaces -> Chiffrement des assets -> Signature des binaires -> Tests de pénétration.
7. **Livrables attendus** : Pipeline de packaging chiffré, système de sauvegarde signé et vérifié.
8. **Problèmes courants** : Impact négatif des solutions anti-tamper lourdes sur les temps de chargement et les FPS.
9. **Solutions techniques** : Chiffrement ciblé uniquement sur l'index et les données critiques plutôt que sur l'intégralité des médias lourds.
10. **Critères de qualité** : Impact performance < 1 %, protection efficace contre la modification triviale des sauvegardes.
11. **Ressources de formation** : GDC Security talks, OWASP Game Security guidelines.
12. **Références documentaires** : Epic Games, *Signing and Encrypting Pak Files*, Unreal Engine 5 Documentation.

---

## PÔLE 8 : QUALITÉ, ACCESSIBILITÉ & SAVOIR

### 43. QA Engineering (`QA-01`)
1. **Responsabilités** : Vérification systématique de la qualité fonctionnelle, détection des bugs de collision, de quêtes, d'affichage et de stabilité sur l'ensemble de Kinshasa.
2. **Compétences requises** : Rigueur analytique, rédaction de rapports de bugs reproductibles, maîtrise des outils de débogage moteur.
3. **Méthodes de travail** : Plans de test structurés par fonctionnalité et par secteur géographique (quadrillage de la carte).
4. **Outils professionnels** : Jira, TestRail, Unreal Engine Console Commands (`bugitgo`), logiciels de capture vidéo.
5. **Technologies utilisées** : Coordonnées spatiales automatisées dans les rapports de bugs, journaux de crash (Crash Reporter).
6. **Processus de production** : Réception build -> Smoke Test -> Tests fonctionnels/exploratoires -> Rapport Jira -> Vérification du correctif.
7. **Livrables attendus** : Plans de test, tickets de bugs qualifiés (étapes, logs, coordonnées), bilans de certification (TRC/TCR).
8. **Problèmes courants** : Bugs intermittents difficiles à reproduire dans un monde ouvert dynamique.
9. **Solutions techniques** : Enregistrement automatique des paramètres de session (seed, position exacte, état des quêtes) lors de chaque signalement.
10. **Critères de qualité** : Taux de reproductibilité des bugs > 90 %, zéro bug critique (Classe A) à la livraison.
11. **Ressources de formation** : ISTQB Game Testing, GDC QA Summit.
12. **Références documentaires** : Schultz, C. P., & Bryant, R. D. (2016), *Game Testing: All in One* (3rd ed.), Mercury Learning.

### 44. Automated Testing (`QA-02`)
1. **Responsabilités** : Conception et maintenance de tests automatisés (unitaires, fonctionnels, tests de charge et bots d'exploration autonome).
2. **Compétences requises** : C++/Python, écriture de tests déterministes, automatisation de navigation IA pour tests de stress.
3. **Méthodes de travail** : Exécution nocturne automatique sur fermes de machines après chaque build.
4. **Outils professionnels** : Unreal Gauntlet Automation Framework, Unreal Automation System, Python.
5. **Technologies utilisées** : `IMPLEMENT_SIMPLE_AUTOMATION_TEST`, Functional Tests Actors, bots de survol/marche automatique.
6. **Processus de production** : Écriture des scénarios de test -> Intégration CI/CD -> Exécution nocturne -> Alertes sur régressions.
7. **Livrables attendus** : Suite de tests Gauntlet, rapports automatisés de mémoire/FPS par secteur de Kinshasa.
8. **Problèmes courants** : Tests fragiles (flaky tests) échouant à cause de variations de timing asynchrone.
9. **Solutions techniques** : Synchronisation explicite sur les événements moteur plutôt que des délais fixes (`sleep`).
10. **Critères de qualité** : Couverture des systèmes critiques > 80 %, taux de faux positifs < 2 %.
11. **Ressources de formation** : Epic Games *Gauntlet Automation Framework Documentation*.
12. **Références documentaires** : Epic Games, *Automation System & Gauntlet Overview*, Unreal Engine 5 Documentation.

### 45. Accessibility (`QA-03`)
1. **Responsabilités** : Garantie que ZAÏRE soit jouable par le plus grand nombre (handicaps visuels, auditifs, moteurs et cognitifs).
2. **Compétences requises** : Normes d'accessibilité vidéoludique, ergonomie cognitive, audio-description, design d'options d'assistance.
3. **Méthodes de travail** : Intégration dès la pré-production (Accessibility by Design), tests avec des joueurs concernés.
4. **Outils professionnels** : Simulateurs de daltonisme, Unreal Engine Accessibility plugins, lecteurs d'écran.
5. **Technologies utilisées** : Shaders de correction daltonienne, synthèse vocale UI (Text-to-Speech), remapping intégral des touches.
6. **Processus de production** : Audit du GDD -> Implémentation des options -> Tests de conformité XAG -> Validation finale.
7. **Livrables attendus** : Matrice de conformité Xbox Accessibility Guidelines (XAG), menu d'accessibilité complet.
8. **Problèmes courants** : QTE exigeant des appuis répétés rapides, sous-titres illisibles sur fond clair, informations transmises uniquement par la couleur.
9. **Solutions techniques** : Options de maintien au lieu d'appuis répétés, fond semi-opaque réglable derrière les sous-titres, double codage couleur + icône.
10. **Critères de qualité** : Conformité aux standards XAG/PlayStation Accessibility, clarté des options dès le premier lancement.
11. **Ressources de formation** : Game Accessibility Guidelines, Microsoft Xbox Accessibility Guidelines (XAG).
12. **Références documentaires** : Microsoft, *Xbox Accessibility Guidelines (XAG)*, Microsoft Game Dev Documentation.

### 46. Technical Documentation (`QA-04`)
1. **Responsabilités** : Structuration, rédaction et maintenance de la base de connaissances interne du studio (guides d'outils, normes de code, pipelines).
2. **Compétences requises** : Rédaction technique claire, architecture de l'information, diagrammes d'architecture, Markdown/Docs-as-Code.
3. **Méthodes de travail** : Documentation versionnée à côté du code (Docs-as-Code), revues documentaires à chaque évolution d'outil.
4. **Outils professionnels** : Confluence, Notion, MkDocs / Docusaurus, Mermaid.js, Git.
5. **Technologies utilisées** : Markdown, diagrammes Mermaid, génération automatique de documentation C++ (Doxygen).
6. **Processus de production** : Capture du savoir auprès des experts -> Rédaction structurée -> Validation technique -> Publication & indexation.
7. **Livrables attendus** : Portail documentaire du studio, guides de démarrage rapide (< 30 min pour un nouvel arrivant), glossaire technique.
8. **Problèmes courants** : Documentation obsolète ne reflétant plus l'état réel des outils ou du moteur.
9. **Solutions techniques** : Intégration de la mise à jour documentaire dans la *Definition of Done* de chaque tâche technique.
10. **Critères de qualité** : Exactitude vérifiée, recherche rapide, exemples concrets exécutables.
11. **Ressources de formation** : Write the Docs community, Google Technical Writing Courses.
12. **Références documentaires** : Bhatti, J. et al. (2021), *Docs for Developers: An Engineer's Field Guide to Technical Writing*, Apress.
