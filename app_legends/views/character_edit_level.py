from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import Character, CharacterExpertise, CharacterAttribute, CharacterStats

class CharacterEditLevel(View):
    
    def post(self, request, id):
        character = Character.objects.filter(id=id).first()
        characterStats = CharacterStats.objects.filter(character=character).first()
        new_level = int(request.POST.get('level'))
        if new_level > 20:
            new_level = 20
        elif new_level < 1:
            new_level = 1
        character.level = new_level 
        character.save()
        characterStats.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    