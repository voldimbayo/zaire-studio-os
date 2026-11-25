---
name: aud-03-music-designer
description: "Conception de la musique interactive adaptative (score dramatique par stems synchronisés sous Wwise Interactive Music) et programmation musicale de Radio Lokole 104.5 FM (ORG-RADIO-KIN : rumba congolaise, ndombolo, rap kinois) avec garantie d'un mode Streamer Safe 100 % libre de droits."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AUD-03
  department: 06-audio-localization
  stratum: 3
  version: "1.1.0"
  inputs:
    - "audio-bible-aud-01"
    - "cultural-music-research-wld-02"
    - "gameplay-states-gd-01-gd-05"
  outputs:
    - "interactive-music-specification.md"
    - "radio-lokole-programming.csv"
  upstream_dependencies:
    - "AUD-01"
    - "WLD-02"
    - "GD-01"
    - "GD-05"
---

# `AUD-03` — Music Designer (`aud-03-music-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`06-audio-localization`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Conception des transitions musicales dynamiques entre exploration (`DST-*`), infiltration (`SYS-STEALTH`), combat (`SYS-CMB-MELEE`) et poursuite Wewa (`VEH-MOTO-WEWA-01`).
- Programmation de la grille musicale et des jingles de `ORG-RADIO-KIN` diffusés dans les véhicules et les ngandas de `DST-MATONGE`.
- Configuration du flag de conformité juridique `STREAMER_SAFE_FALLBACK` avec `PRD-02` (Risk Manager).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `audio-bible-aud-01`, `cultural-music-research-wld-02`, `gameplay-states-gd-01-gd-05`
- **Sorties produites** : `interactive-music-specification.md`, `radio-lokole-programming.csv`
- **Dépendances Amont Canoniques (DAG)** : `AUD-01`, `WLD-02`, `GD-01`, `GD-05`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne gère pas les bruitages physiques d'environnement ou de véhicules (`AUD-02`).
- **Interdiction / Limite** : Interdit l'intégration de toute piste musicale sous licence commerciale tiers sans qu'une piste de remplacement interne (`Streamer Safe`) ne soit assignée dans le Switch Container Wwise.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer le score interactif en **4 Stems Verticaux Synchronisés** (`Stem_1_SubBass_Pulse`, `Stem_2_Percussion_Lokole`, `Stem_3_Sebene_Guitar_Tension`, `Stem_4_Brass_CombatFull`) pilotés par les Gameplay Tags (`State.Character.Stealth.Concealed`, `State.Character.Combat.Engaged`).
2. Calibrer les règles de transition horizontale dans **Wwise Interactive Music Hierarchy** : transitions d'entrée en combat sur la **prochaine noire (`Next Beat`)** avec stinger percussif, transitions de sortie de combat sur la **prochaine mesure (`Next Bar`)**.
3. Construire la grille de `ORG-RADIO-KIN` en alternant morceaux musicaux, jingles d'antenne et flashs d'information réactifs de `CHR-ALLY-AMINA` (`NAR-05`).
4. Associer à chaque piste le booléen `bIsStreamerSafe` et son ID de fallback libre de droits dans `templates/radio-stations-programming.csv`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Superposition cacophonique entre le score dramatique non-diégétique et une radio diégétique de nganda à Matonge | Lorsque le score de combat ou d'infiltration s'active, atténuer de -12 dB et appliquer un filtre Low-Pass (800 Hz) sur les sources musicales diégétiques environnantes | Éviter tout conflit harmonique ou rythmique |
| Option 'Mode Créateur / Streamer Safe' activée dans les paramètres du jeu | Basculer le Switch Wwise SW_Music_LicenseMode sur STREAMER_SAFE, remplaçant 100 % des titres sous licence tiers par les compositions originales de rumba/ndombolo produites par le studio | Garantir zéro strike DMCA (risque PRD-02) |
| Bascule trop brusque entre exploration calme et combat lors d'une embuscade brève (< 6 secondes) | Introduire un palier intermédiaire 'Tension/Alerte' (Stems 1+2+3) avant de déclencher le Stem 4 Cuivres/Sébène complet | Maintenir une respiration musicale naturelle |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/interactive-music-and-radio.md`
- **Modèle Officiel de Livrable** : `templates/radio-stations-programming.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-interactive-music-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-interactive-music-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/radio-stations-programming.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AUD-03` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Toutes les transitions d'état musical s'exécutent en synchronisation métrique (`Next Beat` ou `Next Bar`) sans clic ni coupe brute.
- [ ] 100 % des pistes de `ORG-RADIO-KIN` disposent d'un statut de licence vérifié et d'un fallback `Streamer Safe`.
- [ ] Respect des structures musicales authentiques congolaises documentées par `WLD-02`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `AUD-01`, `WLD-02`, `PRD-02`.
