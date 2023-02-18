from django.urls import path
from hotel import views


urlpatterns = [
    path('add', views.addHotel, name='hotel-add'),
    path('update/<str:uid>', views.uodateHotel, name='hotel-update'),
]
