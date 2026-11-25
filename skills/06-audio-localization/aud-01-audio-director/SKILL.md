---
name: aud-01-audio-director
description: "Direction audio globale de ZAÏRE. Définit l'Audio Bible, la hiérarchie des bus de mixage HDR sous Audiokinetic Wwise, l'identité acoustique de chaque commune de Kinshasa (DST-*) et le respect strict du budget mémoire audio (<= 512 MB RAM, <= 64 voix physiques)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AUD-01
  department: 06-audio-localization
  stratum: 1
  version: "1.1.0"
  inputs:
    - "creative-pillars-dir-03"
    - "world-bible-wld-01"
    - "cultural-research-wld-02"
  outputs:
    - "audio-bible-specification.md"
    - "wwise-mixing-bus-hierarchy.md"
  upstream_dependencies:
    - "DIR-03"
    - "WLD-01"
    - "WLD-02"
---

# `AUD-01` — Audio Director (`aud-01-audio-director`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`06-audio-localization`** (Strate DAG **1**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Définition de la signature sonore d'une commune (`DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE`, `DST-KALAMU`, `DST-NGALIEMA`).
- Paramétrage des règles de priorité de mixage dynamique (HDR Audio / Side-Chaining) entre dialogues, indices critiques de combat et ambiances urbaines.
- Surveillance du budget `PERF-MEM-AUDIO` (`<= 512 MB` RAM, plafond de `64 voix physiques` simultanées).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `creative-pillars-dir-03`, `world-bible-wld-01`, `cultural-research-wld-02`
- **Sorties produites** : `audio-bible-specification.md`, `wwise-mixing-bus-hierarchy.md`
- **Dépendances Amont Canoniques (DAG)** : `DIR-03`, `WLD-01`, `WLD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne compose pas les pistes musicales (`AUD-03`) et ne développe pas le code C++ du moteur (`ENG-01`).
- **Interdiction / Limite** : Interdit que la musique diégétique ou le bruit du trafic ne masque un dialogue de quête ou le signal sonore d'une attaque ennemie (`GD-05`).
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Organiser la hiérarchie des bus maîtres Wwise selon 5 priorités décroissantes : (1) `BUS_VO_Critical` (Priorité 100), (2) `BUS_SFX_CombatTelegraph` (Priorité 90), (3) `BUS_Music_ScoreAndRadio` (Priorité 75), (4) `BUS_SFX_PlayerVehicle` (Priorité 70), (5) `BUS_Ambience_Kinshasa` (Priorité 50).
2. Configurer le **Side-Chain Ducking HDR** : toute réplique sur `BUS_VO_Critical` abaisse automatiquement `BUS_Music_ScoreAndRadio` et `BUS_Ambience_Kinshasa` de `-6.0 dB` (temps d'attaque `40 ms`, relâchement `350 ms`).
3. Fixer le plafond global à **64 voix physiques simultanées** avec bascule automatique en **Virtual Voices (`From Elapsed Time`)** pour toute source en dessous de `-48 dB`.
4. Documenter la charte dans `templates/audio-bible-template.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Marché de Matonge générant plus de 64 sources sonores simultanées (foule + radios + motos Wewa) | Agréger les voix de foule lointaines en un lit granulaire multicanal 5.1/7.1.4 (1 seule voix Wwise) et limiter les émetteurs individuels ponctuels aux 12 objets les plus proches | Maintenir le plafond de 64 voix physiques et PERF-MEM-AUDIO <= 512 MB |
| Dialogue radio d'Amina (CHR-ALLY-AMINA) couvert par le moteur de la Wewa en pleine course | Activer un filtre High-Pass + boost de présence (2.5 kHz) sur le bus radio et abaisser le bus moteur véhicule de -4.5 dB pendant la réplique | Garantir l'intelligibilité vocale à 100 % |
| Dépassement de l'enveloppe RAM Audio (> 512 MB) | Passer toutes les ambiances longues (> 8 secondes) et musiques de radio en Streaming Disk Wwise (Zero-Latency prefetch 64 KB) au lieu de chargement In-Memory | Respecter le budget mémoire DIR-04 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/wwise-hdr-and-bus-hierarchy.md`
- **Modèle Officiel de Livrable** : `templates/audio-bible-template.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-audio-bible.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-audio-bible.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/audio-bible-template.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AUD-01` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] La cible de sonie globale est étalonnée à **`-23 LUFS` (±1 LU)** selon la norme broadcast EBU R128 / console AAA.
- [ ] Budget RAM Audio total `<= 512 MB` et voix physiques actives `<= 64` en stress test.
- [ ] Chaque commune `DST-*` possède son empreinte acoustique distincte documentée.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-03`, `DIR-04`, `ENG-07`.
