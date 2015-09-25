from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Create your views here.


def homepage(request):
    return render(request, 'game/home.html')

