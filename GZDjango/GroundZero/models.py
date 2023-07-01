from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class VistaObra(models.Model):
    nombreV = models.CharField(max_length=50, null=False, blank = False)
    imgVista = models.ImageField(upload_to='img/', null= False, blank= False)
    def __str__(self):
        return str(self.nombreV)
   
class Artista(models.Model):
    idAr        = models.CharField(primary_key=True, max_length=6, null=False, verbose_name='idAr')
    nombreAr    = models.CharField(max_length=50, null=False, blank=False, verbose_name='nombreAr')
    apellidoAr  = models.CharField(max_length=50, null=True, blank=True, verbose_name='apellidoAr')
    fotoAr      = models.ImageField(upload_to='img/', null=False, blank=False, verbose_name='fotoAr')
    descAr      = models.CharField(max_length=250, null=False, blank=False, verbose_name='descAr')
    fechaIngr   = models.DateField(blank=False, null=False, verbose_name='fechaIgr')

    def __str__(self):
        return str(self.nombreAr)+" "+str(self.apellidoAr)

    class Meta:      
        ordering = ['nombreAr']
    
    def delete(self, using=None, keep_parents=False):
        self.fotoAr.storage.delete(self.fotoAr.name)
        return super().delete()   