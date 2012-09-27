from django import forms
from django.forms import ModelForm
from fan.models import Fan

class FanForm(ModelForm):
    class Meta:
        model = Fan
        exclude = ('direccion','username','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions','tipo_usuario')
        
    
        