from django import forms
from django.forms import ModelForm
from django.db import models
from tema.models import *


class TemaBandaForm(ModelForm):
    class Meta:
        model = TemaBanda
        exclude= ("tema","banda")
    
class TemaForm(ModelForm):
    class Meta:
        model = Tema
    
