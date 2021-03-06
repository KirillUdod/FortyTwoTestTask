from django.core.management import BaseCommand, call_command
from hello.models import Account


class Command(BaseCommand):
    help = "DEV COMMAND: Move admin acc to db"

    def handle(self, *args, **options):
        call_command('loaddata', 'initial_data')
        for user in Account.objects.all():
            user.user.set_password(user.user.password)
            user.user.save()
            user.save()
