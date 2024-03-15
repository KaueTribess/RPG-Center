from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import LoginUserForm
from app_main.models import RPGSystem

class LoginView(View):

    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')
        form = LoginUserForm()
        context = {
            'systems': systems,
            'form': form,
            'form_title': 'Entrar',
            'form_action': reverse('users:login_create'),
        }

        return render(request, 'users/pages/login_user.html', context)