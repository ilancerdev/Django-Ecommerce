# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-28 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0066_auto_20170728_1501'),
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productionorderitem',
            unique_together=set([('production_order', 'product')]),
        ),
    ]
