# Architecture Wwise HDR, Priorités de Mixage & Budgets (`AUD-01`)

## 1. Hiérarchie des Bus & Règles d'Atténuation (Ducking)
| Bus Wwise | Priorité | Cible LUFS | Ducking Appliqué sur Autres Bus | Stratégie Mémoire |
| :--- | :--- | :--- | :--- | :--- |
| `BUS_VO_Critical` | `100 (Max)` | `-20 LUFS` | `-6 dB` sur Musique & Ambiances, `-4.5 dB` sur Véhicules | Streamed + Prefetch `32 KB` |
| `BUS_SFX_CombatTelegraph` | `90` | `-18 LUFS Peak` | `-4 dB` sur Ambiances pendant Startup attaque `GD-05` | In-Memory (`Opus / ADPCM`) |
| `BUS_SFX_PlayerVehicle` | `75` | `-23 LUFS` | `-2 dB` sur Trafic IA distant | In-Memory (`Vorbis Q6`) |
| `BUS_Music_ScoreAndRadio` | `70` | `-24 LUFS` | Ducké par VO et Télégraphes Combat | Streamed + Prefetch `64 KB` |
| `BUS_Ambience_Kinshasa` | `50` | `-28 LUFS` | Ducké par tous les bus prioritaires | Streamed Multichannel |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AUD-01` — Strate DAG 1)

- **Ingénierie Audio Wwise / MetaSounds & Localisation Unicode (UE 5.8)** (`SRC-018`, `SRC-027`, `SRC-028`, `SRC-029`, `SRC-031`) :
  - **Mixage HDR & Budgets (`AUD-01`, `AUD-02`)** : Cible `-23 LUFS` (`±1 LU`), plafond de `64 voix physiques` simultanées (virtualisation sous `-48 dB`), budget RAM `<= 512 MB`, propagation acoustique par `UAkRoomComponent` & `UAkPortalComponent`, `>= 6 variations` par Random Container SFX.
  - **Musique Interactive & Conformité DMCA (`AUD-03`, `SRC-028`)** : 4 stems verticaux synchronisés au tempo (`Next Beat` / `Next Bar`), bascule instantanée `SW_Music_LicenseMode = STREAMER_SAFE` vers des compositions 100 % originales.
  - **Localisation & Accessibilité XAG 104 (`AUD-04`, `SRC-029`, `SRC-031`)** : Format `[LOCUTEUR] : Texte`, support UTF-8 natif des voyelles lingala `ɛ` et `ɔ`, réserve d'expansion UI `>= +35 %`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `WLD-01`, `WLD-02`
- **Audit des Entrées (`inputs`)** :
  - `creative-pillars-dir-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `world-bible-wld-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-research-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `audio-bible-specification.md` : Doit respecter le gabarit `templates/audio-bible-template.md` et passer l'audit croisé.
  - `wwise-mixing-bus-hierarchy.md` : Doit respecter le gabarit `templates/audio-bible-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-03`, `DIR-04`, `ENG-07`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Marché de Matonge générant plus de 64 sources sonores simultanées (foule + radios + motos Wewa) | Blocage / Dégradation si ignoré | Agréger les voix de foule lointaines en un lit granulaire multicanal 5.1/7.1.4 (1 seule voix Wwise) et limiter les émetteurs individuels ponctuels aux 12 objets les plus proches | Escalade vers Maintenir le plafond de 64 voix physiques et PERF-MEM-AUDIO <= 512 MB |
| Mode de Défaillance 2: Dialogue radio d'Amina (CHR-ALLY-AMINA) couvert par le moteur de la Wewa en pleine course | Blocage / Dégradation si ignoré | Activer un filtre High-Pass + boost de présence (2.5 kHz) sur le bus radio et abaisser le bus moteur véhicule de -4.5 dB pendant la réplique | Escalade vers Garantir l'intelligibilité vocale à 100 % |
| Mode de Défaillance 3: Dépassement de l'enveloppe RAM Audio (> 512 MB) | Blocage / Dégradation si ignoré | Passer toutes les ambiances longues (> 8 secondes) et musiques de radio en Streaming Disk Wwise (Zero-Latency prefetch 64 KB) au lieu de chargement In-Memory | Escalade vers Respecter le budget mémoire DIR-04 |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AUD-01`)

- [ ] **Contrôle DoD #1** : La cible de sonie globale est étalonnée à **`-23 LUFS` (±1 LU)** selon la norme broadcast EBU R128 / console AAA.
- [ ] **Contrôle DoD #2** : Budget RAM Audio total `<= 512 MB` et voix physiques actives `<= 64` en stress test.
- [ ] **Contrôle DoD #3** : Chaque commune `DST-*` possède son empreinte acoustique distincte documentée.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
