# Exemple d'Exécution `DIR-01` — Mission d'Infiltration au Port ONATRA

## 1. Requête Utilisateur
> « Concevoir une mission d'infiltration nocturne dans les entrepôts du Port ONATRA à la Gombe avec exfiltration en moto Wewa. »

## 2. Sortie Générée (`execution-plan-dag.json`)
```json
{
  "orchestration_id": "ORC-2026-042",
  "user_intent": "Conception complète de la mission MSN-MAIN-002-ONATRA (Infiltration Port de Kinshasa + Fuite Wewa)",
  "referenced_entities": [
    {"id": "DST-GOMBE", "status": "CONFIRMED"},
    {"id": "LOC-GOMBE-PORT", "status": "CONFIRMED"},
    {"id": "CHR-PROTAG-KOFFI", "status": "CONFIRMED"},
    {"id": "ORG-CARTEL-FLEUVE", "status": "CONFIRMED"},
    {"id": "VEH-MOTO-WEWA-01", "status": "CONFIRMED"},
    {"id": "SYS-STEALTH", "status": "CONFIRMED"}
  ],
  "dag_waves": [
    {
      "wave_index": 1,
      "parallel_tasks": [
        {"task_id": "TSK-2026-101", "target_skill": "WLD-02", "objective": "Documenter le jargon portuaire lingala/français kinois des dockers ONATRA"},
        {"task_id": "TSK-2026-102", "target_skill": "WLD-03", "objective": "Spécifier la morphologie des quais, grues et dépôts de conteneurs de LOC-GOMBE-PORT"},
        {"task_id": "TSK-2026-103", "target_skill": "GD-06", "objective": "Calibrer l'adhérence de VEH-MOTO-WEWA-01 sur béton portuaire humide"}
      ]
    },
    {
      "wave_index": 2,
      "parallel_tasks": [
        {"task_id": "TSK-2026-104", "target_skill": "GD-02", "objective": "Concevoir la machine à états sans soft-lock de MSN-MAIN-002-ONATRA"},
        {"task_id": "TSK-2026-105", "target_skill": "NAR-02", "objective": "Rédiger le script dramatique et la beat sheet de la mission"}
      ]
    },
    {
      "wave_index": 3,
      "parallel_tasks": [
        {"task_id": "TSK-2026-106", "target_skill": "WLD-05", "objective": "Produire le blockout métrique (allées >= 350cm, couverts conteneurs 200cm)"},
        {"task_id": "TSK-2026-107", "target_skill": "NAR-04", "objective": "Rédiger les barks d'alerte en lingala/français des gardes ORG-CARTEL-FLEUVE"},
        {"task_id": "TSK-2026-108", "target_skill": "AI-01", "objective": "Configurer le State Tree de patrouille nocturne pour 18 gardes max"}
      ]
    },
    {
      "wave_index": 4,
      "parallel_tasks": [
        {"task_id": "TSK-2026-109", "target_skill": "NAR-06", "objective": "Auditer la continuité narrative avec MSN-MAIN-001-ARRIVEE"},
        {"task_id": "TSK-2026-110", "target_skill": "PRD-04", "objective": "Établir le plan de test QA d'infiltration et d'exfiltration"}
      ]
    }
  ],
  "final_status": "PROPOSED"
}
```
