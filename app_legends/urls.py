from django.urls import path
from app_legends import views

app_name = 'legends'

urlpatterns = [
    path('', views.main_view, name="legends"),
    path('character/list/', views.CharactersList.as_view(), name="character_list"),
    path('character/sheet/<int:id>/', views.CharacterSheet.as_view(), name="character_sheet"),
    path('character/edit/info/<int:id>/', views.CharacterEdit.as_view(), name="character_edit"),
    path('character/edit/image/<int:id>/', views.character_edit_image, name="character_edit_image"),
    path('character/edit/attribute/<int:id>/', views.CharacterEditAttribute.as_view(), name="character_edit_attribute"),
    path('character/edit/expertise/<int:id>/', views.CharacterEditExpertise.as_view(), name="character_edit_expertise"),
    path('character/edit/stats/<int:id>/', views.CharacterEditStatsBars.as_view(), name="character_edit_stats"),
    path('character/edit/level/<int:id>/', views.CharacterEditLevel.as_view(), name="character_edit_level"),
    path('character/edit/skills/<int:id>/', views.CharacterEditSkills.as_view(), name="character_edit_skills"),

    path('character/weapon/create/<int:id>/', views.CharacterWeaponCreate.as_view(), name="character_weapon_create"),
    path('character/weapon/delete/<int:id>/', views.CharacterWeaponDelete.as_view(), name="character_weapon_delete"),
    path('character/weapon/update/name/<int:id>/', views.CharacterWeaponUpdateName.as_view(), name="character_weapon_update_name"),
    path('character/weapon/update/weapontype/<int:id>/', views.CharacterWeaponUpdateWeaponType.as_view(), name="character_weapon_update_weapon_type"),
    path('character/weapon/update/modifier/<int:id>/', views.CharacterWeaponUpdateModifier.as_view(), name="character_weapon_update_modifier"),
    path('character/weapon/update/damagetype/<int:id>/', views.CharacterWeaponUpdateDamageType.as_view(), name="character_weapon_update_damage_type"),

    path('race/list/', views.RaceList.as_view(), name="race_list"),
    path('race/<int:id>/', views.RaceSheet.as_view(), name="race"),

    path('specialization/<int:id>/', views.main_view, name="specialization"),
    path('skill/<int:id>/', views.SkillSheet.as_view(), name="skill"),

    path('spell/list/', views.SpellList.as_view(), name="spell_list"),
    path('spell/<int:id>/', views.SpellSheet.as_view(), name="spell"),

    path('item/<int:id>/', views.main_view, name="item"),
    path('search/', views.main_view, name="search"),
]