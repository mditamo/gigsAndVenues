from django.forms        import ModelForm
from general.forms       import make_custom_datefield
from negociacion.models  import Negociacion

class NegociacionComplejoFormPaso1(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('fecha,hora,bandas,evento,monto,complejo,tipo_banda,inicio_negociacion,estado,condiciones')
        
class NegociacionBandaFormPaso1(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('banda')

class NegociacionComplejoFormPaso2(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('nombre,inicio_negociacion,fecha,hora,complejo,sede,evento,monto,estado,condiciones')
        
class NegociacionBandaFormPaso2(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('banda')
        
class NegociacionComplejoFormPaso3(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('nombre,inicio_negociacion,hora,complejo,sede,evento,monto,estado,bandas,condiciones')
        
class NegociacionBandaFormPaso3(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Negociacion
        exclude = ('banda')        
"""class NegociacionForm(ModelForm,UsuarioRegistrado):
    formfield_callback = make_custom_datefield
    
    def excluir(self,UsuarioRegistrado):
        if UsuarioRegistrado.is_complejo():
            return 'complejo'
        else: 
            return 'banda' 
    class Meta:
        model = Negociacion
        exclude = (excluir(UsuarioRegistrado))"""
