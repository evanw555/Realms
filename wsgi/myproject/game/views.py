from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Create your views here.


def helloworld(request):
    return HttpResponse('Hello, world')

