from django.conf.urls.defaults import *
from usuario.forms import UsuarioRegistradoForm

urlpatterns = patterns('',
    url(r'^usuario/register/$', 'registration.views.register',
            {'backend': 'registro_usuario.CustomBackend', 'form_class': UsuarioRegistradoForm}),
    url(r'^usuario/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^usuario/', include('registration.backends.default.urls')),
    (r'^usuario/perfil', 'usuario.views.perfil'),
)

