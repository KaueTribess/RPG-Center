from django.views import View
from django.shortcuts import redirect
from app_users.forms import RegisterUserForm
from django.http import Http404
from django.contrib import messages

class RegisterCreate(View):
    def get(self, request):
        raise Http404()
    
    def post(self, request):
        POST = request.POST
        request.session['register_form_data'] = POST
        form = RegisterUserForm(POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            del(request.session['register_form_data'])
            return redirect('users:login_view')
        
        messages.error(request, 'Corrija os erros do formulário e envie novamente')

        return redirect('users:register_view')