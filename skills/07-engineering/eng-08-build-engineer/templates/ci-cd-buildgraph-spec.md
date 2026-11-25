# Spécification Pipeline CI/CD BuildGraph & Packaging (`ENG-08`)

- **Nom du Pipeline** : `BG_Zaire_...`
- **Cible Temps Build Incrémental (`PERF-CI-BUILD`)** : `<= 15.0 minutes`
- **Taux de Cache Hit Zen DDC Requis** : `>= 95 %`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Étapes du Graphe BuildGraph / Horde
| Étape | Commande UAT / Commandlet | Timeout (min) | Condition d'Échec Bloquant |
| :--- | :--- | :--- | :--- |
| `1_Validate` | `RunUnreal -Commandlet=DataValidation` | `3 min` | `> 0 asset invalide (ENG-03)` |

## 2. Sécurité Packaging IoStore & Gestion des Secrets
- **Chiffrement Index `.utoc`** : `AES-256 via Variable d'Environnement (Zéro clé en dur)`
- **Overhead CPU Décompression** : `[< 0.5 %]`

## Contraintes Studio & Validation Pré-Handoff (`ENG-08`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-04, PRD-05, ENG-07`
