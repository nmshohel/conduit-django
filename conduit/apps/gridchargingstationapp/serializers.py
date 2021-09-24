
# from typing_extensions import Required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from .models import GridChargingStationInfo
from conduit.apps.authentication.models import User

class UserReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']    

class GridChargingStationInfoSerializer(serializers.ModelSerializer):
    # user = UserReferenceSerializer()

    charging_station_nos=serializers.IntegerField()
    charging_station_capacity=serializers.IntegerField()
    month=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    year=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    fy=serializers.CharField(max_length=50, allow_blank=True, allow_null=True)
    pbs_code=serializers.CharField(max_length=3, allow_blank=True, allow_null=True)

    class Meta:
        model = GridChargingStationInfo
        fields = ['id','charging_station_nos', 'charging_station_capacity',
        'month','year','fy','pbs_code']
        depth = 1
        # read_only_fields = ('user',)
        # @csrf_exempt
        def create(self, validated_data):
           
            return GridChargingStationInfo.objects.create(**validated_data)

        def update(self, instance, validated_data):
            
            instance.charging_station_nos = validated_data.get('charging_station_nos', instance.charging_station_nos)
            instance.charging_station_capacity = validated_data.get('charging_station_capacity', instance.charging_station_capacity)
            instance.month = validated_data.get('month', instance.month)
            instance.year = validated_data.get('year', instance.year)
            instance.fy = validated_data.get('fy', instance.fy)
            instance.pbs_code = validated_data.get('pbs_code', instance.pbs_code)
            instance.save()
            return instance