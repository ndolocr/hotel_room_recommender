from django.db import models
from neomodel import (
    Relationship,
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
    IntegerProperty,
    ArrayProperty, 
    DateProperty, 
    FloatProperty
)

# Create your models here.
class HotelGuest(StructuredNode):
    uid = UniqueIdProperty()
    title = StringProperty()
    gender = StringProperty()
    address = StringProperty()
    religion = StringProperty()
    id_number = StringProperty()
    residency = StringProperty()
    last_name = StringProperty()
    first_name = StringProperty()
    middle_name = StringProperty()
    nationality = StringProperty()
    phone_number = StringProperty()
    email_address = StringProperty()
    marital_status = StringProperty()
    
    dob = DateProperty()
    updated_on = DateProperty()
    created_on = DateProperty()


class GuestChild(StructuredNode):
    uid = UniqueIdProperty()
    gender = StringProperty()
    last_name = StringProperty()
    first_name = StringProperty()
    middle_name = StringProperty()

    dob = DateProperty()
    updated_on = DateProperty()
    created_on = DateProperty()
    

class GuestAttributes(StructuredNode):
    uid = UniqueIdProperty()
    isSmoker = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()


class Disability(StructuredNode):
    name = StringProperty()
    disability_type = StringProperty()
    disability_description = StringProperty()