from django import forms
from django.forms import ModelForm
from disco.models import *
from general.forms import make_custom_datefield


class TemaBandaForm(ModelForm):
    class Meta:
        model = TemaBanda
        exclude= ("tema","banda")
    
class TemaForm(ModelForm):
    class Meta:
        model = Tema
    
class DiscoForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Disco
        exclude = ('banda', 'temas')

class ComposicionDiscoForm(ModelForm):
    class Meta:
        model = ComposicionDisco
        exclude = ('disco','tema_banda')

