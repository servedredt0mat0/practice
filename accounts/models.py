from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=3, default="USA")


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(default='default.jpg', upload_to="profile_pics/")

    def __str__(self):
        return f'{self.user.username} Profile'
    