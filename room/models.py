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

    updated_on = DateProperty()
    created_on = DateProperty()

class RoomType(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    description = StringProperty()
    max_capacity = IntegerProperty()

    updated_on = DateProperty()
    created_on = DateProperty()

class RoomViewPreference(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()   
    description = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

class RoomTemprature(StructuredNode):
    uid = UniqueIdProperty()
    max_temprature = FloatProperty()
    min_temprature = FloatProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

class RoomHumidity(StructuredNode):
    uid = UniqueIdProperty()
    max_humidity = FloatProperty()
    min_humidity = FloatProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

class RoomLight(StructuredNode):
    uid = UniqueIdProperty()
    max_light = FloatProperty()
    min_light = FloatProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

class RoomScent(StructuredNode):
    uid = UniqueIdProperty()
    scent_name = StringProperty()
    description = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

class RoomAccessibility(StructuredNode):
    uid = UniqueIdProperty()
    description = StringProperty()
    accessibility_name = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()


class Room(StructuredNode):
    AVAILABILITY_CHOICES = [        
        ('Booked', 'Booked'),        
        ('Reserved', 'Reserved'),
        ('available', 'available'),
    ]

    PETROOM_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]

    DISABILITYFEATURES_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]

    uid = UniqueIdProperty()
    floor = StringProperty()
    created_on = DateProperty()
    hotel_id = StringProperty()    
    room_number = StringProperty()
    cost_per_night = FloatProperty()    
    pet_room = StringProperty(choices=PETROOM_CHOICES)    
    availability = StringProperty(choices=AVAILABILITY_CHOICES)
    disability_features = StringProperty(choices=DISABILITYFEATURES_CHOICES)

    room_view_id = StringProperty()
    room_type_id = StringProperty()
    room_light_id = StringProperty()
    room_scent_id = StringProperty()
    room_element_id = StringProperty()    
    room_humidity_id = StringProperty()
    room_temprature_id = StringProperty()
    room_accessibility_id = StringProperty()
    
    updated_on = DateProperty()
    created_on = DateProperty()

    hotel = RelationshipTo(Hotel, 'Room in a Hotel')
    room_type = RelationshipTo(RoomType, 'Room Type')
    room_scent = RelationshipTo(RoomScent, 'Scent in a Room')
    room_element = RelationshipTo(RoomElement, 'Element in a Room')
    room_light = RelationshipTo(RoomLight, 'Lighting Range in a Room')
    room_humidity = RelationshipTo(RoomHumidity, 'Humidity Range in a Room')    
    room_view = RelationshipTo(RoomViewPreference, 'View visible while in room')
    room_temprature = RelationshipTo(RoomTemprature, 'Temprature Range in a Room')
    room_accessibility = RelationshipTo(RoomAccessibility, 'Accessibility of the Room')



    
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