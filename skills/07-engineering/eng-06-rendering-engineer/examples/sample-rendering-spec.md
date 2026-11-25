# Exemple `ENG-06` — Pipeline Lumen/VSM Urbain & Shader d'Eau du Fleuve Congo

- **Passe Graphique / Feature** : `Lumen GI/Reflections`, `VSM Caching` & `Single Layer Water (Fleuve Congo)`
- **Budget GPU Mode Perf (60 FPS)** : `4.25 ms` (Lumen) + `2.20 ms` (Nanite/VSM) + `0.45 ms` (Fleuve)
- **Budget GPU Mode Qualité (30 FPS)** : `6.60 ms` (Lumen HW RT) + `3.50 ms` (Nanite/VSM)
- **Statut** : `CONFIRMED`

## 1. Configuration des Passes RHI & CVar
| CVar / Paramètre | Valeur Perf (60 FPS) | Valeur Qualité (30 FPS) | Justification Technique |
| :--- | :--- | :--- | :--- |
| `r.Lumen.HardwareRayTracing` | `0` | `1` | Le Software Ray Tracing sur Global Distance Field tient en `4.25 ms` dans `DST-MATONGE`. |
| `r.Lumen.Reflections.MaxRoughnessToTrace` | `0.40` | `0.55` | Concentre les rayons de réflexion sur les flaques de pluie, vitres de la Gombe et carrosseries. |
| `r.Shadow.Virtual.Cache.StaticSeparate` | `1` | `1` | Isole les ombres de l'architecture statique Nanite des acteurs mobiles `AI-02`/`AI-03`. |

## 2. Rendu du Fleuve Congo (`LOC-GOMBE-PORT` & `DST-NGALIEMA`)
- Utilisation du shading model **`SingleLayerWater`** avec diffusion anisotrope (`ScatteringCoefficients` brun-ocre du limon fluvial, profondeur de visibilité optique `85 cm`) et champ de vecteurs de courant (`FlowMap 2D`) ralentissant près des quais ONATRA et s'accélérant dans les rapides de Kinsuka.
