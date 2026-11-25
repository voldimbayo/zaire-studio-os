# Exemple `ENG-05` — Configuration Chaos pour `VEH-MOTO-WEWA-01` & Étals Destructibles

- **Système** : `SYS-PHYS-CHAOS`
- **Cible Physique** : `VEH-MOTO-WEWA-01` & `GC_Matonge_MarketStall_01`
- **Budget CPU Max (`PERF-CPU-CHAOS`)** : `1.18 ms` mesuré en collision de marché (`<= 1.5 ms` requis)
- **Statut** : `CONFIRMED`

## 1. Paramètres du Solveur Chaos & Async Tick
- **Fréquence Async Tick** : `60 Hz` asynchrone (`bTickPhysicsAsync = true`), interpolation lissée du châssis sur le Render Thread.
- **Suspension `VEH-MOTO-WEWA-01`** : `SphereCast` de rayon `32 cm` par roue (élimine les accrocs sur les bordures de caniveaux de `WLD-03`), ressort `Stiffness = 45.0`, `Damping = 6.8`.
- **Contrainte Anti-Retournement** : Couple angulaire de stabilisation latérale proportionnel à $(1 - \min(v / 35\text{ km/h}, 1))$ implémenté dans `FZaireMotoPhysicsSim`.

## 2. Règles de Collision & Destruction (`GC_Matonge_MarketStall_01`)
- **Fracturation** : 1 seul niveau de Voronoï (`14 fragments convexes`).
- **Profil Post-Rupture** : Bascule immédiate sur le profil `ChaosDebris` (ignore `Pawn`, `Camera` et les autres `ChaosDebris`), mise en sommeil forcée à `1.2 s` et disparition alpha-dithered à `3.5 s`.
