from django.http import HttpResponseRedirect

def IndexRedirect(request):
  return HttpResponseRedirect('admin')
