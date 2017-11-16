# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from accounts.models import User

# Create your models here.
class Poll(models.Model):
    name = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class PollUser(models.Model):
    evaluador_id = models.IntegerField(null=True)
    level_id = models.ForeignKey('Level')
    status = models.BooleanField(default=False)
    poll = models.ForeignKey('Poll')
    user = models.ForeignKey('accounts.User')

class Level(models.Model):
    name = models.CharField(max_length=255)