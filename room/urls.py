from django.urls import path
from room import views

urlpatterns = [
    path('', views.getAllRooms, name='get-all-rooms'),
    path('add', views.addRoom, name='room-details'),
    path('element/add', views.addRoomElement, name='element-add'),
    path('room/type/add', views.addRoomType, name='room-type-add'),
    path('connect/to/hotel', views.connectHotelToRoom, name="connect-hotel-to-room"),
    path('connect/to/room/type', views.connectRoomTypeToRoom, name="connect-room-type-to-room"),
    path('connect/to/room/element', views.connectRoomElelemntToRoom, name="connect-room-element-to-room"),
]