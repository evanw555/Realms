"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from ..game import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('game.urls')),
]
