# Exemple `ART-06` — Shotlist MoCap & Protocole Retargeting Acte I

## 1. Extrait de la Shotlist Validée (`mocap-shotlist.csv`)
| Take ID | Catégorie | Personnage | Description Action | Praticables Plateau (cm) | Frames (60fps) | Capture Faciale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `MCP_CMB_KOFFI_MACHETE_L01` | `COMBAT` | `CHR-PROTAG-KOFFI` | Taille rapide machette (`Startup 12f / Active 5f / Recovery 14f`) | Machette factice `65 cm` | `31 f` | Non |
| `MCP_LOC_KOFFI_VAULT_100` | `PARKOUR` | `CHR-PROTAG-KOFFI` | Franchissement rapide caisse portuaire | Module bois `H = 100 cm` | `33 f` | Non |
| `MCP_VEH_KOFFI_WEWA_MOUNT` | `VEHICLE` | `CHR-PROTAG-KOFFI` | Enjambement rapide et démarrage au kick | Gabarit `VEH-MOTO-WEWA-01` (`Selle 78 cm`) | `45 f` | Non |
| `MCP_CIN_MSN001_ARRIVEE_01` | `CINEMATIC` | `CHR-PROTAG-KOFFI` | Accostage au quai N°4 et dialogue radio avec Amina | Quai `H = 90 cm` | `600 f (10s)` | Oui (`MetaHuman Animator` 60fps) |

## 2. Contrôle Qualité Retargeting (`IKRT_Zaire_Humanoid`)
- **Chaînes IK Verrouillées (100 % FK/IK Blend)** : `LeftFoot_IK`, `RightFoot_IK`, `LeftHand_WeaponSocket`, `RightHand_WeaponSocket` (aucun décalage sur le guidon de la Wewa ni sur l'arête de `100 cm`).
