# Spécification de Blockout Level Design (`WLD-05`)

- **ID Blockout** : `BLK-[LOC]-[NUM]`
- **Lieu & Mission** : `LOC-...` | `MSN-...`
- **Validation Script Métriques** : `PASS (check_spatial_metrics.py)`
- **Statut Blockout** : `PROPOSED_FOR_PLAYTEST` | `APPROVED_FOR_ENV_ART`

## 1. Relevé des Métriques Spatiales (en cm UE5)
- **Largeur minimale couloir** : `[>= 350 cm]`
- **Hauteur sous plafond minimale** : `[>= 320 cm]`
- **Couverts Bas / Hauts** : `[100 cm / >= 200 cm]`
- **Couloir exfiltration Wewa** : `[>= 130 cm]`

## 2. Topologie des Parcours & Approches (`GD-02`)
- **Voie A (Furtivité / Social)** : `[Cheminement & cônes de vue]`
- **Voie B (Verticalité / Parkour)** : `[Accroches 260-300 cm & Smart Links]`
- **Voie C (Mêlée / Exfiltration)** : `[Arènes >= 500 cm & sortie véhicule]`

## Contraintes Studio & Validation Pré-Handoff (`WLD-05`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, AI-01, WLD-06`
