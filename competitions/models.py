# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Competition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey('CompetitionType')
    company = models.ForeignKey('accounts.Company')

class CompetitionType(models.Model):
    name = models.CharField(max_length=255)

class Behavior(models.Model):
    name = models.CharField(max_length=255)
    competition = models.ForeignKey('competitions.Competition', related_name='behaviors', on_delete=models.CASCADE)