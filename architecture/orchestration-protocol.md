# Protocole d'Orchestration Multi-Agents (`orchestration-protocol.md`)

Ce document spécifie le fonctionnement opérationnel du **Studio Orchestrator (`DIR-01`)** et de la **Direction Centrale** pour traiter toute requête de production sur ZAÏRE.

---

## 1. Cycle de Vie d'une Requête (Workflow en 6 Phases)

### Phase 1 : Ingestion & Qualification (`INTAKE`)
1. Le `Studio Orchestrator` (`DIR-01`) reçoit la demande (ex. *"Concevoir une mission d'infiltration dans un entrepôt du port de Kinshasa avec fuite en moto Wewa"*).
2. Il identifie les **entités existantes** dans le `Knowledge Registry` (quartier `DST-*`, personnages `CHR-*`, véhicules `VEH-*`, systèmes `SYS-*`) et vérifie leur statut (`CONFIRMED`, `PROPOSED`, `RESEARCH_REQUIRED`, `BLOCKED`, `DEPRECATED`).
3. Si une entité critique est `DEPRECATED` ou `BLOCKED`, l'orchestrateur interrompt l'exécution et sollicite un arbitrage (`DIR-02`/`DIR-03`/`DIR-04`).

### Phase 2 : Décomposition & Planification DAG (`PLANNING`)
1. `DIR-01` consulte `skill-dependencies.md` pour sélectionner le sous-ensemble minimal de skills requis (principe d'économie d'agents).
2. Il construit un **Graphe Orienté Acyclique (DAG)** ordonnant les tâches en vagues parallélisables :
   - *Vague 1 (Parallèle)* : `WLD-02` (contexte portuaire kinois) + `WLD-03` (typologie entrepôts fleuve) + `GD-06` (tuning moto Wewa).
   - *Vague 2 (Séquentielle)* : `GD-02` (Mission Design `MSN-*`) + `NAR-02` (Scénario).
   - *Vague 3 (Parallèle)* : `WLD-05` (Blockout Level Design) + `NAR-04` (Dialogues/Barks) + `AI-01` (IA gardes).
   - *Vague 4 (Audit)* : `NAR-06` (Continuité) + `PRD-04` (Plan de test QA).

### Phase 3 : Dispatch & Contrats d'Exécution (`DISPATCH`)
Chaque skill activé reçoit un **Ordre de Mission Typé (Task Envelope)** :
```json
{
  "task_id": "TSK-2026-042",
  "target_skill": "GD-02",
  "objective": "Spécifier la mission MSN-014 (Infiltration Port Fluvial)",
  "context_entities": ["DST-GOMBE", "LOC-PORT-ONATRA", "VEH-WEWA-01", "SYS-STEALTH"],
  "constraints": {
    "max_npc_active": 24,
    "target_frametime_ms": 16.6,
    "languages": ["fr-CD", "ln-CD"]
  },
  "required_output_template": "mission-design-template.md",
  "upstream_artifacts": ["WLD-02-brief.md", "WLD-03-port-spec.md"]
}
```

### Phase 4 : Exécution & Handoff Inter-Départements (`EXECUTION & HANDOFF`)
1. Le skill exécute sa tâche dans les strictes limites de son périmètre.
2. S'il lui manque une donnée factuelle (ex. vocabulaire technique fluvial en lingala), il ne l'invente jamais : il crée une entrée avec le statut **`RESEARCH_REQUIRED`** et émet une sous-requête vers `WLD-02`.
3. À la fin de son exécution, le skill produit un **Handoff Packet** contenant :
   - L'artefact principal conforme au modèle.
   - La liste des nouvelles entités proposées (`PROPOSED`) avec leurs IDs normalisés.
   - La checklist d'auto-validation remplie.

### Phase 5 : Contrôle Qualité & Arbitrage Collégial (`REVIEW & GATEKEEPING`)
1. Les livrables passent devant les gardiens de cohérence :
   - `NAR-06` (Continuité narrative).
   - `PRD-06` (Accessibilité XAG si UI/contrôles).
   - `ENG-07` / `DIR-04` (Respect des budgets techniques).
2. En cas de conflit (ex. `GD-02` demande 60 gardes simultanés mais `DIR-04` limite à 24 pour le budget CPU), le `Studio Orchestrator` déclenche un **Protocole d'Arbitrage** réunissant `DIR-04` (Technical Director) et `DIR-05` (Lead Game Designer) pour statuer (ex. 24 gardes `AI-01` + 40 dockers civils `AI-02` Mass Crowd).

### Phase 6 : Consolidation & Mise à Jour du Registre (`CONSOLIDATION`)
1. `PRD-03` (Documentation Specialist) indexe les livrables et met à jour le `Knowledge Registry`.
2. `DIR-06` (Documentation Director) et `DIR-07` (Quality Director) valident la promotion des entités de `PROPOSED` vers `CONFIRMED`.
3. `DIR-01` (Studio Orchestrator) livre la synthèse consolidée à l'utilisateur avec traçabilité complète des IDs et statuts.

---

## 2. Protocoles d'Exception
- **Détection de Boucle / Blocage (`DEADLOCK_HANDLER`)** : Si un skill reste bloqué plus d'une itération sur une dépendance `RESEARCH_REQUIRED`, `DIR-01` escalade vers `PRD-02` (Risk Manager) et `DIR-02` (Executive Producer) pour définir une hypothèse de travail temporaire balisée (`PROPOSED [ASSUMPTION]`).
- **Violation de Périmètre (`SCOPE_GUARD`)** : Si un skill génère un livrable empiétant sur un autre métier (ex. `Screenwriter` qui écrit du code Blueprint), `DIR-01` rejette la section hors périmètre et la reroute vers le skill légitime (`ENG-02`).
