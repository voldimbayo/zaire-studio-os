# Directives d'Authenticité Culturelle — Kinshasa, RDC (`cultural-guidelines.md`)

Ce document établit les règles d'authenticité culturelle, sociale, linguistique et esthétique obligatoires pour tous les livrables de **ZAÏRE STUDIO OS**, sous la supervision de `WLD-02` (Cultural Researcher) et `DIR-03` (Creative Director).

---

## 1. Principes Fondamentaux d'Authenticité
1. **Spécificité Kinoise (Zéro "Afrique Générique")** : Kinshasa est une mégapole francophone et lingalaphone contemporaine de plus de 15 millions d'habitants. Il est strictement interdit d'y plaquer des éléments architecturaux, vestimentaires, fauniques ou linguistiques issus d'autres régions (ex. pas de savane sauvage en centre-ville, pas d'argot d'Afrique de l'Ouest ou d'Afrique de l'Est non pratiqué à Kinshasa).
2. **Modernité & Débrouillardise Urbaine ("Article 15")** : Représenter fidèlement la coexistence entre infrastructures formelles (banques et tours de la Gombe, grands bus `ORG-TRANSCO`) et l'économie ingénieuse du quotidien (réparateurs mécaniques de Kalamu, coursiers `VEH-MOTO-WEWA-01`, marchés vivants, micro-studios musicaux).
3. **Traçabilité Stricte (`RESEARCH_REQUIRED`)** : Lorsqu'un skill a besoin d'une référence historique, toponymique ou linguistique précise non présente dans `knowledge/`, il ne doit jamais l'inventer ; il doit insérer le marqueur `RESEARCH_REQUIRED` et solliciter `WLD-02`.

---

## 2. Codes Linguistiques & Registres de Langue (`NAR-03`, `NAR-04`, `AUD-04`)
Les dialogues de **ZAÏRE** reflètent le bilinguisme organique et le *code-switching* entre le **français de RDC** et le **lingala kinois** :
- **Registre Institutionnel / Élite (`DST-GOMBE`)** : Français soutenu ou administratif ponctué de marqueurs pragmatiques locaux.
- **Registre Urbain Quotidien (`DST-KALAMU`, `DST-MATONGE`, `DST-LIMETE`)** : Alternance fluide français/lingala (code-switching naturel).
- **Typographie Unicode Obligatoire** : Respecter systématiquement les voyelles ouvertes du lingala (`ɛ` U+025B, `ɔ` U+0254) dans tous les fichiers `.po`/`.locres`, sous-titres et textes UI (`GD-07`, `AUD-04`).

---

## 3. Codes Vestimentaires & Morphologie Sociale (`ART-03`)
- **Diversité Urbaine Réelle** : Alterner tenues professionnelles modernes, streetwear kinois, pagnes wax/hollandais taillés sur mesure, uniformes de travail (dockers du port, mécaniciens, chauffeurs) et tenues de **Sapeurs** (Société des Ambianceurs et des Personnes Élégantes) lors d'événements sociaux spécifiques à Matonge.
- **Calibration des Carnations (`ART-03` / `ART-07`)** : Les shaders de peau UE5 (Subsurface Profile) et l'exposition caméra Lumen doivent être spécifiquement étalonnés pour restituer la richesse des carnations foncées sous un éclairage équatorial direct (Zénith EV100 = 15-16) comme sous éclairage nocturne urbain, sans écrasement des noirs ni spécularité plastique.

---

## 4. Patrimoine Musical & Sonore (`AUD-01`, `AUD-03`)
- **Identité Musicale** : La musique diégétique (`ORG-RADIO-KIN`, terrasses de `DST-MATONGE`) s'appuie sur les structures rythmiques authentiques de la **rumba congolaise** (section sébène, guitares mi-solo/solo), du **ndombolo**, du **rap kinois** et des chorales urbaines.
- **Droits & Licences (`PRD-02`)** : Toute œuvre musicale référencée doit distinguer explicitement les compositions originales interactives du studio et les pistes sous licence nécessitant un flag `STREAMER_SAFE_FALLBACK`.
