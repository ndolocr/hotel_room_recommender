from django.urls import path
from user_manager import views
urlpatterns = [
    path('register', views.register, name='user-registration'),
]