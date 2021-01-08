
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    permits = models.PositiveIntegerField(default=1)
    REQUIRED_FIELDS = ['permits', 'email']

    def __str__(self):
        return self.username
