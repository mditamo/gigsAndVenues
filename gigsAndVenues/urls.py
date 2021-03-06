from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from forum.sitemap import SitemapForum, SitemapTopic
from djangobb_forum import settings as forum_settings
from gigsAndVenues import settings

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    (r'^', include('usuario.urls')),
    url(r'^$', 'home.views.index'),
	(r'^', include('mapa.urls')),
    (r'^', include('multimedia.urls')),
    (r'^', include('celular.urls')),
    (r'^', include('banda.urls')),
    (r'^', include('musico.urls')),
    (r'^', include('disco.urls')),
    (r'^', include('noticia.urls')),
    (r'^', include('equipo.urls')),
    (r'^', include('genero.urls')),
    (r'^', include('complejo.urls')),
    (r'^', include('buscador.urls')),
    (r'^', include('sede.urls')),
    (r'^', include('suscripcion.urls')),
    (r'^', include('fan.urls')), 
	(r'^', include('evento.urls')),
    (r'^', include('negociacion.urls')),
    (r'^', include('oferta.urls')),
    (r'^', include('condiciones.urls')),
	(r'^', include('transferencia.urls')),
    (r'^', include('entrada.urls')),
    (r'^', include('cronograma.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/static'}),
    (r'css/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/css'}),
    (r'images/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/images'}),
    (r'js/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT + 'templates/js'}),
   
    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^forum/account/', include('django_authopenid.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),                       

)

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('django_messages.urls')),
   )

if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


