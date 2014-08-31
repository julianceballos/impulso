#!/usr/bin/python
#encoding: utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response as render

from django.template import RequestContext

import csv

from models import Contact, Group

def IndexRedirect(request):
  return HttpResponseRedirect('admin')

def upload_contacts(request):
  if not request.user.is_authenticated():
    return HttpResponse('You are not logged in')
  if request.FILES.__contains__('csv'):
    rows = csv.reader(request.FILES['csv'])
    count = 0
    for row in rows:
      if count > 0 and len(row) == 11:
        contactExists = Contact.objects.filter(email=row[4]).count()
        if not contactExists:
          contact = Contact(
            first_name = row[0],
            last_name = row[1],
            phone = row[2],
            mobile = row[3],
            email = row[4],
            address = row[5],
            colony = row[6],
            city = row[7],
            zip_code = row[8],
            birth_date = row[10] if row[10] != '' else '1988-11-16',
            amount = '',
            period = '',
            payment = '',
            tax_info = ''
          )
          contact.save()
          if len(row[9]) > 0:
            for group in Group.objects.filter(id__in=row[9].split(' ')):
              contact.group.add(group)
          contact.save()
      count+=1
    return HttpResponseRedirect('/admin/impulso/contact/')
  return render('admin/upload.html', {}, context_instance = RequestContext(request))

def view_contact(request, id):
  if not request.user.is_authenticated():
    return HttpResponse('You are not logged in')
  contact = Contact.objects.get(pk=id)
  return render('admin/view.html', {
    'contact': contact
  }, context_instance = RequestContext(request))
