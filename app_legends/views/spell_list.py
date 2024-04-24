from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_legends.models import Spell
from app_main.models import RPGSystem

class SpellList(View):

    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')
        spells = Spell.objects.filter(
            # public=True,
        ).order_by('-id')
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'spells': spells,
        }

        return render(request, 'legends/pages/spell-list.html', context)
    