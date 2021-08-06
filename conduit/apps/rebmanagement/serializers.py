# from typing_extensions import Required
from rest_framework import serializers
from django.db import models
from .models import Management


class RebSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    management_id=serializers.IntegerField()
    management_name_en=serializers.CharField(max_length=100,allow_blank=True, allow_null=True)
    management_name_bn=serializers.CharField(max_length=200,allow_blank=True, allow_null=True)

    class Meta:
        model = Management
        fields = ('username','management_id','management_name_en','management_name_en',)

        read_only_fields = ('username',)
    
    

    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image

    #     return obj