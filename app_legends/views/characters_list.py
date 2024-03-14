from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_legends.models import Character
from app_main.models import RPGSystem

class CharactersList(View):

    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')
        characters = Character.objects.filter(
            public=True,
        ).order_by('-id')
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'characters': characters,
        }

        return render(request, 'legends/pages/characters_list.html', context)
    