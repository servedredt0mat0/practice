from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
import datetime

MUSHROOMS = (
    ('Amanita', 'Amanita'),
    ('Beech Mushrooms', 'Beech Mushrooms'),
    ('Black Trumpet Mushrooms', 'Black Trumpet Mushrooms'),
    ('Brown Cap Boletus', 'Brown Cap Boletus'),
    ('Button Mushrooms', 'Button Mushrooms'),
    ('Chanterelle Mushrooms', 'Chanterelle Mushrooms'),
    ('Cremini Mushrooms', 'Cremini Mushrooms'),
    ('Enoki Mushrooms', 'Enoki Mushrooms'),
    ('Green Amanita', 'Green Amanita'),
    ('Hedgehog Mushrooms', 'Hedgehog Mushrooms'),
    ('Hen of the Woods Mushrooms', 'Hen of the Woods Mushrooms'),
    ('Chicken of the Woods', 'Chicken of the Woods'),
    ('Honey Agaric', 'Honey Agaric'),
    ('Lactarius Indigo', 'Lactarius Indigo'),
    ('King Trumpet Mushrooms', 'King Trumpet Mushrooms'),
    ('Milk Mushrooms', 'Milk Mushrooms'),
    ('Morel Mushrooms', 'Morel Mushrooms'),
    ('Oyster Mushrooms', 'Oyster Mushrooms'),
    ('Porcini Mushrooms', 'Porcini Mushrooms'),
    ('Portobello Mushrooms', 'Portobello Mushrooms'),
    ('Russula', 'Russula'),
    ('Shitake Mushrooms', 'Shitaki Mushrooms'),
    ('Toadstool', 'Toadstool'),
    ('Puffball Mushrooms', 'Puffball Mushrooms'),
)

MUSHROOM_TYPES = (
    ('Cultivated Mushrooms', 'Cultivated Mushrooms'),
    ('Wild Mushrooms', 'Wild Mushrooms'),
    ('Medicinal Mushrooms', 'Medicinal Mushrooms'),
    ('Psychoactive Mushrooms', 'Psychoactive Mushrooms'),
    ('Poisonous Mushrooms', 'Poisonous Mushrooms'),
    ('Useful Mushrooms', 'Useful Mushrooms'),
)

CLASSIFICATIONS = (
    ('Saprotrophic Mushrooms', 'Saprotrophic Mushrooms'),
    ('Mycorrhizal Mushrooms', 'Mycorrhizal Mushrooms'),
    ('Parasitic Mushrooms', 'Parasitic Mushrooms'),
    ('Endophytes', 'Endophytes'),
)

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
    short_comment = models.TextField(max_length=512, help_text="You may type a 512 char short description of your find or leave the current date and time.", default=datetime.datetime.now())
    latitude = models.DecimalField( max_digits=11, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    count = models.DecimalField(max_digits=14, decimal_places=3, null=True, blank=True)
    unit = models.CharField(max_length=56, choices=COUNT_TYPES, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
        
    def __str__(self):
        return self.foraged_material

    def get_absolute_url(self):
        return reverse('entry_detail', args=[str(self.project_id)])


class Mushrooms(models.Model):
    mushroom = models.CharField(max_length=255, choices=MUSHROOMS)

class MushroomData(models.Model):
    mushroom = models.OneToOneField(Mushrooms, on_delete=models.CASCADE, related_name='mushroom_details')
    associated_names = models.CharField(max_length=512)
    image = models.ImageField()
    description = models.TextField()
    mushroom_type = models.CharField(max_length=255, choices=MUSHROOM_TYPES)
    classification = models.CharField(max_length=255, choices=CLASSIFICATIONS)

