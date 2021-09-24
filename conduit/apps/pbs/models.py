from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
# from conduit.apps.authentication.models import User
from conduit.apps.core.models import TimestampedModel

class Pbs(TimestampedModel):

    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE)

    management=models.ForeignKey('rebmanagement.Management', on_delete=models.CASCADE,blank=True,null=True)
    pbs_code=models.CharField(max_length=3,blank=True,null=True)
    pbs_name_en=models.CharField(max_length=100,blank=True,null=True)
    pbs_name_bn=models.CharField(max_length=150,blank=True,null=True)
    address_en=models.CharField(max_length=200,blank=True,null=True)
    address_bn=models.CharField(max_length=200,blank=True,null=True)
    lat_long_value=models.CharField(max_length=200,blank=True,null=True)
    office_head_name=models.CharField(max_length=100,blank=True,null=True)
    office_head_Designation=models.CharField(max_length=100,blank=True,null=True)
    office_head_mobile_num=models.CharField(max_length=11,blank=True,null=True)
    complain_center_mobile_num=models.CharField(max_length=11,blank=True,null=True)
    # pbs_logo=models.ImageField(upload_to='pbs/',blank=True,null=True)
    total_consumer_nos=models.IntegerField(blank=True,null=True)
    total_billing_consumer_nos=models.IntegerField(blank=True,null=True)
    total_service_area_km=models.IntegerField(blank=True,null=True)
    total_line_km=models.IntegerField(blank=True,null=True)
    total_employee_nos=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return "%s %s" %(self.user.username, self.pbs_name_en)
