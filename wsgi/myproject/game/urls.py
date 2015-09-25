"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from ..game import views

urlpatterns = [
    url(r'^$', views.helloworld),
]
