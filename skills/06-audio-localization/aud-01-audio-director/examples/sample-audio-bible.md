# Exemple `AUD-01` — Audio Bible de `DST-GOMBE` (`LOC-GOMBE-PORT`) vs `DST-MATONGE`

- **Zone / Système** : `LOC-GOMBE-PORT` & `LOC-MATONGE-VICTOIRE`
- **Budget RAM Audio Max** : `385 MB` alloués (`<= 512 MB` requis)
- **Plafond Voix Physiques Wwise** : `48 voix moyennes / 64 max`
- **Statut** : `CONFIRMED`

## 1. Signature Acoustique & Couches d'Ambiance
- **`LOC-GOMBE-PORT` (Quais ONATRA)** :
  - *Bed Ambisonic* : Courant grave du fleuve Congo (`LEX-005 Ebale`), clapotis contre les coques métalliques des barges.
  - *Ponctuels 3D* : Grincement des câbles de grues, choc sourd des conteneurs ISO, mouettes fluviales.
  - *Réverbération* : `RT60 = 2.4 s` à l'intérieur du hangar N°4 (réflexions métalliques franches).
- **`LOC-MATONGE-VICTOIRE`** :
  - *Bed Ambisonic* : Murmure polyphonique chaleureux de foule, circulation dense.
  - *Ponctuels 3D* : Appels de chauffeurs taxis, coups de klaxon codés de `VEH-MOTO-WEWA-01`, diffusion spatialisée de `ORG-RADIO-KIN` depuis les terrasses de ngandas.

## 2. Règles de Mixage HDR & Ducking
- **Priorité Voix (`BUS_VO_Critical`)** : Ducking immédiat de `-6.0 dB` sur les enceintes des ngandas de Matonge dès qu'un dialogue de quête (`NAR-04`) débute.
- **Signalétique Sonore Gameplay (`PRD-06` XAG)** : L'attaque lourde imblocable de `ENM-CARTEL-BRUTE` (`GD-05`) déclenche un sifflement métallique montant à `1.8 kHz` sur `BUS_SFX_CombatTelegraph`, identifiable même sans indice visuel.
