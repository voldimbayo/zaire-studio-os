# Pipeline UE5 Localization Dashboard & Doublage (`AUD-04`)

## 1. Locales Supportées & Règles de Transcréation
- **`fr-CD` (Locale Native Maîtresse)** : Français de Kinshasa avec code-switching naturel en lingala (`LEX-001` à `LEX-012`).
- **`ln-CD` (Doublage & Sous-titres Lingala Complet)** : Version intégrale en lingala kinois utilisant l'alphabet Unicode normalisé (`a, e, ɛ, i, o, ɔ, u`).
- **`en-US` / `en-GB` (Internationalisation)** : Sous-titres et doublage anglais conservant les marqueurs identitaires (*Mbote*, *Wewa*, *Nganda*) accompagnés d'un contexte limpide.

## 2. Formule de Budget d'Expansion UI (`GD-07` <-> `AUD-04`)
$$\text{Capacité Conteneur UI (chars)} \ge \lceil \text{Longueur}(\text{Source}_{fr-CD}) \times 1.35 \rceil$$

---

## 3. Spécifications Techniques & Compatibilité Moteur (`AUD-04` — Strate DAG 3)

- **Ingénierie Audio Wwise / MetaSounds & Localisation Unicode (UE 5.8)** (`SRC-018`, `SRC-027`, `SRC-028`, `SRC-029`, `SRC-031`) :
  - **Mixage HDR & Budgets (`AUD-01`, `AUD-02`)** : Cible `-23 LUFS` (`±1 LU`), plafond de `64 voix physiques` simultanées (virtualisation sous `-48 dB`), budget RAM `<= 512 MB`, propagation acoustique par `UAkRoomComponent` & `UAkPortalComponent`, `>= 6 variations` par Random Container SFX.
  - **Musique Interactive & Conformité DMCA (`AUD-03`, `SRC-028`)** : 4 stems verticaux synchronisés au tempo (`Next Beat` / `Next Bar`), bascule instantanée `SW_Music_LicenseMode = STREAMER_SAFE` vers des compositions 100 % originales.
  - **Localisation & Accessibilité XAG 104 (`AUD-04`, `SRC-029`, `SRC-031`)** : Format `[LOCUTEUR] : Texte`, support UTF-8 natif des voyelles lingala `ɛ` et `ɔ`, réserve d'expansion UI `>= +35 %`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `NAR-04`, `GD-07`, `WLD-02`
- **Audit des Entrées (`inputs`)** :
  - `dialogue-trees-nar-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `ui-screen-specs-gd-07` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lingala-glossary-wld-02` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `localization-pipeline-spec.md` : Doit respecter le gabarit `templates/localized-string-table.csv` et passer l'audit croisé.
  - `localized-string-table.csv` : Doit respecter le gabarit `templates/localized-string-table.csv` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `PRD-04`, `PRD-06`, `WLD-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Terme culturel kinois (ex: Wewa, Libongo, Nganda, Mbote) rencontré lors de la traduction vers l'anglais (en-US) | Blocage / Dégradation si ignoré | Conserver le terme kinois d'origine en italique dans le dialogue anglais lorsque le contexte visuel est explicite, ou utiliser la tournure naturelle du glossaire WLD-02 | Escalade vers Préserver la couleur locale authentique de Kinshasa en version internationale |
| Mode de Défaillance 2: Chaîne traduite dépassant la limite de caractères du widget Common UI | Blocage / Dégradation si ignoré | Alerter GD-07 pour élargir la boîte ou reformuler la traduction sous le plafond de +35 % validé par check_l10n_unicode.py | Escalade vers Éliminer 100 % des troncatures de texte |
| Mode de Défaillance 3: Police de caractères de secours (fallback font) remplaçant 'ɛ' ou 'ɔ' par un carré vide (tofu □) | Blocage / Dégradation si ignoré | Bloquer le build LQA et imposer l'inclusion des plages Unicode Latin Extended-B (U+0180..U+024F) et IPA Extensions (U+0250..U+02AF) dans l'asset UFont UE5 | Escalade vers Garantir un rendu typographique irréprochable |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`AUD-04`)

- [ ] **Contrôle DoD #1** : `python skills/06-audio-localization/aud-04-voice-localization-specialist/scripts/check_l10n_unicode.py` retourne un code `0`.
- [ ] **Contrôle DoD #2** : 0 clé manquante (`TXT_MISSING`) et 0 caractère corrompu sur `ɛ` / `ɔ`.
- [ ] **Contrôle DoD #3** : 100 % des sous-titres incluent le préfixe locuteur `[NOM]` et un timecode synchronisé avec `ART-06`.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
