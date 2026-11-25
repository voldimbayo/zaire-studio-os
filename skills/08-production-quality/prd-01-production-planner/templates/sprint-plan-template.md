# Plan de Sprint & Matrice RACI (`PRD-01`)

- **ID Sprint** : `SPR-2026-NN`
- **Jalon Cible (`DIR-02`)** : `[Vertical Slice / Alpha / Beta / Gold]`
- **Capacité Planifiée / Buffer** : `85 % Planifié / 15 % Buffer Aléas`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Séquencement des Livrables sur le Chemin Critique
| Task ID | Livrable / Entité | Skill `R` (Responsible) | Skill `A` (Accountable) | Skills `C` (Consulted) | Strate DAG |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TSK-...` | `[Livrable]` | `[Skill unique]` | `DIR-...` | `[Auditeurs]` | `[1..5]` |

## 2. Goulots d'Étranglement & Dépendances Surveillées
- **Verrou Blockout First** : `[État de validation WLD-05 -> ART-02]`

## Contraintes Studio & Validation Pré-Handoff (`PRD-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-01, DIR-02`
