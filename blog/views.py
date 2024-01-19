from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    print('Blog do App')
    return HttpResponse('Blog do App 1')