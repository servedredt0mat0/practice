from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=3, default="USA")