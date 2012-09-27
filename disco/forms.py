from django import forms
from django.forms import ModelForm
from disco.models import Disco, ComposicionDisco
from general.forms import make_custom_datefield

class DiscoForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Disco
        exclude = ('banda', 'temas')

class ComposicionDiscoForm(ModelForm):
    class Meta:
        model = ComposicionDisco
        exclude = ('disco')

