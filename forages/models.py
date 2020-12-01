from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Projects(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

class Entry(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='entries')
    material = models.CharField(max_length=255)
    latitude = models.DecimalField( max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8,)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.material

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.project_id)])
