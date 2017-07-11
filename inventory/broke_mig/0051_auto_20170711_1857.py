# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-11 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0050_auto_20170711_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productbillofmaterial',
            options={'ordering': ('material__supplier', 'material', 'product')},
        ),
        migrations.AlterModelOptions(
            name='umbrellaproductbillofmaterial',
            options={'ordering': ('material__supplier', 'material', 'umbrella_product')},
        ),
        migrations.RenameField(
            model_name='umbrellaproductbillofmaterial',
            old_name='product',
            new_name='umbrella_product',
        ),
        migrations.AlterUniqueTogether(
            name='productbillofmaterial',
            unique_together=set([('material', 'product')]),
        ),
        migrations.AlterUniqueTogether(
            name='umbrellaproductbillofmaterial',
            unique_together=set([('material', 'umbrella_product')]),
        ),
    ]