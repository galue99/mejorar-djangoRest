# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behavior',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='behaviors', to='competitions.Competition'),
        ),
    ]
