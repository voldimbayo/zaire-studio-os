# Plan de Test QA Open World & Anti-Soft-Lock (`PRD-04`)

- **ID Plan de Test** : `QATP-[MSN/DST]-[NUM]`
- **Cible Testée** : `MSN-...` | `LOC-...` (`DST-...`)
- **Cellules World Partition Couvertes** : `[Grid_X.._Y..]`
- **Taux de Reproductibilité Exigé** : `>= 90 %`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Matrice de Couverture Fonctionnelle & Destructive
| Test Case ID | Catégorie (`NOMINAL` / `DESTRUCTIVE`) | Action Testeur / Perturbation | Résultat Attendu (Zéro Soft-Lock) | Automatisation (`PRD-05`) |
| :--- | :--- | :--- | :--- | :--- |
| `TC-001` | `DESTRUCTIVE` | `[Destruction véhicule / Fuite]` | `[Handler de récupération GD-02 actif]` | `Oui (Gauntlet)` |

## 2. Format de Ticket d'Anomalie Déterministe
- **Coordonnées UE5 (X, Y, Z cm) & Seed** : `[X=..., Y=..., Z=... | Seed=19600630]`
- **Gameplay Tags & Data Layers Actifs** : `[Liste]`

## Contraintes Studio & Validation Pré-Handoff (`PRD-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-07, PRD-05`
