# Exemple `NAR-04` — Dialogue & Barks de `MSN-MAIN-001-ARRIVEE`

## 1. Graphe de Dialogue Validé (`DLG-MSN-001-PORT.json`)
```json
{
  "dialogue_id": "DLG-MSN-001-PORT",
  "mission_id": "MSN-MAIN-001-ARRIVEE",
  "location_id": "LOC-GOMBE-PORT",
  "interrupt_handlers": {
    "on_combat_triggered": "BARK_CMB_ALERT_01",
    "on_player_walk_away": "BARK_WAIT_KOFFI_01",
    "on_resume_conversation": "N01"
  },
  "nodes": [
    {
      "node_id": "N01",
      "speaker_id": "CHR-PROTAG-KOFFI",
      "line_text": "Mbote vieux! J'ai le laissez-passer ONATRA pour le quai numéro quatre.",
      "emotion_tag": "WARM",
      "camera_framing": "OTS_LEFT",
      "required_gameplay_tag": "State.Character.Stealth.Disguised",
      "is_terminal": false,
      "next_nodes": ["N02"]
    },
    {
      "node_id": "N02",
      "speaker_id": "CHR-ALLY-AMINA",
      "line_text": "Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue principale. Tɔ́kɛndɛ́!",
      "emotion_tag": "URGENT",
      "camera_framing": "CLOSE_UP",
      "required_gameplay_tag": "",
      "is_terminal": true,
      "next_nodes": []
    }
  ]
}
```

## 2. Table de Barks Contextuels (`LOC-GOMBE-PORT` & `DST-MATONGE`)
| Bark ID | Catégorie IA | Déclencheur Gameplay Tag | Texte Français / Lingala (`<= 20 mots`) | Émotion |
| :--- | :--- | :--- | :--- | :--- |
| `BRK-PORT-01` | Garde `AI-01` | `State.Character.Stealth.Disguised` | « Papier ONATRA validé. Reste loin des grues du secteur nord, compris ? » | `TENSE` |
| `BRK-PORT-02` | Garde `AI-01` | `State.Character.Combat.Engaged` | « Kɛbá ! Un intrus près des conteneurs ! Verrouillez la grille du *libongo* ! » | `ANGRY` |
| `BRK-CROWD-01` | Citoyen `AI-02` | `Vehicle.Type.MotoWewa` | « Eh *Wewa* ! Attention aux flaques devant le rond-point Victoire ! » | `URGENT` |
| `BRK-CROWD-02` | Citoyen `AI-02` | `World.Weather.TropicalStorm` | « La pluie arrive fort sur Matonge, abritez les marchandises sous la tôle ! » | `URGENT` |
