# Spécification Simulation Physique Chaos (`ENG-05`)

- **Système** : `SYS-PHYS-CHAOS`
- **Cible Physique** : `[VEH-* / Props Destructibles / Ragdoll]`
- **Budget CPU Max (`PERF-CPU-CHAOS`)** : `<= 1.5 ms`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Paramètres du Solveur Chaos & Async Tick
- **Fréquence Async Tick** : `60 Hz (16.66 ms pas fixe)`
- **Iterations Solveur (Position / Velocity)** : `[8 / 2]`
- **Seuils de Mise en Sommeil (Linear / Angular Sleep)** : `[Valeurs]`

## 2. Règles de Collision & Destruction (`Geometry Collection`)
- **Primitives autorisées** : `[Box / Sphere / Capsule / Convex <= 18]`
- **Politique de recyclage des débris** : `[Sleep <= 1.2s, Cull <= 4.0s]`

## Contraintes Studio & Validation Pré-Handoff (`ENG-05`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-07, PRD-05, GD-06`
