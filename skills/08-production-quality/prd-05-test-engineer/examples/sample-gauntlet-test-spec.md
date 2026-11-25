# Exemple `PRD-05` — Suite Automatisée `GT_MSN001_And_Matonge_Soak`

- **Nom de la Suite / Contrôleur** : `AFT_Zaire_MSN001_AntiSoftLock` & `UZaireGauntletKinshasaTraversal`
- **Systèmes Critiques Couverts (`SYS-*`)** : `SYS-WLD-STREAMING`, `SYS-STEALTH`, `SYS-CMB-MELEE`, `SYS-CROWD-MASS`, `SYS-TRAFFIC-ZONE`, `SYS-PHYS-CHAOS` (**Couverture : 88.5 %** `>= 80 %`)
- **Taux de Faux Positifs** : `0.4 %` sur 250 runs Horde (`< 2 %` requis)
- **Statut** : `CONFIRMED`

## 1. Protocole de Synchronisation Événementielle (Zéro `Sleep`)
| Étape du Test | Delegate / Événement Attendu | Assertion Vérifiée | Timeout Sécurité |
| :--- | :--- | :--- | :--- |
| `1_SpawnAndStream` | `UZaireDistrictStreamingSubsystem::OnDistrictReady` | `LOC-GOMBE-PORT` chargé, `VRAM <= 6144 MB`. | `20 s` |
| `2_TestParryGAS` | `UZaireGA_MeleeParry::OnParryDeflectTriggered` | Tag `State.Character.Combat.Parrying` actif + Hitstop `85 ms`. | `10 s` |
| `3_DestroyWewaFallback` | `AZaireVehicle::OnChaosVehicleDestroyed` | Transition `MSN-MAIN-001-ARRIVEE` vers `ST-03_BackupVehicle` en `< 1 frame`. | `5 s` |
| `4_MatongeTrafficSoak` | `UZaireTrafficWatchdog::OnIntersectionCycle` | 600 PNJ `AI-02` + 75 véhicules `AI-03` pendant 2h, `0 deadlock > 8s`, `P99 <= 16.6 ms`. | `120 min` |
