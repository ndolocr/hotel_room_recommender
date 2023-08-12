from django.urls import path
from room import views

urlpatterns = [
    

    # Room View
    path('view/preference/add', views.addRoomViewPreference, name='room-view-preference-add'),
    path('view/preference', views.viewAllRoomViewPreferences, name='room-view-preference-all'),
    # path('view/preference/<str:uid>', views.getSingleRoomViewPreference, name="room-view-preference-single"),

    # Room Type
    path('type/add', views.addRoomType, name='room-type-add'),
    path('type', views.getAllRoomTypes, name='room-type-view-all'),
    path('type/view/<str:uid>', views.getSingleRoomType, name="room-type-view-single"),
    
    # Room Element
    path('element/add', views.addRoomElement, name='room-element-add'),
    path('element', views.getAllRoomElements, name='room-element-view-all'),
    path('element/view/<str:uid>', views.getSingleRoomElement, name="room-element-view-single"),

    # Room Light
    path('light/add', views.addRooLight, name='room-light-add'),
    path('light', views.viewAllRoomLight, name='room-light-view-all'),

    # Room Scent
    path('scent/add', views.addRoomScent, name='room-scent-add'),
    path('scent', views.viewAllRoomScent, name='room-scent-view-all'),

    # Room Temprature
    path('temprature/add', views.addRoomTemprature, name='room-temprature-add'),
    path('temprature', views.getAllRoomTemprature, name='room-temprature-view-all'),

    # Room Humidity
    path('humidity/add', views.addRoomHumidity, name='room-humidity-add'),
    path('humidity', views.viewAllRoomHumidity, name = 'room-humidity-view-all'),

    # Room Accessibility
    path('accessibility/add', views.addAccessibilityFeature, name='room-accessibility-add'),
    path('accessibility', views.getAllAccessibilityFeatures, name='room-accessibility-view-all'),
    

    path('connect/to/hotel', views.connectHotelToRoom, name="connect-hotel-to-room"),
    path('connect/to/room/type', views.connectRoomTypeToRoom, name="connect-room-type-to-room"),
    path('connect/to/room/element', views.connectRoomElelemntToRoom, name="connect-room-element-to-room"),

    # Room
    path('add', views.addRoom, name='room-add'),
    path('', views.getAllRooms, name='room-view-all'),
    path('view/<str:uid>', views.getSingleRoom, name='room-view-single'),
    
    # filter Rooms
    path('filter', views.filterRooms, name='filter-rooms'), 

    # Book a room
    path('book/room', views.bookRoom, name='book-room'),
]