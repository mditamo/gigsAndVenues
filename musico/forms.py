from django import forms
from django.forms import ModelForm
from musico.models import Musico

class MusicoForm(ModelForm):
    class Meta:
        model = Musico
        exclude = ('direccion','username','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions','tipo_usuario')
        
    
        