# Fiche d'Indexation & Traçabilité Registre (`PRD-03`)

- **Lot Documentaire Audité** : `[Task ID / Handoff Packet]`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`
- **Statut d'Indexation** : `READY_FOR_DIR06_PROMOTION` | `REJECTED_PHANTOM_ID`

## 1. Entrées Formatées pour `knowledge/entities-registry.csv`
```csv
id,category,name,district_id,status,owner_skill,validated_by,dependencies,sources,last_updated,summary
```

## 2. Contrôle des Références & Sources (`SRC-*`)
- **IDs Vérifiés** : `[Liste]`
- **Sources Rattachées** : `[SRC-*]`

## Contraintes Studio & Validation Pré-Handoff (`PRD-03`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-06, DIR-01`
