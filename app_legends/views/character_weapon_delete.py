from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import CharacterWeapon

class CharacterWeaponDelete(View):
    def post(self, request, id):
        character_weapon = CharacterWeapon.objects.filter(
            id=id
        ).first()
        character_id = character_weapon.character.id
        character_weapon.delete()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': character_id}))
    