from django.conf.urls import patterns, include, url
from usuario.forms import UsuarioRegistradoForm
from gigsAndVenues import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gigsAndVenues.views.home', name='home'),
    # url(r'^gigsAndVenues/', include('gigsAndVenues.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^usuario/register/$', 'registration.views.register',
            {'backend': 'registro_usuario.CustomBackend', 'form_class': UsuarioRegistradoForm}),
    url(r'^usuario/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^usuario/', include('registration.backends.default.urls')),
    (r'^usuario/perfil', 'usuario.views.perfil'),
    url(r'^$', 'home.views.index'),
    (r'^', include('banda.urls')),
    (r'^', include('musico.urls')),
    (r'^', include('disco.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'css/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/css'}),
    (r'images/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/images'}),
    (r'js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/js'}),


)
