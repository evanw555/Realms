"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.helloworld),
    url(r'^test$', views.helloworld),
]
