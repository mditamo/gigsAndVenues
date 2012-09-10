from django import forms
from django.db import models
from django.forms import ModelForm
from banda.models import ComposicionBanda, Banda, Genero
from general.forms import make_custom_datefield

class ComposicionBandaForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = ComposicionBanda
        exclude = ('banda','musico')


class BandaForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Banda
        exclude = ('musicos')
