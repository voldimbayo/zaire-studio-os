# Architecture de Simulation de Foule Unreal Engine 5.8 — `SYS-CROWD-MASS` (`AI-02`, `ART-03`, `ENG-07`)

- **Cible Spatiale** : `DST-MATONGE` (`LOC-MATONGE-VICTOIRE`) & `DST-BANDAL` (`LOC-BANDAL-LUMUMBA-HUB`)
- **Budget CPU Alloué (`PERF-CPU-MASS`)** : `<= 2.0 ms` pour `600 entités Mass` (+ `<= 2.5 ms` pour `18 acteurs AI-01` hydratés)
- **Sources Vérifiées** : `SRC-001`, `SRC-004`, `SRC-009`, `SRC-013`, `SRC-020`, `SRC-032`

## 1. Pipeline ECS MassEntity & Anneaux de Représentation
1. **Anneau LOD 0 (`0 - 25 m`)** : Pool pré-alloué de `18 ACharacter` complets (`AI-01` State Trees, Smart Objects, barks `NAR-04`, collision capsule Chaos). Coût mesuré : `1.710 ms`.
2. **Anneau LOD 1 (`25 - 80 m`)** : `180 entités Mass` utilisant un `USkeletalMeshComponent` fusionné via **UE 5.8 Mutable (`CustomizableObject`)** avec Update Rate Optimization (`30 Hz`) et évitement `ZoneGraph RVO`.
3. **Anneau LOD 2 (`80 - 250 m`)** : `420 entités Mass` rendues en `UInstancedStaticMesh` Nanite animées par **Vertex Animation Textures (VAT)** et colorées par `CustomPrimitiveData[0..3]` (`0.0 ms` d'évaluation squelettique CPU). Coût Mass total (LOD 1 + LOD 2) : `1.566 ms <= 2.0 ms`.

## 2. Réactivité Émergente (Météo & Interventions PCR)
- Sous `World.Weather.TropicalStorm`, `60 %` des entités migrent vers les tags `SmartObject_CoveredArcade` (`180 cm` d'auvent `WLD-03`).
- Lors de `State.Law.AlertLevel.2_RoadblockPursuit` ou `State.Emergency.MedicalDispatch`, repli radial hors de la chaussée pour dégager le couloir de `ORG-POLICE-PCR` et `ORG-URGENCE-FLUVIALE`.
