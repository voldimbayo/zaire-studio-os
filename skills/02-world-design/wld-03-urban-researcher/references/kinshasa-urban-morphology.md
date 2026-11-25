# Morphologie Urbaine & Réseau Viaire de Kinshasa (`WLD-03`)

## 1. Hiérarchie du Réseau Routier (Standards UE5 / ZoneGraph)
1. **Artères Primaires (Boulevard du 30 Juin `LOC-GOMBE-BD30JUIN`, Boulevard Lumumba)** :
   - 2 × 3 ou 2 × 4 voies de `400 cm` chacune + terre-plein central arboré ou bétonné (`200-400 cm`) + trottoirs `400 cm`.
2. **Avenues Secondaires & Carrefours (`LOC-MATONGE-VICTOIRE`, Avenue Kasa-Vubu)** :
   - 2 × 2 voies de `350 cm` + stationnement latéral informel (`220 cm`) + trottoirs/galeries `300-600 cm`.
3. **Ruelles Tertiaires (`DST-KALAMU`, quartiers intérieurs)** :
   - Chaussée mixte asphalte dégradé / latérite compactée de `450 cm` à `600 cm` + caniveaux latéraux de `60 cm` (accès privilégié `VEH-MOTO-WEWA-01` et piétons).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-03` — Strate DAG 1)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `DIR-04`
- **Audit des Entrées (`inputs`)** :
  - `osm-gis-data` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `district-profiles-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `knowledge/technical-specs/spatial-metrics.md` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `urban-typology-spec.md` : Doit respecter le gabarit `templates/urban-typology-spec.md` et passer l'audit croisé.
  - `road-network-hierarchy.csv` : Doit respecter le gabarit `templates/urban-typology-spec.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `WLD-04`, `ENG-04`, `AI-03`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Quartier secondaire (ex: DST-MASINA) dépourvu de tracés de ruelles précis dans OSM | Blocage / Dégradation si ignoré | Fournir une règle de subdivision d'îlots orthogonale/organique paramétrique (parcelles 15x25m) et marquer les repères spécifiques en RESEARCH_REQUIRED | Escalade vers Permettre à ENG-04 de tester le HDA sans inventer de monuments erronés |
| Mode de Défaillance 2: Axe routier trop étroit pour le croisement de deux bus VEH-BUS-TRANSCO-01 | Blocage / Dégradation si ignoré | Imposer une largeur minimale de chaussée de 700 cm (2 voies de 350 cm) ou restreindre la spline ZoneGraph aux taxis et motos Wewa | Escalade vers Synchroniser avec AI-03 |
| Mode de Défaillance 3: Transition abrupte entre sol en asphalte et ruelle en latérite | Blocage / Dégradation si ignoré | Spécifier une bande de transition de 200 cm avec caniveau de drainage ouvert pour l'intégration RVT (ART-02) | Escalade vers Respecter la morphologie réelle des voiries kinoises |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-03`)

- [ ] **Contrôle DoD #1** : Toutes les cotes routières et parcellaires sont exprimées en centimètres UE5 (`1 UU = 1 cm`).
- [ ] **Contrôle DoD #2** : Chaque typologie d'îlot définit le nombre d'étages min/max, le retrait de façade et la densité de câblage/végétation.
- [ ] **Contrôle DoD #3** : Compatibilité validée avec le générateur procédural `ENG-04` et le graphe routier `AI-03`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
