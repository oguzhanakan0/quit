from django.db import models
from src.enums import AuthSource, Relationship
import uuid

# Create your models here.


class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True) # ok
    uid = models.CharField(max_length=100, unique=True) # ok
    username = models.CharField(max_length=40, unique=True, null=True, blank=True) # ok
    first_name = models.CharField(max_length=100) # ok
    last_name = models.CharField(max_length=100) # ok
    email = models.EmailField(unique=True) # ok
    last_login = models.DateTimeField(null=True, blank=True) # ok
    first_joined = models.DateTimeField(null=True, blank=True) # ok
    birth_date = models.DateField(blank=True, null=True) # ok
    auth_source = models.CharField(max_length=20, choices=AuthSource.choices) # ok
    is_info_complete = models.BooleanField(default=False) # ok
    marketing_check =  models.BooleanField(default=False) # ok


class UserConnection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smoker = models.ForeignKey(User, on_delete=models.PROTECT,db_column='smokerid', to_field='id', related_name='+')
    supporter = models.ForeignKey(User, on_delete=models.PROTECT, db_column='supporter_username',to_field='username', related_name='+', blank=True, null=True)
    verification_code = models.CharField(max_length=100, unique=True)
    supporter_email = models.EmailField(blank=True, null=True)


class SmokerSupporter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smoker = models.ForeignKey(User, on_delete=models.PROTECT,db_column='smokerid', to_field='id', related_name='+')
    supporter = models.ForeignKey(User, on_delete=models.PROTECT, db_column='supporterid', to_field='id', related_name='+')
    date_linked = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    relationship = models.IntegerField(choices=Relationship.choices)
