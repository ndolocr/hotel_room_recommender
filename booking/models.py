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
from guest.models import Pet
from guest.models import Guest
from guest.models import Allergy
from guest.models import Illness
from guest.models import ChildGuest
from guest.models import Disability
from guest.models import GuestAttributes
# Create your models here.

class Reservation(StructuredNode):
    pass
