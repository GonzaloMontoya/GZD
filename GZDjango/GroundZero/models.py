from django.db import models

# Create your models here.

class VistaObra(models.Model):
    nombreV = models.CharField(max_length=50)
    imgVista = models.ImageField(upload_to='img/', null= False, blank= False)
   
class Artista(models.Model):
    nombreAr    = models.CharField(max_length=50, null=False, blank=False)
    apellidoAr  = models.CharField(max_length=50, null=True, blank=True)
    fotoAr      = models.ImageField(upload_to='img/', null=False, blank=False)
    descAr      = models.CharField(max_length=250, null=False, blank=False)
    fechaIngr   = models.DateField(blank=False, null=False)

    def __str__(self):
        return str(self.nombreAr)+" "+str(self.apellidoAr)