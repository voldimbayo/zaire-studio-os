# Exemple `ART-03` — Spécification de `CHR-PROTAG-KOFFI` & Kit Foule `NPC-KIT-MATONGE`

- **ID Personnage / Kit Foule** : `CHR-PROTAG-KOFFI` & `NPC-KIT-MATONGE`
- **Commune / Faction** : `DST-KALAMU` / `DST-MATONGE`
- **Squelette Cible** : `SK_Zaire_Master_Humanoid`
- **Statut** : `CONFIRMED`

## 1. Budgets Géométriques, Textures & Groom (`CHR-PROTAG-KOFFI`)
- **Polycount (LOD 0 / LOD 1 / LOD 2)** : `82 000 / 40 000 / 16 500 triangles`.
- **Calibration Shader Peau** : Albédo `62 sRGB` (sous-ton chaud cuivré), Dual Specular `0.26 / 0.44` avec Micro-Normal Map pores `4K` et masque de sueur progressif piloté par l'effort/météo.
- **Stratégie Cheveux** : Coupe courte texturée avec dégradé net en Hair Cards haute densité dès le LOD 0 gameplay (`3 800 tris`), zéro surcoût Groom Strands en monde ouvert.

## 2. Table des Slots Modulaires & Variations (`NPC-KIT-MATONGE` pour `AI-02`)
| Slot Modulaire | Nombre de Variantes Mesh | Atlas / Palette Shader | Budget VRAM |
| :--- | :--- | :--- | :--- |
| `Head_Sculpts` | `12 visages distincts` | 3 nuances de carnation SSS + pilosité/maquillage | `140 MB` |
| `Hair_Headgear` | `14 (Tresses, locks, bérets, casques Wewa)` | Hair Cards alpha-to-coverage | `95 MB` |
| `UpperBody_Tops` | `16 (Chemises wax, polos, vestes Sapeurs)` | Motifs procéduraux par index `CustomPrimitiveData` | `210 MB` |
| `LowerBody_Pants` | `12 (Pantalons toile, jeans, jupes pagnes)` | Variations teintes/usure latérite RVT | `135 MB` |
