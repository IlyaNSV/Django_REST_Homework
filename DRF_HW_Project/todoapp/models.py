from uuid import uuid4
from django.db import models
from userapp.models import DefaultUser


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(unique=True, max_length=64)
    repository_link = models.URLField(blank=True)
    members = models.ManyToManyField(DefaultUser)

    def __str__(self):
        return self.name


class ToDoNote(models.Model):
    ACTIVE = 'ACT'
    CLOSED = 'CLD'

    NOTE_ACTUALITY_TYPE = [
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    ]

    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator_user = models.ForeignKey(DefaultUser, on_delete=models.CASCADE)
    actual_sign = models.CharField(
        max_length=3,
        choices=NOTE_ACTUALITY_TYPE,
        default=CLOSED,
    )
