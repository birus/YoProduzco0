from django.db import models
from django.contrib.auth.models import User

class Provincia(models.Model):
	nombre=models.CharField(max_length=40)

	def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):
	provincia=models.ForeignKey('Provincia')
	nombre=models.CharField(max_length=40)

	def __unicode__(self):
		return self.nombre

class CategoriaProduccion(models.Model):
	nombre=models.CharField(max_length=40)

	def __unicode__(self):
		return self.nombre


class PerfilUsuario(models.Model):
	usuario=models.OneToOneField(User)
	descripcion=models.TextField(max_length=500)
	telefono=models.IntegerField(max_length=9, null=True, blank=True)
	provincia=models.ForeignKey('Provincia')
	ciudad=models.ForeignKey('Ciudad')
	categoria=models.ForeignKey('CategoriaProduccion')

	def __unicode__(self):
		return self.usuario.username
