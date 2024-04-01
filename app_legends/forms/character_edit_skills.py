from django import forms
from app_legends.models import Character

class CharacterEditSkillsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['skills'].label = 'Habilidades'

    class Meta:
        model = Character
        fields = ['skills']