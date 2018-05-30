""" Create an auth token for the api when a user is created
"""

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def init_new_user(sender, instance, signal, created, **kwargs):
    """ creates and stores a new bearer auth token when a new user is created """
    if created:
        Token.objects.create(user=instance)
