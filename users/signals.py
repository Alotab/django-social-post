# this signal will create a new user any time a profile is created

from django.db.models.signals import post_save  # this signal gets fired after an object is save
from django.contrib.auth.models import User   # this user here is the sender
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) # when a User is save (post_save), then sender this signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
   instance.profile.save()