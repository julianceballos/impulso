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
  
  first_name = models.CharField(max_length=255, verbose_name='Nombre')
  last_name = models.CharField(max_length=255, verbose_name='Apellido')
  birth_date = models.DateField(verbose_name='Fec. Nac.')
  picture = thumbs.ImageWithThumbsField(upload_to="pictures", sizes=((50,50), (125,125), (200,200), (300,300)), verbose_name='Foto')
  email = models.EmailField(verbose_name='Correo')
  phone = models.CharField(max_length=10, verbose_name='Teléfono')
  mobile = models.CharField(max_length=10, verbose_name='Celular')
  street = models.CharField(max_length=255, verbose_name='Calle')
  number = models.CharField(max_length=255, verbose_name='Número')
  colony = models.CharField(max_length=255, verbose_name='Colonia')
  city = models.CharField(max_length=255, verbose_name='Ciudad')
  state = models.CharField(max_length=255, verbose_name='Estado')
  country = models.CharField(max_length=255, verbose_name='País')
  zip_code = models.CharField(max_length=5, verbose_name='Código postal')
  group = models.ManyToManyField(Group, related_name="group", verbose_name='Grupo')
  verified = models.BooleanField(default=False, verbose_name='Verificado')
  active = models.BooleanField(default=True, verbose_name='Activo')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

  def __unicode__(self):
    return self.first_name + ' ' + self.last_name
