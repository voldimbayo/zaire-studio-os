---
name: prd-06-accessibility-specialist
description: "Ingénierie de l'accessibilité universelle selon les Xbox Accessibility Guidelines (XAG) : accessibilité visuelle (double codage forme+couleur, contraste >= 4.5:1, daltonisme), auditive (sous-titres enrichis avec préfixe [KOFFI], glyphes Unicode lingala ɛ/ɔ, indicateurs directionnels), motrice (remapping complet, maintien continu Hold au lieu des QTE rapides) et cognitive."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: PRD-06
  department: 08-production-quality
  stratum: 5
  version: "1.1.0"
  inputs:
    - "ui-screen-specs-gd-07"
    - "combat-design-gd-05"
    - "localization-tables-aud-04"
  outputs:
    - "xag-compliance-matrix.csv"
    - "accessibility-audit-report.md"
  upstream_dependencies:
    - "GD-07"
    - "GD-05"
    - "AUD-04"
---

# `PRD-06` — Accessibility Specialist (`prd-06-accessibility-specialist`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`08-production-quality`** (Strate DAG **5**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Audit obligatoire de toute interface utilisateur (`GD-07`), mécanique de combat (`GD-05`), conduite (`GD-06`) ou système de sous-titrage (`AUD-04`).
- Exécution du validateur automatisé `scripts/check_xag_compliance.py` avant toute certification qualité par `DIR-07`.
- Spécification des options du menu Accessibilité de ZAÏRE (accessibles dès le premier lancement du jeu, *First-Boot Accessibility Screen*).

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `ui-screen-specs-gd-07`, `combat-design-gd-05`, `localization-tables-aud-04`
- **Sorties produites** : `xag-compliance-matrix.csv`, `accessibility-audit-report.md`
- **Dépendances Amont Canoniques (DAG)** : `GD-07`, `GD-05`, `AUD-04`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne programme pas directement les widgets C++ (`ENG-02`) ni les shaders post-process (`ART-08`), mais détient un droit de blocage qualité avec `DIR-07` en cas de non-conformité XAG.
- **Interdiction / Limite** : Interdit toute mécanique reposant exclusivement sur la couleur, le son ou le martèlement rapide de touche (Button Mashing QTE) sans alternative.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Exécuter `scripts/check_xag_compliance.py` sur les spécifications UI/Gameplay soumises.
2. Vérifier la conformité **XAG 101 / 102 (Visuel)** : ratio de contraste `>= 4.5:1` (`>= 7:1` sur les sous-titres), mise à l'échelle de l'UI jusqu'à `+35 %`, double codage systématique (Couleur + Forme/Icône).
3. Vérifier la conformité **XAG 104 (Sous-titrage & Audio)** : préfixe explicite du locuteur coloré et différencié (`[KOFFI]`, `[AMINA]`), support parfait des caractères Unicode du lingala (`ɛ`, `ɔ`), fond semi-opaque réglable (`50 %` à `100 %`) et indicateur visuel directionnel pour les menaces sonores (`BUS_SFX_CombatTelegraph`).
4. Vérifier la conformité **XAG 107 (Moteur)** : remapping complet des touches (`Enhanced Input`), option de remplacement des pressions répétées (QTE) par un maintien continu (`Hold`) ou une validation automatique, et assistance au maintien de voie sur `VEH-MOTO-WEWA-01`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Séquence de lutte au corps-à-corps ou de crochetage exigeant un martèlement rapide de bouton (Button Mashing) | Imposer l'intégration native de l'option 'QTE Input Mode : Tap / Hold / Auto-Complete' dans Enhanced Input (ENG-02) | Respecter XAG 107 et quality-standards.md Section 2.D |
| Alarme d'attaque lourde ennemie transmise uniquement par un signal sonore (AUD-02) | Ajouter un indicateur visuel radial directionnel à fort contraste autour de Koffi synchronisé sur le Startup de l'attaque (>= 22 frames) | Assurer une jouabilité complète pour les joueurs sourds ou malentendants |
| Sous-titre dépourvu du nom du locuteur ou fond transparent illisible sous le soleil équatorial de midi | Forcer le format '[LOCUTEUR] : Texte' et un fond sombre semi-opaque par défaut à 78 % d'opacité (ratio contraste >= 7:1) | Garantir la validation de check_xag_compliance.py |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/xag-compliance-standards.md`
- **Modèle Officiel de Livrable** : `templates/xag-compliance-matrix.csv`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-accessibility-audit.md`
- `scripts/check_xag_compliance.py` : Script exécutable déterministe associé à `PRD-06` (supporte `--file`).
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-accessibility-audit.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/xag-compliance-matrix.csv` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `PRD-06` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] `python skills/08-production-quality/prd-06-accessibility-specialist/scripts/check_xag_compliance.py` retourne un code `0`.
- [ ] Les 4 piliers XAG (Visuel, Auditif, Moteur, Cognitif) sont couverts et validés sans exception.
- [ ] L'écran de configuration d'accessibilité est présenté dès le premier démarrage du jeu (*First-Boot Flow*).
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-07`, `GD-07`, `AUD-04`.
