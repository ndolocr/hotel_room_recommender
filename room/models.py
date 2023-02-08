from django.db import models
from hotel.models import Hotel

# Create your models here.
class RoomElement(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    elementType = models.CharField(max_length=255, null=True)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    max_capacity = models.IntegerField(null=True)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name



class Room(models.Model):
    floor = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    cost_per_night = models.FloatField(null=True)
    availabilty = models.CharField(max_length=255, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)