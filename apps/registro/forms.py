from django import forms
from .models import Provincia, Ciudad, CategoriaProduccion
from django.contrib.auth.forms import UserCreationForm

class FormCrearCiudad(forms.Form):
	provincia=forms.ModelChoiceField(queryset=Provincia.objects.all())	
	nombre=forms.CharField(max_length=40)

class FormPerfilUsuario(UserCreationForm):
	descripcion=forms.CharField(widget=forms.Textarea)
	telefono=forms.CharField(max_length=9)
	provincia=forms.ModelChoiceField(queryset=Provincia.objects.all())
	ciudad=forms.ModelChoiceField(queryset=Ciudad.objects.filter(provincia=1))
	categoria=forms.ModelChoiceField(queryset=CategoriaProduccion.objects.all())