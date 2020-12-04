from django.db.models.signals import post_save
from django.contrib.auth.models import CustomUser
from django.dispatct import receiver
from .models import Profile

@reciever(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(accounts=instance)

@reciever(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
