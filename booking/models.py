from django.db import models
from neomodel import(
    Relationship,
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
    IntegerProperty,
    ArrayProperty, 
    DateProperty
)

from room.models import Room
from user_manager.models import Pet
from user_manager.models import UserNode

# from guest.models import Guest
# from guest.models import Allergy
# from guest.models import Illness
# from guest.models import ChildGuest
# from guest.models import Disability
# from guest.models import GuestAttributes

from room.models import RoomType
from room.models import RoomType
from room.models import RoomScent
from room.models import RoomLight
from room.models import RoomElement
from room.models import RoomHumidity
from room.models import RoomTemprature
from room.models import RoomViewPreference
from room.models import RoomAccessibility
# Create your models here.

class Reservation(StructuredNode):
    uid = UniqueIdProperty()    
    date_to = DateProperty()
    date_from = DateProperty()
    min_light = StringProperty()
    max_light = StringProperty()
    amount_paid = StringProperty()         
    min_humidity = StringProperty()
    max_humidity = StringProperty()
    min_temprature = StringProperty()
    max_temprature = StringProperty()
    religious_book = StringProperty()

    pet = RelationshipTo(Pet, 'Pet in the room')
    room = RelationshipTo(Room, 'Room Reserved')
    room_type = RelationshipTo(RoomType, 'Room type chosen')
    guest = RelationshipTo(UserNode, 'Guest made Reservation')
    room_scent = RelationshipTo(RoomScent, 'Room scent chosen')
    room_element = RelationshipTo(RoomElement, 'Room element chosen')
    room_view = RelationshipTo(RoomViewPreference, 'Room view chosen')    
    
    room_access = RelationshipTo(RoomAccessibility, 'Room access chosen')
       

    updated_on = DateProperty()
    created_on = DateProperty()
