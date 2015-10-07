"""myproject URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = (
    url(r'^$', views.homepage, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^login_attempt/$', views.login_attempt, name='login_attempt'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^signup/attempt/$', views.sign_up_attempt, name='signup_attempt'),
    url(r'^realm_select/$', views.realm_select, name='realm_select'),
    url(r'^realm/$', views.realm_select, name='realm_view'),
    # url(r'^update_attempt/$', views.update_attempt, name='update_attempt')
)
