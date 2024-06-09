from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_legends.models import Race
from app_main.models import RPGSystem

class RaceList(View):

    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')
        playable_races = Race.objects.filter(
            normalCharCanUse=True,
        ).order_by('name')
        non_playable_races = Race.objects.filter(
            normalCharCanUse=False,
        ).order_by('name')

        context = {
            'systems': systems,
            'playable_races': playable_races,
            'non_playable_races': non_playable_races,
        }

        return render(request, 'legends/pages/race-list.html', context)
    