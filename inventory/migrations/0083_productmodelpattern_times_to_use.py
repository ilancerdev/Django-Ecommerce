# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0082_auto_20170917_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodelpattern',
            name='times_to_use',
            field=models.IntegerField(default=0),
        ),
    ]
