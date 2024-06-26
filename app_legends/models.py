from django.db import models
from django.contrib.auth.models import User
from utils.legends_upload_paths import *
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Expertise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Effect(models.Model):
    name = models.CharField(max_length=255)
    description = models.TimeField()

    def __str__(self):
        return self.name


class ItemType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    ilustration = models.ImageField(upload_to=item_ilustration_upload, blank=True, null=True)
    description = models.TextField()
    weight = models.FloatField()
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['type', 'name']


class DamageType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class WeaponTrait(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Modifier(models.Model):
    name = models.CharField(max_length=255)
    manaCost = models.IntegerField(blank=True, null=True)
    cost = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name', 'cost']


class Weapon(models.Model):
    class WeaponRarityName(models.TextChoices):
        Comum = 'Comum', _('Comum')
        Especial = 'Especial', _('Especial')

    class WeaponTypeName(models.TextChoices):
        Simples = 'Simples', _('Simples')
        Avancada = 'Avançada', _('Avançada')

    class WeaponCombatName(models.TextChoices):
        Combate = 'Combate', _('Combate')
        Precisao = 'Precisão', _('Precisão')

    class ReloadType(models.TextChoices):
        Rapido = 'Rápido', _('Rápido')
        Medio = 'Médio', _('Médio')
        Lento = 'Lento', _('Lento')

    name = models.CharField(max_length=255)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=weapon_ilustration_upload, blank=True, null=True)
    rarity = models.CharField(max_length=8, choices=WeaponRarityName.choices, default=WeaponRarityName.Comum)
    type = models.CharField(max_length=8, choices=WeaponTypeName.choices, default=WeaponTypeName.Simples)
    combat = models.CharField(max_length=8, choices=WeaponCombatName.choices, default=WeaponCombatName.Combate)
    
    baseDamage = models.CharField(max_length=255)
    damageType = models.ForeignKey(DamageType, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    weight = models.FloatField()
    traits = models.ManyToManyField(WeaponTrait, blank=True)
    modifiers = models.ManyToManyField(Modifier, blank=True)
    combatRange = models.FloatField(default=1.5)

    # POSSIBLE TRAIT FIELDS
    shotRange = models.CharField(max_length=255, blank=True, null=True)
    ammunition = models.ManyToManyField(Item, blank=True)
    magazine = models.IntegerField(blank=True, null=True)
    reloadTime = models.CharField(max_length=6, choices=ReloadType.choices, blank=True, null=True)
    versatileDamage = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    guardBlock = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-combat', 'rarity', 'type', 'name']

    def save(self, *args, **kwargs):
        has_reach = self.traits.filter(
            name='Alcance'
        ).first()
        if has_reach:
            self.combatRange = 3
        super(Weapon, self).save(*args, **kwargs)


class MagicElement(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class MagicGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    elements = models.ManyToManyField(MagicElement, blank=True)

    def __str__(self):
        return self.name
    
    
class Skill(models.Model):
    class SkillTypeName(models.TextChoices):
        Passiva = 'Passiva', _('Passiva')
        Ativa = 'Ativa', _('Ativa')

    name = models.CharField(max_length=255)
    skillType = models.CharField(max_length=7, choices=SkillTypeName.choices, default=SkillTypeName.Passiva)
    skillCost = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    normalCharCanUse = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Armor(models.Model):
    class ArmorTypeName(models.TextChoices):
        Leve = 'Leve', _('Leve')
        Media = 'Média', _('Média')
        Pesada = 'Pesada', _('Pesada')

    name = models.CharField(max_length=255)
    armorType = models.CharField(max_length=7, choices=ArmorTypeName.choices, default=ArmorTypeName.Media)
    cost = models.IntegerField(default=0)
    weight = models.FloatField()
    description = models.TextField()

    firstRequirement = models.ForeignKey(Expertise, related_name='first_req', blank=True, null=True, on_delete=models.CASCADE)
    firstRequirementValue = models.IntegerField(blank=True, null=True)
    secondRequirement = models.ForeignKey(Expertise, related_name='second_req', blank=True, null=True, on_delete=models.CASCADE)
    secondRequirementValue = models.IntegerField(blank=True, null=True)

    resistedDamages = models.ManyToManyField(DamageType, blank=True, related_name='resisted_dmg')
    immunityDamages = models.ManyToManyField(DamageType, blank=True, related_name='immunity_dmg')
    resistedEffects = models.ManyToManyField(Effect, blank=True, related_name='resisted_effect')
    immunityEffects = models.ManyToManyField(Effect, blank=True, related_name='immunity_effect')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['armorType']


class SpellOrigin(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Spell(models.Model):
    class SpellTypeName(models.TextChoices):
        Encantamento = 'Encantamento', _('Encantamento')
        Feitico = 'Feitiço', _('Feitiço')
        Conjuracao = 'Conjuração', _('Conjuração')
        Ritual = 'Ritual', _('Ritual')
    class SpellTierName(models.TextChoices):
        Simples = 'Simples', _('Simples')
        Intermediaria = 'Intermediária', _('Intermediária')
        Avancada = 'Avançada', _('Avançada')
    class SpellExpertiseName(models.TextChoices):
        Arcanismo = 'Arcanismo', _('Arcanismo')
        Crenca = 'Crença', _('Crença')
        Performance = 'Performance', _('Performance')

    name = models.CharField(max_length=255)
    origin = models.ForeignKey(SpellOrigin, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    firstElement = models.ForeignKey(MagicElement, related_name='first_element', on_delete=models.CASCADE, null=True, blank=True)
    secondElement = models.ForeignKey(MagicElement, related_name='second_element', on_delete=models.CASCADE, null=True, blank=True)
    spellType = models.CharField(max_length=12, choices=SpellTypeName.choices, default=SpellTypeName.Feitico)
    spellTier = models.CharField(max_length=13, choices=SpellTierName.choices, default=SpellTierName.Simples)
    spellExpertise = models.CharField(max_length=11, choices=SpellExpertiseName.choices, default=SpellExpertiseName.Arcanismo)
    group = models.ForeignKey(MagicGroup, on_delete=models.CASCADE)
    castingTime = models.CharField(max_length=255)
    range = models.FloatField()
    manaCost = models.IntegerField()

    ingredientCost = models.ManyToManyField(Item, blank=True)
    health = models.IntegerField(blank=True, null=True)
    heal = models.CharField(max_length=255, blank=True, null=True)
    damage = models.CharField(max_length=255, blank=True, null=True)
    damageType = models.ForeignKey(DamageType, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    areaOfEffect = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=specialization_ilustration_upload, blank=True, null=True)

    healDice = models.CharField(max_length=255)
    baseHP = models.IntegerField()
    levelHP = models.IntegerField()
    baseMP = models.IntegerField()

    requiredElements = models.ManyToManyField(MagicElement, blank=True)

    expertiseAmout = models.IntegerField()
    expertises = models.ManyToManyField(Expertise, blank=True)

    startingMoney = models.CharField(max_length=255)
    startingWeapons = models.ManyToManyField(Weapon, blank=True)
    startingArmor = models.ManyToManyField(Armor, blank=True)
    startingItems = models.ManyToManyField(Item, blank=True, related_name='items')
    startingTools = models.ManyToManyField(Item, blank=True, related_name='tools')
    startingSpells = models.ManyToManyField(Spell, blank=True)
    startingSkill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-baseHP', 'name']


class Race(models.Model):
    class BodyTypeName(models.TextChoices):
        Pequeno = 'Pequeno', _('Pequeno')
        Normal = 'Normal', _('Normal')
        Grande = 'Grande', _('Grande')

    class AttributeName(models.TextChoices):
        Corpo = 'Corpo', _('Corpo')
        Destreza = 'Destreza', _('Destreza')
        Conhecimento = 'Conhecimento', _('Conhecimento')
        Mente = 'Mente', _('Mente')
        Social = 'Social', _('Social')

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=race_ilustration_upload, blank=True, null=True)
    age = models.TextField()
    bodyType = models.CharField(max_length=7, choices=BodyTypeName.choices, default=BodyTypeName.Normal)
    height = models.TextField()
    baseMovement = models.FloatField()
    magicAffinity = models.ManyToManyField(MagicElement, blank=True)
    attributeIncrease1 = models.CharField(max_length=12, choices=AttributeName.choices, null=True, blank=True)
    attributeIncreaseValue1 = models.IntegerField()
    attributeIncrease2 = models.CharField(max_length=12, choices=AttributeName.choices, null=True, blank=True)
    attributeIncreaseValue2 = models.IntegerField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    normalCharCanUse = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Character(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100, blank=True)
    lore = models.TextField(blank=True)
    ilustration = models.ImageField(upload_to=character_ilustration_upload, blank=True, null=True)
    
    creator = models.ForeignKey(User, related_name='creator_user', on_delete=models.CASCADE)
    editor = models.ForeignKey(User, related_name='editor_user', blank=True, null=True, on_delete=models.CASCADE)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    magicGroup = models.ForeignKey(MagicGroup, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    spells = models.ManyToManyField(Spell, blank=True)
    armor = models.ForeignKey(Armor, on_delete=models.SET_NULL, null=True, blank=True)

    crowns = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    remainingPoints = models.IntegerField()
    proficiency = models.IntegerField(default=1)
    
    createdAt = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        used_points = 0
        attributes = CharacterAttribute.objects.filter(character=self.id)
        for attribute in attributes:
            used_points += attribute.level
        self.remainingPoints = (85 + ((self.level - 1) * 5)) - used_points
        self.proficiency = (self.level // 5) + 1
        super(Character, self).save(*args, **kwargs)


class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f'{self.item.name} x{self.amount}'
  

class CharacterExpertise(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    level = models.IntegerField()
    proficient = models.BooleanField(default=False)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.character.name} - {self.expertise.name}'
    
    def save(self, *args, **kwargs):
        if self.proficient:
            self.value = self.level + self.character.proficiency
        else:
            self.value = self.level
        super(CharacterExpertise, self).save(*args, **kwargs)
    

class CharacterAttribute(models.Model):
    name = models.CharField(max_length=255)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    expertises = models.ManyToManyField(CharacterExpertise, blank=True)
    level = models.IntegerField()
    remaining = models.IntegerField()

    def __str__(self):
        return f'{self.character.name} - {self.name}'
    
    def save(self, *args, **kwargs):
        used_points = 0
        for expertise in self.expertises.all():
            used_points += expertise.level + 1
        self.remaining = self.level - used_points
        super(CharacterAttribute, self).save(*args, **kwargs)
    

class CharacterStats(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    corpo = models.ForeignKey(CharacterAttribute, related_name='corpo', on_delete=models.CASCADE, null=True, blank=True)
    destreza = models.ForeignKey(CharacterAttribute, related_name='destreza', on_delete=models.CASCADE, null=True, blank=True)
    conhecimento = models.ForeignKey(CharacterAttribute, related_name='conhecimento', on_delete=models.CASCADE, null=True, blank=True)
    mente = models.ForeignKey(CharacterAttribute, related_name='mente', on_delete=models.CASCADE, null=True, blank=True)
    social = models.ForeignKey(CharacterAttribute, related_name='social', on_delete=models.CASCADE, null=True, blank=True)
    
    maxHP = models.IntegerField(null=True, blank=True)
    currentHP = models.IntegerField(null=True, blank=True)
    maxEP = models.IntegerField(null=True, blank=True)
    currentEP = models.IntegerField(null=True, blank=True)
    armorClass = models.IntegerField(null=True, blank=True)

    passivePerception = models.IntegerField(null=True, blank=True)
    movement = models.FloatField(default=0)

    maxWeight = models.FloatField(null=True, blank=True)
    currentWeight = models.FloatField(null=True, blank=True)
    weightStatus = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.character.name}'
    
    def save(self, *args, **kwargs):
        self.corpo = CharacterAttribute.objects.filter(character=self.character, name="Corpo").first()
        self.destreza = CharacterAttribute.objects.filter(character=self.character, name="Destreza").first()
        self.conhecimento = CharacterAttribute.objects.filter(character=self.character, name="Conhecimento").first()
        self.mente = CharacterAttribute.objects.filter(character=self.character, name="Mente").first()
        self.social = CharacterAttribute.objects.filter(character=self.character, name="Social").first()

        specialization = self.character.specialization
        race = self.character.race
        bodyTypes = {"Pequeno": 0.5, "Normal": 1, "Grande": 1.5}

        vitalidade = self.corpo.expertises.filter(expertise__name="Vitalidade").first().level
        self.maxHP = (specialization.baseHP + vitalidade) + ((self.character.level - 1) * (specialization.levelHP + vitalidade))
        if self.currentHP is None:
            self.currentHP = self.maxHP

        energia = self.corpo.expertises.filter(expertise__name="Energia").first().level
        self.maxEP = specialization.baseMP + 5 * energia
        if self.currentEP is None:
            self.currentEP = self.maxEP

        reflexos = self.destreza.expertises.filter(expertise__name="Reflexos").first().level
        if self.character.skills.filter(name="Armadura Natural").exists():
            self.armorClass = 12 + reflexos
        else:
            self.armorClass = 10 + reflexos

        percepcao = self.mente.expertises.filter(expertise__name="Percepção").first().level
        self.passivePerception = 10 + percepcao

        agilidade = self.destreza.expertises.filter(expertise__name="Agilidade").first().level
        if agilidade >= 10:
            self.movement = race.baseMovement + 3
        elif agilidade >= 5:
            self.movement = race.baseMovement + 1.5
        else:
            self.movement = race.baseMovement

        forca = self.corpo.expertises.filter(expertise__name="Força").first().level
        if forca == 0:
            forca = 0.75
        elif forca < 0:
            forca = 0.5

        self.maxWeight = bodyTypes[race.bodyType] * (forca * 6)
        if self.currentWeight is None:
            self.currentWeight = self.maxWeight

        if self.currentWeight < self.maxWeight:
            self.weightStatus = "Normal"
        elif self.currentWeight >= self.maxWeight * 1.5:
            self.weightStatus = "Extremamente Pesado"
        else:
            self.weightStatus = "Pesado"
        
        super(CharacterStats, self).save(*args, **kwargs)


class CharacterProficiencies(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    expertises = models.ManyToManyField(Expertise, blank=True)
    weapons = models.ManyToManyField(Weapon, blank=True)
    elements = models.ManyToManyField(MagicElement, blank=True)
    tools = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.character.name
    

class CharacterWeapon(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    damageType = models.ForeignKey(DamageType, on_delete=models.CASCADE, null=True, blank=True)
    weight = models.FloatField()
    modifier = models.ForeignKey(Modifier, on_delete=models.SET_NULL, null=True, blank=True)
    attackRoll = models.CharField(max_length=255, null=True, blank=True)
    finalDamage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.character.name} - {self.weapon.name}'
    
    def save(self, *args, **kwargs):
        match self.weapon.combat:
            case 'Combate':
                weapon_scaling = CharacterExpertise.objects.filter(
                    character=self.character,
                    expertise__name='Combate'
                ).first()
                attack_modifier = weapon_scaling.value
                weapon_scaling = weapon_scaling.level
            case 'Precisão':
                weapon_scaling = CharacterExpertise.objects.filter(
                    character=self.character,
                    expertise__name='Precisão'
                ).first()
                attack_modifier = weapon_scaling.value
                weapon_scaling = weapon_scaling.level
            case _:
                attack_modifier = 0
                weapon_scaling = 0

        is_arcane = self.weapon.traits.filter(
            name='Arcana'
        ).first()

        if is_arcane:
            weapon_scaling = CharacterExpertise.objects.filter(
                character=self.character,
                expertise__name='Arcanismo'
            ).first().level

        match weapon_scaling:
            case weapon_scaling if weapon_scaling < 0:
                weapon_scaling *= -1
                self.finalDamage = f'{self.weapon.baseDamage} - {weapon_scaling}'
            case 0:
                self.finalDamage = f'{self.weapon.baseDamage}'
            case weapon_scaling if weapon_scaling > 0:
                self.finalDamage = f'{self.weapon.baseDamage} + {weapon_scaling}'

        match attack_modifier:
            case attack_modifier if attack_modifier < 0:
                attack_modifier *= -1
                self.attackRoll = f'1d20 - {attack_modifier}'
            case 0:
                self.attackRoll = '1d20'
            case attack_modifier if attack_modifier > 0:
                self.attackRoll = f'1d20 + {attack_modifier}'

        super(CharacterWeapon, self).save(*args, **kwargs)

