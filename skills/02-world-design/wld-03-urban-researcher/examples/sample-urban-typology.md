# Exemple `WLD-03` — Typologie Urbaine de `DST-MATONGE` & `LOC-MATONGE-VICTOIRE`

- **Zone / Commune** : `DST-MATONGE` (`LOC-MATONGE-VICTOIRE`)
- **Code Typologie** : `TYP-MATONGE-COMM`
- **Statut Données SIG/OSM** : `CONFIRMED`

## 1. Règles Géométriques d'Îlots & Bâti (en cm UE5)
- **Dimensions moyennes d'îlot** : `8000 cm × 4500 cm` (`80 m × 45 m`), subdivisés en parcelles commerciales de `1200 cm` de façade.
- **Hauteur de bâti (Étages / cm)** : `1 à 3 étages` (`400 cm` au rez-de-chaussée commercial avec auvent en porte-à-faux de `180 cm`, `350 cm` aux étages supérieurs).
- **Matériaux dominants (`ART-02`)** : Béton peint patiné par l'humidité, enseignes métalliques peintes, toitures en tôle galvanisée ondulée, trottoirs bordés de terre rouge latéritique.

## 2. Profil de Voirie & Réseau (`ENG-04` / `AI-03`)
| Type de Voie | Nombre de Voies | Largeur par Voie (cm) | Trottoir (cm) | Véhicules Autorisés (`VEH-*`) |
| :--- | :--- | :--- | :--- | :--- |
| Anneau Rond-Point Victoire | 3 voies circulaires | `380 cm` | `500 cm` (avec étals) | `VEH-BUS-TRANSCO-01`, `VEH-TAXI-JAUNE-01`, `VEH-MOTO-WEWA-01` |
| Avenues Radiales Commerciales | 2 × 1 voie + bande arrêt | `350 cm` | `400 cm` | `VEH-TAXI-JAUNE-01`, `VEH-MOTO-WEWA-01` |
| Passages Piétons / Galeries | Voie partagée | `400 cm` | Sans bordure haute | Piétons `AI-02` + `VEH-MOTO-WEWA-01` à basse vitesse |
