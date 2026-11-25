# Exemple `GD-04` — Arbre de Progression de Koffi & Réputation `DST-MATONGE`

- **Système Lié** : `SYS-WLD-REPUTATION` & Progression `CHR-PROTAG-KOFFI`
- **Statut** : `CONFIRMED`

## 1. Matrice des Compétences Déblocables (Mapping GAS)
| Skill Node ID | Branche | Gameplay Tag Associé | Prérequis | Effet Tactique Concret |
| :--- | :--- | :--- | :--- | :--- |
| `SKL-CMB-01` | Mêlée & Agilité | `State.Character.Combat.Parrying` | Niveau 2 | Élargit la fenêtre de parade parfaite de `+50 ms` avec `ITM-WPN-MACHETTE` et désarme l'assaillant. |
| `SKL-VEH-01` | Mécanique & Wewa | `Vehicle.Type.MotoWewa` | Niveau 3 | Amortissement amélioré après un saut de rampe et maintien de l'adhérence sous `World.Weather.TropicalStorm`. |
| `SKL-NET-01` | Voix de Kinshasa | `State.Character.Stealth.Disguised` | Niveau 4 | Permet d'interpeller les citoyens en lingala (`LEX-001 Mbote`) pour créer une diversion sonore devant les gardes `AI-01`. |

## 2. Paliers de Réputation à `DST-MATONGE`
| Palier | Seuil Points | Effet sur la Foule (`AI-02`) & Commerces (`GD-03`) |
| :--- | :--- | :--- |
| 1. Inconnu | `0 - 249` | Foule neutre, tarifs standards (`1.0x`). |
| 2. Respecté | `250 - 599` | Salutations positives en barks (`NAR-04`), remise `-10 %` chez les mécaniciens. |
| 3. Enfant du Quartier | `600 - 999` | Les chauffeurs de `VEH-MOTO-WEWA-01` cèdent immédiatement leur guidon en cas d'urgence ; remise `-15 %`. |
