# Audit des Agent Skills Existants (GitHub & Écosystème)

## 1. Analyse Structurelle du Standard Agent Skills (`SKILL.md`)
L'examen des dépôts publics révèle une convergence vers une architecture normalisée autour de fichiers `SKILL.md` dotés d'un en-tête YAML (`name`, `description`) et d'instructions structurées, accompagnés optionnellement de répertoires `scripts/`, `references/` et `assets/`.

### Points Forts Observés
- **Chargement Progressif (Progressive Disclosure)** : Séparation entre la description déclenchante (légère) et les instructions détaillées + ressources annexes chargées uniquement à la demande.
- **Spécialisation Technique Ciblée** : Les meilleurs dépôts découpent les compétences par sous-système précis (ex. C++ UE5, GAS, UI, Build) plutôt qu'un unique prompt monolithique.

### Limites Critiques des Dépôts Existants pour ZAÏRE
1. **Focus quasi exclusif sur la programmation** : La majorité des skills publics couvrent le code (C++, Blueprints, shaders) mais ignorent presque totalement la **production AAA**, le **level/mission design**, la **narration interactive**, l'**audio middleware (Wwise)** et la **recherche culturelle**.
2. **Absence d'orchestration inter-métiers** : Les skills existants fonctionnent en silos isolés sans protocole de passage de relais (handoff) entre départements (ex. Level Design -> Environment Art -> Lighting -> QA).
3. **Généricité géographique et culturelle** : Aucun skill public ne prend en compte les contraintes spécifiques d'un monde ouvert contemporain africain (topographie et urbanisme de Kinshasa, multilinguisme français/lingala, éclairage équatorial).

---

## 2. Dépôts GitHub Repérés et Analysés

### Dépôt 1 : `quodsoler/unreal-engine-skills`
- **URL** : `https://github.com/quodsoler/unreal-engine-skills`
- **Statut de vérification** : Consulté (Extrait/Index via recherche GitHub).
- **Description** : Collection de 27 à 31 skills spécialisés pour agents IA de codage axés sur le développement C++ Unreal Engine (`ue-cpp-foundations`, `ue-gameplay`, etc.).
- **Forces** : Granularité fine par domaine technique UE5 C++, structure modulaire installable par sous-module Git ou CLI.
- **Limites** : Centré uniquement sur l'ingénierie logicielle C++ UE5 ; ne couvre ni Houdini, ni Wwise, ni les métiers créatifs/production.
- **Réutilisabilité & Licence** : À vérifier dans le fichier `LICENSE` du dépôt avant toute inspiration structurelle. Servira de référence d'architecture pour la granularité de nos skills `ENG-01` et `ENG-02`, mais ZAÏRE STUDIO OS nécessite une conception sur mesure intégrée à l'ensemble du studio.

### Dépôt 2 : `gamedev-skills/awesome-gamedev-agent-skills`
- **URL** : `https://github.com/gamedev-skills/awesome-gamedev-agent-skills`
- **Statut de vérification** : Consulté (Extrait/Index via recherche GitHub).
- **Description** : Répertoire curaté et routeur multi-moteurs d'Agent Skills couvrant Unreal Engine, Unity, Godot, Three.js, Bevy, etc.
- **Forces** : Approche par routage intelligent orientant la requête vers le bon moteur et le bon domaine.
- **Limites** : Approche généraliste multi-moteurs (compromis sur la profondeur spécifique à UE5 AAA / World Partition / Mass Entity).
- **Réutilisabilité & Licence** : Référence utile pour la conception du **méta-routeur ZAÏRE STUDIO OS** qui aiguillera les demandes entre nos 46 spécialités.

---

## 3. Recommandations d'Architecture pour la Phase 2 (Conception des Skills)
1. **Ne pas copier-coller** les dépôts tiers : rédiger des skills originaux, sous licence propre au projet ZAÏRE, en s'inspirant uniquement des meilleures pratiques ergonomiques (progressive disclosure, checklists de qualité, formats de livrables).
2. **Structurer en 3 niveaux** :
   - **Niveau 0 (Orchestrateur)** : `zaire-studio-director` — Analyse la demande, identifie les départements impliqués et séquence les appels de skills.
   - **Niveau 1 (Skills Métiers)** : 46 skills spécialisés regroupés par pôles cohérents, chacun embarquant ses propres gabarits (`assets/`) et référentiels (`references/`).
   - **Niveau 2 (Référentiel Partagé ZAÏRE)** : Base documentaire commune sur Kinshasa (communes, métriques, glossaire lingala, budgets techniques UE5) évitant la duplication dans chaque skill.
