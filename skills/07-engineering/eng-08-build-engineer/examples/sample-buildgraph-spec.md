# Exemple `ENG-08` — Pipeline BuildGraph `BG_Zaire_Incremental_And_Nightly`

- **Nom du Pipeline** : `BG_Zaire_Incremental_And_Nightly`
- **Cible Temps Build Incrémental (`PERF-CI-BUILD`)** : `11.4 minutes` mesuré (`<= 15.0 minutes` requis)
- **Taux de Cache Hit Zen DDC Requis** : `97.2 %` sur le cluster Zen Server
- **Statut** : `CONFIRMED`

## 1. Étapes du Graphe BuildGraph / Horde
| Étape | Commande UAT / Commandlet | Durée Moyenne | Condition d'Échec Bloquant |
| :--- | :--- | :--- | :--- |
| `0_StudioOS_Verify` | `python -m unittest discover -s tests` | `0.2 min` | Erreur de registre, cycle DAG ou skill invalide. |
| `1_Compile_UBA` | `BuildCookRun -build -uba -WarningsAsErrors` | `3.5 min` | Tout warning ou erreur C++20. |
| `2_DataValidation` | `UnrealEditor-Cmd -run=DataValidation` | `1.8 min` | Violation `ART-04` / `ENG-01` détectée par `ENG-03`. |
| `3_Cook_IoStore` | `BuildCookRun -cook -iostore -pak -compressed` | `5.9 min` | Asset corrompu ou référence manquante. |
| `4_Gauntlet_Smoke` | `RunUnreal -test=ZaireSmokeTestSuite` | `4.0 min` (Post-Build) | Crash, P99 > `16.6 ms` (`ENG-07`) ou soft-lock (`PRD-05`). |

## 2. Sécurité Packaging IoStore & Gestion des Secrets
- **Chiffrement Index `.utoc` & Signature RSA** : Les clés `ZAIRE_PAK_AES256_KEY` et `ZAIRE_PAK_RSA_SIGN_KEY` sont lues exclusivement depuis le coffre-fort d'environnement du runner Horde au moment de l'étape `3_Cook_IoStore`, puis purgées de la mémoire volatile.
- **Overhead CPU Runtime** : `0.35 %` (`< 1 %` requis grâce au chiffrement ciblé de la table d'allocation `.utoc` et compression `Oodle Kraken`).
