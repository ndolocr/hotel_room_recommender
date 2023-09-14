from django.urls import path
from score import views

urlpatterns = [
    path('', views.viewAll, name='scores-view-all'),
    path('add', views.addScore, name='score-add'),
]