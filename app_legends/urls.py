from django.urls import path
from app_legends import views

urlpatterns = [
    path('', views.main_view, name="legends"),
    path('search/', views.main_view, name="search"),
    path('character/<int:id>/', views.main_view, name="character"),
    path('spell/<int:id>/', views.main_view, name="spell"),
    path('item/<int:id>/', views.main_view, name="item"),
    path('skill/<int:id>/', views.main_view, name="skill"),
    path('dashboard/<int:id>/', views.main_view, name="dashboard"),
]