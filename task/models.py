"""Model File of Task"""
from django.db import models

from user.models import User


class Task(models.Model):
    """Model of Task"""

    STATUS_TYPE = (
        (0, 'Pending'),
        (1, 'Done')
    )

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.PositiveIntegerField(choices=STATUS_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, null=True, blank=True, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        """Get name of task by default"""
        return self.name

    def user(self):
        """Client data"""
        return self.user_id