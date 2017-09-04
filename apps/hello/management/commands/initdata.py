from django.core.management import BaseCommand, call_command
from hello.models import Account


class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        call_command('loaddata', 'initial_data')
        for user in Account.objects.all():
            user.set_password(user.password)
            user.save()