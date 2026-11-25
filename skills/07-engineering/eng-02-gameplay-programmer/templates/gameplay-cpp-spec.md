# Spécification d'Implémentation C++ Gameplay & GAS (`ENG-02`)

- **Classe C++** : `UZaireGA_...` | `UZaire...Component`
- **Système Game Design Source** : `SYS-...` (`GD-01`..`GD-07`)
- **Budget CPU Tick** : `0.0 ms (Event-Driven)` | `[<= 0.15 ms]`
- **Statut** : `PROPOSED` | `CONFIRMED`

## 1. Contrat de Classe C++20 & Configuration GAS
```cpp
UCLASS()
class ZAIREGAME_API UZaireGA_Example : public UZaireGameplayAbility
{
    GENERATED_BODY()
    // ...
};
```

## 2. Sécurité d'État & Nettoyage (`EndAbility` / Anti-Soft-Lock)
- **Tags Octroyés (`ActivationOwnedTags`)** : `[Tags]`
- **Tags Annulés (`CancelAbilitiesWithTag`)** : `[Tags]`
- **Garantie de Nettoyage sur Interruption** : `[Comportement EndAbility]`
