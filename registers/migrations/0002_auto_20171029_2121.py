# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='nit_company',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
