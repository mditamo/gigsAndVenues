from django import forms
from registration.forms import RegistrationForm
from usuario.models import TipoUsuario
from direccion.models import Barrio

class UsuarioRegistradoForm(RegistrationForm):
    fecha_nacimiento=forms.DateField()
    tipo_usuario=forms.ModelChoiceField(queryset=TipoUsuario.objects.all())
    calle = forms.CharField(max_length=200)
    numero=forms.DecimalField()
    barrio=forms.ModelChoiceField(queryset=Barrio.objects.all())