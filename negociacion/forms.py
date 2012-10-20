from django.forms        import ModelForm
from general.forms       import make_custom_datefield
from negociacion.models  import Negociacion
from sede.models         import Sede


class NegociacionComplejoFormPaso1(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        fields = ('nombre','sede')        

        
class NegociacionBandaFormPaso1(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        fields = ('nombre','complejo')

class NegociacionComplejoFormPaso2(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('nombre,inicio_negociacion,fecha,hora,complejo,sede,evento,monto,estadoNegociacion,condiciones,banda')
        
class NegociacionBandaFormPaso2(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        fields = ('sede','banda')
        
class NegociacionComplejoFormPaso3(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        fields = ('fecha','hora')  
        
class NegociacionBandaFormPaso3(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        fields = ('fecha','hora')     


