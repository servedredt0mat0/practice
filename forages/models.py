from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
import datetime

COUNT_TYPES = (
    ("ton", "ton"),
    ("lbs", "lbs"),
    ("oz", "oz"),
    ("g", "g"),
    ("kg", "kg"),
    ("tons", "tons"),
    ("whole", "whole"),
    ("dozen", "dozen")
)

FORAGED_MATERIALS =(
    ("Mushroom", "Mushroom"),
    ("Shell Foods", "Shell Foods"),
    ("Crop", "Crop"),
    ("Material", "Material"),
    ("In Response", "In Response"),
)

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    likes = models.ManyToManyField(CustomUser, related_name="project_post")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class Entry(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='entries')
    foraged_material = models.CharField(max_length=255, choices=FORAGED_MATERIALS )
    short_comment = models.TextField(max_length=255, help_text="You may type a 255 char short description of your find or leave the current date and time.", default=datetime.datetime.now())
    latitude = models.DecimalField( max_digits=11, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    count = models.DecimalField(max_digits=14, decimal_places=3, null=True, blank=True)
    unit = models.CharField(max_length=56, choices=COUNT_TYPES, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.material

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.project_id)])
