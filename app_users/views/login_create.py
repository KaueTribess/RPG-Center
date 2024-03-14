from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from app_users.forms import LoginUserForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login

class LoginCreate(View):
    def get(self, request):
        raise Http404()
    
    def post(self, request):
        POST = request.POST
        form = LoginUserForm(POST)
        home_url = reverse('main:home')
        login_url = reverse('users:login_view')

        if form.is_valid():
            authenticated_user = authenticate(
                username = form.cleaned_data.get('username', ''),
                password = form.cleaned_data.get('password', ''),
            )

            if authenticated_user is not None:
                messages.success(request, 'Logado com sucesso')
                login(request, authenticated_user)
                return redirect(home_url)
            else:
                messages.error(request, 'Credenciais inválidas')
        else:
            messages.error(request, 'Erro ao validar credenciais')

        return redirect(login_url)