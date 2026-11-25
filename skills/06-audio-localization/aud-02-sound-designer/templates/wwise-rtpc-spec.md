# Spécification SFX, RTPC & Spatial Audio Wwise (`AUD-02`)

- **ID Banque / Système** : `SB_[DOMAINE]_[SLUG]`
- **Bus Wwise Parent (`AUD-01`)** : `BUS_...`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Catalogue d'Événements Wwise & Variations
| Event Name (`Play_...`) | Type Conteneur | Variations Min | Pitch Random (cents) | Rayon Atténuation Max (cm) |
| :--- | :--- | :--- | :--- | :--- |
| `Play_...` | `Random / Blend` | `6` | `±120` | `[XXXX cm]` |

## 2. Matrice des Paramètres Temps Réel (RTPC / Switches)
| Nom RTPC / Switch | Source UE5 (`ENG-02`/`ENG-05`) | Plage Entrée | Paramètre Audio Piloté |
| :--- | :--- | :--- | :--- |
| `RTPC_...` | `[Variable C++/Chaos]` | `[Min - Max]` | `[Pitch / LPF / Volume dB]` |

## Contraintes Studio & Validation Pré-Handoff (`AUD-02`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `AUD-01, ENG-07, GD-05, GD-06`
