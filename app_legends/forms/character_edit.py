from django import forms
from app_legends.models import Character

class CharacterEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Nome completo'
        self.fields['title'].label = 'Título'
        self.fields['race'].label = 'Raça'
        self.fields['specialization'].label = 'Classe'
        self.fields['level'].label = 'Nível'
        self.fields['magicGroup'].label = 'Grupo mágico'
        
        self.fields['lore'].label = 'História'
        self.fields['lore'].widget.attrs = {'class': 'span-2',}

        self.fields['public'].label = 'Público:'
        self.fields['public'].help_text = 'Ao marcar este campo você não poderá mais editar este personagem!'
        self.fields['public'].widget.attrs = {'class': 'warning checkbox no-change span-2',}

    class Meta:
        model = Character
        fields = 'name', 'title', 'race', 'specialization', 'level', 'magicGroup', 'lore', 'public'