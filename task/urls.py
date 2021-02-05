"""Urls of Task"""

from rest_framework import routers

from task.views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

task_urls = router.urls
