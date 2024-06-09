from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import Character, CharacterWeapon, Weapon

class CharacterWeaponCreate(View):
    def post(self, request, id):
        character = Character.objects.filter(
            id=id
        ).first()
        base_weapon = Weapon.objects.filter(
            name='Porrete'
        ).first()
        new_character_weapon = CharacterWeapon.objects.create(
            character=character,
            weapon=base_weapon,
            name='Nova arma!',
            damageType=base_weapon.damageType,
            weight=base_weapon.weight,
        )

        character.save()
        new_character_weapon.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    