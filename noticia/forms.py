from django.forms import ModelForm
from django import forms
from noticia.models import NoticiaBanda, NoticiaComplejo
from django.db import models


class NoticiaBandaForm(ModelForm):
    class Meta:
        model = NoticiaBanda
        exclude=('banda','fecha_publicacion','estado')
        widgets={
                 'contenido': forms.Textarea(attrs={'cols':120, 'class':'ckeditor'})
        }

class NoticiaComplejoForm(ModelForm):
    class Meta:
        model = NoticiaComplejo
        exclude=('complejo','fecha_publicacion','estado')
        widgets={
                 'contenido': forms.Textarea(attrs={'cols':120, 'class':'ckeditor'})
        }
