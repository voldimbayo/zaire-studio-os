# Spécification d'Écran UI/UX — Common UI (`GD-07`)

- **ID Widget** : `UI-[LAYER]-[SLUG]`
- **Gameplay Tag Layer** : `UI.Layer.[HUD / DiegeticPhone]`
- **Profondeur Navigation** : `[<= 3 actions]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Architecture Visuelle & Comportement Contextuel
- **Condition d'Affichage / Auto-Hide** : `[Règle d'apparition et de masquage]`
- **Binding Gameplay Tags** : `[Tags écoutés]`

## 2. Conformité Localisation (`AUD-04`) & Accessibilité XAG (`PRD-06`)
- **Tolérance Expansion Texte (+35 %)** : `[Validé / Conteneur dynamique]`
- **Support Glyphes Lingala (`ɛ`, `ɔ`)** : `[Police & encodage UTF-8]`
- **Double Codage Forme + Couleur** : `[Icônes associées aux états]`
- **Ratio de Contraste Minimum** : `[>= 4.5:1]`

## Contraintes Studio & Validation Pré-Handoff (`GD-07`)
- **Budgets Cibles UE 5.8** : `<= 16.6 ms` (60 FPS) / `<= 33.3 ms` (30 FPS) | Métriques `spatial-metrics.md` (`>= 350 cm`)
- **Entités Registre (`entities-registry.csv`)** : `[Lister IDs CHR-*, LOC-*, MSN-*, ORG-*, VEH-*, SYS-*]`
- **Sources (`source-registry.csv`)** : `[SRC-001..SRC-035 ou Engineering Recommendation]`
- **Auditeurs Requis** : `PRD-06, AUD-04, DIR-05`
