from django.shortcuts import render


# Create your views here.

def base(request):
    return render(request, 'GroundZero/base.html')

def index(request):
    return render(request, 'index.html')

def obras(request):
    return render(request, 'obras.html')

def artistas(request):
    return render(request, 'artistas.html')

def baseproducto(request):
    return render(request, 'baseproducto.html')

def baseingreso(request):
    return render(request, 'baseingreso.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')