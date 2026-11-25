# Standards de Qualité, Métriques & Validation (`quality-standards.md`)

Ce document établit les seuils d'acceptation techniques, artistiques, narratifs et d'accessibilité issus de la recherche Phase 1 (`research/technical-reference.md`) applicables à tous les livrables de **ZAÏRE STUDIO OS**.

---

## 1. Budgets Techniques Cibles (Unreal Engine 5 — Monde Ouvert Kinshasa)

| Métrique Système | Mode Performance (60 FPS) | Mode Qualité (30 FPS) | Responsable Surveillance |
| :--- | :--- | :--- | :--- |
| **Frametime Total (CPU + GPU)** | **<= 16.6 ms** (P99) | **<= 33.3 ms** (P99) | `ENG-07` (Performance Eng) |
| **Budget CPU — NPC AI (`AI-01`)** | <= 2.5 ms | <= 3.0 ms | `AI-01` / `ENG-07` |
| **Budget CPU — Mass Crowd & Traffic (`AI-02`/`03`)** | <= 2.0 ms (500+ entités) | <= 2.5 ms (800+ entités) | `AI-02` / `AI-03` |
| **Budget CPU — Chaos Physics (`ENG-05`)** | <= 1.5 ms | <= 2.0 ms | `ENG-05` |
| **Budget GPU — Lumen GI & Reflections (`ART-07`)** | <= 4.5 ms | <= 7.0 ms | `ART-07` / `ENG-06` |
| **Budget GPU — Niagara VFX (`ART-09`)** | <= 1.5 ms | <= 2.0 ms | `ART-09` / `ENG-06` |
| **Temps de Build Incrémental (`ENG-08`)** | <= 15 minutes | <= 15 minutes | `ENG-08` |
| **Taux de Reproductibilité Bugs QA (`PRD-04`)** | >= 90 % | >= 90 % | `PRD-04` |
| **Couverture Tests Automatisés (`PRD-05`)** | >= 80 % systèmes critiques | >= 80 % systèmes critiques | `PRD-05` |

---

## 2. Standards de Production par Discipline

### A. Ingénierie & Moteur (`ENG-01`..`ENG-08`)
- **Zero Synchronous Loading** : Interdiction d'utiliser `LoadSynchronous()` sur le Game Thread en runtime ; usage obligatoire de `FStreamableManager` et `TSoftObjectPtr`.
- **PSO Caching** : Toute nouvelle passe matériau/VFX doit être intégrée à la collecte automatisée de Pipeline State Objects pour prévenir les saccades de compilation shaders.
- **Modularité** : Logique gameplay découpée en `UActorComponent` et capacités `UGameplayAbility` pilotées par `FGameplayTag`.

### B. World Design, Art & Environnement (`WLD-01`..`WLD-06`, `ART-01`..`ART-09`)
- **Règle Blockout First** : Aucun asset final (`ART-02`) n'est produit sur un lieu (`LOC-*`) tant que le blockout (`WLD-05`) n'a pas été validé en playtest gameplay.
- **Standardisation Métrique** : 1 unité UE = 1 cm ; largeur minimale de couloir jouable >= 350 cm pour éviter les collisions caméra ; Texel Density standardisée à `10.24 px/cm` pour les environnements urbains à hauteur d'œil.
- **Authenticité Culturelle** : Tout élément architectural, vestimentaire ou linguistique lié à Kinshasa doit être validé par `WLD-02` (Cultural Researcher) et exempt de stéréotypes.

### C. Narration & Localisation (`NAR-01`..`NAR-06`, `AUD-04`)
- **Zéro Soft-Lock Narratif** : Toute machine à états de mission (`MSN-*`) doit gérer la fuite du joueur, la destruction d'un véhicule ou l'interruption d'un dialogue.
- **Support Unicode & Expansion UI** : Toutes les polices UI doivent supporter les caractères spéciaux du lingala (`ɛ`, `ɔ`, tonalités) et les conteneurs UI doivent tolérer une expansion de texte de **+35 %** sans troncature.

### D. Accessibilité (`PRD-06` — Conformité XAG)
- **Double Codage** : Aucune information critique de gameplay ne doit reposer uniquement sur la couleur (ajout systématique d'icônes, formes ou indices sonores).
- **Assistance Motrice** : Option de remplacement des pressions répétées rapides (QTE) par un maintien continu ou une validation automatique.
- **Sous-titres Enrichis** : Identification explicite du locuteur (`[KOFFI]`), réglage de taille de police et fond semi-opaque paramétrable.

---

## 3. Definition of Done (DoD) Universelle d'un Livrable Skill
Pour qu'un livrable passe du statut `PROPOSED` au statut **`CONFIRMED`**, il doit satisfaire aux **6 critères obligatoires** :
1. **Format & Gabarit** : Conforme au template officiel du skill (`templates/`).
2. **Intégrité des IDs** : Tous les identifiants (`CHR-*`, `LOC-*`, `MSN-*`, etc.) sont enregistrés et valides.
3. **Traçabilité** : Toutes les sources techniques ou culturelles sont citées ; toute donnée incertaine est isolée en `RESEARCH_REQUIRED`.
4. **Périmètre Respecté** : Aucun empiètement sur les responsabilités d'un autre skill.
5. **Budgets & Standards** : Respect des métriques spatiales, budgets CPU/GPU/RAM et règles d'accessibilité XAG.
6. **Validation Croisée** : Signature logique des skills auditeurs (`NAR-06` pour la narration, `ENG-07` pour la performance, `DIR-06`/`DIR-07` pour la gouvernance).
