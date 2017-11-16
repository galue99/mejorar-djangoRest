# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Answer(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()

class UserAnswer(models.Model):
    poll_users = models.ForeignKey('polls.PollUser')
    answer = models.ForeignKey('answers.Answer')
    phrase = models.ForeignKey('items.Phrase')