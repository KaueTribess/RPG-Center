from django.urls import path
from app_users import views

urlpatterns = [
    path('', views.main_view, name="users"),
    path('signin/', views.main_view, name="signin"),
    path('login/', views.main_view, name="login"),
    path('logout/', views.main_view, name="logout"),
    path('profile/<slug:slug>/', views.main_view, name="profile"),
]