from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.models import Race
from app_main.models import RPGSystem
from django.http import Http404

class RaceSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        race = Race.objects.filter(id=id).first()
        if not race:
            raise Http404()
        skills = race.skills.all().order_by('name')
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'race': race,
            'skills': skills,
        }

        return render(request, 'legends/pages/race_sheet.html', context)
    
    def post(self, request, id):
        return redirect('legends:character_sheet', kwargs={'id': id})