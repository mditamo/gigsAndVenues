from django import forms
from django.forms import ModelForm
from suscripcion.models import SuscripcionBanda, SuscripcionComplejo, SuscripcionGenero, SuscripcionMusico

class SuscripcionBandaForm(ModelForm):
    class Meta:
        model = SuscripcionBanda
        exclude = ('banda','usuario')
        
class SuscripcionComplejoForm(ModelForm):
    class Meta:
        model = SuscripcionComplejo
        exclude = ('complejo','usuario')    
        
class SuscripcionGeneroForm(ModelForm):
    class Meta:
        model = SuscripcionGenero
        exclude = ('genero','usuario')       

class SuscripcionMusicoForm(ModelForm):
    class Meta:
        model = SuscripcionMusico
        exclude = ('musico','usuario')