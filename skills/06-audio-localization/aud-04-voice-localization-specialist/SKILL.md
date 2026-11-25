---
name: aud-04-voice-localization-specialist
description: "Ingénierie de localisation (i18n/L10n) sous UE5 Localization Dashboard (.po/.locres), direction du doublage vocal multilingue (fr-CD, ln-CD, en-US) et contrôle LQA. Garantit la préservation des glyphes Unicode du lingala (ɛ, ɔ), le préfixe locuteur XAG ([KOFFI]) et la tolérance d'expansion de texte de +35 %."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: AUD-04
  department: 06-audio-localization
  stratum: 3
  version: "1.1.0"
  inputs:
    - "dialogue-trees-nar-04"
    - "ui-screen-specs-gd-07"
    - "lingala-glossary-wld-02"
  outputs:
    - "localization-pipeline-spec.md"
    - "localized-string-table.csv"
  upstream_dependencies:
    - "NAR-04"
    - "GD-07"
    - "WLD-02"
---

# `AUD-04` — Voice and Localization Specialist (`aud-04-voice-localization-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`06-audio-localization`** (Strate DAG **3**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Intégration et traduction des graphes de dialogue (`NAR-04`) et des chaînes d'interface utilisateur (`GD-07`).
- Préparation des scripts d'enregistrement vocal (Voice-Over) avec indications phonétiques pour le français de RDC (`fr-CD`) et le lingala (`ln-CD`).
- Exécution du contrôle automatisé `scripts/check_l10n_unicode.py` avant tout String Freeze.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `dialogue-trees-nar-04`, `ui-screen-specs-gd-07`, `lingala-glossary-wld-02`
- **Sorties produites** : `localization-pipeline-spec.md`, `localized-string-table.csv`
- **Dépendances Amont Canoniques (DAG)** : `NAR-04`, `GD-07`, `WLD-02`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne modifie jamais l'intention dramatique ou les embranchements de quête (`NAR-01`/`NAR-02`/`GD-02`).
- **Interdiction / Limite** : Interdit toute chaîne codée en dur (hardcoded string) hors des `FText` / `LOCTEXT` et des String Tables UE5.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Assigner à chaque réplique ou texte UI une clé unique immuable au format `[CAT]_[MSN/UI]_[SPEAKER]_[NUM]` (ex: `SUB_MSN001_AMINA_02`).
2. Préfixer systématiquement chaque chaîne de sous-titre par le nom du locuteur entre crochets (`[KOFFI] : ...`, `[AMINA] : ...`) conformément aux normes d'accessibilité XAG (`PRD-06`).
3. Vérifier que les termes du glossaire `knowledge/world-bible/lingala-french-glossary.csv` conservent leurs caractères Unicode exacts (`ɛ` U+025B, `ɔ` U+0254) dans toutes les langues cibles.
4. Exécuter `scripts/check_l10n_unicode.py` pour certifier l'absence de `TXT_MISSING` et la réserve d'expansion de `+35 %` sur chaque conteneur UI (`GD-07`).

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Terme culturel kinois (ex: Wewa, Libongo, Nganda, Mbote) rencontré lors de la traduction vers l'anglais (en-US) | Conserver le terme kinois d'origine en italique dans le dialogue anglais lorsque le contexte visuel est explicite, ou utiliser la tournure naturelle du glossaire WLD-02 | Préserver la couleur locale authentique de Kinshasa en version internationale |
| Chaîne traduite dépassant la limite de caractères du widget Common UI | Alerter GD-07 pour élargir la boîte ou reformuler la traduction sous le plafond de +35 % validé par check_l10n_unicode.py | Éliminer 100 % des troncatures de texte |
| Police de caractères de secours (fallback font) remplaçant 'ɛ' ou 'ɔ' par un carré vide (tofu □) | Bloquer le build LQA et imposer l'inclusion des plages Unicode Latin Extended-B (U+0180..U+024F) et IPA Extensions (U+0250..U+02AF) dans l'asset UFont UE5 | Garantir un rendu typographique irréprochable |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/ue5-localization-and-vo-pipeline.md`
- **Modèle Officiel de Livrable** : `templates/localized-string-table.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-localization-spec.md`
- `scripts/check_l10n_unicode.py` : Script exécutable déterministe associé à `AUD-04` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-localization-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/localized-string-table.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `AUD-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/06-audio-localization/aud-04-voice-localization-specialist/scripts/check_l10n_unicode.py` retourne un code `0`.
- [ ] 0 clé manquante (`TXT_MISSING`) et 0 caractère corrompu sur `ɛ` / `ɔ`.
- [ ] 100 % des sous-titres incluent le préfixe locuteur `[NOM]` et un timecode synchronisé avec `ART-06`.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `PRD-04`, `PRD-06`, `WLD-02`.
