
# from typing_extensions import Required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from .models import NetMeterInfo,User

class UserReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']    

class NetMeterInfoSerializer(serializers.ModelSerializer):
    # user = UserReferenceSerializer()

    install_meter_nos=serializers.IntegerField()
    capacity_of_install_meter=serializers.IntegerField()
    month=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    year=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    fy=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    office_code=serializers.IntegerField()

    class Meta:
        model = NetMeterInfo
        fields = ['id','install_meter_nos', 'capacity_of_install_meter',
        'month','year','fy','office_code']
        depth = 1
        # read_only_fields = ('user',)
        # @csrf_exempt
        def create(self, validated_data):
            """
            Create and return a new `NetMeterInfo` instance, given the validated data.
            """
            return NetMeterInfo.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `NetMeterInfo` instance, given the validated data.
            """
            instance.install_meter_nos = validated_data.get('install_meter_nos', instance.install_meter_nostitle)
            instance.capacity_of_install_meter = validated_data.get('capacity_of_install_meter', instance.capacity_of_install_meter)
            instance.month = validated_data.get('month', instance.month)
            instance.year = validated_data.get('year', instance.year)
            instance.fy = validated_data.get('fy', instance.fy)
            instance.pbs_code = validated_data.get('pbs_code', instance.pbs_code)
            instance.save()
            return instance