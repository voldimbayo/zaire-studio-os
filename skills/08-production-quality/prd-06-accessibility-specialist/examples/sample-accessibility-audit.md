# Exemple `PRD-06` — Rapport d'Audit XAG du Vertical Slice (`MSN-MAIN-001-ARRIVEE`)

## 1. Exécution du Validateur (`scripts/check_xag_compliance.py`)
- **Cible Auditée** : `UI-HUD-MAIN-OVERLAY`, `DLG-MSN-001-PORT`, `SYS-CMB-MELEE`, `VEH-MOTO-WEWA-01`
- **Résultat Script** : `PASS (100 % conforme aux normes XAG)`

## 2. Synthèse de Conformité par Pilier (`xag-compliance-matrix.csv`)
| Code XAG | Pilier | Vérification sur le Vertical Slice Kinshasa | Statut |
| :--- | :--- | :--- | :--- |
| **XAG 101** | Visuel & Typographie | Contraste mesuré à `7.2:1` sous le soleil équatorial de midi (`EV100 = 15`). Rendu parfait des glyphes `Kɛbá!` et `Tɔ́kɛndɛ́` jusqu'à `+38 %` d'expansion. | **CONFORME** |
| **XAG 102** | Double Codage | Les jauges de vigilance des gardes de `LOC-GOMBE-PORT` combinent couleur, forme géométrique (cercle/triangle/losange) et motif hachuré. | **CONFORME** |
| **XAG 104** | Sous-titres & Radar Audio | Format `[AMINA] : « Kɛbá Koffi... »` sur fond noir `78 %` d'opacité + arc visuel directionnel lors des attaques lourdes `ENM-CARTEL-BRUTE`. | **CONFORME** |
| **XAG 107** | Moteur & Contrôles | Remapping complet clavier/manette via `Enhanced Input`, maintien continu (`Hold`) sur les prises de mêlée et assistance de trajectoire optionnelle en `VEH-MOTO-WEWA-01`. | **CONFORME** |
