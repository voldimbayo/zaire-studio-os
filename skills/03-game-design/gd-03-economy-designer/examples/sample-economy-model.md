# Exemple `GD-03` — Modèle Économique de l'Acte I & Simulation 40h

## 1. Résultat de `scripts/simulate_economy.py`
- **Durée simulée** : `40 heures`
- **Ratio Moyen `Sink / Faucet`** : `0.844` (Cible `[0.75, 0.92]` -> **CONFORME**)
- **Solde Net Final (Heure 40)** : `395 000 FC` (`economy_healthy: true`)

## 2. Extrait de la Table d'Équilibrage (`economy-balance-sheet.csv`)
| ID Entité | Type | Flux | Valeur de Base (FC) | Modificateur Réputation (`SYS-WLD-REPUTATION`) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `MSN-MAIN-001-ARRIVEE` | `MISSION` | `FAUCET` | `15 000 FC` | Fixe (`1.0x`) | Capital initial débloquant l'atelier `FAM-KABONGO`. |
| `MSN-SIDE-014-WEWA` | `MISSION` | `FAUCET` | `6 500 FC` | `+20 %` si livraison sans collision | Course express à `DST-MATONGE`. |
| `ITM-WPN-MACHETTE` | `ITEM` | `SINK` | `8 500 FC` | `0.85x` à Kalamu (allié) | Forge et équilibrage lame renforcée. |
| `ITM-DOC-PASSEPORT` | `ITEM` | `SINK` | `5 000 FC` | `1.25x` à la Gombe | Renouvellement falsifié du laissez-passer ONATRA. |
