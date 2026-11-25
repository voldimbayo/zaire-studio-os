# Exemple `PRD-01` — Plan du Sprint `SPR-2026-04` (Vertical Slice `LOC-GOMBE-PORT`)

- **ID Sprint** : `SPR-2026-04`
- **Jalon Cible (`DIR-02`)** : `Vertical Slice (MSN-MAIN-001-ARRIVEE)`
- **Capacité Planifiée / Buffer** : `85 % Planifié / 15 % Buffer Optimisation P99`
- **Statut** : `CONFIRMED`

## 1. Séquencement des Livrables sur le Chemin Critique
| Task ID | Livrable / Entité | Skill `R` | Skill `A` | Skills `C` | Strate DAG |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TSK-2026-041` | Habillage Modulaire `KIT-GOMBE-PORT` sur `BLK-GOMBE-PORT-01` validé | `ART-02` | `DIR-03` | `WLD-06`, `ART-04`, `WLD-05` | Strate 3 |
| `TSK-2026-042` | State Tree Patrouille 16 Gardes `ORG-CARTEL-FLEUVE` | `AI-01` | `DIR-04` | `GD-05`, `ENG-07` | Strate 3 |
| `TSK-2026-043` | Éclairage Aube Brumeuse `LGT_GOMBE_DAWN_FOG` (`<= 4.2 ms`) | `ART-07` | `DIR-03` | `ART-01`, `ENG-06` | Strate 3 |
| `TSK-2026-044` | Audit P99 (`<= 16.6 ms`) & Suite Gauntlet `MSN-MAIN-001-ARRIVEE` | `ENG-07` | `DIR-04` | `PRD-05`, `DIR-07` | Strates 4-5 |

## 2. Goulots d'Étranglement & Dépendances Surveillées
- **Verrou Blockout First** : `BLK-GOMBE-PORT-01` a été validé par `DIR-05` au Sprint 03 ; `ART-02` peut produire les kits Nanite sans risque de reprise métrique.
