from django.db import models

# Create your models here.
class RoomElement(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    elementType = models.CharField(max_length=255, null=True)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name


class roomType(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    max_capacity = models.IntegerField(null=True)

    updated_on = models.DateTimeField( auto_now = True)
    created_on = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.name
