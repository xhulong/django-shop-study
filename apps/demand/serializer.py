from rest_framework import serializers
from .models import Task, DeliveryTask, ErrandTask, TaskUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'type', 'creator', 'status', 'created_at']

class DeliveryTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = DeliveryTask
        fields = ['id', 'task', 'package_size', 'pickup_location']

class ErrandTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = ErrandTask
        fields = ['id', 'task', 'start_location', 'end_location']

class TaskUserSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TaskUser
        fields = ['id', 'user', 'task', 'accepted_at']
