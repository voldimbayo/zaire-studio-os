# ADR-TECH-NNN : [Titre de la Décision d'Architecture UE5]

- **Statut** : `PROPOSED` | `CONFIRMED`
- **Autorité** : `DIR-04 (Technical Director)`
- **Sous-systèmes Impactés** : `[PERF-CPU-* / PERF-GPU-* / SYS-*]`

## 1. Problématique & Contrainte Budgétaire
`[Description de la contrainte technique et de l'enveloppe ms/MB]`

## 2. Architecture Retenue
`[Spécification précise UE5 / Houdini / Wwise]`

## 3. Seuils de Validation (`ENG-07` / `PRD-05`)
- **Budget CPU max** : `[X.X ms]`
- **Budget GPU max** : `[Y.Y ms]`
- **Budget VRAM max** : `[Z MB]`

## Contraintes Studio & Validation Pré-Handoff (`DIR-04`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `ENG-07, DIR-07`
