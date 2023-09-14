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
    code = FloatProperty()
    score = FloatProperty()    
    uid = UniqueIdProperty()
    score_for = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()