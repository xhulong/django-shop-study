from rest_framework import serializers
from .models import School, SchoolUserPermissions, SchoolConfig

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'status', 'is_delete']

class SchoolUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolUserPermissions
        fields = ['id', 'user', 'school', 'permission', 'is_disable']
