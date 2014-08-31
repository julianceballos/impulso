#!/usr/bin/python
#encoding: utf-8

import thumbs

from django.db import models

class Group(models.Model):
  
  name = models.CharField(max_length=255, verbose_name='Grupo')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

  def __unicode__(self):
    return self.name

class Contact(models.Model):
  
  first_name = models.CharField(max_length=255, verbose_name='Nombre', blank=True)
  last_name = models.CharField(max_length=255, verbose_name='Apellido', blank=True)
  birth_date = models.DateField(verbose_name='Fec. Nac.', blank=True, null=True)
  picture = thumbs.ImageWithThumbsField(upload_to="pictures", sizes=((50,50), (125,125), (200,200), (300,300)), verbose_name='Foto', blank=True)
  email = models.EmailField(verbose_name='Correo', blank=True, null=True)
  phone = models.CharField(max_length=10, verbose_name='Teléfono', blank=True)
  mobile = models.CharField(max_length=10, verbose_name='Celular', blank=True)
  address = models.CharField(max_length=255, verbose_name='Dirección', blank=True)
  colony = models.CharField(max_length=255, verbose_name='Colonia', blank=True)
  city = models.CharField(max_length=255, verbose_name='Ciudad', blank=True)
  state = models.CharField(max_length=255, verbose_name='Estado', blank=True)
  zip_code = models.CharField(max_length=5, verbose_name='Código postal', blank=True)
  group = models.ManyToManyField(Group, related_name="groups", verbose_name='Grupo', blank=True, null=True)
  amount = models.CharField(max_length=10, verbose_name='Monto de donativo', blank=True)
  payment = models.CharField(max_length=255, verbose_name='Tipo de pago', blank=True)
  period = models.CharField(max_length=255, verbose_name='Periodo de pago', blank=True)
  tax_info = models.CharField(max_length=13, verbose_name='RFC', blank=True)
  verified = models.BooleanField(default=False, verbose_name='Verificado')
  active = models.BooleanField(default=True, verbose_name='Activo')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

  def group_list(self):
    out = ''
    for group in self.group.all():
      out += group.name + ', '
    return out[0: len(out) - 2]

  def __unicode__(self):
    return self.first_name + ' ' + self.last_name
