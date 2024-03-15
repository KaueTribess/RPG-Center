from django.views import View
from django.shortcuts import render
from django.db.models import Q
from app_legends.models import Character
from app_main.models import RPGSystem
from django.http import Http404

class CharacterSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        character = Character.objects.filter(
            Q(public=True) |
            Q(editor=request.user),
            id=id,
        ).first()
        if not character:
            raise Http404()
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'character': character,
        }

        return render(request, 'legends/pages/character_sheet.html', context)
    