from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_legends.models import Character, CharacterStats

class CharacterEditStatsBars(View):
    
    def post(self, request, id):
        character = Character.objects.filter(id=id).first()
        character_stats = CharacterStats.objects.filter(character=character).first()
        if request.POST.get('type') == 'energy':
            character_stats.currentEP = int(request.POST.get('current_ep'))
            character_stats.save()
        if request.POST.get('type') == 'health':
            character_stats.currentHP = int(request.POST.get('current_hp'))
            character_stats.save()
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    