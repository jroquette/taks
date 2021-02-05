"""Urls of User"""

from rest_framework import routers

from user.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')

user_urls = router.urls
