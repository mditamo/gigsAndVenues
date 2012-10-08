from django.forms import ModelForm
from entrada.models import ReservaEvento
from entrada.models import ConfiguracionEntradaEvento

class ReservaEventoForm(ModelForm):
    class Meta:
        model = ReservaEvento
        exclude = ('fan','codigo_retiro','fecha_vencimiento','estado')
        
    def __init__(self,evento_id, *args, **kwargs):
        super(ReservaEventoForm, self).__init__(*args, **kwargs)
        #self.fields['usuario'].widget.attrs['hidden'] = 'hidden'
        self.fields['tipo_entrada'].queryset = ConfiguracionEntradaEvento.objects.filter(evento__id=evento_id)
        
        
class ConfiguracionEntradaEventoForm(ModelForm):
    class Meta:
        model = ConfiguracionEntradaEvento
        exclude = ('evento','cantidad_entradas_disponibles','cantidad_entradas_reserva')