from django.urls import path
from hotel import views


urlpatterns = [
    path('add', views.addHotel, name='hotel-add'),
    path('', views.getAllHotels, name='hotel-get-all'),
    path('update/<str:uid>', views.updateHotel, name='hotel-update'),
    path('delete/<str:uid>', views.deleteHotel, name='hotel-delete'),
    path('get/single/<str:uid>', views.getSingleHotel, name='hotel-get-single'),
]
