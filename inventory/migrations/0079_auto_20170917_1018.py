# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0078_auto_20170917_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umbrellaproductimage',
            name='image',
            field=models.ImageField(upload_to='media/products/%Y/%m/%d'),
        ),
    ]