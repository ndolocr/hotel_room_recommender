from django.urls import path
from administrator import views

urlpatterns = [
    path('', views.index, name='admin-home'),
]