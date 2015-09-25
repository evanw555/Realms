"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls')),
    url(r'^$', include('game.urls')),
]
