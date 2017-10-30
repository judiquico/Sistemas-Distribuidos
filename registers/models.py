# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Company(models.Model):
    CONTRIBUTIVE_REGIMEN = [
        ('Simplificado', 'Simplificado'),
        ('Comun', 'Comun'),
        ('Prima media con prestacion definida', 'Prima media con prestacion definida'),
        ('Legal vigente', 'Legal vigente'),
        ('Especial', 'Especial'),
        ('Ahorro individual con solidaridad', 'Ahorro individual con solidaridad'),
    ]

    user  = models.ForeignKey(User)
    nit_company = models.CharField(max_length=50, unique=True)
    contributive_regimen = models.CharField(choices=CONTRIBUTIVE_REGIMEN , default='Comun', max_length=50)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', blank=True)
    dian_resolution = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    name_register = models.CharField(max_length=50)
    id_representant = models.CharField(max_length=50)
    name_representan = models.CharField(max_length=50)
    last_name_representan = models.CharField(max_length=50)
