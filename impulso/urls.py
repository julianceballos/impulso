#!/usr/bin/python
#encoding: utf-8

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import IndexRedirect

urlpatterns = patterns('',
    (r'^$', IndexRedirect),
    (r'^admin/', include(admin.site.urls)),
)
