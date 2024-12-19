from rest_framework import serializers
from cs415.models import (
    Webuser,
    Addresstype,
    Useraddress,
    Userinfo,
    Phonetype,
    Userphone,
    Pagedata,
)

# Serializer for WebUser
class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webuser
        fields = ['web_user_id', 'first_name', 'last_name', 'email', 'created_date', 'is_active', 'last_login']  # Exclude password

# Serializer for AddressType
class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresstype
        fields = '__all__'

# Serializer for UserAddress
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

# Serializer for UserInfo
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'

# Serializer for PhoneType
class PhoneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        fields = '__all__'

# Serializer for UserPhone
class UserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields = '__all__'

# Serializer for PageData
class PageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagedata
        fields = '__all__'
