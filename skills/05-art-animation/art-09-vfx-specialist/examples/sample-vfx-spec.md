# Exemple `ART-09` — Spécification de `NS_Weather_TropicalRain` & `NS_Cmb_MacheteParry`

- **Nom Système Niagara** : `NS_Weather_TropicalRain` & `NS_Cmb_MacheteParry`
- **Gameplay Tag Déclencheur** : `World.Weather.TropicalStorm` & `State.Character.Combat.Parrying`
- **Budget GPU Alloué** : `0.62 ms` (Pluie) + `0.18 ms` (Parade) = `0.80 ms` (`<= 1.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Architecture Émetteurs & Optimisation Overdraw
- **`NS_Weather_TropicalRain`** :
  - **Simulation** : `GPU Compute` (12 000 gouttes en boîte caméra `1800 × 1800 × 800 cm`).
  - **Collisions** : Évaluation sur le **Global Distance Field** générant automatiquement les impacts d'éclaboussures sur les toits en tôle, les conteneurs de `LOC-GOMBE-PORT` et la chaussée, tout en gardant les intérieurs et le dessous des auvents (`180 cm` de `DST-MATONGE`) parfaitement secs.
- **`NS_Cmb_MacheteParry`** :
  - **Simulation** : Burst instantané de `35 étincelles chaudes` (`0.18 s` de durée de vie) lors d'une parade réussie avec `ITM-WPN-MACHETTE`, synchronisé sur le Hitstop de `85 ms` (`GD-05`).
  - **Distance de Culling & Max Instances** : `2500 cm | Max 4 instances`.
