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

    guest_relation = RelationshipTo(Guest, 'Child od')
    
    

