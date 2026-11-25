# Spécification de Mission Principale — `MSN-MAIN-001-ARRIVEE` (L'Accostage de l'Aube)

- **ID Mission** : `MSN-MAIN-001-ARRIVEE` (`CONFIRMED`)
- **Lieu & Commune** : `LOC-GOMBE-PORT` (`DST-GOMBE`) -> `DST-KALAMU`
- **Personnages** : `CHR-PROTAG-KOFFI`, `CHR-ALLY-AMINA`, `CHR-ALLY-PAPA-ETIENNE`, Gardes `ORG-CARTEL-FLEUVE`
- **Plafond Acteurs `AI-01`** : `16 gardes actifs` (`<= 24 max`, budget `1.65 ms <= 2.5 ms`)

## 1. Objectifs, Étapes & Approches Multiples (`GD-02`)
| Étape | Objectif | Approche A (Furtivité/Social) | Approche B (Parkour/Mêlée) | Handler Anti-Soft-Lock |
| :--- | :--- | :--- | :--- | :--- |
| `ST-01` | Accéder au Hangar Douanier N°4 | Présenter `ITM-DOC-PASSEPORT` (`State.Character.Stealth.Disguised`) | Escalader la grue ouest (`+400 cm`, Ledge `280 cm`) | Si passeport compromis, ouverture de la brèche latérale conteneurs. |
| `ST-02` | Saisir le manifeste `FAM-KABONGO` | Piratage/ouverture silencieuse sous pluie (`World.Weather.TropicalStorm`) | Affrontement machette (`ITM-WPN-MACHETTE`, max 2 Attack Tokens) | Coffre toujours accessible après neutralisation de l'escouade locale. |
| `ST-03` | Exfiltration vers `DST-KALAMU` | Slalom en `VEH-MOTO-WEWA-01` via couloirs `150 cm` | Repli alternatif en `VEH-TAXI-JAUNE-01` | Spawn de 2 Wewa coursiers de secours si la moto initiale est détruite. |

## 2. Conséquences Persistantes (`NAR-01` & `SYS-WLD-REPUTATION`)
- **Branche Furtive** : `ITM-DOC-PASSEPORT` reste valide pour les quêtes secondaires à `DST-GOMBE` ; `+15 000 FC` (`GD-03`).
- **Branche Assaut** : Niveau de vigilance de `ORG-CARTEL-FLEUVE` accru au port, mais `+35 Réputation` immédiate auprès des dockers de `DST-KALAMU` et flash spécial sur `ORG-RADIO-KIN`.
