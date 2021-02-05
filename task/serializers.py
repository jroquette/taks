"""Serializer of Client"""

from rest_framework import serializers

from task.models import Task
from user.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """Serializer Class of Task"""
    user_id = UserSerializer(read_only=True)

    class Meta:
        """Meta Class"""
        model = Task
        fields = '__all__'
