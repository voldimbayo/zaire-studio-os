# Narration Environnementale & Découpage Modulaire (`WLD-06`)

## 1. Les 3 Couches d'Habillage d'un Lieu Kinois (`LOC-*`)
1. **Couche 1 — Ossature & Patine Climatique** : Structure béton/brique, traces de ruissellement des pluies équatoriales, oxydation des tôles, poussière rouge latéritique à la base des murs (via Runtime Virtual Texturing `ART-02`).
2. **Couche 2 — Activité Sociale & Signalétique** : Enseignes peintes à la main (`NAR-05`), étals modulaires, câblages aériens, mobilier de nganda, caisses de fret portuaires.
3. **Couche 3 — Affordance Gameplay & Guidage Visuel** : Marquage chromatique subtil (bâches jaunes/bleues, éclairage fonctionnel `ART-07`, usure des rebords) sur les points de franchissement (`100 cm`) et d'escalade (`280 cm`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`WLD-06` — Strate DAG 2)

- **Architecture Spatiale, SIG & World Partition (UE 5.8 / Houdini 22.0)** (`SRC-001`, `SRC-005`, `SRC-012`, `SRC-019`, `SRC-021`, `SRC-023`) :
  - **Échelle & Gabarits Immuables (`spatial-metrics.md`)** : `1 UU = 1 cm` ; largeur minimale de couloir jouable `>= 350 cm` (`500 cm` en arène de mêlée) ; hauteur sous plafond `>= 320 cm` ; couvert bas/vault `100 cm` (`[90, 110] cm`) ; couvert haut `>= 200 cm` ; saut d'accroche `260-300 cm` ; couloir inter-file moto Wewa `>= 130 cm` (`150 cm` recommandé).
  - **Règle Blockout First (`SRC-012`)** : Validation complète en volumes gris (`WLD-05`) et éclairage d'intention (`ART-07`) avant toute passe `WLD-06` / `ART-02`.
  - **Streaming & Landmarks (`SRC-001`, `SRC-023`)** : Cellules `World Partition` de `12800 cm` (`128 m`), espacement minimal de `256 m` entre deux arènes lourdes (`> 20 PNJ AI-01`), règle d'intérêt visuel des `40 secondes`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `WLD-05`, `ART-01`, `WLD-02`, `WLD-03`
- **Audit des Entrées (`inputs`)** :
  - `validated-blockouts-wld-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `art-bible-art-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-briefs-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `urban-typology-wld-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `environment-design-brief.md` : Doit respecter le gabarit `templates/environment-brief-template.md` et passer l'audit croisé.
  - `modular-asset-kit-manifest.csv` : Doit respecter le gabarit `templates/environment-brief-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `ART-01`, `WLD-05`, `ART-08`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Demande d'ajout d'éléments de décor réduisant un couloir de 400 cm en dessous de 350 cm | Blocage / Dégradation si ignoré | Interdire tout prop à collision dans l'enveloppe des 350 cm ou placer l'habillage en retrait mural/plafond | Escalade vers Préserver l'intégrité du NavMesh et de la caméra WLD-05 |
| Mode de Défaillance 2: Besoin d'un asset architectural unique non réutilisable | Blocage / Dégradation si ignoré | Limiter les meshes uniques aux Landmarks Tier 1/2 et composer 85 % du bâti avec les kits modulaires partagés | Escalade vers Respecter le budget VRAM de DIR-04 et ART-04 |
| Mode de Défaillance 3: Signalétique ou enseigne de rue requise sur une façade | Blocage / Dégradation si ignoré | Utiliser exclusivement les textes validés par NAR-05 et WLD-02 | Escalade vers Éviter tout texte placeholder générique |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`WLD-06`)

- [ ] **Contrôle DoD #1** : Le taux de réutilisation modulaire du manifeste d'assets est `>= 80 %` sur le quartier.
- [ ] **Contrôle DoD #2** : Les 3 couches de narration environnementale sont détaillées avec références culturelles (`WLD-02`).
- [ ] **Contrôle DoD #3** : 0 collision ajoutée dans les volumes de franchissement ou de couverture du blockout `WLD-05`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
