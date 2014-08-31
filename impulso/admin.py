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

  output = 'nombre,apellido,fecha nacimiento,correo,telefono,movil,direccion,colonia,ciudad,estado,codigo postal,grupo\n'

  for item in queryset:
    output += item.first_name + ',' + item.last_name + ',' + str(item.birth_date.year) + '-' + str(item.birth_date.month) + '-' + str(item.birth_date.day) + ',' + item.email + ',' + item.phone + ',' + item.mobile + ',' + item.address + ',' + item.colony + ',' + item.city + ',' + item.state + ',' + item.zip_code + ',' + item.amount + ',' + item.payment + ',' + item.period + ',' + item.tax_info + ','
    for group in item.group.all():
      output += group.name + ' '
    output = output[0: len(output) - 1]
    output += '\n'

  response = HttpResponse(output, mimetype='text/csv')
  response['Content-Disposition'] = 'attachment; filename=contacts.csv'
  return response

export.short_description = 'Exportar seleccionados'

contact_admin_actions = [verify_all, export]

class ContactAdmin(admin.ModelAdmin):

  list_display = ('first_name', 'last_name', 'email', 'phone', 'birth_date', 'colony', 'state', 'zip_code', 'verified', 'group_list', 'options')
  list_display_links = ()
  list_filter = ('verified', 'city', 'colony', ('group', UnionFieldListFilter))
  search_fields = ('first_name', 'last_name', 'email')
  actions = contact_admin_actions

  def options(self, obj):
    return u"<a style='background: #417690; padding: 4px 8px; color: white; border-radius: 15px;' href='/admin/impulso/contact/" + str(obj.id) + "/view'>Ver contacto</a> <a style='background: #417690; padding: 4px 8px; color: white; border-radius: 15px;' href='/admin/impulso/contact/" + str(obj.id) + "'>Editar contacto</a>"

  options.allow_tags = True


class GroupAdmin(admin.ModelAdmin):

  pass

admin.site.register(Contact, ContactAdmin)

admin.site.register(Group)

from django.contrib.sites.models import Site

admin.site.unregister(Site)

from django.contrib.auth.models import Group

admin.site.unregister(Group)
