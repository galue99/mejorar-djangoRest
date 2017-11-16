# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    poll = models.ForeignKey('polls.Poll', related_name='items')
    name = models.CharField(max_length=255)
    competition_type = models.ForeignKey('competitions.CompetitionType', related_name='competition_type', null=True)


class Phrase(models.Model):
    name = models.CharField(max_length=255)
    item = models.ForeignKey('Item', related_name='phrases')
