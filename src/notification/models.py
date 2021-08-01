from django.db import models
from user.models import User, SmokerSupporter
from smoke.models import SmokeConfig
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
import uuid

class NotifLaunch(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userid             = models.ForeignKey(User, on_delete=models.PROTECT, db_column='userid', to_field= 'id', related_name='+')
    content            = models.CharField(max_length=100, unique=True) #@TODO burayi text mi yapmak lazim char ve belli karakter sayisi daha dogru gibi geldi notification content oldugundan
    launch_date        = models.DateTimeField(auto_now_add=True)
    class NotifType(models.IntegerChoices):
        google   = 1
        facebook = 2
        apple    = 3
        email    = 4
        
    notif_type         = models.IntegerField(choices=NotifType.choices) #@TODO ya ne secenek yapcaktik buna aq

class NotifConfig(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokersupporterid  = models.ForeignKey(SmokerSupporter, on_delete=models.PROTECT, db_column='smokersupporterid', to_field= 'id', related_name='+')
    smokeconfigid      = models.ForeignKey(SmokeConfig, on_delete=models.PROTECT, db_column='smokeconfigid', to_field= 'id', related_name='+')
    class NotifType(models.IntegerChoices):
        google   = 1
        facebook = 2
        apple    = 3
        email    = 4
        
    notif_type         = models.IntegerField(choices=NotifType.choices) #@TODO ya ne secenek yapcaktik buna aq
    time               = models.TimeField()

class NotifDay(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notifconfigid      = models.ForeignKey(NotifConfig, on_delete=models.PROTECT, db_column='notifconfigid', to_field= 'id', related_name='+')
    class Day(models.IntegerChoices):
        monday    = 1
        tuesday   = 2
        wednesday = 3
        thursday  = 4
        friday    = 5
        saturday  = 6
        sunday    = 7
        
    day                = models.IntegerField(choices=Day.choices)



