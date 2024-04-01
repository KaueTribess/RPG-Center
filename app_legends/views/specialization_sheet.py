from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.models import Specialization
from app_main.models import RPGSystem
from django.http import Http404

class SpecializationSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        specialization = Specialization.objects.filter(id=id).first()
        if not specialization:
            raise Http404()
        skills = specialization.skills.all().order_by('name')
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'specialization': specialization,
            'skills': skills,
        }

        return render(request, 'legends/pages/specialization_sheet.html', context)
        