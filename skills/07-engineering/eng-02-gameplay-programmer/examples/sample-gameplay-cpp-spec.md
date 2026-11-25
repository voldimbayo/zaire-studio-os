# Exemple `ENG-02` — Implémentation C++ de `UZaireGA_MeleeParry` (`SYS-CMB-MELEE`)

- **Classe C++** : `UZaireGA_MeleeParry : public UZaireGameplayAbility`
- **Système Game Design Source** : `SYS-CMB-MELEE` (`GD-05`) & `ITM-WPN-MACHETTE`
- **Budget CPU Tick** : `0.0 ms (100 % Event-Driven par AnimNotifyState & GameplayEvents)`
- **Statut** : `CONFIRMED`

## 1. Contrat de Classe C++20 & Configuration GAS
```cpp
UCLASS()
class ZAIREGAME_API UZaireGA_MeleeParry : public UZaireGameplayAbility
{
    GENERATED_BODY()
public:
    UZaireGA_MeleeParry();
    virtual void ActivateAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo, const FGameplayEventData* TriggerEventData) override;
    virtual void EndAbility(const FGameplayAbilitySpecHandle Handle, const FGameplayAbilityActorInfo* ActorInfo,
        const FGameplayAbilityActivationInfo ActivationInfo, bool bReplicateEndAbility, bool bWasCancelled) override;

protected:
    UFUNCTION()
    void OnIncomingStrikeDeflected(FGameplayEventData Payload);

    UPROPERTY(EditDefaultsOnly, Category = "Zaire|Combat")
    float PerfectParryHitstopSeconds = 0.085f; // 85 ms (GD-05)
};
```

## 2. Sécurité d'État & Nettoyage (`EndAbility` / Anti-Soft-Lock)
- **Tags Octroyés** : `State.Character.Combat.Parrying` pendant la fenêtre active (`frames 4 à 15` à 60 FPS).
- **Tags Annulés** : Annule la phase `Recovery` de `Ability.Melee.LightAttack` dès la frame 20 (`GD-05`).
- **Garantie de Nettoyage** : Si `EndAbility` est appelé suite à une chute ou une explosion pendant le Hitstop (`0.085 s`), le `CustomTimeDilation` de Koffi et de l'assaillant est systématiquement restauré à `1.0f`.
