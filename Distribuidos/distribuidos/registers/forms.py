# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Company

        fields = [
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
        ]

        labels = {
            'nit_company' : 'Nit',
            'contributive_regimen' : 'Regimen Contributivo',
            'name' : 'Nombre Empresa',
            'country' : 'Pais',
            'department' : 'Departamento',
            'city' : 'Ciudad',
            'logo' : 'Logo',
            'dian_resolution' : 'Resolucion Dian',
            'address' : 'Direccion',
            'telephone' : 'Telefono' ,
            'name_register' : 'Nombre Registro',
            'id_representant' : 'Id Representante',
            'name_representan' : 'Nombre Representante',
            'last_name_representan' : 'Apellido Representante',
        }

        widgets = {
            'nit_company' : forms.TextInput(attrs={'class': 'form-control'}),
            'contributive_regimen' : forms.Select(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'country' : forms.TextInput(attrs={'class': 'form-control'}),
            'department' : forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'dian_resolution':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'telephone':forms.TextInput(attrs={'class': 'form-control'}),
            'name_register':forms.TextInput(attrs={'class': 'form-control'}),
            'id_representant':forms.TextInput(attrs={'class': 'form-control'}),
            'name_representan':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_representan':forms.TextInput(attrs={'class': 'form-control'}),
        }
