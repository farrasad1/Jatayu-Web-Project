from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sign_in(request):
    return HttpResponse('This is sign in page')

def register(request):
    return HttpResponse('This is register page')