from django.forms import ModelForm
from noticia.models import NoticiaBanda

class NoticiaBandaForm(ModelForm):
    class Meta:
        model = NoticiaBanda
        exclude=('banda','fecha_publicacion','estado')

