from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Logs


@receiver(post_save)
def saved_model(sender, instance, created, **kwargs):
    if sender.__name__ != "Logs":
        if created:
            log = Logs(content_object=instance, action='0')
            log.save()
        else:
            log = Logs(content_object=instance, action='1')
            log.save()
    return None


@receiver(post_delete)
def deleted(sender, instance, created, **kwargs):
    log = Logs(content_object=instance, action='2')
    log.save()
    return None
