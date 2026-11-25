# Conception Systémique Orientée UE5 GAS (`GD-01`)

## 1. Mapping Standard vers Gameplay Ability System
- **Activation Owned Tags** : Tags octroyés à l'acteur pendant que le système est actif (ex: `State.Character.Stealth.Disguised`).
- **Activation Blocked Tags** : Tags interdisant l'activation (ex: `State.Character.Combat.Engaged` bloque immédiatement l'accréditation sociale `ITM-DOC-PASSEPORT`).
- **Émergence Systémique** : L'averse équatoriale (`World.Weather.TropicalStorm`) atténue de `-40 %` le rayon de perception auditive des gardes (`AI-01`) tout en dispersant la foule civile (`AI-02`).

---

## 3. Spécifications Techniques & Compatibilité Moteur (`GD-01` — Strate DAG 1)

- **Systèmes Gameplay, GAS & Common UI (UE 5.8)** (`SRC-002`, `SRC-024`, `SRC-025`, `SRC-026`, `SRC-031`) :
  - **Gameplay Ability System (`SRC-002`)** : Découplage total par `FGameplayTag` (`knowledge/technical-specs/gameplay-tags-taxonomy.csv`), zéro variable booléenne ad-hoc, nettoyage garanti dans `EndAbility()`.
  - **Combat & Game Feel (`SRC-025`)** : Frame Data à `60 FPS` (`1 frame = 16.66 ms`), Startup ennemi `>= 22 frames (366 ms)`, Hitstop calibré (`40-90 ms`), plafond d'`Attack Tokens` à `2 assaillants simultanés` (`1` en couloir `< 500 cm`).
  - **Économie (`SRC-024`) & Véhicules (`SRC-004`)** : Ratio `Sink / Faucet` maintenu entre `0.75` et `0.92` sur 40 heures ; modulation des prix et de la tolérance policière (`ORG-POLICE-PCR` / `SYS-LAW-ESCALATION`) par `SYS-WLD-REPUTATION`.

---

## 4. Contrats d'Entrées / Sorties & Traçabilité Inter-Skills

- **Dépendances Amont Obligatoires (`upstream_dependencies`)** : `DIR-03`, `DIR-05`
- **Audit des Entrées (`inputs`)** :
  - `creative-pillars-dir-03` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `lead-gd-directives-dir-05` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
  - `open-world-structure-wld-04` : Vérifier la présence, le format et le statut (`CONFIRMED` ou `PROPOSED`) avant traitement.
- **Garanties sur les Sorties (`outputs`)** :
  - `system-design-document.md` : Doit respecter le gabarit `templates/system-design-doc-template.md` et passer l'audit croisé.
  - `gameplay-tags-mapping.csv` : Doit respecter le gabarit `templates/system-design-doc-template.md` et passer l'audit croisé.
- **Auditeurs de Validation Croisée** : `DIR-05`, `ENG-02`

---

## 5. Matrice des Modes de Défaillance (FMEA) & Protocoles de Récupération

| Mode de Défaillance Détecté | Impact Potentiel sur ZAÏRE | Action Corrective Immédiate | Protocole d'Escalade |
| :--- | :--- | :--- | :--- |
| Mode de Défaillance 1: Deux systèmes doivent communiquer (ex: météo pluie -> bruit de pas infiltration) | Blocage / Dégradation si ignoré | Interdire le couplage direct entre classes et passer exclusivement par un Gameplay Tag partagé (World.Weather.TropicalStorm) | Escalade vers Maintenir la modularité GAS validée avec ENG-02 |
| Mode de Défaillance 2: Mécanique complexe nécessitant plus de 3 minutes de tutoriel texte | Blocage / Dégradation si ignoré | Simplifier la règle d'activation contextuelle à un seul input et enseigner par l'affordance spatiale en jeu (WLD-05) | Escalade vers Appliquer le standard d'onboarding DIR-05 |
| Mode de Défaillance 3: Système impactant le budget CPU par un polling frame-by-frame | Blocage / Dégradation si ignoré | Remplacer le polling par des callbacks événementiels sur changement de Gameplay Tag | Escalade vers Respecter l'enveloppe Game Thread <= 6.5 ms |
| Référence à une entité absente de `knowledge/entities-registry.csv` | Corruption de l'intégrité référentielle (Référence Fantôme) | Rejeter l'identifiant libre et enregistrer un ID normalisé (`CHR-`, `LOC-`, `MSN-`, `ORG-`, `SYS-`...) au statut `PROPOSED` ou `RESEARCH_REQUIRED` | `PRD-03` / `DIR-06` |
| Donnée factuelle incertaine sur Kinshasa ou non testée dans le moteur binaire | Risque d'hallucination documentaire ou technique | Isoler explicitement l'élément avec le statut `RESEARCH_REQUIRED` (donnée) ou `NOT TESTED` (exécution binaire UE 5.8 / Houdini 22 / Wwise) | `WLD-02` / `DIR-04` / `DIR-07` |

---

## 6. Checklist d'Inspection Qualité Pré-Handoff (`GD-01`)

- [ ] **Contrôle DoD #1** : 100 % des états et déclencheurs du système sont mappés sur des Gameplay Tags enregistrés.
- [ ] **Contrôle DoD #2** : Le document définit clairement les règles d'activation, d'annulation (Cancel Tags) et de blocage (Block Tags) sous UE5 GAS.
- [ ] **Contrôle DoD #3** : Les cas limites (interruption par combat, entrée dans un véhicule, transition de quartier) sont couverts.
- [ ] **Contrôle Référentiel** : Tous les identifiants d'entités cités existent dans `knowledge/entities-registry.csv`.
- [ ] **Contrôle Sources** : Toutes les références documentaires citées (`SRC-001` à `SRC-035`) sont enregistrées dans `research/source-registry.csv` avec leur niveau réel de vérification ; les recommandations d'ingénierie internes sont explicitement balisées.
- [ ] **Contrôle Périmètre (Scope Guard)** : Aucune section du livrable n'empiète sur les responsabilités des skills amont ou aval.
