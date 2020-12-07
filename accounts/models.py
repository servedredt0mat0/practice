from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=3, default="USA")


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    profile_pic = models.ImageField(default='media/default.jpg', upload_to="media/profile_pics/")

    def __str__(self):
        return self.user
    
    def get_absolute_url(self):
        use = get_user_model()
        user = use.pk
        return reverse('profile', kwargs = {'pk': self.user })