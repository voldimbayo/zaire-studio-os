# Exemple `AI-01` — Architecture IA des Gardes Portuaires (`ORG-CARTEL-FLEUVE`)

- **ID Profil IA** : `AI-PRF-PORT-GUARD`
- **Archétypes Associés (`GD-05`)** : `ENM-PORT-VIGILE` (1 jeton), `ENM-CARTEL-BRUTE` (2 jetons)
- **Plafond Acteurs Simultanés** : `16 gardes` dans `LOC-GOMBE-PORT`
- **Budget CPU Alloué** : `1.65 ms` mesuré (`<= 2.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Hiérarchie UE5 State Tree
| État State Tree | Condition d'Entrée | Tâches & Smart Objects | Bark Associé (`NAR-04`) |
| :--- | :--- | :--- | :--- |
| `ST_Dock_Duty` | Alerte = 0 | Inspecte les caisses `KIT-CARGO-CRATE-100`, s'abrite sous le hangar si `World.Weather.TropicalStorm`. | `BRK-PORT-01` |
| `ST_Verify_Pass` | Voit Koffi avec `State.Character.Stealth.Disguised` à `< 500 cm` | Interpelle le joueur pendant `3.0 s` sans dégainer. | `BRK-PORT-01` |
| `ST_Combat_Engage` | Tag `State.Character.Combat.Engaged` | Demande un Attack Token ; si accordé, engage au corps-à-corps ; sinon encercle à `450 cm`. | `BRK-PORT-02` |

## 2. Configuration des Requêtes EQS & Attack Tokens
- **Requête EQS (`EQS_FindPortCover`)** : Grille `1600 cm × 1600 cm`, pas de `150 cm`, filtre par distance d'abord puis test de ligne de vue vers `CHR-PROTAG-KOFFI` sur les conteneurs (`240 cm`) et caisses (`100 cm`).
- **Gestion des Attack Tokens (`GD-05`)** : Jeton relâché immédiatement dès l'entrée en phase `Recovery` de l'attaque ou sur parade réussie (`State.Character.Combat.Parrying`).
