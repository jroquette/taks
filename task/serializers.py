"""Serializer of Client"""

from rest_framework import serializers

from task.models import Task
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Serializer Class of Task"""
    user = UserSerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Task
        fields = ['name', 'description', 'status', 'created_at', 'user', 'user_id']
        extra_kwargs = {'user_id': {'write_only': True}}
