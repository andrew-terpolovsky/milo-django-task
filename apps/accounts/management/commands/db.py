import datetime

from django.core.management.base import BaseCommand

from apps.accounts.models import User

USERS = [
    ['google', datetime.date(1997, 1, 1)],
    ['yahoo', datetime.date(2010, 1, 1)],
    ['instagram', datetime.date(1988, 1, 1)],
    ['snapchat', datetime.date(2003, 1, 1)],
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = []
        for user in USERS:
            users.append(User(
                username=user[0],
                birthday=user[1],
            ))

        User.objects.bulk_create(users)
