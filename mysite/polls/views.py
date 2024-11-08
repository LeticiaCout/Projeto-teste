from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, meu nome não é Johnny")