from django.urls import path
from score import views

urlpatterns = [
    path('', views.ViewAll, name='scores-view-all'),
]