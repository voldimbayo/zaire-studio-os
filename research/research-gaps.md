# Lacunes Documentaires & Zones à Approfondir (`research-gaps.md`)

Une recherche rigoureuse impose d'identifier explicitement ce qui n'est **pas encore suffisamment documenté** avant de passer à l'architecture des skills.

## 1. Lacunes Techniques & Moteur (À combler avant Phase 2)
- **Pipelines Houdini -> UE5 PCG à grande échelle (Houdini 20.5/21+ & UE 5.5/5.6+)** : Les tutoriels officiels SideFX (*City Sample*) datent initialement de UE 5.0/5.1. Les évolutions récentes de l'interopérabilité native entre Houdini Engine et le graphe **UE5 PCG (Procedural Content Generation)** nécessitent une vérification technique approfondie sur la documentation SideFX/Epic la plus récente.
- **Détails d'implémentation de Mass Traffic & ZoneGraph** : La documentation publique d'Epic Games sur `MassTraffic` reste largement concentrée sur le projet *City Sample* et manque de guides de référence détaillés pour les comportements irréguliers (motos slalomant entre les files, arrêts impromptus de taxis-bus), typiques du trafic de Kinshasa.
- **Accès intégral aux conférences GDC Vault payantes** : Plusieurs présentations clés (notamment sur la création d'outils chez Insomniac Games et l'éclairage de Naughty Dog) ont été vérifiées via leurs résumés officiels et notes publiques, mais leurs diapositives complètes sont derrière le paywall GDC Vault.

## 2. Lacunes Spécifiques au Contexte de ZAÏRE (Kinshasa, RDC)
- **Données SIG / Topographiques haute précision de Kinshasa** : Les données OpenStreetMap (OSM) couvrent les grands axes (Boulevard du 30 Juin, Avenue Lumumba, Gombe), mais la couverture des ruelles secondaires de communes populaires (Matonge, Kalamu, Masina, Ngaliema) est hétérogène. Un pipeline procédural compensatoire (règles de subdivision d'îlots inspirées de l'urbanisme réel) devra être conçu.
- **Base de référence architecturale et sonore locale** : Il manque encore un corpus structuré interne (photogrammétrie, textures de façades locales, signalétique, enregistrements d'ambiances en lingala) qui constituera le répertoire `references/` partagé des skills `ART-03`, `NAR-04` et `AUD-02`.
- **Standardisation linguistique Lingala / Français kinois** : Absence de glossaire technique normalisé pour l'interface utilisateur et le sous-titrage multilingue (gestion des emprunts lexicaux et du code-switching naturel).

## 3. Lacunes dans l'Écosystème Public d'Agent Skills
- **Licences non vérifiées sur certains dépôts communautaires** : Les dépôts repérés (`quodsoler/unreal-engine-skills`, `gamedev-skills/awesome-gamedev-agent-skills`) ont été audités sur leur structure publique, mais leurs fichiers `LICENSE` complets doivent être inspectés avant toute réutilisation de conventions.
- **Absence de standards pour les métiers non-code** : Aucun dépôt public ne fournit de modèles éprouvés pour automatiser ou assister la production de *Quest Flowcharts*, *Wwise Soundbanks* ou *Lighting Passes*. Ces skills devront être entièrement prototypés et testés lors de la Phase 2.
