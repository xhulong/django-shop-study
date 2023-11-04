from rest_framework import serializers
from apps.user.models import User, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'money', 'integral', 'avatar','last_name']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'email': {'required': True},
            'mobile': {'required': True},
            'money': {'required': True},
            'integral': {'required': True},
            'avatar': {'required': True},
        }

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
            model = Address
            fields = '__all__'