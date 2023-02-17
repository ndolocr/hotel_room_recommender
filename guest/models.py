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

# Create your models here.
class Guest(StructuredNode):
    name = StringProperty()
    title = StringProperty()
    gender = StringProperty()
    address = StringProperty()
    religion = StringProperty()
    date_of_birth = DateProperty()
    nationality = StringProperty()
    phone_number = StringProperty()
    marital_status = StringProperty()
    country_of_residence = StringProperty()
    email = StringProperty(unique_index=True)    
    id_num = StringProperty(unique_index=True)

class childGuest(StructuredNode):
    name = StringProperty()
    gender = StringProperty()
    date_of_birth = DateProperty()

    guest = RelationshipTo(Guest, 'Child of')

class Pet(StructuredNode):
    name = StringProperty()
    pet_type = StringProperty()

    guest = RelationshipTo(Guest, 'Pet of Guest')

class GuestAttributes(StructuredNode):
    is_smoker = StringProperty()
    health_condition = StringProperty()

    guest = RelationshipTo(Guest, 'Attributes of Guest')
    
class Allergy(StructuredNode):
    name = StringProperty()
    description = StringProperty()
    guest = RelationshipTo(Guest, 'Guest allergy')
