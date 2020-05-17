from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, Murli and Doston!')

def about(request):
    return HttpResponse("THis is about page")