# Spécification Système VFX Niagara (`ART-09`)

- **Nom Système Niagara** : `NS_[CAT]_[SLUG]`
- **Gameplay Tag Déclencheur** : `[World.Weather... / Ability.Melee...]`
- **Budget GPU Alloué** : `[<= X.XX ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture Émetteurs & Optimisation Overdraw
- **Mode de Simulation** : `GPU Compute` | `CPU Burst`
- **Collisions** : `Global Distance Field` | `Analytical Plane`
- **Cutout Geometry & Packing Texture** : `[8-verts Cutout / Texture RGBA]`
- **Distance de Culling & Max Instances (`UNiagaraEffectType`)** : `[XXXX cm | N instances]`

## Contraintes Studio & Validation Pré-Handoff (`ART-09`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-07, GD-05, ART-07`
