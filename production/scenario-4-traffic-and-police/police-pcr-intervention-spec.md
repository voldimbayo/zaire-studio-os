# Spécification du Système de Circulation & Interventions Policières (`AI-03`, `AI-04`, `ENG-04`)

- **Systèmes** : `SYS-TRAFFIC-ZONE` & `SYS-LAW-ESCALATION`
- **Organisations** : `ORG-POLICE-PCR` (Police de Circulation Routière), `ORG-TRANSCO`, `ORG-URGENCE-FLUVIALE`
- **Véhicules** : `VEH-MOTO-WEWA-01`, `VEH-TAXI-JAUNE-01`, `VEH-BUS-TRANSCO-01`, `VEH-POLICE-PICKUP-01`
- **Dépendance Amont Critique** : `ENG-04` (Houdini HDA génère les splines `ZoneGraph` et les sous-voies inter-files de `150 cm` **avant** l'exécution d'`AI-03`).

## 1. Algorithme de Circulation & Slalom Wewa (`AI-03`)
- **Taxis Collectifs (`VEH-TAXI-JAUNE-01`)** : Déboîtement sur les encoches latérales (`220 cm`) pendant `8 s` devant les marchés de `DST-MATONGE` et `DST-BANDAL`.
- **Motos-Taxis (`VEH-MOTO-WEWA-01`)** : Dès que la vitesse moyenne d'une voie principale descend sous `20 km/h`, activation des sous-voies inter-files (`150 cm >= 130 cm`) à `35 km/h`.
- **Watchdog Anti-Deadlock** : Si un rond-point (`LOC-MATONGE-VICTOIRE` ou `LOC-BANDAL-LUMUMBA-HUB`) affiche une vitesse `< 2 km/h` pendant `8.0 s`, gel des entrées radiales pendant `4.0 s` et recyclage hors frustum (`> 115 m`).

## 2. Escalade Graduée `SYS-LAW-ESCALATION` (`ORG-POLICE-PCR`)
1. **Niveau 1 (`State.Law.AlertLevel.1_TrafficInfraction`)** : Agent PCR au carrefour (hydraté en `AI-01`), coup de sifflet (`AUD-02`), dialogue court (`NAR-04`). Si `SYS-WLD-REPUTATION >= 600` (*Enfant du Quartier*), simple avertissement verbal (`LEX-007 Kɛbá!`).
2. **Niveau 2 (`State.Law.AlertLevel.2_RoadblockPursuit`)** : Poursuite par 2 `VEH-POLICE-PICKUP-01` et chicane partielle au rond-point suivant (conservant une échappatoire Wewa de `150 cm` pour éviter tout soft-lock).
3. **Niveau 3 (`State.Law.AlertLevel.3_SectorLockdown`)** : Barrage complet des boulevards ; en cas de blessés civils, activation de `State.Emergency.MedicalDispatch` (`ORG-URGENCE-FLUVIALE`).
