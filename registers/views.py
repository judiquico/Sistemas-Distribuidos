# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import *
from .models import *

def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            user = User.objects.create(
                username=company.nit_company,
                password=company.id_representant,
                email=company.nit_company + '@gmail.com',
            )
            company.user = user
            company.save()
            return render(request, 'save.html', {
                'username': company.nit_company,
                'password': company.id_representant,
            })
        return render(request, 'index.html', {'form': form })
    return render(request, 'index.html', {'form': RegisterForm()})
