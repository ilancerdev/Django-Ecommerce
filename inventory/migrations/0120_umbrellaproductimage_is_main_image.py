# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-24 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0119_auto_20180219_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='umbrellaproductimage',
            name='is_main_image',
            field=models.BooleanField(default=False),
        ),
    ]
