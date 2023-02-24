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
    hotel_guest_id = StringProperty()
    
    dob = DateProperty()
    updated_on = DateProperty()
    created_on = DateProperty()

    spouse = RelationshipTo('HotelGuest', 'Spouse to')    
    friend = RelationshipTo('HotelGuest', 'Friend to')    
    parent = RelationshipTo('HotelGuest', 'Parent to')
    sibling = RelationshipTo('HotelGuest', 'Sibling to')
    colleague = RelationshipTo('HotelGuest', 'Colleague to')


class GuestChild(StructuredNode):
    uid = UniqueIdProperty()
    gender = StringProperty()
    last_name = StringProperty()
    first_name = StringProperty()
    middle_name = StringProperty()
    hotel_guest_id = StringProperty()

    dob = DateProperty()
    updated_on = DateProperty()
    created_on = DateProperty()

    guardian = RelationshipTo(HotelGuest, 'Child to')
    

class GuestAttributes(StructuredNode):
    uid = UniqueIdProperty()
    isSmoker = StringProperty()
    hotel_guest_id = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

    hotel_guest = RelationshipTo(HotelGuest, 'Guest smokes')

class Disability(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    disability_type = StringProperty()
    disability_description = StringProperty()
    hotel_guest_id = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()

    hotel_guest = RelationshipTo(HotelGuest, 'Is Disabled in')

class Allergy(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    allergy_type = StringProperty()
    allergy_description = StringProperty()
    hotel_guest_id = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()

    hotel_guest = RelationshipTo(HotelGuest, 'Has allergies of')

class Illness(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    illness_description = StringProperty()
    hotel_guest_id = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()
    hotel_guest = RelationshipTo(HotelGuest, 'Suffers from')

class Pet(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    pet_type = StringProperty()
    hotel_guest_id = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()

    hotel_guest = RelationshipTo(HotelGuest, 'Pet belongs to')



