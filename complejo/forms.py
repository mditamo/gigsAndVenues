from django import forms
from django.forms import ModelForm
from complejo.models import Complejo
       
class ComplejoForm(ModelForm):
    class Meta:
        model = Complejo
        exclude = ('direccion','username','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions','tipo_usuario')
        widgets={
                 'descripcion': forms.Textarea(attrs={'cols':10, 'class':'ckeditor', 'width': '500px'}),
        }