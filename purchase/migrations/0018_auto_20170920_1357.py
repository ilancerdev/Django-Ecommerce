# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0017_auto_20170909_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='status',
        ),
        migrations.AddField(
            model_name='delivery',
            name='_is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]