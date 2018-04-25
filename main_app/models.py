# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
