# Limitations Connues, Composants Non Testés & Décisions Humaines Requises (`known-limitations.md`)

Conformément aux exigences d'intégrité d'audit (Phase 4), ce document recense sans omission les composants classés **`NOT TESTED`** dans l'environnement d'exécution actuel, les limitations techniques intrinsèques et les décisions relevant d'un arbitrage humain.

---

## 1. Composants Classés `NOT TESTED` (Exécution Binaire Moteur Externe)

Bien que 100 % des scripts Python, schémas JSON, tables CSV et contrats C++/HDA/Wwise de **ZAÏRE STUDIO OS** aient été exécutés et validés (`PASS`), les opérations binaires suivantes sont classées **`NOT TESTED`** car les exécutables tiers propriétaires ne sont pas installés dans l'environnement d'audit :

| Composant / Pipeline | Skill(s) Associé(s) | Statut Audit | Raison Factuelle & Prérequis d'Exécution |
| :--- | :--- | :--- | :--- |
| **Compilation C++20 par UnrealBuildTool (UBT)** | `ENG-01`, `ENG-02`, `ENG-03` | **`NOT TESTED`** | Les en-têtes et contrats C++20 (`UZaireDistrictStreamingSubsystem`, `UZaireGA_MeleeParry`, `UZaireNaniteAndTextureValidator`) sont syntaxiquement vérifiés mais nécessitent une installation locale d'**Unreal Engine 5.4/5.5+** et **Visual Studio 2022 / MSVC** pour produire les binaires `.dll`/`.exe`. |
| **Cuisson Géométrique SideFX Houdini (`hython` / PDG)** | `ENG-04` | **`NOT TESTED`** | La spécification HDA/PCG (`HDA_Zaire_UrbanBlock_Gen`) est complète mais sa cuisson géométrique réelle requiert une licence **SideFX Houdini 20.5+** et le plugin **Houdini Engine for UE5**. |
| **Génération des SoundBanks Binaires Wwise (`.bnk` / `.wem`)** | `AUD-01`, `AUD-02`, `AUD-03` | **`NOT TESTED`** | L'architecture des bus HDR, RTPC et Stems interactifs est spécifiée, mais la génération des fichiers audio binaires requiert **Audiokinetic Wwise Authoring CLI**. |
| **Exécution Runtime d'Unreal Gauntlet & Captures GPU RenderDoc** | `ENG-06`, `ENG-07`, `PRD-05` | **`NOT TESTED`** | Le script `check_perf_budget.py` audite avec succès les profils JSON de frametime P99 (`<= 16.6 ms`), mais la capture GPU live nécessite un build client UE5 exécuté sur GPU DX12/Vulkan cible. |

---

## 2. Limitations Documentaires et Techniques Connues (Héritées de `research/research-gaps.md`)

1. **Hétérogénéité des données OpenStreetMap (OSM) sur les communes périphériques (`DST-MASINA`)** :
   - Les grands axes de `DST-GOMBE`, `DST-MATONGE`, `DST-LIMETE` et `DST-KALAMU` sont bien couverts, mais les ruelles tertiaires de `DST-MASINA` restent partielles.
   - *Mitigation active* : `DST-MASINA` est verrouillé au statut `RESEARCH_REQUIRED` dans `knowledge/entities-registry.csv` et exclu du jalon Vertical Slice (`DIR-02` / `PRD-02` `RSK-DATA-002`).
2. **Adaptation sur mesure de `MassTraffic` pour le slalom des motos-taxis Wewa (`AI-03`)** :
   - Le plugin standard `MassTraffic` d'Epic Games (*City Sample*, `SRC-004`) est conçu pour des véhicules nord-américains respectant des voies strictes. Le système de sous-voies virtuelles inter-files (`130-150 cm`) spécifié dans `AI-03` et `ENG-04` devra faire l'objet d'un prototype C++ dédié lors de l'intégration moteur.
3. **Sources GDC Vault consultées par extraits/index (`SRC-008`, `SRC-014`, `SRC-020`)** :
   - Ces trois références sont clairement marquées `Repérée (À approfondir)` dans `research/source-registry.csv`.

---

## 3. Points Nécessitant une Décision Humaine (Gouvernance Studio)

Aucun blocage technique n'empêche la livraison de **ZAÏRE STUDIO OS v1.0.0**, mais les 3 décisions suivantes relèvent exclusivement de la direction humaine du studio :
1. **Validation Juridique & Licences Musicales Tiers (`AUD-03` / `PRD-02` `RSK-LEGL-003`)** : La signature des contrats de synchronisation avec les ayants droit de la rumba et du ndombolo pour `ORG-RADIO-KIN` doit être effectuée par la production humaine (le fallback technique `STREAMER_SAFE` 100 % original est déjà en place).
2. **Acquisition Terrain Audio & Photogrammétrie à Kinshasa (`WLD-02`, `ART-02`, `AUD-02`)** : Planification d'une campagne réelle d'enregistrement d'ambiances sonores et de références photographiques de façades à Kinshasa pour alimenter les banques de production.
3. **Validation par des Locuteurs Natifs Kinois (`WLD-02` / `AUD-04`)** : Relecture finale humaine par des consultants linguistiques de Kinshasa lors des sessions de doublage (`fr-CD` et `ln-CD`).
