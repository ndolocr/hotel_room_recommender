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

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class UserModuleManager(BaseUserManager):
    use_in_migrations = True 

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        email, password, False, **data
        """

        print("Creating User in Django DB!")

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(str(password))
        user.is_active = True
        user.save()
        created = True
        return user, created

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, (str(password)), **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        # raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, (str(password)), **extra_fields)
    

    
    
class UserNode(StructuredNode):
    """creates a usermodel that supports email address instead of username"""
    USERROLE_CHOICES = [
        ('Guest', 'Guest'),
        ('Staff', 'Staff'),        
        ('Admin', 'Admin'),
    ]

    USERTYPE_CHOICES = [
        ('Minor', 'Minor'),
        ('Mature', 'Mature'),
    ]

    uid = UniqueIdProperty()
    town = StringProperty()    
    email = StringProperty()
    title = StringProperty()
    gender = StringProperty()
    address = StringProperty()
    password = StringProperty()
    religion = StringProperty()
    area_code = StringProperty()
    residency = StringProperty()
    last_name = StringProperty()
    first_name = StringProperty()
    middle_name = StringProperty()
    nationality = StringProperty()
    phone_number = StringProperty()    
    marital_status = StringProperty()
    id_document_type = StringProperty()
    id_document_number = StringProperty()
    user_role = StringProperty(choices=USERROLE_CHOICES)
    user_type = StringProperty(choices=USERTYPE_CHOICES)

    dob = DateProperty()
    updated_on = DateProperty()
    created_on = DateProperty()

    # user = models.OneToOneField("UserManager", on_delete=models.CASCADE)

    child = RelationshipTo('UserNode', 'Child of')
    guest = RelationshipTo('UserNode', 'Guest of') 

class Pet(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required = False)
    pet_type = StringProperty(required = False)

    guest = RelationshipTo(UserNode, 'Pet of')

class Smoker(StructuredNode):
    uid = UniqueIdProperty()
    is_smoker = StringProperty()

    guest = RelationshipTo(UserNode, 'Attributes of Guest')
    
class Allergy(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required = False)
    description = StringProperty(required = False)
    guest = RelationshipTo(UserNode, 'Guest allergy')

class Disability(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required = False)
    disability_type = StringProperty(required = False)
    diasability_description = StringProperty()

    guest = RelationshipTo(UserNode, 'Guest disability')

class Illness(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required = False)
    description = StringProperty(required = False)

    guest = RelationshipTo(UserNode, 'Guest suffers from')

class ViewPrefence(StructuredNode):
    uid = UniqueIdProperty()
    view_preference = StringProperty()

    updated_on = DateProperty()
    created_on = DateProperty()

    guest = RelationshipTo(UserNode, 'View prefered')

class UserManager(AbstractBaseUser):
    """Django User model using a UserNode"""

    # Django user properties
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.CharField(max_length=100, unique=True, null=True, default="")
    user_node_id = models.CharField(max_length=255, null=True, default="")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserModuleManager()
