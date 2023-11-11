from rest_framework import serializers
from apps.user.models import User, Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'last_login', 'date_joined','create_time','update_time','is_delete','openid')
        extra_kwargs = {
            'id': {'read_only': True}
        }

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
            model = Address
            fields = '__all__'