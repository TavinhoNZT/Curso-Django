from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('Home do App')
    return HttpResponse('Home do App')