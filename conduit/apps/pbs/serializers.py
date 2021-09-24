# from typing_extensions import Required
from rest_framework import serializers
from django.db import models
from .models import Pbs


class PbsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    management_id=serializers.CharField(max_length=250,allow_blank=True, allow_null=True)
    pbs_code=serializers.CharField(max_length=3,allow_blank=True, allow_null=True)
    pbs_name_en=serializers.CharField(max_length=100,allow_blank=True, allow_null=True)
    pbs_name_bn=serializers.CharField(max_length=150,allow_blank=True, allow_null=True)
    address_en=serializers.CharField(max_length=200,allow_blank=True, allow_null=True)
    address_bn=serializers.CharField(max_length=200,allow_blank=True, allow_null=True)
    lat_long_value=serializers.CharField(max_length=200,allow_blank=True, allow_null=True)
    office_head_name=serializers.CharField(max_length=100,allow_blank=True, allow_null=True)
    office_head_Designation=serializers.CharField(max_length=100,allow_blank=True, allow_null=True)
    office_head_mobile_num=serializers.CharField(max_length=11,allow_blank=True, allow_null=True)
    complain_center_mobile_num=serializers.CharField(max_length=11,allow_blank=True, allow_null=True)
    # pbs_logo=serializers.ImageField(allow_null=True, required=False)
    total_consumer_nos=serializers.IntegerField(required=False,allow_null=True)
    total_billing_consumer_nos=serializers.IntegerField(required=False,allow_null=True)
    total_service_area_km=serializers.IntegerField(required=False,allow_null=True)
    total_line_km=serializers.IntegerField(required=False,allow_null=True)
    total_employee_nos=serializers.IntegerField(required=False,allow_null=True)

    class Meta:
        model = Pbs
        fields = ('username','management_id','pbs_code','pbs_name_en','pbs_name_bn','address_en',
        'address_bn','lat_long_value','office_head_name','office_head_Designation',
        'office_head_mobile_num','complain_center_mobile_num','total_consumer_nos',
        'total_billing_consumer_nos','total_service_area_km','total_line_km','total_employee_nos',)
        read_only_fields = ('username','management_name_en',)

    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image

    #     return obj.image