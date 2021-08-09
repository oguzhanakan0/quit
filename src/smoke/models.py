from django.db import models
from user.models import User, SmokerSupporter
from django.db.models.base import Model
from django.contrib.auth.models import User as DjangoUser
import uuid

class SmokeConfig(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userid             = models.ForeignKey(User, on_delete=models.PROTECT, db_column='userid', to_field= 'id', related_name='+')
    class Frequency(models.IntegerChoices):
        pack_1    = 1
        pack_more = 2
        pack_half = 3
        few       = 4
        
    frequency          = models.IntegerField(choices=Frequency.choices) #@TODO ya ne secenek yapcaktik buna aq
    cost_per_pack      = models.FloatField()
    class Currency(models.IntegerChoices):
        lira   = 1
        dollar = 2
        euro   = 3
        yen    = 4
        other  = 5
        
    currency           = models.IntegerField(choices=Currency.choices)
    
    class SmokingType(models.IntegerChoices):
        pack_1    = 1
        pack_more = 2
        pack_half = 3
        few       = 4
        
    smoking_type       = models.IntegerField(choices=SmokingType.choices) #@TODO ya ne secenek yapcaktik buna aq

    class Brand(models.IntegerChoices):
        marlboro   = 1
        kent       = 2
        camel      = 3
        davidoff   = 4
        other      = 5
    brand              = models.IntegerField(choices=Brand.choices) #@TODO ya ne secenek yapcaktik buna aq

    quit_date          = models.DateTimeField(auto_now_add=True)
    years_smoked       = models.IntegerField()

class SmokeEntry(models.Model):
    id                 = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    smokeconfigid      = models.ForeignKey(SmokeConfig, on_delete=models.PROTECT, db_column='smokeconfigid', to_field= 'id', related_name='+')
    smoked             = models.IntegerField()
    cravings           = models.IntegerField()
    class Intensity(models.IntegerChoices):
        low       = 1
        mild      = 2
        high      = 3
        extreme   = 4
    intensity          = models.IntegerField(choices=Intensity.choices)
    date               = models.DateField(auto_now_add=True)
    date_filled        = models.DateField(auto_now_add=True)


