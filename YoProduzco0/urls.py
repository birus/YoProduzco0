from django.conf.urls import patterns, include, url
from .views import Inicio
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',Inicio.as_view(), name='inicio'),
    #Registro
    url(r'^registro/',include('apps.registro.urls')),
    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
