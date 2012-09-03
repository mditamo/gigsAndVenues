from django import forms
from django.forms import ModelForm
from equipo.models import EquipoMusico

class EquipoMusicoForm(ModelForm):
    class Meta:
        model = EquipoMusico
        exclude = ('musico')