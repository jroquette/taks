"""Model File of User"""
from django.db import models


class User(models.Model):
    """Model of User"""
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)

    def __str__(self):
        """Get name of task by default"""
        return self.name
