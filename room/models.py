from django.db import models
from hotel.models import Hotel
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
class RoomElement(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    description = StringProperty()
    elementType = StringProperty()

    created_on = DateProperty()

class RoomType(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    description = StringProperty()
    max_capacity = IntegerProperty()

    created_on = DateProperty()

class Room(StructuredNode):
    uid = UniqueIdProperty()
    floor = StringProperty()
    created_on = DateProperty()
    hotel_id = StringProperty()    
    availability = StringProperty()
    room_number  = StringProperty()
    cost_per_night = FloatProperty()
    room_type_id = StringProperty()
    room_element_id = StringProperty()

    hotel = RelationshipTo(Hotel, 'Room in a Hotel')
    room_type = RelationshipTo(RoomType, 'Room Type')
    room_element = RelationshipTo(RoomElement, 'Element in a Room')


# class RoomElement(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     description = models.TextField(null=True)
#     elementType = models.CharField(max_length=255, null=True)

#     updated_on = models.DateTimeField( auto_now = True)
#     created_on = models.DateTimeField( auto_now_add = True)

#     def __str__(self):
#         return self.name


# class RoomType(models.Model):
#     name = models.CharField(max_length=255, null=True)
#     description = models.TextField(null=True)
#     max_capacity = models.IntegerField(null=True)

#     updated_on = models.DateTimeField( auto_now = True)
#     created_on = models.DateTimeField( auto_now_add = True)

#     def __str__(self):
#         return self.name



# class Room(models.Model):
#     floor = models.CharField(max_length=255, null=True)
#     image = models.CharField(max_length=255, null=True)
#     cost_per_night = models.FloatField(null=True)
#     availabilty = models.CharField(max_length=255, null=True)
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     room_number  = models.CharField(max_length=255, null=True)
#     room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)