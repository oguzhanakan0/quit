from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
from src.enums import AuthSource, Relationship
import uuid

# Create your models here.

class User(models.Model):
    id                 = models.UUIDField(default=uuid.uuid4,primary_key=True)
    username           = models.CharField(max_length=40, unique=True)
    first_name         = models.CharField(max_length=100)
    last_name          = models.CharField(max_length=100)
    email              = models.EmailField(unique=True)
    last_login         = models.DateTimeField(null=True, blank=True)
    first_joined       = models.DateTimeField(null=True, blank=True)
    birth_date         = models.DateField(blank=True, null=True)
    auth_source        = models.IntegerField(choices=AuthSource.choices)
    is_info_complete   = models.BooleanField(default=False)
    


class UserConnection(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smoker             = models.ForeignKey(User, on_delete=models.PROTECT, db_column='smokerid', to_field= 'id', related_name='+')
    supporter          = models.ForeignKey(User, on_delete=models.PROTECT, db_column='supporter_username', to_field= 'username', related_name='+', blank=True, null=True)
    verification_code  = models.CharField(max_length=100, unique=True)
    supporter_email	   = models.EmailField(blank=True, null=True)


class SmokerSupporter(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smoker             = models.ForeignKey(User, on_delete=models.PROTECT, db_column='smokerid', to_field= 'id', related_name='+')
    supporter          = models.ForeignKey(User, on_delete=models.PROTECT, db_column='supporterid', to_field= 'id', related_name='+')
    date_linked        = models.DateTimeField(auto_now_add=True)
    is_active          = models.BooleanField(default=False)
    relationship       = models.IntegerField(choices=Relationship.choices)
