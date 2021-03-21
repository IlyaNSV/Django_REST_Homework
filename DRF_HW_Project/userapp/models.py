from uuid import uuid4
from django.db import models


class DefaultUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    mail = models.CharField(unique=True, max_length=64)
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.user_name
