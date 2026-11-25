# Décision de Jalon & Arbitrage de Scope (`DIR-02`)

- **Jalon Évalué** : `Vertical Slice` | `Alpha` | `Beta` | `Gold`
- **Décision Exécutive** : `GO` | `CONDITIONAL_GO` | `NO_GO`
- **Variation Charge / Budget** : `[+X % / -Y %]`

## 1. Arbitrage du Périmètre (Scope Matrix)
| ID Entité / Système | Priorité (`P0`/`P1`/`P2`) | Décision (`MAINTAIN` / `DEFER` / `DEPRECATE`) | Justification |
| :--- | :--- | :--- | :--- |
| `DST-...` | `P0` | `MAINTAIN` | Cœur du Vertical Slice |

## 2. Risques Critiques & Conditions de Passage
- **Conditions obligatoires avant clôture** : `[Liste]`

## Contraintes Studio & Validation Pré-Handoff (`DIR-02`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-01, DIR-07`
