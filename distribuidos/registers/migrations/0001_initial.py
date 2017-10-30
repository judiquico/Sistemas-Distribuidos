# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 23:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit_company', models.CharField(max_length=50)),
                ('contributive_regimen', models.CharField(choices=[('Simplificado', 'Simplificado'), ('Comun', 'Comun'), ('Prima media con prestacion definida', 'Prima media con prestacion definida'), ('Legal vigente', 'Legal vigente'), ('Especial', 'Especial'), ('Ahorro individual con solidaridad', 'Ahorro individual con solidaridad')], default='Comun', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='logos/')),
                ('dian_resolution', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('name_register', models.CharField(max_length=50)),
                ('id_representant', models.CharField(max_length=50)),
                ('name_representan', models.CharField(max_length=50)),
                ('last_name_representan', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
