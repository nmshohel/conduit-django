from django.db.models import signals
from django.db.models.fields import NullBooleanField
from django.db.models.signals import post_save
from django.dispatch import receiver

from conduit.apps.profiles.models import Profile
from conduit.apps.rebmanagement.models import Management
from conduit.apps.pbs.models import Pbs
from conduit.apps.authentication.models import User


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):

    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.

    if instance and created:
        # instance.profile = Profile.objects.create(user=instance)
        if isinstance:
            ins= instance.is_management
            if ins==False:
                instance.pbs = Pbs.objects.create(user=instance)
            elif ins==True:
                instance.management = Management.objects.create(user=instance)
            else:
                pass            
        else:
            return NullBooleanField

         
    
