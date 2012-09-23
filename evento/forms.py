from django.forms import ModelForm
from general.forms import make_custom_datefield
from evento.models import Evento

class EventoForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Evento
        exclude = ('fans','nombre_complejo','complejo')
