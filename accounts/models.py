from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings


class User(AbstractUser):
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE, related_name="rol", null=True, blank=True)
    dni = models.IntegerField(unique=True, blank=True, null=True)
    position = models.CharField(max_length=140, null=True, blank=True)
    branch_office = models.CharField(max_length=140, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="company", null=True, blank=True)

    def __str__(self):
        return self.username

class Rol(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=140)
    url = models.CharField(max_length=140)

    def __str__(self):
        return self.name