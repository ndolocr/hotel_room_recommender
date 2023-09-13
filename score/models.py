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

class Score(StructuredNode):
    score = FloatProperty()
    uid = UniqueIdProperty()
    scoreFor = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()