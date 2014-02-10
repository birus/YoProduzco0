from django.views.generic import FormView
from .forms import FormCrearCiudad, FormPerfilUsuario
from django.core.urlresolvers import reverse_lazy
from .models import Ciudad, PerfilUsuario

class CrearCiudad(FormView):
	template_name = 'registro/crear_ciudad.html'
	form_class= FormCrearCiudad
	success_url=reverse_lazy('inicio')

	def form_valid(self, form):
		ciudad=Ciudad()
		ciudad.nombre=form.cleaned_data['nombre']
		ciudad.provincia=form.cleaned_data['provincia']
		ciudad.save()

		return super(CrearCiudad, self).form_valid(form)

class RegistraUsuario(FormView):
	template_name='registro/registrarse.html'
	form_class=FormPerfilUsuario
	success_url=reverse_lazy('inicio')

	def form_valid(self, form):
		user=form.save()
		perfil= PerfilUsuario()
		perfil.usuario=user
		perfil.descripcion=form.cleaned_data['descripcion']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.provincia=form.cleaned_data['provincia']
		perfil.ciudad=form.cleaned_data['ciudad']
		perfil.categoria=form.cleaned_data['categoria']
		perfil.save()

		return super(RegistraUsuario, self).form_valid(form)