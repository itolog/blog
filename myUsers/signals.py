from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def createUser(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def saveUser(sender, instance, **kwards):
    instance.profile.save()