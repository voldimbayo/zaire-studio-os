# ZAÏRE STUDIO OS — Architecture Système Complète (Phase 2)

## 1. Vision & Principes Architecturaux
**ZAÏRE STUDIO OS** est un système multi-agents modulaire et déterministe conçu pour reproduire l'organisation, les flux de données et les contrôles qualité d'un studio de développement AAA sur le projet pilote **ZAÏRE** (action-aventure en monde ouvert situé à Kinshasa, République Démocratique du Congo).

### Principes Directeurs (Architecture Decision Records — ADR)
1. **ADR-01 — Séparation Orchestration / Exécution / Savoir** :
   - **Couche 0 (Direction Centrale — 7 rôles)** : Analyse d'intention, décomposition en graphes de tâches acycliques (DAG), arbitrage créatif/technique et validation finale.
   - **Couche 1 (Spécialistes Métiers — 50 skills répartis en 7 départements)** : Exécution atomique sur un périmètre strict avec entrées/sorties typées, zéro overlap de responsabilité.
   - **Couche 2 (Single Source of Truth — Knowledge Base & Registry)** : Base de connaissances partagée régie par un cycle de vie à 5 statuts (`CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`) et des identifiants uniques normalisés.
2. **ADR-02 — Graphe Orienté Acyclique (DAG) et Zéro Dépendance Circulaire** :
   - Les dépendances entre départements suivent un flux unidirectionnel strict : `Direction -> Recherche & Worldbuilding -> Narration & Game Design -> Ingénierie & Art/Audio -> Intégration & QA`.
   - Tout retour arrière (ex. bug détecté en QA ou dépassement de budget détecté par Performance Engineer) passe par une **boucle de rétroaction événementielle** gérée par le `Studio Orchestrator` et le `Production Planner`, jamais par un appel direct circulaire entre deux skills métiers.
3. **ADR-03 — Progressive Disclosure (Chargement Progressif)** :
   - Conformément à l'audit technique (`research/skills-discovery.md`), chaque skill expose uniquement ses métadonnées YAML (`name`, `description`, `metadata`) au routeur central, et ne charge ses gabarits (`templates/`), exemples (`examples/`) et référentiels (`references/`) que lors de son activation effective.
4. **ADR-04 — Ancrage Technique UE5 / Houdini / Wwise** :
   - L'architecture cible directement les pipelines vérifiés en Phase 1 (`research/technical-reference.md`) : **Unreal Engine 5** (World Partition, Data Layers, OFPA, HLOD, GAS, Mass Entity, ZoneGraph, Nanite, Lumen, Chaos, Niagara, Common UI, Gauntlet), **SideFX Houdini** (HDA/PDG + OSM) et **Audiokinetic Wwise + MetaSounds**.

---

## 2. Topologie Globale du Système (3 Couches)

```
+-----------------------------------------------------------------------------------+
|                        COUCHE 0 : DIRECTION CENTRALE (7 Rôles)                    |
|  [Studio Orchestrator] <---> [Executive Producer] [Creative Dir.] [Technical Dir.] |
|  [Lead Game Designer]        [Documentation Dir.] [Quality Director]              |
+-----------------------------------------+-----------------------------------------+
                                          | Dispatch DAG & Consolidation
                                          v
+-----------------------------------------------------------------------------------+
|                   COUCHE 1 : 7 DÉPARTEMENTS SPÉCIALISÉS (50 Skills)               |
|  +---------------+  +---------------+  +---------------+  +--------------------+  |
|  | 1. NARRATIVE  |  | 2. WORLD      |  | 3. GAME       |  | 4. AI & SIMULATION |  |
|  |   (6 skills)  |  |   DESIGN (6)  |  |   DESIGN (7)  |  |    (4 skills)      |  |
|  +---------------+  +---------------+  +---------------+  +--------------------+  |
|  +---------------+  +---------------+  +---------------+                          |
|  | 5. ART & ANIM |  | 6. AUDIO      |  | 7. ENGINEERING|  +--------------------+  |
|  |   (9 skills)  |  |   (4 skills)  |  |   (8 skills)  |  | 8. PRODUCTION & QA |  |
|  +---------------+  +---------------+  +---------------+  |    (6 skills)      |  |
|                                                           +--------------------+  |
+-----------------------------------------+-----------------------------------------+
                                          | Lecture / Écriture contrôlée (IDs)
                                          v
+-----------------------------------------------------------------------------------+
|              COUCHE 2 : KNOWLEDGE MANAGEMENT & CONSISTENCY ENGINE                 |
|  - Registre d'Entités Uniques (CHR, FAM, ORG, DST, LOC, MSN, ITM, VEH, SYS)       |
|  - Machine à États (CONFIRMED | PROPOSED | RESEARCH_REQUIRED | BLOCKED | DEPRECATED)|
|  - Budgets Techniques & Métriques Spatiales Kinshasa                              |
+-----------------------------------------------------------------------------------+
```

