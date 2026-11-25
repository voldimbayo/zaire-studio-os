# Exemple `PRD-02` — Registre des Risques Critiques & Plans de Contingence

## 1. Risques Critiques Traités (`Score >= 12/25`)
| ID Risque | Catégorie | Description | $P 	imes I$ | Score | Skill Owner | Plan de Mitigation & Fallback Actif |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `RSK-LEGL-003` | `LEGAL / AUDIO` | Revendications DMCA sur les streams utilisant la radio `ORG-RADIO-KIN`. | `4 × 4` | **16/25** | `AUD-03` | Switch Wwise `SW_Music_LicenseMode = STREAMER_SAFE` remplaçant 100 % des titres tiers par les rumbas originales du studio. |
| `RSK-TECH-001` | `PERFORMANCE` | Cumul de coût GPU Lumen + Niagara Pluie + 600 PNJ à `DST-MATONGE`. | `3 × 5` | **15/25** | `ENG-07` | Sous `World.Weather.TropicalStorm`, `AI-02` abrite 60 % des piétons sous les galeries (réduisant le coût CPU/GPU tout en augmentant le réalisme). |
| `RSK-DATA-002` | `WORLD / GIS` | Ruelles secondaires de `DST-MASINA` peu détaillées dans OpenStreetMap. | `4 × 3` | **12/25** | `WLD-03` | Maintien de `DST-MASINA` en `RESEARCH_REQUIRED` hors du Vertical Slice (`DIR-02`) et règles de subdivision d'îlots `ENG-04`. |
