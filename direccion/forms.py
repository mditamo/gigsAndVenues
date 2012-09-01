from django import forms
from django.forms import ModelForm
from direccion.models import Direccion

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
