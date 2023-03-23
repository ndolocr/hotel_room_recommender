from django.urls import path
from user_manager import views
urlpatterns = [
    path('home', views.login, name="login"),
    path('register', views.register, name='user-registration'),    
]