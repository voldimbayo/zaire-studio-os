# Exemple `AUD-03` — Score Interactif `MSN-MAIN-001-ARRIVEE` & Grille `ORG-RADIO-KIN`

## 1. Score Adaptatif de `LOC-GOMBE-PORT` (`MUS_SCORE_PORT_STEALTH_01`)
- **Tempo & Signature** : `98 BPM`, `4/4` (Grid Wwise synchronisée à la double-croche).
- **Couches Actives par Phase de `MSN-MAIN-001-ARRIVEE`** :
  1. *Approche en barge & Quai (`State.Character.Stealth.Disguised`)* : Nappe grave analogique + percussions bois *lokole* feutrées (`Stem 1 + Stem 2 à -6 dB`).
  2. *Infiltration Hangar N°4 (`State.Character.Stealth.Concealed`)* : Entrée d'une basse fretless syncopée sur la mesure suivante (`Next Bar`).
  3. *Combat ou Exfiltration en `VEH-MOTO-WEWA-01`* : Déclenchement sur le temps suivant (`Next Beat`) de la guitare sébène électrique rapide et des cuivres (`Stem 3 + Stem 4`).

## 2. Programmation `ORG-RADIO-KIN` & Conformité Streamer Safe
- Chaque piste `LICENSED_THIRD_PARTY` pointe vers une composition originale `STUDIO_ORIGINAL` (`MUS_RAD_LOKOLE_RUMBA_01`) activée instantanément lorsque `SW_Music_LicenseMode = STREAMER_SAFE`.
