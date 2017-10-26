# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models


def get_rand_num():
    return randint(1, 100)


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    rand_num = models.IntegerField(default=get_rand_num)
