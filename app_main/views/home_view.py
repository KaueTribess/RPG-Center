from django.views import View
from app_main.models import Tag, RPGSystem
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')

        context = {
            'systems': systems
        }

        return render(request, 'main/pages/home.html', context)