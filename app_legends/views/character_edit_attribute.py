from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from app_legends.models import Character, CharacterExpertise, CharacterAttribute
from app_legends.forms import CharacterEditForm
from app_main.models import RPGSystem
from django.http import Http404, JsonResponse
from django.contrib import messages

class CharacterEditAttribute(View):
    
    def post(self, request, id):
        character = Character.objects.filter(id=id).first()
        attribute_id = request.POST.get('attribute_id')
        attribute = CharacterAttribute.objects.filter(id=attribute_id).first()
        if attribute:
            if request.POST.get('type') == 'raise':
                if attribute.level < 70 and character.remainingPoints > 0:
                    attribute.level += 1
                    attribute.save()
                    character.save()
            if request.POST.get('type') == 'decrease':
                if attribute.level > 0 and attribute.remaining > 0:
                    attribute.level -= 1
                    attribute.save()
                    character.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    