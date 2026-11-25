# Exemple `GD-05` — Spécification Combat `ITM-WPN-MACHETTE` & Vigiles `ORG-CARTEL-FLEUVE`

- **Système** : `SYS-CMB-MELEE`
- **Arme / Capacité Évaluée** : `ITM-WPN-MACHETTE` (`Ability.Melee.LightAttack`, `Ability.Melee.HeavyAttack`, `State.Character.Combat.Parrying`)
- **Plafond Attack Tokens Escouade** : `2 jetons simultanés max` (1 jeton en couloir `< 500 cm`)
- **Statut** : `CONFIRMED`

## 1. Table Frame Data (Base 60 FPS)
| Mouvement | Gameplay Tag | Startup (f) | Active (f) | Recovery (f) | Dégâts | Hitstop (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Taille Rapide Machette | `Ability.Melee.LightAttack` | `12 f` | `5 f` | `14 f` | `25` | `55 ms` |
| Fente Brise-Garde | `Ability.Melee.HeavyAttack` | `24 f` | `6 f` | `20 f` | `55` | `90 ms` |
| Parade Renforcée | `State.Character.Combat.Parrying` | `3 f` | `12 f` | `10 f` | `0 (+Stagger)` | `85 ms` |

## 2. Archétypes Ennemis & Comportement IA (`AI-01`)
| ID Archétype | Coût Attack Token | Santé (HP) | Pattern d'Attaque & Télégraphe | Contre Tactique Joueur |
| :--- | :--- | :--- | :--- | :--- |
| `ENM-PORT-VIGILE` | `1 jeton` | `100 HP` | Coup de matraque télégraphié (`24 frames / 400 ms` + bark `BRK-PORT-02`). | Parade `State.Character.Combat.Parrying` suivie d'une Taille Rapide. |
| `ENM-CARTEL-BRUTE` | `2 jetons` | `220 HP` | Charge lourde imblocable (`36 frames / 600 ms` + son métallique lourd `AUD-02`). | Esquive latérale obligatoire puis punition par `Ability.Melee.HeavyAttack`. |
