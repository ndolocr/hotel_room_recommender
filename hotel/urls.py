from django.urls import path
from hotel import views


urlpatterns = [
    path('add', views.addHotel, name='hotel-add'),
    path('update/<str:uid>', views.updateHotel, name='hotel-update'),
    path('delete/<str:uid>', views.deleteHotel, name='hotel-delete'),
]
