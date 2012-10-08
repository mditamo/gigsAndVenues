from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^condiciones/(?P<negociacion_id>\d+)/agregarCondicion','condiciones.views.agregarCondicion'),
)
