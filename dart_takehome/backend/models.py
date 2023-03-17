from enum import Enum
from uuid import uuid4

from django.db import models


class Task(models.Model):

    class Status(models.TextChoices):
        NEW = 'new'
        IN_PROGRESS = 'in_progress'
        DONE = 'done'

    uuid = models.UUIDField(unique=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField()
    title = models.TextField(default='')
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.NEW,
    )
    
