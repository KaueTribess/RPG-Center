from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.models import Skill
from app_main.models import RPGSystem
from django.http import Http404

class SkillSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        skill = Skill.objects.filter(id=id).first()
        if not skill:
            raise Http404()
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'skill': skill,
        }

        return render(request, 'legends/pages/skill-sheet.html', context)