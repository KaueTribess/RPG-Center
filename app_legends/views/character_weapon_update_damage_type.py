from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import CharacterWeapon, DamageType

class CharacterWeaponUpdateDamageType(View):
    def post(self, request, id):
        character_weapon = CharacterWeapon.objects.filter(
            id=id
        ).first()
        new_damage_type = DamageType.objects.filter(
            name=str(request.POST.get('weapon_damage_type'))
        ).first()
        character_weapon.damageType = new_damage_type
        character_id = character_weapon.character.id
        character_weapon.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': character_id}))
    