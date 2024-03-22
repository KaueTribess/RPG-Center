from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import Character, CharacterExpertise, CharacterAttribute, CharacterStats

class CharacterEditExpertise(View):
    
    def post(self, request, id):
        character = Character.objects.filter(id=id).first()
        characterStats = CharacterStats.objects.filter(character=character).first()
        attribute_id = request.POST.get('attribute_id')
        attribute = CharacterAttribute.objects.filter(id=attribute_id).first()
        expertise_id = request.POST.get('expertise_id')
        expertise = CharacterExpertise.objects.filter(id=expertise_id).first()
        if expertise and attribute:
            if request.POST.get('type') == 'raise':
                if expertise.level < 10 and attribute.remaining > 0:
                    expertise.level += 1
                    expertise.save()
                    attribute.save()
                    character.save()
                    characterStats.save()
            if request.POST.get('type') == 'decrease':
                if expertise.level > -1:
                    expertise.level -= 1
                    expertise.save()
                    attribute.save()
                    character.save()
                    characterStats.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    