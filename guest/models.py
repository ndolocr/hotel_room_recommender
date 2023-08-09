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
    name = StringProperty(required = True)
    title = StringProperty(required = True)
    gender = StringProperty(required = True)
    address = StringProperty(required = True)
    religion = StringProperty(required = True)
    date_of_birth = DateProperty(required = True)
    nationality = StringProperty(required = True)
    phone_number = StringProperty(required = True)
    marital_status = StringProperty(required = True)
    country_of_residence = StringProperty(required = True)
    email = StringProperty(unique_index=True, required = True)    
    id_num = StringProperty(unique_index=True, required = True)
    
    relaton_to_guest = StringProperty()
    guest = RelationshipTo('Guest', 'Guest of')

class ChildGuest(StructuredNode):
    name = StringProperty(required = False)
    gender = StringProperty(required = False)
    date_of_birth = DateProperty(required = False)

    guest = RelationshipTo(Guest, 'Child of')

class Pet(StructuredNode):
    name = StringProperty(required = False)
    pet_type = StringProperty(required = False)

    guest = RelationshipTo(Guest, 'Pet of')

class GuestAttributes(StructuredNode):
    is_smoker = StringProperty(required = False)
    health_condition = StringProperty(required = False)

    guest = RelationshipTo(Guest, 'Attributes of Guest')
    
class Allergy(StructuredNode):
    name = StringProperty(required = False)
    description = StringProperty(required = False)
    guest = RelationshipTo(Guest, 'Guest allergy')

class Disability(StructuredNode):
    name = StringProperty(required = False)
    disability_type = StringProperty(required = False)
    diasability_description = StringProperty()

    guest = RelationshipTo(Guest, 'Guest disability')

class Illness(StructuredNode):
    name = StringProperty(required = False)
    description = StringProperty(required = False)

    guest = RelationshipTo(Guest, 'Guest suffers from')
