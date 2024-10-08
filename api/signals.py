from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
            group = Group.objects.get(name='Doctors')
        else:
            group = Group.objects.get(name='Patients')
        instance.groups.add(group)