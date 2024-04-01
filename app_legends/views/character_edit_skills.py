from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import Character, CharacterStats, CharacterExpertise

class CharacterEditSkills(View):
    
    def post(self, request, id):
        character = Character.objects.filter(id=id).first()
        character_stats = CharacterStats.objects.filter(character=character).first()
        character_expertise = CharacterExpertise.objects.filter(character=character).first()
        character.skills.set(request.POST.getlist('skills'))
        character.save()
        character_stats.save()
        character_expertise.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    