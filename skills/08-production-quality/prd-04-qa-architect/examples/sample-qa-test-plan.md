# Exemple `PRD-04` — Plan de Test QA `QATP-MSN-001-PORT` (`MSN-MAIN-001-ARRIVEE`)

- **ID Plan de Test** : `QATP-MSN-001-PORT`
- **Cible Testée** : `MSN-MAIN-001-ARRIVEE` & `LOC-GOMBE-PORT` (`DST-GOMBE`)
- **Cellules World Partition Couvertes** : `Grid_X04_Y08` à `Grid_X10_Y12` (transition `DST-GOMBE` -> `DST-KALAMU`)
- **Taux de Reproductibilité Exigé** : `96 %` mesuré (`>= 90 %` requis)
- **Statut** : `CONFIRMED`

## 1. Matrice de Couverture Fonctionnelle & Destructive
| Test Case ID | Catégorie | Action Testeur / Perturbation | Résultat Attendu | Automatisation (`PRD-05`) |
| :--- | :--- | :--- | :--- | :--- |
| `TC-MSN001-01` | `NOMINAL` | Infiltration sociale avec `ITM-DOC-PASSEPORT` jusqu'au coffre du hangar N°4. | Tag `State.Character.Stealth.Disguised` reconnu par `AI-01`, bark `BRK-PORT-01` joué, 0 alerte. | `Oui (Functional Test)` |
| `TC-MSN001-02` | `DESTRUCTIVE` | Déclencher le combat à la machette (`ITM-WPN-MACHETTE`) au milieu du dialogue `DLG-MSN-001-PORT`. | Handler `on_combat_triggered` exécuté, coffre de quête toujours interactif après le combat. | `Oui (Functional Test)` |
| `TC-MSN001-03` | `DESTRUCTIVE` | Détruire la `VEH-MOTO-WEWA-01` de la rampe est avant l'étape d'exfiltration `ST-03`. | Apparition validée des Wewa de secours à la sortie du port + objectif réalisable en `VEH-TAXI-JAUNE-01` (**0 Soft-Lock**). | `Oui (Gauntlet)` |
| `TC-MSN001-04` | `BOUNDARY` | Franchir la frontière `DST-GOMBE` -> `DST-KALAMU` à `95 km/h` sous `World.Weather.TropicalStorm`. | Déchargement de `DL_MSN001_SyndicateAlert` sans hitch (`P99 <= 16.6 ms`). | `Oui (Gauntlet Perf Bot)` |
