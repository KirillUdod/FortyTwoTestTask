from django.core.management.base import BaseCommand
from django.db import models
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = 'print all project models and the count of objects in every model'

    def handle(self, *args, **options):
        temp = {}
        for model in models.get_models(include_auto_created=True):
            try:
                q = len(model.objects.all())
            except OperationalError:
                q = 0
            temp[model.__name__] = q
            print('error: %s - %s' % (model.__name__, q))
