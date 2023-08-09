"""hotel_room_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index
from django.urls import include
from core.views import dashboard
from booking.views import booking
from booking.views import booking_self
from booking.views import booking_room
from booking.views import capture_guest_data

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name="login-page"),
    path('', dashboard, name='home-page'),
    path('dashboard/', dashboard, name="dashboard"),
    path('booking', booking, name='customer-booking'),
    path('booking/self', booking_self, name='booking_self'),
    path('booking/room/<str:guest_uid>/<str:room_uid>', booking_room, name='booking_room'),
    path('capture/guest/information', capture_guest_data, name="capture_guest_information"),
    
    
    path('room/', include('room.urls')),    
    path('user/', include('user_manager.urls')),
    # path('admin', include('administrator.urls')),

    # Admin pages
    path('hotel/', include('hotel.urls')),
]
