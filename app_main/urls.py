from django.urls import path
from app_main import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name="home"), 
]