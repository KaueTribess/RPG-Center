from django.db import models
from django.contrib.auth.models import User
from utils.legends_upload_paths import *
import PIL

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=race_ilustration_upload, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Specialization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=specialization_ilustration_upload, blank=True, null=True)

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class DamageType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

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

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    elements = models.ManyToManyField(MagicElement, blank=True)
    group = models.ForeignKey(MagicGroup, on_delete=models.CASCADE)
    castingTime = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    manaCost = models.IntegerField()

    ingredientCost = models.ManyToManyField(Item, blank=True)
    health = models.IntegerField(blank=True, null=True)
    heal = models.CharField(max_length=255, blank=True, null=True)
    damage = models.CharField(max_length=255, blank=True, null=True)
    damageType = models.ForeignKey(DamageType, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=100, blank=True)
    lore = models.TextField(blank=True)
    ilustration = models.ImageField(upload_to=character_ilustration_upload, blank=True, null=True)

    level = models.IntegerField()
    movement = models.FloatField()
    health = models.IntegerField()
    mana = models.IntegerField
    passivePerception = models.IntegerField()
    armorClass = models.IntegerField()

    maxWeight = models.FloatField()
    currentWeight = models.FloatField()
    weightStatus = models.CharField(max_length=255)

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    magicGroup = models.ForeignKey(MagicGroup, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    spells = models.ManyToManyField(Spell, blank=True)
    
    createdAt = models.DateField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f'{self.item.name} x{self.amount}'
    

class Wallet(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    goldCoins = models.IntegerField()
    silverCoins = models.IntegerField()

    def __str__(self):
        return self.character.name
    

class Modifier(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class WeaponTrait(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Weapon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ilustration = models.ImageField(upload_to=weapon_ilustration_upload, blank=True, null=True)
    range = models.CharField(max_length=255)
    weight = models.FloatField()
    traits = models.ManyToManyField(WeaponTrait, blank=True)
    weaponType = models.ForeignKey(WeaponType, on_delete=models.CASCADE)
    baseDamage = models.CharField(max_length=255)
    damageType = models.ForeignKey(DamageType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CharacterWeapon(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    amount = models.IntegerField()
    weight = models.FloatField()
    finalDamage = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.character.name} - {self.weapon.name} x{self.amount}'


class Expertise(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CharacterExpertise(models.Model):
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    level = models.IntegerField()

    def __str__(self):
        return f'{self.expertise.name}'
    

class CharacterAttribute(models.Model):
    name = models.CharField(max_length=255)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    expertises = models.ManyToManyField(CharacterExpertise, blank=True)
    level = models.IntegerField()

    def __str__(self):
        return f'{self.character.name} - {self.name}'
    

class CharacterProficiencies(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    expertises = models.ManyToManyField(Expertise, blank=True)
    weapons = models.ManyToManyField(WeaponType, blank=True)
    elements = models.ManyToManyField(MagicElement, blank=True)
    tools = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return self.character.name
    

