# Spécification Audio Bible & Architecture Mixage (`AUD-01`)

- **Zone / Système** : `DST-...` | `SYS-...`
- **Budget RAM Audio Max** : `<= 512 MB`
- **Plafond Voix Physiques Wwise** : `<= 64 voix`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Signature Acoustique & Couches d'Ambiance
- **Fond Continu (Bed Quad/Ambisonic)** : `[Description]`
- **Ponctuels Spatialisés (3D One-Shots)** : `[Sources locales]`
- **Réverbération Spatiale (Wwise Late Reverb)** : `[RT60 & pré-délai]`

## 2. Règles de Mixage HDR & Ducking
- **Priorité Voix (`BUS_VO_Critical`)** : `[Règle d'atténuation]`
- **Signalétique Sonore Gameplay (`PRD-06` XAG)** : `[Indice audio distinctif]`

## Contraintes Studio & Validation Pré-Handoff (`AUD-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-03, DIR-04, ENG-07`
