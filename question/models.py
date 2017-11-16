# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class OtherQuestion(models.Model):
    question = models.TextField()
    poll = models.ForeignKey('polls.Poll')

class UserAnswerOtherQuestion(models.Model):
    answers = models.TextField(models.Model)
    otherquestion = models.ForeignKey('OtherQuestion')
    polluser = models.ForeignKey('polls.PollUser')