---
name: gd-04-progression-designer
description: "Conception des systèmes de progression de Koffi (CHR-PROTAG-KOFFI) : courbes d'expérience, arbres de compétences (Combat Urbain, Ingénierie & Wewa, Réseau & Infiltration Sociale) et paliers de réputation par commune (SYS-WLD-REPUTATION)."
license: "Proprietary - ZAÏRE STUDIO OS"
compatibility: "Claude.ai, Claude Code, Google Antigravity, Cursor"
metadata:
  id: GD-04
  department: 03-game-design
  stratum: 2
  version: "1.1.0"
  inputs:
    - "game-systems-gd-01"
    - "combat-design-gd-05"
    - "narrative-architecture-nar-01"
  outputs:
    - "progression-curve.csv"
    - "skill-tree-specification.md"
  upstream_dependencies:
    - "GD-01"
    - "GD-05"
    - "NAR-01"
---

# `GD-04` — Progression Designer (`gd-04-progression-designer`)

## 1. Conditions d'Utilisation & Périmètre Opérationnel

Ce skill appartient au département **`03-game-design`** (Strate DAG **2**) de **ZAÏRE STUDIO OS (v1.1.0)**.

### Déclencheurs d'Activation
- Définition des paliers de montée en niveau et des coûts de déblocage des capacités UE5 GAS (`Ability.*`).
- Calibrage des récompenses systémiques octroyées par la réputation dans chaque quartier (`DST-GOMBE`, `DST-MATONGE`, `DST-KALAMU`, `DST-LIMETE`).
- Équilibrage du rythme d'acquisition des compétences entre le début de l'Acte I et la fin de l'Acte III.

### Contrats d'Interface (Inputs / Outputs)
- **Entrées requises** : `game-systems-gd-01`, `combat-design-gd-05`, `narrative-architecture-nar-01`
- **Sorties produites** : `progression-curve.csv`, `skill-tree-specification.md`
- **Dépendances Amont Canoniques (DAG)** : `GD-01`, `GD-05`, `NAR-01`

---

## 2. Limites Strictes de Responsabilité (Scope Guard)

- **Interdiction / Limite** : Ne fixe pas les prix monétaires en boutique (`GD-03`) et n'implémente pas les classes C++ GAS (`ENG-02`).
- **Interdiction / Limite** : N'accorde aucun bonus purement passif invisible (+1 % dégât) : chaque noeud majeur doit enrichir les options tactiques du joueur.
- **Règle d'Intégrité Référentielle** : Ne jamais référencer une entité du monde de Kinshasa (Personnage `CHR-*`, Famille `FAM-*`, Organisation `ORG-*`, Commune `DST-*`, Lieu `LOC-*`, Mission `MSN-*`, Objet `ITM-*`, Véhicule `VEH-*`, Système `SYS-*`) sans vérifier son statut dans `knowledge/entities-registry.csv` (embarqué sous forme d'instantané dans l'archive ZIP individuelle Claude.ai). Toute information factuelle manquante doit être marquée **`RESEARCH_REQUIRED`** et toute exécution binaire moteur absente **`NOT TESTED`**.

---

## 3. Procédures Opérationnelles Standardisées (SOP)

Exécuter séquentiellement les étapes suivantes lors de toute activation du skill :

1. Structurer la progression autour de **3 Branches de Compétences** alignées sur les piliers créatifs (`DIR-03`) : (1) *Mêlée & Agilité Urbaine* (`GD-05`), (2) *Mécanique & Maîtrise Wewa* (`GD-06`), (3) *Voix de Kinshasa & Infiltration* (`GD-01`).
2. Modéliser la courbe d'XP selon une fonction polynomiale contrôlée afin de garantir un nouveau déblocage toutes les 45 à 60 minutes de jeu actif.
3. Définir les 4 paliers de `SYS-WLD-REPUTATION` par commune (*Inconnu -> Respecté -> Enfant du Quartier -> Pilier de Kinshasa*) et leurs avantages concrets en jeu.
4. Rédiger la spécification dans `templates/skill-tree-spec.md`.

---

## 4. Règles de Décision & Arbre d'Arbitrage

| Condition Détectée | Décision / Action Obligatoire | Escalade & Protocole de Repli |
| :--- | :--- | :--- |
| Compétence indispensable au franchissement d'un blockout principal (ex: Ability.Movement.Vault) | L'inclure dans le kit de base de Koffi dès MSN-MAIN-001-ARRIVEE (ne jamais verrouiller une métrique spatiale de base derrière un arbre d'XP) | Garantir la cohérence avec WLD-05 |
| Branche de compétences choisie par moins de 15 % des profils de jeu simulés | Ajouter une synergie transversale (ex: l'arbre Réseau débloque aussi des raccourcis de livraison Wewa et des diversions de foule AI-02) | Équilibrer l'attractivité des 3 approches |
| Gain de puissance en fin d'Acte II rendant les affrontements de l'Acte III triviaux | Plafonner les multiplicateurs de santé/dégâts à +35 % sur l'ensemble du jeu et concentrer la progression sur la variété tactique | Synchroniser avec GD-05 |

---

## 5. Chargement Progressif des Références, Modèles et Scripts

Afin d'optimiser la fenêtre de contexte, chargez uniquement à la demande les ressources suivantes incluses dans ce skill :

- **Référentiel Métier, Modes de Défaillance & Compatibilité UE 5.8 / Houdini 22 / Wwise** : `references/progression-and-reputation-math.md`
- **Modèle Officiel de Livrable** : `templates/skill-tree-spec.md`
- **Exemple Complet d'Exécution (Input/Output)** : `examples/sample-progression-spec.md`
- **Référentiel Partagé Studio (Couche 2)** : `knowledge/entities-registry.csv`, `knowledge/technical-specs/performance-budgets.csv`, `knowledge/technical-specs/spatial-metrics.md`, `knowledge/technical-specs/gameplay-tags-taxonomy.csv`

---

## 6. Exemples Concrets d'Entrées et Sorties

Consultez le fichier `examples/sample-progression-spec.md` pour un cas réel complet appliqué à **ZAÏRE (Kinshasa)** comprenant l'enveloppe de tâche (`Task Envelope`) reçue, l'artefact généré conforme à `templates/skill-tree-spec.md` et le paquet de passation (`Handoff Packet`).

---

## 7. Critères de Validation & Definition of Done (DoD)

Un livrable produit par `GD-04` ne peut passer du statut `PROPOSED` au statut `CONFIRMED` que si tous les contrôles suivants sont validés :

- [ ] Chaque compétence débloquée correspond à une `UGameplayAbility` ou un `UGameplayEffect` identifié par un `FGameplayTag`.
- [ ] Les 4 paliers de réputation locale (`SYS-WLD-REPUTATION`) produisent des effets visibles sur les PNJ, le trafic et les commerçants.
- [ ] Aucune capacité obligatoire pour le chemin critique n'est verrouillée derrière un choix optionnel.
- **Validation Croisée Obligatoire** : Soumettre le Handoff Packet aux skills auditeurs : `DIR-05`, `GD-03`, `GD-05`.
