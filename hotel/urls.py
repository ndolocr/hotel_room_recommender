from django.urls import path
from hotel import views


urlpatterns = [
    path('add', views.addHotel, name='hotel-add'),
]
