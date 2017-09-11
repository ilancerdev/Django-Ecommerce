# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-07 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20170907_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='country',
            field=models.CharField(choices=[(b'AT', b'Austria'), (b'BE', b'Belgium'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'FR', b'France'), (b'DE', b'Germany'), (b'GB', b'Great Brittain'), (b'IT', b'Italy'), (b'NL', b'Netherlands'), (b'NO', b'Norway'), (b'RU', b'Russia'), (b'SE', b'Sweden'), (b'CH', b'Switzerland')], max_length=2),
        ),
        migrations.AlterField(
            model_name='ownaddress',
            name='country',
            field=models.CharField(choices=[(b'AT', b'Austria'), (b'BE', b'Belgium'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'FR', b'France'), (b'DE', b'Germany'), (b'GB', b'Great Brittain'), (b'IT', b'Italy'), (b'NL', b'Netherlands'), (b'NO', b'Norway'), (b'RU', b'Russia'), (b'SE', b'Sweden'), (b'CH', b'Switzerland')], max_length=2),
        ),
        migrations.AlterField(
            model_name='relation',
            name='country',
            field=models.CharField(choices=[(b'AT', b'Austria'), (b'BE', b'Belgium'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'FR', b'France'), (b'DE', b'Germany'), (b'GB', b'Great Brittain'), (b'IT', b'Italy'), (b'NL', b'Netherlands'), (b'NO', b'Norway'), (b'RU', b'Russia'), (b'SE', b'Sweden'), (b'CH', b'Switzerland')], max_length=2),
        ),
        migrations.AlterField(
            model_name='relationaddress',
            name='country',
            field=models.CharField(choices=[(b'AT', b'Austria'), (b'BE', b'Belgium'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'FR', b'France'), (b'DE', b'Germany'), (b'GB', b'Great Brittain'), (b'IT', b'Italy'), (b'NL', b'Netherlands'), (b'NO', b'Norway'), (b'RU', b'Russia'), (b'SE', b'Sweden'), (b'CH', b'Switzerland')], max_length=2),
        ),
    ]