from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import RegisterUserForm
from app_main.models import RPGSystem

class RegisterView(View):

    def get(self, request):
        systems = RPGSystem.objects.all().order_by('name')
        register_form_data = request.session.get('register_form_data', None)
        form = RegisterUserForm(register_form_data)
        context = {
            'systems': systems,
            'form': form,
            'form_title': 'Cadastro',
            'form_action': reverse('users:register_create'),
        }

        return render(request, 'users/pages/register_user.html', context)
    