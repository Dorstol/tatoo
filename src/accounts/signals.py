from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save
from django.dispatch import receiver

from tatoo.models import Pinner

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_pinner(sender, instance, created, **kwargs):
    try:
        instance.pinner.save()
    except ObjectDoesNotExist:
        Pinner.objects.create(
            user=instance,
        )
