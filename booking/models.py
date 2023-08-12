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
from user_manager.models import UserNode

from guest.models import Guest
from guest.models import Allergy
from guest.models import Illness
from guest.models import ChildGuest
from guest.models import Disability
from guest.models import GuestAttributes
# Create your models here.

class Reservation(StructuredNode):
    uid = UniqueIdProperty()    
    date_to = DateProperty()
    date_from = DateProperty()
    amount_paid = StringProperty()
    religious_book = StringProperty()    

    pet = RelationshipTo(Pet, 'Pet in the room')
    room = RelationshipTo(Room, 'Guest made Reservation')
    guest = RelationshipTo(UserNode, 'Guest made Reservation')

    updated_on = DateProperty()
    created_on = DateProperty()
