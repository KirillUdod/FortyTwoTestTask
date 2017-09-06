from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from hello.models import Account, Logs, WebRequest


@receiver(post_save, sender=Account)
@receiver(post_save, sender=WebRequest)
def saved_model(sender, instance, created, **kwargs):
    if created:
        Logs.objects.create(content_object=instance, action='0')
    else:
        Logs.objects.create(content_object=instance, action='1')
    return None


@receiver(post_delete, sender=Account)
@receiver(post_delete, sender=WebRequest)
def deleted(sender, instance, created, **kwargs):
    Logs.objects.create(content_object=instance, action='2')
    return None
