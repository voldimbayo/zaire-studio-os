# Exemple `PRD-03` — Indexation de la Mission `MSN-SIDE-014-WEWA`

- **Lot Documentaire Audité** : `TSK-2026-114 (Handoff GD-02 & WLD-04)`
- **Résultat `validate_registry.py`** : `PASS (0 erreur)`
- **Statut d'Indexation** : `READY_FOR_DIR06_PROMOTION`

## 1. Entrées Formatées pour `knowledge/entities-registry.csv`
```csv
id,category,name,district_id,status,owner_skill,validated_by,dependencies,sources,last_updated,summary
MSN-SIDE-014-WEWA,MISSION,Course Contre la Pluie,DST-MATONGE,PROPOSED,GD-02,DIR-05,LOC-MATONGE-VICTOIRE|VEH-MOTO-WEWA-01,SRC-002,2026-11-25,Mission secondaire de livraison urgente en moto Wewa à travers Matonge sous une averse équatoriale.
```

## 2. Contrôle des Références & Sources (`SRC-*`)
- **IDs Vérifiés** : `DST-MATONGE` (`CONFIRMED`), `LOC-MATONGE-VICTOIRE` (`CONFIRMED`), `VEH-MOTO-WEWA-01` (`CONFIRMED`). Zéro référence fantôme.
- **Sources Rattachées** : `SRC-002` (UE5 GAS / State Machines).
