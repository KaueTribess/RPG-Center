from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.users_forms_validators import *

class LoginUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Nome de usuário'
        self.fields['username'].required = True
        self.fields['username'].widget.attrs = {'class': 'span-2',}

        self.fields['password'].label = 'Senha'
        self.fields['password'].required = True
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs = {'class': 'span-2',}
        
    username = forms.CharField()
    password = forms.CharField()