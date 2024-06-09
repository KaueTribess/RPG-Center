from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import CharacterWeapon

class CharacterWeaponUpdateName(View):
    def post(self, request, id):
        character_weapon = CharacterWeapon.objects.filter(
            id=id
        ).first()
        new_name = str(request.POST.get('weapon_name'))
        character_weapon.name = new_name
        character_id = character_weapon.character.id
        character_weapon.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': character_id}))
    