from django import forms
from app_legends.models import Character

class CharacterEditImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['ilustration'].label = 'Imagem:'

    class Meta:
        model = Character
        fields = ['ilustration']