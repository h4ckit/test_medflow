from django.conf import settings
from django.core.management.base import BaseCommand
from medflow.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser('admin@admin.ad', 'admin', 'adminF', 'adminL')
        else:
            print('Admin account can only be initialized if no Accounts exist')
