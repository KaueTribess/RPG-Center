from django.urls import path
from app_legends import views

app_name = 'legends'

urlpatterns = [
    path('', views.main_view, name="legends"),
    path('character/list/', views.CharactersList.as_view(), name="character_list"),
    path('character/sheet/<int:id>/', views.CharacterSheet.as_view(), name="character_sheet"),
    path('character/edit/<int:id>/', views.CharacterEdit.as_view(), name="character_edit"),
    path('spell/<int:id>/', views.main_view, name="spell"),
    path('item/<int:id>/', views.main_view, name="item"),
    path('skill/<int:id>/', views.main_view, name="skill"),
    path('search/', views.main_view, name="search"),
]