from django.conf.urls import patterns, url
from .views import CrearCiudad, RegistraUsuario

urlpatterns = patterns('',
    
    url(r'^crear_ciudad', CrearCiudad.as_view(), name='nueva_ciudad'),
    url(r'^registrarse', RegistraUsuario.as_view(), name='nuevo_usuario'),    
)
