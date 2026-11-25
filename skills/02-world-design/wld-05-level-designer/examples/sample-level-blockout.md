# Exemple `WLD-05` — Blockout `BLK-GOMBE-PORT-01` (`LOC-GOMBE-PORT`)

- **ID Blockout** : `BLK-GOMBE-PORT-01`
- **Lieu & Mission** : `LOC-GOMBE-PORT` | `MSN-MAIN-001-ARRIVEE`
- **Validation Script Métriques** : `PASS (check_spatial_metrics.py)`
- **Statut Blockout** : `APPROVED_FOR_ENV_ART`

## 1. Relevé des Métriques Spatiales (en cm UE5)
- **Largeur minimale couloir** : `400 cm` entre les rangées de conteneurs ISO.
- **Hauteur sous plafond minimale** : `360 cm` dans les bureaux de douane ; `900 cm` sous la charpente du hangar N°4.
- **Couverts Bas / Hauts** : Caisses de fret standardisées à `100 cm` ; conteneurs et piliers béton à `240 cm`.
- **Couloir exfiltration Wewa** : `150 cm` garantis le long de la rampe de chargement est jusqu'au Boulevard du 30 Juin.

## 2. Topologie des Parcours & Approches (`GD-02`)
- **Voie A (Social / Disguise)** : Entrée principale sud via la guérite douanière (utilise `ITM-DOC-PASSEPORT` + tag `State.Character.Stealth.Disguised`).
- **Voie B (Parkour / Infiltration)** : Échelle de grue à l'ouest -> passerelle suspendue (`hauteur +400 cm`) -> saut d'accroche (`280 cm`) sur le toit des conteneurs.
- **Voie C (Combat & Fuite)** : Cour centrale de déchargement (`1200 cm × 1800 cm`) offrant 6 couverts bas et un accès direct à la moto `VEH-MOTO-WEWA-01` garée sous l'auvent.
