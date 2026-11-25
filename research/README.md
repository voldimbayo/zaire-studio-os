# ZAÏRE STUDIO OS — Phase 1 : Research & Knowledge Discovery

## Contexte du Projet
**ZAÏRE STUDIO OS** est une architecture modulaire d'Agent Skills conçue pour modéliser et orchestrer les métiers, pipelines et standards d'ingénierie d'un studio AAA. Le projet pilote de référence est **ZAÏRE**, un jeu d'action-aventure en monde ouvert ambitieux situé à **Kinshasa (République Démocratique du Congo)**.

## Objectif de la Phase 1
Constituer une base de connaissances documentaire vérifiée, structurée et sans spéculation couvrant l'ensemble des départements d'un studio AAA (46 domaines identifiés) afin de préparer la conception d'Agent Skills spécialisés dans les phases ultérieures. Aucun skill n'est généré durant cette phase.

## Architecture des Livrables (`research/`)
- `README.md` : Vue d'ensemble, périmètre, conventions de vérification et guide de lecture.
- `research-index.md` : Index maître des 46 domaines de spécialisation classés par pôles de production.
- `industry-methodologies.md` : Analyse des méthodes de production publiquement documentées chez Rockstar Games, Ubisoft, CD Projekt Red, Naughty Dog, Insomniac Games et Guerrilla Games.
- `technical-reference.md` : Référentiel technique exhaustif (12 critères obligatoires) pour chacun des 46 domaines appliqués au contexte UE5 / Houdini / Kinshasa.
- `skills-discovery.md` : Audit des dépôts publics d'Agent Skills (architecture `SKILL.md`, licences, limites et réutilisabilité).
- `skills-coverage-matrix.md` : Matrice de couverture croisant les 46 domaines AAA, leur criticité pour ZAÏRE, l'état de l'existant et la granularité cible des futurs skills.
- `research-gaps.md` : Identification des lacunes documentaires (domaines AAA, spécificités culturelles/urbaines de Kinshasa, limitations des sources publiques).
- `source-registry.csv` : Registre normalisé des sources documentaires (UTF-8, séparateur virgule) exploitable par script.
- `source-registry.md` : Version lisible et commentée du registre des sources avec distinction explicite entre sources consultées et repérées.

## Règles de Rigueur & Traçabilité
1. **Zero Fabrication** : Toutes les URL, conférences GDC, documentations techniques et dépôts GitHub proviennent exclusivement de sources vérifiables.
2. **Distinction des Statuts** :
   - `Consultée (Extrait/Index)` : Source dont le contenu, les métadonnées ou les extraits techniques ont été directement examinés via recherche documentaire.
   - `Repérée (À approfondir)` : Source primaire identifiée avec certitude (URL/référence exacte) nécessitant une lecture intégrale ou un accès payant (ex. GDC Vault complet).
3. **Absence de Spéculation Propriétaire** : Les analyses sur Rockstar Games, Ubisoft, CD Projekt Red, Naughty Dog et Insomniac Games reposent uniquement sur leurs publications publiques (GDC, SIGGRAPH, blogs d'ingénierie).
