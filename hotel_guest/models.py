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
class HotelGuest(models.Model):
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


class GuestChild(models.Model):
    gender = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True) 

    dob = models.DateTimeField(auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    

    