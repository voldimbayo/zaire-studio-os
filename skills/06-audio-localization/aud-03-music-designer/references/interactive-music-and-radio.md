# Architecture Wwise Interactive Music & Radio Lokole (`AUD-03`)

## 1. Matrice d'Activation des Stems par Gameplay Tag
| État Gameplay (`FGameplayTag`) | Stem 1 (Pulse) | Stem 2 (Percus Congolaises) | Stem 3 (Guitare Mi-Solo) | Stem 4 (Sébène / Cuivres) | Règle Transition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Exploration Libre** | Muets (Priorité Radio/Ville) | Muet | Muet | Muet | Fondu `2.0 s` |
| `State.Character.Stealth.Concealed` | **Actif (`0 dB`)** | Actif (`-6 dB`, filtré) | Muet | Muet | `Next Bar` |
| **Alerte / Poursuite Wewa** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | Muet | `Next Beat` + Stinger |
| `State.Character.Combat.Engaged` | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | **Actif (`0 dB`)** | `Next Beat` + Impact |

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AUD-03` — Strate DAG 3)

- **Ingénierie Audio Wwise / MetaSounds & Localisation Unicode (UE 5.8)** (`SRC-018`, `SRC-027`, `SRC-028`, `SRC-029`, `SRC-031`) :
  - **Mixage HDR & Budgets (`AUD-01`, `AUD-02`)** : Cible `-23 LUFS` (`±1 LU`), plafond de `64 voix physiques` simultanées (virtualisation sous `-48 dB`), budget RAM `<= 512 MB`, propagation acoustique par `UAkRoomComponent` & `UAkPortalComponent`, `>= 6 variations` par Random Container SFX.
  - **Musique Interactive & Conformité DMCA (`AUD-03`, `SRC-028`)** : 4 stems verticaux synchronisés au tempo (`Next Beat` / `Next Bar`), bascule instantanée `SW_Music_LicenseMode = STREAMER_SAFE` vers des compositions 100 % originales.
  - **Localisation & Accessibilité XAG 104 (`AUD-04`, `SRC-029`, `SRC-031`)** : Format `[LOCUTEUR] : Texte`, support UTF-8 natif des voyelles lingala `ɛ` et `ɔ`, réserve d'expansion UI `>= +35 %`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `AUD-01`, `WLD-02`, `GD-01`, `GD-05`
- **Audit des Entrées (`inputs`)** :
  - `audio-bible-aud-01` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `cultural-music-research-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `gameplay-states-gd-01-gd-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `interactive-music-specification.md` : Doit respecter le gabarit `templates/radio-stations-programming.csv` et passer l'audit croisé.
  - `radio-lokole-programming.csv` : Doit respecter le gabarit `templates/radio-stations-programming.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `AUD-01`, `WLD-02`, `PRD-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Superposition cacophonique entre le score dramatique non-diégétique et une radio diégétique de nganda à Matonge | Blocage / Dégradation si ignoré | Lorsque le score de combat ou d'infiltration s'active, atténuer de -12 dB et appliquer un filtre Low-Pass (800 Hz) sur les sources musicales diégétiques environnantes | Escalade vers Éviter tout conflit harmonique ou rythmique |
| Mode de Défaillance 2: Option 'Mode Créateur / Streamer Safe' activée dans les paramètres du jeu | Blocage / Dégradation si ignoré | Basculer le Switch Wwise SW_Music_LicenseMode sur STREAMER_SAFE, remplaçant 100 % des titres sous licence tiers par les compositions originales de rumba/ndombolo produites par le studio | Escalade vers Garantir zéro strike DMCA (risque PRD-02) |
| Mode de Défaillance 3: Bascule trop brusque entre exploration calme et combat lors d'une embuscade brève (< 6 secondes) | Blocage / Dégradation si ignoré | Introduire un palier intermédiaire 'Tension/Alerte' (Stems 1+2+3) avant de déclencher le Stem 4 Cuivres/Sébène complet | Escalade vers Maintenir une respiration musicale naturelle |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AUD-03`)

- [ ] **Contrôle DoD #1** : Toutes les transitions d'état musical s'exécutent en synchronisation métrique (`Next Beat` ou `Next Bar`) sans clic ni coupe brute.
- [ ] **Contrôle DoD #2** : 100 % des pistes de `ORG-RADIO-KIN` disposent d'un statut de licence vérifié et d'un fallback `Streamer Safe`.
- [ ] **Contrôle DoD #3** : Respect des structures musicales authentiques congolaises documentées par `WLD-02`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
