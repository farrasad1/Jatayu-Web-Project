from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def map(request):
    return render(request, 'home.html')

def tentang(request):
    return render(request, 'tentang.html')

def kontak(request):
    return render(request, 'kontak.html')

def unduh(request):
    return render(request, 'unduh.html')