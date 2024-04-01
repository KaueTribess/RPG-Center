from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from app_legends.models import Character, CharacterStats
from app_legends.forms import CharacterEditForm
from app_main.models import RPGSystem
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(
    login_required(login_url='users:login_view', redirect_field_name='next'),
    name='dispatch'
)
class CharacterEdit(View):

    def get_character(self, request, id):
        character = Character.objects.filter(
            id=id,
            editor=request.user,
        ).first()

        if not character:
            raise Http404()

        return character

    def get(self, request, id):
        character = self.get_character(request, id)
        systems = RPGSystem.objects.all().order_by('name')

        form = CharacterEditForm(
            request.POST or None,
            request.FILES or None,
            instance=character
        )

        context = {
            'systems': systems,
            'header_title': 'Legends',
            'form': form,
            'form_title': f'Editor de ficha - {character.name}',
            'character': character,
        }

        return render(request, 'legends/pages/character_edit.html', context)
    
    def post(self, request, id):
        character = self.get_character(request, id)
        character_stats = CharacterStats.objects.filter(character=character).first()

        form = CharacterEditForm(
            request.POST or None,
            request.FILES or None,
            instance=character
        )

        if form.is_valid():
            character = form.save(commit=False)
            if not character.creator:
                character.creator = request.user
            if not character.editor:
                character.editor = request.user
            
            character.save()
            character_stats.save()
            
            messages.success(request, 'Personagem editado com sucesso!')
            
        return redirect(reverse('legends:character_sheet', kwargs={'id': id}))
    