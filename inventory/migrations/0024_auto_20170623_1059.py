# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-23 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_auto_20170623_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
