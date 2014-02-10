from django.contrib import admin
from .models import Provincia, Ciudad, CategoriaProduccion, PerfilUsuario

admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(PerfilUsuario)
admin.site.register(CategoriaProduccion)