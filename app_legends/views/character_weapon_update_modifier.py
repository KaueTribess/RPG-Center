from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import CharacterWeapon, Modifier

class CharacterWeaponUpdateModifier(View):
    def post(self, request, id):
        character_weapon = CharacterWeapon.objects.filter(
            id=id
        ).first()
        new_modifier = str(request.POST.get('weapon_modifier'))

        if new_modifier == 'Nenhum':
            character_weapon.modifier = None
        else:
            new_modifier = Modifier.objects.filter(
                name=new_modifier
            ).first()
            character_weapon.modifier = new_modifier
        
        character_id = character_weapon.character.id
        character_weapon.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': character_id}))
    