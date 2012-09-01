from django import forms
from django.db import models
from django.forms import ModelForm
from banda.models import ComposicionBanda, Banda, Genero

class ComposicionBandaForm(ModelForm):
    class Meta:
        model = ComposicionBanda
        exclude = ('banda','musico')

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%d/%m/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class ComposicionBandaForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = ComposicionBanda
        exclude = ('banda','musico')


class BandaForm(ModelForm):
    class Meta:
        model = Banda
        exclude = ('musicos')
