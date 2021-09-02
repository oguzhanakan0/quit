from django.db import models
from user.models import User, SmokerSupporter
from smoke.models import SmokeConfig
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
from src.enums import NotifType, Day
import uuid

class NotifLaunch(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user               = models.ForeignKey(User, on_delete=models.PROTECT, db_column='userid', to_field= 'id', related_name='+')
    title              = models.CharField(max_length=80)
    content            = models.CharField(max_length=150)
    launch_date        = models.DateTimeField(auto_now_add=True)    
    notif_type         = models.IntegerField(choices=NotifType.choices)

class NotifConfig(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokersupporter    = models.ForeignKey(SmokerSupporter, on_delete=models.PROTECT, db_column='smokersupporterid', to_field= 'id', related_name='+')
    smokeconfig        = models.ForeignKey(SmokeConfig, on_delete=models.PROTECT, db_column='smokeconfigid', to_field= 'id', related_name='+')    
    notif_type         = models.IntegerField(choices=NotifType.choices)
    time               = models.TimeField()
    term               = models.IntegerField(blank=True, null=True)

class NotifDay(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notifconfig        = models.ForeignKey(NotifConfig, on_delete=models.PROTECT, db_column='notifconfigid', to_field= 'id', related_name='+')
    day                = models.IntegerField(choices=Day.choices)



