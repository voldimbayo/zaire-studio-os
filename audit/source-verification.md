# Vérification des Sources & Niveau Réel de Preuve (`source-verification.md`)

- **Date de Révision** : `2026-11-26`
- **Registre Audité** : [research/source-registry.csv](file:///C:/Users/Voldi%20Otk/Desktop/zaire-studio-os/research/source-registry.csv) (**35 sources** : `SRC-001` à `SRC-035`)
- **Classification Globale des Sources** : **`PARTIAL`** (0 source inventée ; documentation officielle moteur et standard XAG vérifiés via web ; ouvrages papier cités à titre bibliographique sans lecture du texte intégral en session).

---

## 1. Taxonomie Honnête des Statuts de Vérification dans `source-registry.csv`

Afin d'éliminer toute sur-déclaration (aucun livre non lu en texte intégral ne doit être qualifié simplement de « Vérifiée »), chaque entrée porte désormais l'un des statuts exacts suivants :

1. **`Vérifiée via Recherche Web (Documentation Officielle / Microsoft Learn)`** (`SRC-031` à `SRC-035`) :
   - `SRC-031` (**Microsoft XAG**) : Vérifié sur Microsoft Learn — XAG 101 (*Text Display*), XAG 102 (*Contrast & Color Independence*), XAG 104 (*Subtitles & Captions*), XAG 107 (*Input*). *(Note : une confusion antérieure dans PRD-06 attribuant l'indépendance couleur à XAG 102 seul ou fusionnant 101/102 a été clarifiée).*
   - `SRC-032` (**UE 5.8 MegaLights**) : Vérifié — système d'éclairage direct stochastique passé d'expérimental (5.5) au statut production en UE 5.8, requérant le support Hardware Ray Tracing (ou chemin supporté).
   - `SRC-033` (**UE Mutable Plugin**) : Vérifié — génération runtime de Skeletal Meshes/textures modulaires, suppression des faces cachées et fusion de matériaux.
   - `SRC-034` (**UE AnimNext / UAF**) : Vérifié — nouveau framework d'animation orienté données (traits/graphes), **toujours exposé principalement via des modules C++/Python expérimentaux** (ne doit pas remplacer `Pose Search` sans prototype).
   - `SRC-035` (**SideFX Houdini Copernicus & APEX**) : Vérifié — **Copernicus (COP)** a été introduit en Beta dans Houdini 20.5 puis étendu en 21 et 22 (remplaçant COP2, et non appelé « Copernicus 2.0 » dans la nomenclature officielle SideFX), tandis qu'**APEX** assure l'évaluation procédurale de graphes et le rigging KineFX.
2. **`Consultée (Extrait/Index)`** (`SRC-001` à `SRC-007`, `SRC-009` à `SRC-013`, `SRC-016` à `SRC-019`) :
   - Pages de documentation et résumés techniques consultés en Phase 1.
3. **`Métadonnées Vérifiées via Recherche Web (Texte intégral non consulté)`** (`SRC-021`) :
   - Filip De Boeck & Marie-Françoise Plissart, *Kinshasa: Tales of the Invisible City* (Ludion 2004, ISBN `9789055445288` ; rééd. Leuven University Press 2014, ISBN `9789058679673`).
4. **`Référence Bibliographique (Texte intégral non consulté en session)`** (`SRC-020`, `SRC-022` à `SRC-030`) :
   - Ouvrages classiques de l'industrie (Gregory, Heussner, Totten, Adams & Dormans, Swink, Hodent, Farnell, Phillips, O'Hagan & Mangiron, Bhatti) dont l'existence et la pertinence méthodologique sont établies, mais dont les pages n'ont pas été inspectées en session.
5. **`Repérée (Index secondaire / Annonce — Texte intégral non consulté)`** (`SRC-008`, `SRC-014`, `SRC-015`) :
   - Conférences GDC derrière le paywall GDC Vault documentées uniquement via index public ou annonce officielle GDC.
