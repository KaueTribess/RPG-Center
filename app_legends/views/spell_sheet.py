from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.models import Spell
from app_main.models import RPGSystem
from django.http import Http404

class SpellSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        spell = Spell.objects.filter(id=id).first()
        if not spell:
            raise Http404()
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'spell': spell,
        }

        return render(request, 'legends/pages/spell-sheet.html', context)