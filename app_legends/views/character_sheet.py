from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from app_legends.forms import CharacterEditSkillsForm
from app_legends.models import Character, CharacterAttribute, CharacterExpertise, CharacterStats, CharacterWeapon, Weapon, DamageType
from app_main.models import RPGSystem
from django.http import Http404

class CharacterSheet(View):

    def get(self, request, id):
        systems = RPGSystem.objects.all().order_by('name')
        character = Character.objects.filter(
            Q(public=True) |
            Q(editor=request.user),
            id=id,
        ).first()
        if not character:
            raise Http404()
        character_attributes = CharacterAttribute.objects.filter(
            character=character
        ).order_by('id')
        character_expertises = CharacterExpertise.objects.filter(
            character=character
        ).order_by('id')
        character_stats = CharacterStats.objects.filter(
            character=character
        ).first()
        character_weapons = CharacterWeapon.objects.filter(
            character=character
        ).order_by('id')
        base_weapons = Weapon.objects.filter(
            rarity='Comum'
        ).order_by('combat', '-type')
        damage_types = DamageType.objects.all().order_by('name')
        skills_form = CharacterEditSkillsForm(
            request.POST or None,
            instance=character
        )
        
        context = {
            'systems': systems,
            'header_title': 'Legends',
            'base_weapons': base_weapons,
            'character': character,
            'char_attrs': character_attributes,
            'char_exper': character_expertises,
            'char_stats': character_stats,
            'char_weapons': character_weapons,
            'damage_types': damage_types,
            'skills_form': skills_form,
        }

        return render(request, 'legends/pages/character-sheet.html', context)
    
    def post(self, request, id):
        return redirect('legends:character_sheet', kwargs={'id': id})