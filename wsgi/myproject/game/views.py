from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts.urlresolvers import reverse

# Create your views here.


def helloworld(request):
    return HttpResponse('Hello, world')

