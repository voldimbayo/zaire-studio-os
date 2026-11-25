# Exemple `ENG-01` — Architecture de `UZaireDistrictStreamingSubsystem` (`SYS-WLD-STREAMING`)

- **Module / Subsystem** : `ZaireWorldRuntime` | `UZaireDistrictStreamingSubsystem : public UWorldSubsystem`
- **Système Associé** : `SYS-WLD-STREAMING`
- **Budget Game Thread (`PERF-CPU-GAME`)** : `0.45 ms` mesuré (inclus dans `<= 6.5 ms`)
- **Statut** : `CONFIRMED`

## 1. Architecture des Classes C++ & Dépendances Modules
- **Classe Principale** : `UZaireDistrictStreamingSubsystem` pilote l'activation asynchrone des `UDataLayerAsset` selon la progression des missions (`MSN-*`) et projette une `FWorldPartitionStreamingSource` anticipée de `+4000 cm` lorsque le joueur pilote `VEH-MOTO-WEWA-01` à plus de `50 km/h`.
- **Gestion Mémoire & Streaming** : Zéro pointeur dur vers les acteurs de mission ; pré-chargement asynchrone déclenché `180 m` avant l'entrée dans l'arène `LOC-GOMBE-PORT`.

## 2. Configuration World Partition & Data Layers
| Data Layer | Type | Condition d'Activation | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `DL_Gombe_Port_Base` | `Runtime` | Permanent dans le rayon `256 m` de `LOC-GOMBE-PORT` | `420 MB` |
| `DL_MSN001_SyndicateAlert` | `Runtime` | Actif uniquement pendant `MSN-MAIN-001-ARRIVEE` | `115 MB` |
| `DL_Matonge_NightMarket` | `Runtime` | Heure `[18h00 - 04h00]` dans `World.District.Matonge` | `280 MB` |
