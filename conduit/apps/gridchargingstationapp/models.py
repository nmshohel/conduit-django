from django.db import models

# Create your models here.

class GridChargingStationInfo(models.Model):
    charging_station_nos=models.IntegerField(blank=True, null=True)
    charging_station_capacity=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True, verbose_name='Financial Year')
    pbs_code=models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.month
