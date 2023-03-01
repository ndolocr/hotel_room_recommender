from django.urls import path
from room import views

urlpatterns = [
    # Room
    path('add', views.addRoom, name='room-add'),
    path('', views.getAllRooms, name='room-view-all'),
    path('view/<str:uid>', views.getSingleRoom, name='room-view-single'),

    # Room View
    path('view/preference/add', views.addRoomViewPreference, name='room-view-preference-add'),
    path('view/preference', views.getAllRoomViewPreferences, name='room-view-preference-view-all'),
    path('view/preference/<str:uid>', views.getSingleRoomType, name="room-view-preference-single"),

    # Room Type
    path('type/add', views.addRoomType, name='room-type-add'),
    path('type', views.getAllRoomTypes, name='room-type-view-all'),
    path('type/view/<str:uid>', views.getSingleRoomType, name="room-type-view-single"),
    
    # Room Element
    path('element/add', views.addRoomElement, name='room-element-add'),
    path('element', views.getAllRoomElements, name='room-element-view-all'),
    path('element/view/<str:uid>', views.getSingleRoomElement, name="room-element-view-single"),
    

    path('connect/to/hotel', views.connectHotelToRoom, name="connect-hotel-to-room"),
    path('connect/to/room/type', views.connectRoomTypeToRoom, name="connect-room-type-to-room"),
    path('connect/to/room/element', views.connectRoomElelemntToRoom, name="connect-room-element-to-room"),
]