from django.core.exceptions import ValidationError
import re

def clear_name(name):
    new_name = ''.join(e for e in name if e.isalnum() or e.isspace())
    new_name = ' '.join(new_name.split())
    return new_name

def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            'Senha muito fraca'
        )