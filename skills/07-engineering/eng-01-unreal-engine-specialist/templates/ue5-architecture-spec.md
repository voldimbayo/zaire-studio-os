# Spécification d'Architecture C++20 Unreal Engine 5 (`ENG-01`)

- **Module / Subsystem** : `ZaireCore` | `UZaire...Subsystem`
- **Système Associé** : `SYS-...`
- **Budget Game Thread (`PERF-CPU-GAME`)** : `<= 6.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture des Classes C++ & Dépendances Modules
- **Classe Principale** : `U...` (Héritage, cycle de vie)
- **Gestion Mémoire & Streaming** : `[TSoftObjectPtr / FStreamableManager]`

## 2. Configuration World Partition & Data Layers
| Data Layer | Type (`Runtime` / `Editor`) | Condition d'Activation | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `DL_...` | `Runtime` | `[Gameplay Tag / État Quête]` | `[XX MB]` |

## Contraintes Studio & Validation Pré-Handoff (`ENG-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-04, ENG-07`
