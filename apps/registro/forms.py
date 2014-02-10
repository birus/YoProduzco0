from django import forms
from .models import Provincia


class FormCrearCiudad(forms.Form):
	provincia=forms.ModelChoiceField(queryset=Provincia.objects.all())	
	nombre=forms.CharField(max_length=40)