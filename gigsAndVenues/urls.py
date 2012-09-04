from django.conf.urls import patterns, include, url
from usuario.forms import UsuarioRegistradoForm
from gigsAndVenues import settings

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from forum.sitemap import SitemapForum, SitemapTopic
from djangobb_forum import settings as forum_settings

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    url(r'^usuario/register/$', 'registration.views.register',
            {'backend': 'registro_usuario.CustomBackend', 'form_class': UsuarioRegistradoForm}),
    url(r'^usuario/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^usuario/', include('registration.backends.default.urls')),
    (r'^usuario/perfil', 'usuario.views.perfil'),
    url(r'^$', 'home.views.index'),
    (r'^', include('banda.urls')),
    (r'^', include('musico.urls')),
    (r'^', include('disco.urls')),
    (r'^', include('noticia.urls')),
    (r'^', include('equipo.urls')),
    (r'^', include('genero.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
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


