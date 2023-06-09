from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [ 

    #Vistas
    path('base', views.base, name='base'),
    path('producto', views.producto, name='producto'),
    path('baseingreso', views.baseingreso, name='baseingreso'),
    path('', views.index, name='index'),
    path('artistas', views.artistas, name='artistas'),
    path('obras', views.obras, name='obras'),


    path('agregarArtista', views.agregarArtista, name='agregarArtista'),
    path('editarArtista/<idAr>', views.editarArtista, name='editarArtista'),
    path('borrarArtista/<idAr>', views.borrarArtista, name='borrarArtista'),
    path('gestArtista', views.gestArtista, name='gestArtista'),
    


    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
