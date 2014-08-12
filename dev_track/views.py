from __future__ import print_function, unicode_literals

from django.http import HttpRespense
#from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpRespense('Hello, world ... the dev-demo is running.')
