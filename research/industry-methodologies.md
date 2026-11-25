# Méthodologies Industrielles Documentées (Studios AAA)

> **Avertissement méthodologique** : Les analyses ci-dessous s'appuient exclusivement sur des conférences publiques (GDC, SIGGRAPH), articles techniques publiés et documentations officielles. Aucune méthode interne non publiée n'est revendiquée.

---

## 1. Rockstar Games (RAGE Engine — *Red Dead Redemption 2*, *GTA V*)
### Sources Publiques de Référence
- **GDC 2020** : Mike Jones, *"Player Locomotion in Red Dead Redemption 2"* (annonce officielle GDC Conf).
- **Publications techniques & analyses d'ingénierie** : Systèmes de locomotion hybride et densité de population/trafic.

### Méthodes Documentées
- **Locomotion et Animation Réactive** : Combinaison de graphes d'animation denses avec sélection contextuelle d'extraits de mouvement pour éliminer le glissement des pieds (foot sliding) et maintenir l'inertie physique du personnage.
- **Écosystème Monde Vivant (Population & Trafic)** : Attribution de routines quotidiennes aux PNJ et gestion hiérarchique des véhicules selon la distance caméra et la densité de quartier, permettant une transition fluide entre simulation physique complète à proximité et simulation statistique à distance.
- **Application à ZAÏRE** : Essentiel pour crédibiliser la densité piétonne des marchés de Kinshasa (ex. Grand Marché / Gambela) et la cohabitation chaotique mais régulée des taxis, motos-taxis et piétons.

---

## 2. Ubisoft (AnvilNext / Snowdrop — *Assassin's Creed Unity*, *Odyssey*, *Watch Dogs*)
### Sources Publiques de Référence
- **GDC 2015** : Christine Blondeau (Ubisoft), *"Developing Systemic Crowd Events in Assassin's Creed Unity"*.
- **GDC 2019** : François Paradis (Ubisoft Quebec), *"Procedural Generation of Cinematic Dialogues in 'Assassin's Creed Odyssey'"*.

### Méthodes Documentées
- **Événements Systémiques de Foule** : Découplage entre les animations de masse basse fréquence et les acteurs systémiques locaux capables de déclencher des micro-scènes émergentes sans intervention directe du joueur.
- **Génération Procédurale de Dialogues Cinématiques** : Utilisation de règles de mise en scène automatisées (placements de caméras champ/contre-champ, gestuelle générique pondérée par l'émotion du texte) pour absorber des dizaines de milliers de lignes de dialogue en monde ouvert.
- **Application à ZAÏRE** : Permet de produire un grand volume de dialogues contextuels en français et lingala sans nécessiter de motion capture manuelle sur 100 % des quêtes secondaires.

---

## 3. CD Projekt Red (REDengine -> Unreal Engine 5 — *The Witcher 3*, *Cyberpunk 2077*)
### Sources Publiques de Référence
- **GDC 2014** : Przemysław Czatrowski (CD Projekt Red) & Jasin Bushnaief (Umbra Software), *"Solving Visibility and Streaming in The Witcher 3: Wild Hunt"*.
- **GDC 2026** : Annonces techniques conjointes NVIDIA / CD Projekt Red sur l'évolution des systèmes de Level of Detail (LOD) et rendu path-traced pour mondes ouverts.

### Méthodes Documentées
- **Visibilité et Streaming Spatial** : Séparation stricte entre l'occlusion géométrique (Umbra PVS) et le chargement asynchrone des cellules du monde ouvert afin de garantir l'absence d'écrans de chargement lors des déplacements rapides en milieu urbain dense.
- **Verticalité Urbaine et Densité** : Gestion agressive des budgets mémoire par quartier et découpage en couches logiques (géométrie statique, habillage, PNJ, quêtes).
- **Application à ZAÏRE** : Directement transposable sous **Unreal Engine 5** via **World Partition**, **Data Layers** et **HLOD** pour gérer la transition entre les immeubles de la Gombe et les zones résidentielles denses de Kalamu.

---

## 4. Insomniac Games (Proprietary Engine — *Marvel's Spider-Man*)
### Sources Publiques de Référence
- **GDC 2019** : *"Tools for 'Marvel's Spider-Man': Editing with Immutable Data"* (GDC Vault).
- **GDC 2019** : David Santiago (Insomniac Games), *"Procedurally Crafting Manhattan for 'Marvel's Spider-Man'"*.

### Méthodes Documentées
- **Édition de Données Immuables (Immutable Data Pipeline)** : Architecture d'outils où les modifications d'assets génèrent des graphes de dépendances déterministes, accélérant drastiquement les temps de compilation et évitant la corruption de données lors du travail simultané de centaines de développeurs.
- **Construction Procédurale de Ville à Grande Échelle** : Utilisation de règles modulaires par îlots urbains (lots, façades, toitures, mobilier urbain) pilotées par des outils procéduraux tout en préservant des repères architecturaux (landmarks) sculptés à la main.
- **Application à ZAÏRE** : Modèle idéal pour coupler **SideFX Houdini** et **UE5 PCG** afin de générer les quartiers étendus de Kinshasa tout en intégrant des monuments emblématiques (Tour de l'Échangeur de Limete, Palais du Peuple, Boulevard du 30 Juin).

---

## 5. Naughty Dog (*The Last of Us*, *Uncharted 2*)
### Sources Publiques de Référence
- **GDC 2014** : *"In-Game and Cinematic Lighting of The Last of Us"* (GDC Vault).
- **GDC 2018** : David Shaver (Naughty Dog) & Robert Yang (NYU), *"Level Design Workshop: Blockmesh and Lighting Tips"*.

### Méthodes Documentées
- **Guidage Visuel par la Lumière et le Blockmesh** : Utilisation précoce de l'éclairage et des contrastes chromatiques dès la phase de blockmesh (greyboxing) pour orienter naturellement le regard du joueur sans surcharger l'interface utilisateur (UI).
- **Continuité Cinématique / Gameplay** : Alignement rigoureux des rigs d'éclairage et des paramètres de caméra entre phases jouables et cinématiques temps réel.
- **Application à ZAÏRE** : Exploitation de la lumière naturelle équatoriale intense (ombres franches, reflets sur la latérite humide et le fleuve Congo) pour guider l'exploration urbaine.

---

## 6. Guerrilla Games (Decima Engine — *Horizon Zero Dawn*)
### Sources Publiques de Référence
- **GDC 2017** : Dan Sumaili & Sander van der Steen (Guerrilla Games), *"Creating a Tools Pipeline for 'Horizon: Zero Dawn'"*.
- **GDC 2018** : Daniel Calvert (Guerrilla Games), *"Repopulating the Earth: Character Production on 'Horizon Zero Dawn'"*.

### Méthodes Documentées
- **Pipeline Modulaire de Personnages** : Système d'assemblage modulaire (têtes, coiffures, vêtements superposés, accessoires culturels) permettant une grande diversité visuelle des PNJ sans explosion de la mémoire texture.
- **Outils Orientés Itération Rapide** : Automatisation de la validation des assets avant soumission dans le dépôt central pour empêcher les régressions de performance.
- **Application à ZAÏRE** : Indispensable pour représenter la diversité vestimentaire et culturelle de Kinshasa (sapeurs, commerçants, étudiants, forces de l'ordre) avec un budget mémoire maîtrisé.
