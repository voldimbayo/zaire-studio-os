# Spécification d'Outil Éditeur & Validateur UE5 (`ENG-03`)

- **Nom du Validateur / Outil** : `UZaire...Validator` | `EUW_Zaire_...`
- **Module Cible** : `ZaireEditor (Type: Editor)`
- **Règles Métier Appliquées** : `[ART-04 / ENG-01 / WLD-05]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Logique de Validation & Auto-Fix
- **Condition d'Activation (`CanValidateAsset`)** : `[Classes UObject ciblées]`
- **Contrôles Exécutés (`ValidateLoadedAsset`)** : `[Règles déterministes]`
- **Action Auto-Fix Disponible** : `[Correction automatique proposée]`

## Contraintes Studio & Validation Pré-Handoff (`ENG-03`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-04, ART-04, ENG-01`
