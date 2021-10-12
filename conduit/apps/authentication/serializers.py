from rest_framework.fields import ReadOnlyField
from conduit.apps.pbs.models import Pbs
from conduit.apps.rebmanagement.models import Management
from rest_framework import serializers
from django.contrib.auth import authenticate
from conduit.apps.pbs.serializers import PbsSerializer
from conduit.apps.rebmanagement.serializers import RebSerializer
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token','is_management','office_code']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class SuperUserRegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password','office_code', 'token','is_management']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    office_code=serializers.CharField(max_length=3,read_only=True)
    user_role=serializers.CharField(max_length=5,read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'office_code':user.office_code,
            'user_role':user.user_role,
            'token': user.token
        }

class PbsUserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    pbs = PbsSerializer(write_only=True)
    
    username = serializers.CharField(source='user.username', read_only=True)
    management_id=serializers.CharField(source='pbs.management_id', read_only=True)
    pbs_code=serializers.CharField(source='pbs.pbs_code', read_only=True)
    pbs_name_en=serializers.CharField(source='pbs.pbs_name_en', read_only=True)
    pbs_name_bn=serializers.CharField(source='pbs.pbs_name_bn', read_only=True)
    address_en=serializers.CharField(source='pbs.address_en', read_only=True)
    address_bn=serializers.CharField(source='pbs.address_bn', read_only=True)
    lat_long_value=serializers.CharField(source='pbs.lat_long_value', read_only=True)
    office_head_name=serializers.CharField(source='pbs.office_head_name', read_only=True)
    office_head_Designation=serializers.CharField(source='pbs.office_head_Designation', read_only=True)
    office_head_mobile_num=serializers.CharField(source='pbs.office_head_mobile_num', read_only=True)
    complain_center_mobile_num=serializers.CharField(source='pbs.complain_center_mobile_num', read_only=True)
    # pbs_logo=serializers.ImageField(source='pbs.pbs_logo', read_only=True)
    total_consumer_nos=serializers.IntegerField(source='pbs.total_consumer_nos', read_only=True)
    total_billing_consumer_nos=serializers.IntegerField(source='pbs.total_billing_consumer_nos', read_only=True)
    total_service_area_km=serializers.IntegerField(source='pbs.total_service_area_km', read_only=True)
    total_line_km=serializers.IntegerField(source='pbs.total_line_km', read_only=True)
    total_employee_nos=serializers.IntegerField(source='pbs.total_employee_nos', read_only=True)
    
    class Meta:
        model = User
        fields = ('pbs','username','email','password','management_id','pbs_code','pbs_name_en','pbs_name_bn','address_en',
        'address_bn','lat_long_value','office_head_name','office_head_Designation',
        'office_head_mobile_num','complain_center_mobile_num','total_consumer_nos',
        'total_billing_consumer_nos','token','total_service_area_km','total_line_km','total_employee_nos',)

        read_only_fields = ('token',)


    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop('password', None)

        # profile_data = validated_data.pop('profile', {})
        pbs_data = validated_data.pop('pbs', {})
        for (key, value) in validated_data.items():

            setattr(instance, key, value)

        if password is not None:

            instance.set_password(password)

        instance.save()

        for (key, value) in pbs_data.items():
        # for (key, value) in profile_data.items():
        

            setattr(instance.pbs, key, value)
            # setattr(instance.profile, key, value)

        # instance.profile.save()
        instance.pbs.save()
        return instance

class PbsUsersSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    pbs = PbsSerializer(write_only=True)

    username = serializers.CharField(source='user.username', read_only=True)
    management_id=serializers.CharField(source='pbs.management_id', read_only=True)
    pbs_code=serializers.CharField(source='pbs.pbs_code', read_only=True)
    pbs_name_en=serializers.CharField(source='pbs.pbs_name_en', read_only=True)
    pbs_name_bn=serializers.CharField(source='pbs.pbs_name_bn', read_only=True)
    address_en=serializers.CharField(source='pbs.address_en', read_only=True)
    address_bn=serializers.CharField(source='pbs.address_bn', read_only=True)
    lat_long_value=serializers.CharField(source='pbs.lat_long_value', read_only=True)
    office_head_name=serializers.CharField(source='pbs.office_head_name', read_only=True)
    office_head_Designation=serializers.CharField(source='pbs.office_head_Designation', read_only=True)
    office_head_mobile_num=serializers.CharField(source='pbs.office_head_mobile_num', read_only=True)
    complain_center_mobile_num=serializers.CharField(source='pbs.complain_center_mobile_num', read_only=True)
    # pbs_logo=serializers.ImageField(source='pbs.pbs_logo', read_only=True)
    total_consumer_nos=serializers.IntegerField(source='pbs.total_consumer_nos', read_only=True)
    total_billing_consumer_nos=serializers.IntegerField(source='pbs.total_billing_consumer_nos', read_only=True)
    total_service_area_km=serializers.IntegerField(source='pbs.total_service_area_km', read_only=True)
    total_line_km=serializers.IntegerField(source='pbs.total_line_km', read_only=True)
    total_employee_nos=serializers.IntegerField(source='pbs.total_employee_nos', read_only=True)
    
    class Meta:
        model = Pbs
        fields = ('pbs','username','email','password','management_id','pbs_code','pbs_name_en','pbs_name_bn','address_en',
        'address_bn','lat_long_value','office_head_name','office_head_Designation',
        'office_head_mobile_num','complain_center_mobile_num','total_consumer_nos',
        'total_billing_consumer_nos','token','total_service_area_km','total_line_km','total_employee_nos',)

        read_only_fields = ('token',)


class RebUserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    management = RebSerializer(write_only=True)

    username = serializers.CharField(source='user.username', read_only=True)
    breb_office_name_en=serializers.CharField(source='management.breb_office_name_en', read_only=True)
    breb_office_name_bn=serializers.CharField(source='management.breb_office_name_bn', read_only=True)
 
    class Meta:
        model = User
        fields = ('management','username','email','password','breb_office_name_en','breb_office_name_bn',)

        read_only_fields = ('token',)


    def update(self, instance, validated_data):
        """Performs an update on a User."""

        password = validated_data.pop('password', None)

        management_data = validated_data.pop('management', {})
        for (key, value) in validated_data.items():

            setattr(instance, key, value)

        if password is not None:

            instance.set_password(password)

        instance.save()

        for (key, value) in management_data.items():

            setattr(instance.management, key, value)

        instance.management.save()
        return instance


class RebUsersSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    management = RebSerializer(write_only=True)

    username = serializers.CharField(source='user.username', read_only=True)
    breb_office_name_en=serializers.CharField(source='management.breb_office_name_en', read_only=True)
    breb_office_name_bn=serializers.CharField(source='management.breb_office_name_bn', read_only=True)
   
    class Meta:
        model = Management
        fields = ('management','username','email','password','breb_office_name_en','breb_office_name_bn','token',)

        read_only_fields = ('token',)