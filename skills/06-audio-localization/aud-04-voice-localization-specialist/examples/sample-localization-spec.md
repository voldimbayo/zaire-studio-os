# Exemple `AUD-04` — Table de Localisation & Doublage de `MSN-MAIN-001-ARRIVEE`

## 1. Validation Automatisée (`scripts/check_l10n_unicode.py`)
- **Clés vérifiées** : `SUB_MSN001_KOFFI_01`, `SUB_MSN001_AMINA_02`, `UI_OBJ_MSN001_ST01`
- **Glyphes Unicode (`ɛ`, `ɔ`)** : Présents et intègres en UTF-8 (`Kɛbá`, `Tɔ́kɛndɛ́`).
- **Marge d'Expansion UI (+35 %)** : Chaîne source max = `79 chars` -> Requis `+35 %` = `107 chars` -> Conteneur UI configuré à `120 chars` (**CONFORME**).

## 2. Extrait de la String Table Multilingue (`localized-string-table.csv`)
| Clé Localisation | Locuteur | Texte Source (`fr-CD`) | Adaptation Lingala (`ln-CD`) | Adaptation Anglaise (`en-US`) |
| :--- | :--- | :--- | :--- | :--- |
| `SUB_MSN001_KOFFI_01` | `CHR-PROTAG-KOFFI` | `[KOFFI] : Mbote vieux ! J'ai le laissez-passer ONATRA pour le quai numéro quatre.` | `[KOFFI] : Mbote kulutu! Nazali na mokanda ya ONATRA mpo na libongo ya minei.` | `[KOFFI] : Mbote boss! I've got the ONATRA pass for dock number four.` |
| `SUB_MSN001_AMINA_02` | `CHR-ALLY-AMINA` | `[AMINA] : Kɛbá Koffi, les hommes de Mukendi contrôlent déjà la grue ! Tɔ́kɛndɛ́ !` | `[AMINA] : Kɛbá Koffi, bato ya Mukendi bakangi déjà grue! Tɔ́kɛndɛ́!` | `[AMINA] : Kɛbá Koffi, Mukendi's men already control the main crane! Let's move!` |
