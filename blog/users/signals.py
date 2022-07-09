from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from blog_app.models import Post
from .models import Profile


# signal use for run some process along with changes in database
# Signals are used to perform any action on modification of a model instance.
# The signals are utilities that help us to connect events with actions.
# We can develop a function that will run when a signal calls it.
# Signals are used to perform some action on modify/creat. of a particular entry in DB.

# For example, here
# here create_profile create a profile instance, as soon as a new user instance is created in Database
# also save the profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
