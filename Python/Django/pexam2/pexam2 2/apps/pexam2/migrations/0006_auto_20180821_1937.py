# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-21 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pexam2', '0005_auto_20180821_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='granted',
            field=models.BooleanField(default=False),
        ),
    ]