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
    path('race/<int:id>/', views.RaceSheet.as_view(), name="race"),
    path('specialization/<int:id>/', views.main_view, name="specialization"),
    path('skill/<int:id>/', views.SkillSheet.as_view(), name="skill"),
    path('spell/list/', views.SpellList.as_view(), name="spell_list"),
    path('spell/<int:id>/', views.SpellSheet.as_view(), name="spell"),
    path('item/<int:id>/', views.main_view, name="item"),
    path('search/', views.main_view, name="search"),
]