---

## 3. Rôles de la Direction Centrale (Couche 0)

| ID | Rôle | Périmètre & Responsabilités Clés | Autorité d'Arbitrage |
| :--- | :--- | :--- | :--- |
| `DIR-01` | **Studio Orchestrator** | Point d'entrée unique. Analyse les requêtes utilisateurs, décompose en sous-tâches, sélectionne les skills requis, résout l'ordre topologique (DAG), gère les handoffs et consolide les livrables finaux. | Routage, séquencement, détection de conflits inter-livrables. |
| `DIR-02` | **Executive Producer** | Gouvernance stratégique, alignement périmètre/budget/planning, gestion des jalons (Vertical Slice, Alpha, Beta, Gold), priorisation commerciale et validation des arbitrages de scope. | Validation des jalons, coupes ou ajouts de périmètre majeur. |
| `DIR-03` | **Creative Director** | Gardien des piliers créatifs de ZAÏRE, cohérence tonale, esthétique et émotionnelle entre narration, monde ouvert, direction artistique et audio. | Veto créatif sur toute dérive tonale ou culturelle. |
| `DIR-04` | **Technical Director** | Architecture moteur UE5, définition et surveillance des budgets matériels (VRAM, CPU/GPU frametime), gouvernance des pipelines Houdini/DCC/CI et dette technique. | Veto technique sur toute fonctionnalité hors budget ou non scalable. |
| `DIR-05` | **Lead Game Designer** | Cohérence systémique entre boucles de gameplay, combat, véhicules, économie, progression et conception de missions/niveaux. | Arbitrage sur l'équilibrage, la prise en main (game feel) et les métriques spatiales. |
| `DIR-06` | **Documentation Director** | Gouvernance de la base de connaissances (`knowledge/`), contrôle de l'unicité des identifiants, gestion des transitions de statuts (`PROPOSED` -> `CONFIRMED`) et maintien du glossaire. | Validation structurelle des documents et promotion au statut `CONFIRMED`. |
| `DIR-07` | **Quality Director** | Définition des seuils d'acceptation studio (Definition of Done), gouvernance QA, tests automatisés (Gauntlet), conformité accessibilité (XAG) et certification. | Blocage de livraison (`BLOCKED`) en cas de non-conformité qualité ou accessibilité. |

---

## 4. Décisions Architecturales, Justifications & Limites

### Justifications des Choix Clés
- **Passage de 46 domaines (Phase 1) à 57 composants (7 Direction + 50 Skills Métiers)** : La recherche Phase 1 a montré que regrouper des métiers distincts (ex. Narration et Dialogue, ou Level Design et Environment Art) crée des prompts monolithiques imprécis. La décomposition en **50 skills spécialisés** (ex. séparation explicite entre `Screenwriter`, `Character Writer`, `Dialogue Designer` et `Continuity Editor` en Narration ; ou entre `Level Designer` et `Environment Artist`) garantit des contrats d'entrée/sortie atomiques.
- **Séparation `Level Designer` vs `Environment Artist`** : Inspirée directement de la méthodologie Naughty Dog (`research/industry-methodologies.md`, GDC 2018), le *Level Designer* produit un blockout métrique validé en gameplay avant que l'*Environment Artist* n'applique les kits architecturaux et matériaux PBR.
- **Séparation `NPC AI Architect`, `Crowd Simulation Specialist` et `Traffic AI Specialist`** : Justifiée par l'architecture UE5 (*Behavior/State Trees* pour les acteurs héroïques/combat vs *Mass Entity / ZoneGraph* pour les foules des marchés de Kinshasa et le trafic urbain dense).

### Limites Connues & Prérequis (Issus de `research/research-gaps.md`)
1. **Dépendance aux données locales de Kinshasa** : Tant que le corpus SIG/OSM détaillé des communes secondaires (Matonge, Kalamu, Masina) et le lexique lingala/français kinois ne sont pas enrichis, les skills `Urban Researcher`, `Cultural Researcher` et `Houdini Specialist` doivent marquer les zones non vérifiées avec le statut `RESEARCH_REQUIRED`.
2. **Absence d'exécution moteur directe par les agents textuels** : Les skills produisent des spécifications exploitables (code C++/HLSL, scripts Python UE5, graphes JSON Articy/Wwise, règles HDA/PCG, plans de test Gauntlet), mais la compilation binaire et le rendu visuel requièrent une exécution externe dans l'éditeur Unreal Engine 5 / Houdini.
3. **Besoin d'approfondissement GDC Vault** : Les pipelines détaillés d'assemblage procédural d'îlots (Insomniac Games, `SRC-008`) et de mise en scène procédurale des dialogues (Ubisoft Quebec, `SRC-014`) nécessiteront une enrichissement des fichiers `references/` lors de l'implémentation de la Phase 3.
