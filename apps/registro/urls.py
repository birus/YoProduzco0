from django.conf.urls import patterns, url
from .views import CrearCiudad

urlpatterns = patterns('',
    
    url(r'^crear_ciudad', CrearCiudad.as_view(), name='nueva_ciudad'),
    
)
