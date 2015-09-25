"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^test$', views.homepage),
]
