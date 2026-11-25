# Système de Cohérence & Gestion des Connaissances (`knowledge-management.md`)

## 1. Principe de Source Unique de Vérité (Single Source of Truth)
Pour éviter toute divergence entre les 50 skills spécialisés et les 7 rôles de direction, toutes les entités du monde, du gameplay et de la production de **ZAÏRE** sont centralisées dans un **Registre Maître d'Entités** versionné. Aucun skill n'est autorisé à référencer un nom libre non enregistré sans lui attribuer un identifiant conforme et un statut explicite.

---

## 2. Machine à États des Connaissances (5 Statuts Obligatoires)

Chaque entité, spécification, règle métier ou donnée culturelle possède exactement l'un des **5 statuts** suivants :

| Statut | Définition Opérationnelle | Droits d'Utilisation par les Skills | Autorité de Transition |
| :--- | :--- | :--- | :--- |
| **`CONFIRMED`** | Donnée vérifiée, validée techniquement/créativement et sans contradiction dans le registre. | Lecture et référence libre par tous les départements. Base officielle de production. | `DIR-06` (Doc Director) + `DIR-07` (Quality Director) ou Directeur de pôle compétent. |
| **`PROPOSED`** | Proposition nouvellement créée par un skill, syntaxiquement valide mais en attente d'audit croisé. | Utilisable uniquement à titre exploratoire dans la même chaîne de tâches ; interdit pour le gel de production. | Tout skill spécialisé lors de la création d'un livrable. |
| **`RESEARCH_REQUIRED`** | Information manquante, ambiguë ou nécessitant une vérification documentaire/culturelle/technique avant décision. | Interdiction d'inventer la donnée manquante. Déclenche une tâche vers `WLD-02`, `WLD-03` ou `ENG-*`. | Tout skill détectant une lacune (`research/research-gaps.md`). |
| **`BLOCKED`** | Entité ou spécification en conflit majeur (incohérence narrative, dépassement budget GPU/CPU, bug critique QA). | Production gelée sur cet élément jusqu'à résolution par arbitrage de la Direction Centrale. | `NAR-06`, `ENG-07`, `PRD-04`, `DIR-04`, `DIR-07`. |
| **`DEPRECATED`** | Élément obsolète, coupé du périmètre (scope cut) ou remplacé par une version supérieure. | Interdiction formelle de l'utiliser dans de nouveaux livrables. Conservé uniquement pour traçabilité historique. | `DIR-02` (Exec Prod), `DIR-03` (Creative Dir), `DIR-06` (Doc Dir). |

### Diagramme de Transition des Statuts
```
[RESEARCH_REQUIRED] ---> [PROPOSED] ---> (Audit Continuité / Tech / QA) ---> [CONFIRMED]
                             |                                                   |
                             +---> (Conflit / Dépassement Budget) ---> [BLOCKED] -+
                                                                                 |
                                                   (Scope Cut / Remplacement) ---> [DEPRECATED]
```

---

## 3. Convention d'Identifiants Uniques (9 Catégories Obligatoires)

Tous les identifiants respectent le format strict : **`PREFIXE-CODE_UNIQUE`** (majuscules ASCII, chiffres, tirets, sans accents ni espaces).

| Catégorie | Préfixe | Format Normalisé | Exemple Concret (Projet ZAÏRE) | Propriétaire Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Personnages** | `CHR-` | `CHR-[ROLE]-[SLUG]` | `CHR-PROTAG-KOFFI` / `CHR-ANTAG-MUKENDI` | `NAR-03` (Character Writer) |
| **Familles** | `FAM-` | `FAM-[NOM]` | `FAM-MUKENDI` / `FAM-KABONGO` | `NAR-03` (Character Writer) |
| **Organisations** | `ORG-` | `ORG-[TYPE]-[SLUG]` | `ORG-CARTEL-FLEUVE` / `ORG-TRANSCO` | `NAR-05` (Lore Manager) |
| **Quartiers / Communes** | `DST-` | `DST-[COMMUNE]` | `DST-GOMBE` / `DST-MATONGE` / `DST-LIMETE` | `WLD-01` (Worldbuilding Arch) |
| **Lieux / POI** | `LOC-` | `LOC-[DST]-[SLUG]` | `LOC-LIMETE-ECHANGEUR` / `LOC-GOMBE-PORT` | `WLD-04` (Open World Des) |
| **Missions / Quêtes** | `MSN-` | `MSN-[TYPE]-[NUM]-[SLUG]` | `MSN-MAIN-001-ARRIVEE` / `MSN-SIDE-014-WEWA` | `GD-02` (Mission Designer) |
| **Objets / Équipements** | `ITM-` | `ITM-[CAT]-[SLUG]` | `ITM-WPN-MACHETTE` / `ITM-DOC-PASSEPORT` | `GD-01` / `GD-03` |
| **Véhicules** | `VEH-` | `VEH-[CAT]-[SLUG]` | `VEH-MOTO-WEWA-01` / `VEH-TAXI-JAUNE-01` | `GD-06` (Vehicle Designer) |
| **Systèmes de Gameplay** | `SYS-` | `SYS-[DOMAINE]-[SLUG]` | `SYS-CMB-MELEE` / `SYS-WLD-REPUTATION` | `GD-01` (Game Systems Des) |

---

## 4. Schéma d'Enregistrement d'une Entité (Metadata Record)
Chaque entrée du registre `knowledge/entities-registry.csv` (qui sera instanciée en Phase 3) suit ce schéma :
```yaml
id: "LOC-LIMETE-ECHANGEUR"
category: "LOCATION"
name: "Tour de l'Échangeur de Limete"
district_id: "DST-LIMETE"
status: "CONFIRMED"
owner_skill: "WLD-04"
validated_by: ["DIR-03", "DIR-06"]
dependencies: ["DST-LIMETE", "SYS-WLD-LANDMARKS"]
sources: ["SRC-019"]
last_updated: "2026-11-25"
summary: "Monument emblématique et repère vertical majeur (landmark) orientant la navigation dans la commune de Limete."
```

---

## 5. Règles d'Intégrité Référentielle
1. **Unicité Stricte** : Aucun ID ne peut être réattribué, même après passage au statut `DEPRECATED`.
2. **Interdiction des Références Fantômes** : Tout livrable mentionnant un `CHR-*`, `LOC-*` ou `MSN-*` inexistant dans le registre est automatiquement rejeté par `PRD-03` (Documentation Specialist).
3. **Propagation des Blocages** : Si `DST-MATONGE` passe en `BLOCKED`, toutes les missions `MSN-*` rattachées à `LOC-MATONGE-*` reçoivent automatiquement un drapeau d'alerte `DEPENDENCY_BLOCKED` dans le rapport du `Studio Orchestrator`.
