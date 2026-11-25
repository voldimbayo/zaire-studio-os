# Profil de Commune — World Bible (`WLD-01`)

- **ID Registre** : `DST-[COMMUNE]`
- **Nom de la Commune** : `[Nom]`
- **Gameplay Tag Associé** : `World.District.[Nom]`
- **Statut** : `CONFIRMED` | `PROPOSED` | `RESEARCH_REQUIRED`

## 1. Identité Socio-Économique & Factions
- **Profil Social & Activités** : `[Description]`
- **Factions Dominantes (`ORG-*`)** : `[Liste]`
- **Landmark Directeur (`LOC-*`)** : `LOC-...`

## 2. Paramètres de Simulation & Ambiance
- **Densité Foule (`AI-02`)** : `[Jour / Nuit]`
- **Profil Trafic (`AI-03`)** : `[Types de véhicules VEH-*]`
- **Signature Visuelle (`ART-01`) & Sonore (`AUD-01`)** : `[Synthèse]`

## Contraintes Studio & Validation Pré-Handoff (`WLD-01`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `WLD-02, WLD-03, DIR-03`
