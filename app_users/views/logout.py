from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(
    login_required(login_url='users:login_view', redirect_field_name='next'),
    name='dispatch'
)
class Logout(View):
    def post(self, request):
        if request.POST.get('username') == request.user.username:
            logout(request)
            messages.success(request, 'Desconectado com sucesso')
        return redirect('users:login_view')
        