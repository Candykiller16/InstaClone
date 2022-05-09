from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = u'Add users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Amount of random users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(10), email='', password='123' )