# Spécification Combat & Archétypes Ennemis (`GD-05`)

- **Système** : `SYS-CMB-MELEE`
- **Arme / Capacité Évaluée** : `ITM-...` (`Ability.Melee...`)
- **Plafond Attack Tokens Escouade** : `2 jetons simultanés max`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Table Frame Data (Base 60 FPS)
| Mouvement | Gameplay Tag | Startup (f) | Active (f) | Recovery (f) | Dégâts | Hitstop (ms) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `[Nom coup]` | `Ability.Melee...` | `[XX]` | `[XX]` | `[XX]` | `[XX]` | `[XX ms]` |

## 2. Archétypes Ennemis & Comportement IA (`AI-01`)
| ID Archétype | Coût Attack Token | Santé (HP) | Pattern d'Attaque & Télégraphe | Contre Tactique Joueur |
| :--- | :--- | :--- | :--- | :--- |
| `ENM-...` | `1` | `[HP]` | `[Startup >= 22f + signal]` | `[Parade / Esquive]` |

## Contraintes Studio & Validation Pré-Handoff (`GD-05`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `DIR-05, ENG-02, AI-01, ART-05`
