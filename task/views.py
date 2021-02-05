"""View of Task"""

from rest_framework.viewsets import ModelViewSet

from task.models import Task
from task.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    """View of Task"""
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Get specific queryset to call

        Filters:
        No parameters:
            get all tasks
        user_id :
            get all tasks of a specific user

        :param: user_id
        :return: queryset
        """
        params = self.request.query_params
        user_id = params.get('user_id', None)

        if len(params) == 0:
            queryset = Task.objects.all()
        elif user_id is not None:
            queryset = Task.objects.filter(user_id=user_id)

        return queryset
