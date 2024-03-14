from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.users_forms_validators import *
import re

class RegisterUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Nome'
        self.fields['first_name'].required = True
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ex.: João'

        self.fields['last_name'].label = 'Sobrenome'
        self.fields['last_name'].required = True
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ex.: Souza'

        self.fields['username'].label = 'Nome de usuário'
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs['placeholder'] = 'Como as pessoas verão seu nome'

        self.fields['email'].label = 'E-mail'
        self.fields['email'].required = True
        self.fields['email'].widget.attrs['placeholder'] = 'Ex.: nome@email.com'

        self.fields['password'].label = 'Senha'
        self.fields['password'].validators = [strong_password]
        self.fields['password'].widget = forms.PasswordInput()

        self.fields['password2'].label = 'Repita sua senha'
        self.fields['password2'].required = True
        self.fields['password2'].widget = forms.PasswordInput()

    password2 = forms.CharField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        data = clear_name(data)

        return data
    
    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        data = clear_name(data)

        return data
    
    def clean_username(self):
        data = self.cleaned_data.get('username')
        regex = re.compile(r'[\s!@#$%^&*()_+\-=\[\]{};\'\\:"|,.<>\/?]')
        if regex.search(data):
            raise ValidationError(
                'Utilize apenas letras e números',
                code='invalid'
            )
        if User.objects.filter(username=data).exists():
            raise ValidationError(
                'Nome de usuário já cadastrado',
                code='invalid'
            )

        return data
    
    def clean_email(self):
        data = self.cleaned_data.get('email')
        if User.objects.filter(email=data).exists():
            raise ValidationError(
                'E-mail já cadastrado',
                code='invalid'
            )
        
        return data
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password2': 'As senhas não coincidem'
            })

        return cleaned_data