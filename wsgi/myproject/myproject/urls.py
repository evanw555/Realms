"""myproject URL Configuration"""

from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('game.urls', namespace='game')),
]
