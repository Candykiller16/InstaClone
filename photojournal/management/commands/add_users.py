from random import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed


class Command(BaseCommand):
    help = u'Add users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Amount of random users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        seeder = Seed.seeder()
        for i in range(total):
            User.objects.create_user(username=seeder.faker.user_name(), email=seeder.faker.email(), password='123')
        return 'Done'
        # seeder = Seed.seeder()
        # seeder.add_entity(User, total, {
        #     'username': lambda x: seeder.faker.name(),
        #     'email': lambda x: seeder.faker.email(),
        #     'password': 'password123'
        # })
        # seeder.execute()
