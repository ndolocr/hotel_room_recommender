from django.urls import path
from user_manager import views

urlpatterns = [
    path('home', views.login, name="login"),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register', views.self_register, name='user-self-registration'),    
]