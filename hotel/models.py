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
    FloatProperty,
    DateTimeProperty
)

# Create your models here.
class Hotel(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty()
    city = StringProperty()
    address = StringProperty()
    created_on = DateProperty()
    description = StringProperty()


# class Hotel(models.Model):
    # name = models.CharField(max_length=255, null=True)
    # description = models.TextField(null=True)
    # city = models.CharField(max_length=255, null=True)
    # address = models.CharField(max_length=255, null=True)

    # updated_on = models.DateTimeField( auto_now = True)
    # created_on = models.DateTimeField( auto_now_add = True)

    # def __str__(self):
    #     return self.name