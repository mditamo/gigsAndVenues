from django.forms import ModelForm
from django import forms
from sede.models import Sede,ConfiguracionSede
from django.db import models

class SedeForm(ModelForm):
    class Meta:
        model = Sede
        exclude=('complejo','direccion')
        widgets={
                 'descripcion': forms.Textarea(attrs={'cols':10, 'class':'ckeditor', 'width': '500px'}),
                 'fecha_habilitacion': forms.TextInput(attrs={'class':'datePicker', 'readonly':'true'})
        }

class ConfiguracionSedeForm(ModelForm):
    class Meta:
        model = ConfiguracionSede
        exclude=('sede')
        