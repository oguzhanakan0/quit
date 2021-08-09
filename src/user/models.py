from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
import uuid

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    birth_date      = models.DateField()
    class AuthSource(models.IntegerChoices):
        google   = 1
        facebook = 2
        apple    = 3
        email    = 4
        
    auth_source            = models.IntegerField(choices=AuthSource.choices)


class UserConnection(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokerid           = models.ForeignKey(DjangoUser, on_delete=models.PROTECT, db_column='smokerid', to_field= 'id', related_name='+')
    supporter = models.ForeignKey(DjangoUser, on_delete=models.PROTECT, db_column='supporter_username', to_field= 'username', related_name='+', blank=True, null=True)
    verification_code  = models.CharField(max_length=100, unique=True) #@TODO django base64, encoded meselesi
    supporter_email	   = models.EmailField(blank=True, null=True)

class SmokerSupporter(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokerid           = models.ForeignKey(DjangoUser, on_delete=models.PROTECT, db_column='smokerid', to_field= 'id', related_name='+')
    supporterid        = models.ForeignKey(DjangoUser, on_delete=models.PROTECT, db_column='supporterid', to_field= 'id', related_name='+')
    date_linked        = models.DateTimeField(auto_now_add=True)
    is_active          = models.BooleanField(default=False)
    class Relationship(models.IntegerChoices):
        family   = 1
        friend = 2
        colleague    = 3
        significant_other    = 4
        other = 5
    relationship       = models.IntegerField(choices=Relationship.choices)
