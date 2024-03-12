from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    ...

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    ...
    
@admin.register(MagicElement)
class MagicElementAdmin(admin.ModelAdmin):
    ...

@admin.register(MagicGroup)
class MagicGroupAdmin(admin.ModelAdmin):
    ...

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    ...

@admin.register(DamageType)
class DamageTypeAdmin(admin.ModelAdmin):
    ...

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    ...

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    ...

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    ...

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    ...

@admin.register(Modifier)
class ModifierAdmin(admin.ModelAdmin):
    ...

@admin.register(WeaponTrait)
class WeaponTraitAdmin(admin.ModelAdmin):
    ...

@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    ...

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    ...

@admin.register(CharacterWeapon)
class CharacterWeaponAdmin(admin.ModelAdmin):
    ...

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    ...

@admin.register(CharacterExpertise)
class CharacterExpertiseAdmin(admin.ModelAdmin):
    ...

@admin.register(CharacterAttribute)
class CharacterAttributeAdmin(admin.ModelAdmin):
    ...

@admin.register(CharacterProficiencies)
class CharacterProficienciesAdmin(admin.ModelAdmin):
    ...
