from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.models import Character
from app_legends.forms import CharacterEditImageForm
from app_main.models import RPGSystem
from django.http import Http404
from django.urls import reverse
from django.contrib import messages

class CharacterEditImage(View):
    ...
    # def get_character(self, request, id):
    #     character = Character.objects.filter(
    #         Q(public=True) |
    #         Q(editor=request.user),
    #         id=id,
    #     ).first()
    #     if not character:
    #         raise Http404()
    #     return character

    # def get(self, request, id):
    #     systems = RPGSystem.objects.all().order_by('name')
    #     character = self.get_character(request, id)
    #     form = CharacterEditImageForm(request.POST or None, request.FILES or None)
    #     context = {
    #         'systems': systems,
    #         'header_title': 'Legends',
    #         'character': character,
    #         'form': form,
    #     }

    #     return render(request, 'legends/pages/character_edit_image.html', context)
    
    # def post(self, request, id):
    #     character = self.get_character(request, id)
    #     form = CharacterEditImageForm(request.POST or None, request.FILES or None)

    #     if form.is_valid():
    #         print('deu certo')
        
    #     url = reverse('legends:character_list')
    #     return redirect(url)

def character_edit_image(request, id):
    character = Character.objects.filter(
            Q(public=True) |
            Q(editor=request.user),
            id=id,
        ).first()
    form = CharacterEditImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_instance = form.save(commit=False)
        character.ilustration = new_instance.ilustration
        character.save()

    context = {
        'form': form,
        'return': reverse('legends:character_sheet', args={id,}),
    }
    return render(request, 'legends/pages/character_edit_image.html', context)