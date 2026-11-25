# ADR-NNN : [Titre Court et Explicite de la Décision]

- **Statut** : `PROPOSED` | `CONFIRMED` | `DEPRECATED`
- **Date** : `YYYY-MM-DD`
- **Auteur(s)** : `[DIR-04 / ENG-01 / ...]`
- **Décideurs (Arbitrage)** : `[DIR-01, DIR-02, DIR-03, DIR-04, DIR-05, DIR-06, DIR-07]`
- **Systèmes / Entités Impactés** : `[SYS-*, DST-*, ENG-*]`

---

## 1. Contexte et Problème
Décrire clairement la contrainte technique, ludique ou culturelle rencontrée sur le projet **ZAÏRE** (ex. budget frametime de 16.6 ms sous Unreal Engine 5 à Kinshasa, densité du marché de Matonge, streaming World Partition).

## 2. Facteurs de Décision & Contraintes Budgets
- **Cible Performance (60 FPS)** : `<= 16.6 ms` (CPU/GPU)
- **Cible Qualité (30 FPS)** : `<= 33.3 ms` (CPU/GPU)
- **Contraintes Pipeline** : UE5 (World Partition, Nanite, Lumen, GAS, Mass Entity, ZoneGraph, Chaos, Niagara, Wwise, Houdini HDA/PCG).

## 3. Options Envisagées
1. **Option A** : `[Description, avantages, coûts CPU/GPU/RAM]`
2. **Option B** : `[Description, avantages, coûts CPU/GPU/RAM]`
3. **Option C** : `[Description, avantages, coûts CPU/GPU/RAM]`

## 4. Décision Retenue
Option retenue : **Option [X]**.
Justification détaillée appuyée sur les sources vérifiées (`research/technical-reference.md` / `research/source-registry.csv`).

## 5. Conséquences et Critères de Validation
- **Impacts Positifs** : `[Gains mesurables]`
- **Risques & Mitigations (`PRD-02`)** : `[Actions de réduction de risque]`
- **Métrique de Validation (`ENG-07` / `PRD-05`)** : `[Seuil mesurable dans Unreal Insights ou Gauntlet]`
