# Spécification d'Arbre de Progression & Réputation (`GD-04`)

- **Système Lié** : `SYS-WLD-REPUTATION` & Progression `CHR-PROTAG-KOFFI`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Matrice des Compétences Déblocables (Mapping GAS)
| Skill Node ID | Branche | Gameplay Tag Associé | Prérequis | Effet Tactique Concret |
| :--- | :--- | :--- | :--- | :--- |
| `SKL-...` | `[Mêlée / Wewa / Réseau]` | `Ability....` | `[Niveau / Node]` | `[Description]` |

## 2. Paliers de Réputation par Commune (`DST-*`)
| Palier | Seuil Points | Effet sur la Foule (`AI-02`) & Commerces (`GD-03`) |
| :--- | :--- | :--- |
| 1. Inconnu | `0 - 249` | Comportement neutre, prix standards (`1.0x`). |

## Contraintes Studio & Validation Pré-Handoff (`GD-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, GD-03, GD-05`
