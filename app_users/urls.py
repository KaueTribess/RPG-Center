from django.urls import path
from app_users import views

app_name = 'users'

urlpatterns = [
    path('', views.main_view, name="users"),
    path('register/', views.RegisterView.as_view(), name="register_view"),
    path('register/create', views.RegisterCreate.as_view(), name="register_create"),
    path('login/', views.LoginView.as_view(), name="login_view"),
    path('login/create', views.LoginCreate.as_view(), name="login_create"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('profile/<slug:slug>/', views.main_view, name="profile"),
]