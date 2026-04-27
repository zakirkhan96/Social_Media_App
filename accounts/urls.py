from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from posts import views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
