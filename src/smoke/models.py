from django.db import models
from user.models import User, SmokerSupporter
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
from src.enums import Frequency, Currency, SmokingType, Brand, Intensity
import uuid

class SmokeConfig(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user               = models.ForeignKey(User, on_delete=models.PROTECT, db_column='userid', to_field= 'temp_id', related_name='+')
    frequency          = models.IntegerField(choices=Frequency.choices)
    cost_per_pack      = models.FloatField()
    currency           = models.IntegerField(choices=Currency.choices)
    smoking_type       = models.IntegerField(choices=SmokingType.choices)
    brand              = models.IntegerField(choices=Brand.choices)
    quit_date          = models.DateTimeField(auto_now_add=True)
    years_smoked       = models.IntegerField()

class SmokeEntry(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokeconfig        = models.ForeignKey(SmokeConfig, on_delete=models.PROTECT, db_column='smokeconfigid', to_field= 'id', related_name='+')
    smoked             = models.IntegerField()
    cravings           = models.IntegerField()
    intensity          = models.IntegerField(choices=Intensity.choices)
    date               = models.DateField(auto_now_add=True)
    date_filled        = models.DateField(auto_now_add=True)


