# Exemple `GD-06` — Spécification de `VEH-MOTO-WEWA-01` (Moto-Taxi Wewa 125cc)

- **ID Véhicule** : `VEH-MOTO-WEWA-01`
- **Gameplay Tag** : `Vehicle.Type.MotoWewa`
- **Gabarit (L × l × H en cm)** : `205 × 80 × 115 cm` (compatible couloir inter-file `>= 130 cm`)
- **Statut** : `CONFIRMED`

## 1. Paramètres Dynamiques Chaos Vehicles (`ENG-05`)
- **Masse Totale (kg)** : `210 kg` (moto `135 kg` + `CHR-PROTAG-KOFFI` `75 kg`).
- **Centre de Gravité (Offset Z cm)** : `-28 cm` (abaissé pour stabiliser les changements d'angle rapides en slalom).
- **Vitesse Max & Accélération (0-60 km/h)** : `95 km/h | 3.2 s` (couple élevé à bas régime pour se dégager des carrefours).
- **Assistance & Stabilisation** : Couple de redressement gyroscopique progressif actif de `0 à 35 km/h` ; inclinaison maximale (Lean Angle) plafonnée à `42°` sur sec et `34°` sous `World.Weather.TropicalStorm`.

## 2. Réponse par Surface & Météo
| Surface (`ChaosPhysicalMaterial`) | Multiplicateur Grip Latéral | Multiplicateur Freinage | Effet Caméra / Audio (`AUD-02`) |
| :--- | :--- | :--- | :--- |
| `PM_Asphalt_Dry` (`LOC-GOMBE-BD30JUIN`) | `1.20` | `1.15` | FOV `+4°` à pleine vitesse, RTPC régime moteur clair. |
| `PM_Asphalt_Wet` (`LOC-GOMBE-PORT` pluie) | `0.92` | `0.88` | Légère dérive arrière contrôlable + gerbes d'eau Niagara (`ART-09`). |
| `PM_Laterite_Dry` (`DST-KALAMU`) | `0.96` | `0.92` | Micro-vibrations suspension + traînée de poussière ocre. |
| `PM_Laterite_Mud` (Averse équatoriale) | `0.80` | `0.76` | Patinage roue arrière au démarrage + éclaboussures boueuses. |
