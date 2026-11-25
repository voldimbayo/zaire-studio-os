# Handoff Packet — ZAÏRE STUDIO OS

## 1. Métadonnées d'Exécution
- **Task ID** : `TSK-YYYY-NNN`
- **Skill Émetteur** : `[ID-SKILL] — [Nom du Skill]`
- **Département** : `[00-direction .. 08-production-quality]`
- **Date d'Exécution** : `YYYY-MM-DD`
- **Statut du Livrable** : `PROPOSED` | `RESEARCH_REQUIRED` | `BLOCKED`
- **Skills Aval Destinataires** : `[Liste des IDs skills avals selon skill-dependencies.md]`

---

## 2. Entités Référencées & Créées (`knowledge/entities-registry.csv`)

| ID Entité | Catégorie | Statut | Action (`READ` / `NEW` / `UPDATE`) | Résumé / Justification |
| :--- | :--- | :--- | :--- | :--- |
| `DST-...` | `DISTRICT` | `CONFIRMED` | `READ` | Commune d'ancrage du livrable |
| `LOC-...` | `LOCATION` | `PROPOSED` | `NEW` | Nouveau Point d'Intérêt créé |

---

## 3. Artefact Principal Produit
- **Modèle utilisé** : `templates/...`
- **Chemin / Identifiant de l'artefact** : `[Nom du document ou fichier généré]`

*(Insérer ou référencer ici le corps complet du livrable métier)*

---

## 4. Zones d'Incertitude & Requêtes de Recherche (`RESEARCH_REQUIRED`)
- [ ] Aucune donnée inventée. Les éléments suivants nécessitent une vérification par `WLD-02`, `WLD-03` ou `ENG-*` :
  - `ID / Sujet` : `[Description précise de la lacune documentaire ou technique]`

---

## 5. Checklist Definition of Done (DoD) — Auto-Validation
- [ ] **Format & Gabarit** : Conforme au modèle officiel du skill (`templates/`).
- [ ] **Intégrité des IDs** : 100 % des identifiants respectent la nomenclature (`CHR-`, `FAM-`, `ORG-`, `DST-`, `LOC-`, `MSN-`, `ITM-`, `VEH-`, `SYS-`).
- [ ] **Traçabilité** : Sources techniques (`SRC-*`) et culturelles citées ; zéro extrapolation non balisée.
- [ ] **Périmètre Respecté** : Aucun empiètement sur les responsabilités d'un skill amont ou aval.
- [ ] **Budgets & Standards** : Respect des budgets CPU/GPU/VRAM (`16.6 ms` / `33.3 ms`), métriques spatiales (`1 UE = 1 cm`, couloirs `>= 350 cm`) et accessibilité XAG.
- [ ] **Validation Croisée Requise** : Prêt pour revue par `[NAR-06 / ENG-07 / PRD-04 / PRD-06 / DIR-*]`.
