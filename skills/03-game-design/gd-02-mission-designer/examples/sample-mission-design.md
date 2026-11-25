# Exemple `GD-02` — Mission Design de `MSN-MAIN-001-ARRIVEE` (L'Accostage de l'Aube)

- **ID Mission** : `MSN-MAIN-001-ARRIVEE`
- **Titre** : L'Accostage de l'Aube
- **Lieu & Commune** : `LOC-GOMBE-PORT` (`DST-GOMBE`) -> `DST-KALAMU`
- **Plafond PNJ `AI-01` Actifs** : `16 gardes ORG-CARTEL-FLEUVE` (+ 40 dockers `AI-02` Mass Crowd)
- **Statut** : `CONFIRMED`

## 1. Approches Tactiques Multiples
- **Approche A (Social & Furtivité `SYS-STEALTH`)** : Présenter `ITM-DOC-PASSEPORT` au poste sud (`State.Character.Stealth.Disguised`), traverser le hangar N°4 en évitant les chefs d'équipe et récupérer le manifeste de saisie de `FAM-KABONGO`.
- **Approche B (Verticalité & Mêlée `SYS-CMB-MELEE`)** : Escalader la grue ouest (`+400 cm`), neutraliser les 2 guetteurs à la machette (`ITM-WPN-MACHETTE`) et descendre par la verrière du bureau.
- **Approche C (Exfiltration Véhiculaire `VEH-MOTO-WEWA-01`)** : Rejoindre la moto Wewa sur la rampe est et semer les patrouilles sur le Boulevard du 30 Juin (`LOC-GOMBE-BD30JUIN`) jusqu'à Kalamu.

## 2. Machine à États & Protection Anti-Soft-Lock
| Étape ID | Objectif Joueur | Condition Transition Succès | Handler Anti-Soft-Lock |
| :--- | :--- | :--- | :--- |
| `ST-01` | Pénétrer dans le hangar N°4 de `LOC-GOMBE-PORT` | Entrée dans le volume `VOL_Hangar4_Interior` | Si `ITM-DOC-PASSEPORT` est compromis, bascule automatique sur l'objectif d'accès par la grue ouest ou brèche latérale. |
| `ST-02` | Récupérer le registre de saisie `FAM-KABONGO` | Interaction avec le coffre `OBJ_Manifest_Safe` | Si combat engagé (`State.Character.Combat.Engaged`), le coffre reste ouvrable après neutralisation des 3 gardes proches. |
| `ST-03` | S'exfiltrer vers l'atelier de `DST-KALAMU` | Atteindre `DST-KALAMU` hors état d'alerte | Si la `VEH-MOTO-WEWA-01` initiale est détruite, 2 motos coursiers supplémentaires circulent à la sortie du port + possibilité de monter dans un taxi `VEH-TAXI-JAUNE-01`. |
