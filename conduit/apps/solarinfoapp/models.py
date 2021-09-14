from django.db import models

# Create your models here.


class SolarPanelInfo(models.Model):
    last_month_solar_panel_consumer_nos=models.IntegerField(blank=True, null=True)
    last_month_solar_panel_capacity=models.IntegerField(blank=True, null=True)
    month=models.CharField(max_length=50, blank=True, null=True)
    year=models.CharField(max_length=50, blank=True, null=True)
    fy=models.CharField(max_length=50, blank=True, null=True)
    pbs_code=models.CharField(max_length=3, blank=True, null=True)
    def __str__(self):
        return self.month