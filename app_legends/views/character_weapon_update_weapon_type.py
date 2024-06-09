from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import CharacterWeapon, Weapon

class CharacterWeaponUpdateWeaponType(View):
    def post(self, request, id):
        character_weapon = CharacterWeapon.objects.filter(
            id=id
        ).first()
        new_weapon_type = Weapon.objects.filter(
            name=str(request.POST.get('weapon_type')),
        ).first()
        character_weapon.weapon = new_weapon_type
        character_id = character_weapon.character.id
        if character_weapon.modifier not in character_weapon.weapon.modifiers.all():
            character_weapon.modifier = None
        character_weapon.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': character_id}))
    