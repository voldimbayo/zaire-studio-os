# Exemple `AUD-02` — Spécification SFX de `VEH-MOTO-WEWA-01` & Pluie sur Tôle

- **ID Banque / Système** : `SB_VEH_MOTO_WEWA` & `SB_WEATHER_TROPICAL`
- **Bus Wwise Parent (`AUD-01`)** : `BUS_SFX_PlayerVehicle` & `BUS_Ambience_Kinshasa`
- **Statut** : `CONFIRMED`

## 1. Catalogue d'Événements Wwise & Variations
| Event Name | Type Conteneur | Variations Min | Pitch Random | Rayon Atténuation Max (cm) |
| :--- | :--- | :--- | :--- | :--- |
| `Play_Veh_Wewa_Engine_Loop` | `Blend Container (4 couches RPM)` | Synthèse continue + 4 boucles | Piloté par RTPC | `6500 cm (65 m)` |
| `Play_Veh_Wewa_Horn_Short` | `Random Container` | `8 coups de klaxon kinois` | `±80 cents` | `5000 cm (50 m)` |
| `Play_Cmb_Machete_Parry` | `Blend (Impact + Résonance lame)` | `8 impacts métalliques` | `±150 cents` | `3000 cm (30 m)` |
| `Play_Amb_Rain_SheetMetal_Roof` | `Granular MetaSound / Blend` | `3 boucles asynchrones` | `±50 cents` | `2500 cm (Local Portal)` |

## 2. Matrice des Paramètres Temps Réel (RTPC / Switches)
| Nom RTPC / Switch | Source UE5 | Plage Entrée | Paramètre Audio Piloté |
| :--- | :--- | :--- | :--- |
| `RTPC_Veh_Wewa_RPM` | `UChaosVehicleMovement::GetEngineRPM()` | `1100 - 9200` | Crossfade `Idle -> Low -> Mid -> High` + Pitch shift. |
| `RTPC_Weather_RainIntensity` | Tag `World.Weather.TropicalStorm` | `0.0 - 1.0` | Volume crépitement tôle (`-48 dB à 0 dB`) + niveau éclaboussures pneus. |
| `SW_Surface_Type` | `FHitResult::PhysMaterial` | 5 états | Sélectionne instantanément la couche de roulement/pas (Asphalte, Latérite, Boue, Tôle). |
