from rest_framework import serializers
from .models import Activity, ActivityUser, ActivityBrowse

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'address', 'start_time', 'end_time', 'number_limit', 'creator', 'detail', 'status', 'is_delete']

class ActivityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityUser
        fields = ['id', 'user', 'activity', 'join_status', 'is_delete']

class ActivityBrowseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityBrowse
        fields = ['id', 'user', 'activity', 'is_delete']
