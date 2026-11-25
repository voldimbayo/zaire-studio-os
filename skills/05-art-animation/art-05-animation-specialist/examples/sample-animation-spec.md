# Exemple `ART-05` — Animation Blueprint de `CHR-PROTAG-KOFFI` (Parkour & Machette)

- **Cible Squelette** : `SK_Zaire_Master_Humanoid` (`CHR-PROTAG-KOFFI`)
- **Budget CPU Max (`PERF-CPU-ANIM`)** : `1.42 ms` mesuré (`<= 1.8 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Configuration Motion Matching & Motion Warping
- **Pose Search Channels** : `PSD_Koffi_Locomotion` indexant 140 clips nettoyés (`ART-06`) sur trajectoire `-0.2s, +0.2s, +0.4s, +0.6s`, vitesse du bassin et phase de contact des pieds.
- **Cibles Motion Warping (`WLD-05`)** :
  - `WarpTarget_VaultApex` : Verrouille la main gauche sur l'arête supérieure des caisses de `100 cm` (`[90, 110] cm`) entre les frames `8` et `16`.
  - `WarpTarget_MotoMount` : Aligne le bassin sur la selle de `VEH-MOTO-WEWA-01` depuis n'importe quel angle d'approche (`180°` gauche/droite/arrière).

## 2. Synchronisation Frame Data Combat (`GD-05`)
| Montage Asset | Gameplay Tag | Startup (`f`) | Active Hitbox (`ANS_`) | Recovery / Cancel (`f`) |
| :--- | :--- | :--- | :--- | :--- |
| `AM_Machete_Light_01` | `Ability.Melee.LightAttack` | `f01 - f12` | `f13 - f17` (`ANS_MacheteTrace`) | `f18 - f31` (`Cancel dès f20`) |
| `AM_Machete_Heavy_01` | `Ability.Melee.HeavyAttack` | `f01 - f24` | `f25 - f30` (`ANS_HeavyGuardBreak`) | `f31 - f50` |
| `AM_Machete_Parry_01` | `State.Character.Combat.Parrying` | `f01 - f03` | `f04 - f15` (`ANS_ParryDeflect`) | `f16 - f25` |
