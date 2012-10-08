from django import forms
from django.forms import ModelForm
from multimedia.models import RecursoMultimediaBanda, RecursoMultimediaSede

class RecursoMultimediaBandaForm(ModelForm):
    class Meta:
        model = RecursoMultimediaBanda
        exclude = ('banda')
        
class RecursoMultimediaSedeForm(ModelForm):
    class Meta:
        model = RecursoMultimediaSede
        exclude = ('sede')    