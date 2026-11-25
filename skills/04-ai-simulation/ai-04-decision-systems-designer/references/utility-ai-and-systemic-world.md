# Modèle Utility AI & Événements Systémiques Urbains (`AI-04`)

## 1. Équation de Sélection d'Événement Systémique
Le directeur systémique évalue toutes les 10 secondes les ancres disponibles (`SmartObject` de trottoir à `40 - 90 m` en avant du joueur) selon :
$$U(E) = W_{\text{district}} \cdot W_{\text{time}} \cdot W_{\text{weather}} \cdot W_{\text{cooldown}}$$
L'événement ayant le score $U(E) > 0.65$ le plus élevé est instancié en hydratant 2 à 4 entités `AI-02` vers `AI-01`.

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AI-04` — Strate DAG 3)

- **Architecture IA Hybride : State Trees, MassEntity & ZoneGraph (UE 5.8)** (`SRC-004`, `SRC-013`, `SRC-015`, `SRC-020`, `SRC-032`) :
  - **IA Individuelle (`AI-01`, Budget `<= 2.5 ms`)** : Plafond strict de `24 acteurs ACharacter` actifs simultanément ; `State Trees` UE 5.8 + time-slicing EQS (`<= 0.35 ms/frame`).
  - **Foule ECS (`AI-02`, Budget `<= 2.0 ms` pour `500-800 entités`)** : Anneau 0 (`0-25 m`, `<= 18` acteurs hydratés), Anneau 1 (`25-80 m`, Skeletal Mesh URO 30Hz + RVO), Anneau 2 (`80-250 m`, ISM animé par Vertex Animation Texture VAT).
  - **Trafic & Escalade Policière PCR (`AI-03`, `AI-04`)** : Réseau `ZoneGraph` généré en amont par `ENG-04` ; sous-voies virtuelles inter-files (`130-150 cm`) pour `VEH-MOTO-WEWA-01` lorsque le flux descend sous `20 km/h` ; Watchdog Anti-Deadlock (`8.0 s`) ; escalade graduée `SYS-LAW-ESCALATION` (`State.Law.AlertLevel.1..3`) avec `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-01`, `GD-01`, `NAR-04`
- **Audit des Entrées (`inputs`)** :
  - `world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `reputation-system-gd-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `barks-catalog-nar-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `utility-ai-decision-matrix.csv` : Doit respecter le gabarit `templates/systemic-events-catalog.md` et passer l'audit croisé.
  - `systemic-events-catalog.md` : Doit respecter le gabarit `templates/systemic-events-catalog.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `NAR-06`, `WLD-04`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Mission principale MSN-MAIN-* en cours d'exécution à proximité (< 80 m) | Blocage / Dégradation si ignoré | Forcer le multiplicateur d'utilité des événements systémiques aléatoires à 0.0 dans un rayon de 80 m autour de l'objectif de quête | Escalade vers Éviter toute interférence avec le script de mission GD-02 |
| Mode de Défaillance 2: Même événement systémique tiré deux fois dans le même quartier en moins de 15 minutes | Blocage / Dégradation si ignoré | Appliquer une pénalité de fraîcheur (Decay Factor = 0.05) sur le score d'utilité de cet événement | Escalade vers Garantir la variété de l'exploration open world |
| Mode de Défaillance 3: Réputation de Koffi au palier 'Enfant du Quartier' (>= 600 points) dans la commune | Blocage / Dégradation si ignoré | Activer les événements d'entraide citoyenne (avertissement de patrouille, diversion spontanée de foule, prêt de Wewa) | Escalade vers Récompenser concrètement l'investissement social du joueur |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AI-04`)

- [ ] **Contrôle DoD #1** : Chaque événement du catalogue spécifie sa formule de score Utility AI, son cooldown, ses tags requis et son plafond d'acteurs (`<= 4`).
- [ ] **Contrôle DoD #2** : Exclusion mutuelle garantie avec les arènes de missions principales actives.
- [ ] **Contrôle DoD #3** : Tous les dialogues courts de l'événement proviennent des tables de barks validées par `NAR-04`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
