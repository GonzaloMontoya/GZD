from django.shortcuts import render, redirect, get_object_or_404
from .models import VistaObra, Artista
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import ArtistaForm

# Create your views here.

def base(request):
    return render(request, 'GroundZero/base.html')

def index(request):
    return render(request, 'GroundZero/index.html')

def producto(request):
    return render(request, 'GroundZero/producto.html')

def baseingreso(request):
    return render(request, 'GroundZero/baseingreso.html')

# def gestArtista(request):
#     return render(request, 'GroundZero/gestion/gestArtista.html')


#Datos de la base 
def obras(request):
    obras = VistaObra.objects.all()
    context = {"obras":obras}
    return render(request, 'GroundZero/obras.html', context)

def artistas(request):
    artistas  = Artista.objects.all()
    context = {"artistas":artistas}
    return render(request, 'GroundZero/artistas.html', context)

@login_required
def gestArtista(request):
    artistas  = Artista.objects.all()
    context = {"artistas":artistas}
    return render(request, 'GroundZero/gestion/gestArtista.html', context)

# def agregarArtista(request):
#     return render(request, "GroundZero/gestion/agregarArtista.html")

# def editarArtista(request):
#     return render(request, "GroundZero/gestion/editarArtista.html")


#CRUD gestión de artistas

@login_required
def borrarArtista(request, idAr):
    artistas = Artista.objects.get(idAr=idAr)
    artistas.delete()
    return redirect('gestArtista')

@login_required
def agregarArtista(request):
    Datos = ArtistaForm(request.POST or None, request.FILES or None)
    if Datos.is_valid():
        Datos.save()
        return redirect('gestArtista')
    return render(request, "GroundZero/gestion/agregarArtista.html", {"Datos":Datos})


##No funcional pero despliega datos

@login_required
def editarArtista(request, idAr):
    artistas = Artista.objects.get(idAr=idAr)
    Datos = ArtistaForm(request.POST or None, request.FILES or None, instance=artistas)
    if Datos.is_valid() and request.POST:
        Datos.save()
        return redirect('gestArtista')
    return render(request, "GroundZero/gestion/editarArtista.html", {"Datos":Datos})


## No funciona y no despliega nada ## (Debe ser por el contador en "form.html")
# @login_required    
# def editarArtista(request, idAr):
    
#     artistas = get_object_or_404(Artista, idAr=idAr)

#     data = {
#         'form': ArtistaForm(instance=artistas)
#     }

#     if request.method == 'POST':
#         Datos = ArtistaForm(data=request.POST, instance=artistas, files=request.FILES)
#         if Datos.is_valid():
#             Datos.save()
#             return redirect(to="gestArtista")
#         data["form"] = Datos

#     return render(request, "GroundZero/gestion/editarArtista.html", data)




#Gestión ingreso
def login(request):
    return render(request, "GroundZero/login.html")

def register(request):
    return render(request, "GroundZero/register.html")
