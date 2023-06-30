from django.shortcuts import render, redirect
from .models import VistaObra, Artista
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def base(request):
    return render(request, 'GroundZero/base.html')

def index(request):
    return render(request, 'GroundZero/index.html')

def baseproducto(request):
    return render(request, 'GroundZero/baseproducto.html')

def baseingreso(request):
    return render(request, 'GroundZero/baseingreso.html')

def gestArtista(request):
    return render(request, 'GroundZero/gestion/gestArtista.html')


#Datos de la base 
def obras(request):
    obras = VistaObra.objects.all()
    context = {"obras":obras}
    return render(request, 'GroundZero/obras.html', context)

def artistas(request):
    artistas  = Artista.objects.all()
    context = {"artistas":artistas}
    return render(request, 'GroundZero/artistas.html', context)



#Gestión ingreso
def login(request):
    return render(request, "GroundZero/login.html")

def register(request):
    return render(request, "GroundZero/register.html")
