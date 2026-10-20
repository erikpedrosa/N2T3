from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ola_mundo(request):
    return HttpResponse("Olá! Esta é a minha primeira página oficial no Django.")