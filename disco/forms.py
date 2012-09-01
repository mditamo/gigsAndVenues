from django import forms
from django.forms import ModelForm
from disco.models import Disco

class DiscoForm(ModelForm):
    class Meta:
        model = Disco
        exclude = ('banda, temas')

