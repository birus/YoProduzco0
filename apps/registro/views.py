from django.views.generic import FormView
from .forms import FormCrearCiudad
from django.core.urlresolvers import reverse_lazy
from .models import Ciudad

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