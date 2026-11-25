# Guide de Mise à Jour & Maintenance — ZAÏRE STUDIO OS (`update-guide.md`)

Ce document détaille la procédure standardisée pour faire évoluer **ZAÏRE STUDIO OS** (ajout ou mise à jour d'une entité dans `knowledge/`, modification d'un skill existant, ajout d'une source vérifiée et génération d'une nouvelle release versionnée).

---

## 1. Cycle de Mise à Jour du Registre de Connaissances (`knowledge/`)

Lorsqu'un livrable passe du statut `PROPOSED` au statut `CONFIRMED` (après audit `NAR-06` / `ENG-07` / `PRD-04` / `PRD-06` et cosignature `DIR-06` + `DIR-07`) :
1. Ajoutez ou mettez à jour la ligne correspondante dans [knowledge/entities-registry.csv](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/knowledge/entities-registry.csv) en respectant strictement les 9 préfixes (`CHR-`, `FAM-`, `ORG-`, `DST-`, `LOC-`, `MSN-`, `ITM-`, `VEH-`, `SYS-`).
2. Enregistrez la transition avec horodatage ISO-8601 dans [knowledge/status-audit-log.csv](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/knowledge/status-audit-log.csv).
3. Exécutez immédiatement le validateur d'intégrité référentielle :
   ```bash
   python tools/validate_registry.py
   ```
   *(Aucun commit ne doit être effectué si ce script retourne un code différent de `0`.)*

---

## 2. Modification d'un Skill ou d'un Département (`tools/departments/` & `skills/`)

L'architecture des 57 skills est maintenue de manière modulaire dans `tools/departments/dept_00_direction.py` à `dept_08_production_quality.py` :
1. Modifiez le `SkillBlueprint` du skill concerné dans son module départemental (ou éditez directement son `SKILL.md`, `references/`, `templates/`, `examples/`, `scripts/`).
2. Régénérez et auditez le système complet :
   ```bash
   python tools/build_all_skills.py
   python tools/check_dag_cycles.py
   python tools/lint_skills.py --require-all
   ```
3. Exécutez la suite de tests unitaires, d'intégration et les 5 scénarios fonctionnels :
   ```bash
   python -m unittest discover -s tests -v
   python tools/run_functional_scenarios.py
   ```

---

## 3. Procédure de Publication d'une Nouvelle Version (Semantic Versioning)

1. Incrémentez le numéro de version (`MAJOR.MINOR.PATCH`) dans le fichier [VERSION](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/VERSION) :
   - `PATCH` (`1.0.x`) : Correction de texte, enrichissement du glossaire lingala ou ajustement d'un exemple sans changement de schéma.
   - `MINOR` (`1.x.0`) : Ajout de nouvelles entités `CONFIRMED`, nouvelles règles de validation dans `scripts/` ou passage d'une commune `RESEARCH_REQUIRED` (`DST-MASINA`) en `CONFIRMED`.
   - `MAJOR` (`x.0.0`) : Modification structurelle du graphe DAG ou des schémas JSON (`schemas/`).
2. Documentez les changements dans [CHANGELOG.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/CHANGELOG.md).
3. Exécutez `python tools/package_skills.py` pour régénérer :
   - [docs/skills-index.md](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/docs/skills-index.md)
   - Les 57 archives individuelles dans `releases/skills/*.zip`
   - Les 9 archives départementales dans `releases/departments/*.zip`
   - L'archive globale `releases/zaire-studio-os-v<VERSION>-full.zip`
4. Dans **Claude.ai**, réimportez uniquement les fichiers `.zip` des skills modifiés et mettez à jour `entities-registry.csv` dans le *Project Knowledge*.
