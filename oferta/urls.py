from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^oferta/(?P<negociacion_id>\d+)/generar_oferta', 'condiciones.views.agregarCondicion'), 

)
