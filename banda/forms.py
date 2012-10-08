from django import forms
from django.db import models
from django.forms import ModelForm
from banda.models import ComposicionBanda, Banda
from general.forms import make_custom_datefield

class ComposicionBandaForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = ComposicionBanda
        exclude = ('banda','musico')


class BandaForm(ModelForm):
    class Meta:
        model = Banda
        exclude = ('musicos') 
        widgets={
                 'descripcion': forms.Textarea(attrs={'cols':10, 'class':'ckeditor', 'width': '500px'}),
                 'fecha_creacion': forms.TextInput(attrs={'class':'datePicker', 'readonly':'true'})
        }
