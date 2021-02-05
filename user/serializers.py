"""Serializer of User"""

from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer Class of User"""

    class Meta:
        """Meta Class"""
        model = User
        fields = '__all__'
