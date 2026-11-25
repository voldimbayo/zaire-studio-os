# Exemple de Décision `DIR-06` — Promotion de `LOC-LIMETE-ECHANGEUR`

- **Date d'Audit** : `2026-11-25`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`

## 1. Transitions de Statuts Décidées
| ID Entité | Ancien Statut | Nouveau Statut | Valideurs | Justification & Sources (`SRC-*`) |
| :--- | :--- | :--- | :--- | :--- |
| `LOC-LIMETE-ECHANGEUR` | `PROPOSED` | `CONFIRMED` | `DIR-03, DIR-06, DIR-07` | Landmark majeur de `DST-LIMETE` vérifié (`SRC-019`), dépendances `DST-LIMETE` et `SYS-WLD-LANDMARKS` confirmées. |
| `DST-MASINA` | `PROPOSED` | `RESEARCH_REQUIRED` | `DIR-06` | Maintenu en `RESEARCH_REQUIRED` tant que le réseau de voirie secondaire OSM n'est pas complété par `WLD-03`. |
