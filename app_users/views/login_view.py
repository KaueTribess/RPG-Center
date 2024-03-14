from django.views import View
from django.shortcuts import render
from django.urls import reverse
from app_users.forms import LoginUserForm

class LoginView(View):

    def get(self, request):
        form = LoginUserForm()
        context = {
            'form': form,
            'form_title': 'Entrar',
            'form_action': reverse('users:login_create'),
            'form_class': 'form-large',
        }

        return render(request, 'users/pages/login_user.html', context)