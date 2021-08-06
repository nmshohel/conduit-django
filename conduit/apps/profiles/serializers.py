# from typing_extensions import Required
from rest_framework import serializers
from django.db import models
from .models import Profile
 

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, allow_null=True)
    image = serializers.SerializerMethodField()
    office_code=serializers.CharField(allow_blank=True, allow_null=True)
    office_name=serializers.CharField(allow_blank=True, allow_null=True)
    office_address=serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image','office_code','office_name','office_address',)
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'