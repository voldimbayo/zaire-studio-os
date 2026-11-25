# Exemple `GD-07` — Spécification du HUD Contextuel & Téléphone Diégétique de Koffi

- **ID Widget** : `UI-HUD-MAIN-OVERLAY` & `UI-PHONE-KINSHASA-HUB`
- **Gameplay Tag Layer** : `UI.Layer.HUD` & `UI.Layer.DiegeticPhone`
- **Profondeur Navigation** : `2 actions max` (`D-Pad Haut` -> Ouverture Téléphone -> `LB/RB` bascule Carte / Radio Lokole / Messages)
- **Statut** : `CONFIRMED`

## 1. Architecture Visuelle & Comportement Contextuel
- **Condition d'Affichage / Auto-Hide** : En exploration libre à `DST-MATONGE` ou `DST-GOMBE`, 0 élément HUD permanent à l'écran. Le réticule de furtivité n'apparaît que sous `State.Character.Stealth.Concealed` ; la jauge de mêlée n'apparaît que sous `State.Character.Combat.Engaged`.
- **Binding Gameplay Tags** : `State.Character.Combat.Engaged`, `State.Character.Stealth.Concealed`, `State.Character.Stealth.Disguised`, `World.District.*`.

## 2. Conformité Localisation (`AUD-04`) & Accessibilité XAG (`PRD-06`)
- **Tolérance Expansion Texte (+35 %)** : Les bannières d'objectifs de mission (`MSN-*`) et les bulles SMS utilisent des `USizeBox` et `UVerticalBox` extensibles acceptant jusqu'à `+40 %` de caractères sans rognage.
- **Support Glyphes Lingala (`ɛ`, `ɔ`)** : Police sans-serif Humanist UTF-8 certifiée sur l'intégralité du glossaire (`Kɛbá!`, `Tɔ́kɛndɛ́`, `Bilɔkɔ`).
- **Double Codage Forme + Couleur** :
  - Vigilance Garde `AI-01` : Cercle blanc pointillé (Calme) -> Triangle jaune strié (Soupçon) -> Losange rouge plein avec point d'exclamation + son distinctif (Alerte).
- **Ratio de Contraste Minimum** : `7.2:1` sur le bandeau de sous-titres (`[KOFFI] : « Tɔ́kɛndɛ́ ! »` sur fond `RGBA(12, 12, 16, 0.78)`).
