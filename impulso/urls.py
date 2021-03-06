#!/usr/bin/python
#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from views import IndexRedirect, upload_contacts, view_contact

urlpatterns = patterns('',
    (r'^$', IndexRedirect),
    (r'^admin/impulso/contact/(\d+)/view/$', view_contact),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/impulso/contacts/upload/$', upload_contacts),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
