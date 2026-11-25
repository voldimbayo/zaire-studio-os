# Exemple `ENG-03` — Validateur `UZaireNaniteAndTextureValidator`

- **Nom du Validateur / Outil** : `UZaireNaniteAndTextureValidator : public UEditorValidatorBase`
- **Module Cible** : `ZaireEditor (Type: Editor)`
- **Règles Métier Appliquées** : `ART-04 (asset-validation-rules.json)`
- **Statut** : `CONFIRMED`

## 1. Logique de Validation & Auto-Fix
- **Condition d'Activation (`CanValidateAsset`)** : S'exécute sur tout `UStaticMesh` et `UTexture2D` situé sous `/Game/Zaire/Art/` et `/Game/Zaire/World/`.
- **Contrôles Exécutés (`ValidateLoadedAsset`)** :
  1. Si `UStaticMesh` a `NaniteSettings.bEnabled == true` : parcourt `StaticMaterials` et retourne `EDataValidationResult::Invalid` si un matériau utilise `BLEND_Translucent` ou si `WorldPositionOffsetDisableDistance > 3500.0f`.
  2. Si `UTexture2D` se termine par `_ORM` : vérifie que `SRGB == false` et que `CompressionSettings == TC_Masks`.
- **Action Auto-Fix Disponible** : Menu contextuel *"Zaire Studio OS -> Fix ORM Texture Compression & WPO Cull Distance (3500 cm)"*.
