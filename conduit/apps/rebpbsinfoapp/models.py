from django.db.models.deletion import CASCADE
from conduit.apps.profiles.models import Profile
from django.db import models
from django.db.models.fields.related import ForeignKey
from conduit.apps.core.models import TimestampedModel
from conduit.apps.authentication.models import User
# Create your models here.

class NetMeterInfo(TimestampedModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    install_meter_nos=models.IntegerField(blank=True, null=True)
    capacity_of_install_meter=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True)
    office_code=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.month