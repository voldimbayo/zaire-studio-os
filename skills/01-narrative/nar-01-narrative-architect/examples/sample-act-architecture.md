# Exemple `NAR-01` — Architecture de l'Acte I : Les Courants du Fleuve

- **Acte** : `ACTE-I`
- **Titre** : Les Courants du Fleuve
- **Communes Principales** : `DST-GOMBE`, `DST-KALAMU`
- **Personnages Pivots** : `CHR-PROTAG-KOFFI`, `CHR-ANTAG-MUKENDI`, `CHR-ALLY-AMINA`

## 1. Progression Dramatique & Alignement Gameplay
| Séquence | Objectif Dramatique | Mission Associée | Système Gameplay Sollicité |
| :--- | :--- | :--- | :--- |
| 1 | Retour de Koffi sur les barges du fleuve et saisie de l'atelier familial `FAM-KABONGO` | `MSN-MAIN-001-ARRIVEE` | `SYS-STEALTH`, `SYS-WLD-LANDMARKS` |
| 2 | Première alliance avec `ORG-RADIO-KIN` pour exposer la saisie illégale des grues | `MSN-SIDE-014-WEWA` | `SYS-TRAFFIC-ZONE`, `SYS-WLD-REPUTATION` |

## 2. Embranchements & Conséquences Monde Ouvert
| Point de Choix | Option A (Impact Monde) | Option B (Impact Monde) | Variable d'État Persistante |
| :--- | :--- | :--- | :--- |
| Sabotage ou Saisie des registres à `LOC-GOMBE-PORT` | **Sabotage** : Patrouilles doublées à la Gombe, +25 Réputation à Kalamu | **Saisie discrète** : Accès maintenu via `ITM-DOC-PASSEPORT`, bonus monétaire `GD-03` | `WorldState.Act1.PortApproach` |
