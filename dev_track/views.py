from __future__ import print_function, unicode_literals

from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Hello, world ... the dev-demo is running.')
