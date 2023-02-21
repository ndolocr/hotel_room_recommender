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
    title = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    religion = models.CharField(max_length=255, null=True)
    id_number = models.CharField(max_length=255, null=True)
    residency = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)    
    nationality = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email_address = models.CharField(max_length=255, null=True)
    marital_status = models.CharField(max_length=255, null=True)
    
    dob = models.DateTimeField(auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


class GuestChild(models.Model):
    gender = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True) 

    dob = models.DateTimeField(auto_now=False)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    

    