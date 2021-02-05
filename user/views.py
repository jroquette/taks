"""View of User"""

from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """View of User"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
