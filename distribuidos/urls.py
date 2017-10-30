from django.conf.urls import url
from django.contrib import admin
from registers.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'login^$', login),
]
