# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'nit_company',
        'contributive_regimen',
        'name',
        'country',
        'department',
        'city',
        'logo',
        'dian_resolution',
        'address',
        'telephone',
        'name_register',
        'id_representant',
        'name_representan',
        'last_name_representan',
    )
