from django.forms import ModelForm
from django import forms
from .models import Artista

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista 
        fields = ['idAr', 'nombreAr', 'apellidoAr', 'fotoAr', 
                  'descAr', 'fechaIngr'] 
   
        # fields = '__all__' 
