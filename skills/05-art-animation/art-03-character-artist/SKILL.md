---
name: art-03-character-artist
description: "Conception et production des modèles 3D des protagonistes (CHR-*) et du système d'assemblage modulaire des PNJ kinois (AI-01/AI-02). Spécifie les shaders de peau (Subsurface Profile pour carnations foncées sous soleil équatorial), les vêtements et la bascule Groom Strands -> Hair Cards."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: ART-03
  department: 05-art-animation
  stratum: 3
  version: "1.1.0"
  inputs:
    - "character-bibles-nar-03"
    - "cultural-dress-codes-wld-02"
    - "art-bible-art-01"
    - "3d-standards-art-04"
  outputs:
    - "character-art-specification.md"
    - "modular-npc-assembly-table.csv"
  upstream_dependencies:
    - "NAR-03"
    - "WLD-02"
    - "ART-01"
    - "ART-04"
---

# `ART-03` — Character Artist (`art-03-character-artist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`05-art-animation`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Production du modèle 3D d'un personnage héroïque (`CHR-PROTAG-KOFFI`, `CHR-ANTAG-MUKENDI`, `CHR-ALLY-AMINA`).
- Conception des pièces vestimentaires et morphologiques modulaires alimentant la foule de Kinshasa (`AI-02`, méthodologie Guerrilla Games `SRC-009`).
- Étalonnage des shaders de peau et des coiffures africaines (tresses, locks, coupes courtes, foulards) avec `ART-07` et `ART-08`.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `character-bibles-nar-03`, `cultural-dress-codes-wld-02`, `art-bible-art-01`, `3d-standards-art-04`
- **Sorties produites** : `character-art-specification.md`, `modular-npc-assembly-table.csv`
- **Dépendances Amont Canoniques (DAG)** : `NAR-03`, `WLD-02`, `ART-01`, `ART-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas les Animation Blueprints (`ART-05`) et ne construit pas les rigs de déformation complexes (`ART-08`).
- **Interdiction / Limite** : Interdit l'usage de Groom Hair Strands (alembic) sur les PNJ de foule `AI-02` (réservé exclusivement aux LOD 0/1 des héros en cinématique).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Aligner la topologie de tous les personnages humains sur le **Squelette Maître Unique ZAÏRE (Compatible MetaHuman / UE5 Manny)** afin de mutualiser 100 % des animations (`ART-05`/`ART-06`).
2. Pour les PNJ (`AI-01`/`AI-02`), découper les meshes en 5 slots modulaires interchangeables : `Head`, `Hair/Headgear`, `UpperBody`, `LowerBody`, `Footwear/Accessories` avec variation chromatique par atlas/palette.
3. Configurer le **Subsurface Scattering (SSS) / Substrate Skin Profile** pour les carnations foncées : ajuster le libre parcours moyen (Mean Free Path) rouge/ambre et la rugosité micro-cutanée Dual Lobe Specular (`0.28 / 0.45`) pour éviter tout reflet blanc crayeux sous `ART-07`.
4. Définir les seuils de bascule LOD capillaire : Groom Strands (LOD 0 cinématique héros uniquement) -> Hair Cards optimisées (LOD 1/2 gameplay) -> Casque/Mesh bas (LOD 3 foule lointaine).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Coiffure Groom Strands dépassant 0.4 ms GPU en phase de gameplay ouvert | Forcer la bascule automatique vers le mesh Hair Cards dès le retour en caméra gameplay 3e personne (distance > 180 cm) | Préserver le budget GPU global <= 16.6 ms |
| Répétition visuelle de clones dans les marchés de Matonge (600 PNJ AI-02) | Combiner 12 têtes × 15 hauts × 12 bas × 10 coiffures/chapeaux × 8 palettes de motifs wax/streetwear (plus de 170 000 permutations pour < 768 MB VRAM) | Appliquer le pipeline modulaire Guerrilla Games SRC-009 |
| Vêtement flottant causant du clipping lors des mouvements de combat | Remplacer la simulation Chaos Cloth par du skinning rigide + Normal Map animée sur les PNJ de foule, et limiter Chaos Cloth à la veste de Koffi (LOD 0) | Respecter le budget PERF-CPU-CHAOS <= 1.5 ms |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/character-skin-and-modularity.md`
- **Modèle Officiel de Livrable** : `templates/character-art-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-character-art-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-character-art-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/character-art-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `ART-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Tous les personnages partagent le squelette maître standardisé et supportent le retargeting `ART-06`.
- [ ] Le pool VRAM total des kits modulaires PNJ d'une commune reste `<= 768 MB`.
- [ ] Les carnations et tenues respectent strictement `knowledge/world-bible/cultural-guidelines.md`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `ART-01`, `ART-04`, `WLD-02`, `ENG-07`.
