from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    ...

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    ...

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name', 'baseHP', 'baseMP', 'startingMoney']
    
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
    list_display = ['name', 'type', 'cost']

@admin.register(SpellOrigin)
class SpellOriginAdmin(admin.ModelAdmin):
    ...

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    ...

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'race', 'specialization', 'creator', 'public']

@admin.register(CharacterStats)
class CharacterStatsAdmin(admin.ModelAdmin):
    ...

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Modifier)
class ModifierAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(WeaponTrait)
class WeaponTraitAdmin(admin.ModelAdmin):
    ...

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'rarity', 'type', 'combat', 'cost']

@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
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
