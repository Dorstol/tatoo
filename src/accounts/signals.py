from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from tatoo.models import Pinner

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_pinner(sender, instance, created, **kwargs):
    print(instance)
    if created:
        Pinner.objects.create(
            user=instance,
        )


@receiver(post_save, sender=User)
def save_user_pinner(sender, instance, **kwargs):
    instance.pinner.save()
