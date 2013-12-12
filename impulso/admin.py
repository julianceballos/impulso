#!/usr/bin/python
#encoding: utf-8

from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect

import csv

from extraadminfilters.filters import UnionFieldListFilter

from models import *

def verify_all(modeladmin, request, queryset):
  queryset.update(verified=True)

verify_all.short_description = 'Verificar seleccionados'

def export(modeladmin, request, queryset):

  output = []

  for item in queryset:
    output += item.first_name + ',' + item.last_name + ',' + item.email + '\n'

  response = HttpResponse(output, mimetype='text/csv')
  response['Content-Disposition'] = 'attachment; filename=contacts.csv'
  return response

export.short_description = 'Exportar seleccionados'

contact_admin_actions = [verify_all, export]

class ContactAdmin(admin.ModelAdmin):

  list_display = ('first_name', 'last_name', 'email', 'birth_date', 'colony', 'state', 'zip_code', 'verified')
  list_display_links = ('first_name', 'last_name', 'email')
  list_filter = ('verified', 'city', 'colony', ('group', UnionFieldListFilter))
  search_fields = ('first_name', 'last_name', 'email')
  actions = contact_admin_actions

class GroupAdmin(admin.ModelAdmin):

  pass

admin.site.register(Contact, ContactAdmin)

admin.site.register(Group)

from django.contrib.sites.models import Site

admin.site.unregister(Site)

from django.contrib.auth.models import Group

admin.site.unregister(Group)
