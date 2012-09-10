from django.db import models
from django.contrib.auth.models import User
from direccion.models import Direccion

class TipoUsuario(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TIPO_USUARIO"

    def __unicode__(self):
        return self.nombre

class UsuarioRegistrado(User):
    fecha_nacimiento=models.DateField()
    tipo_usuario=models.ForeignKey(TipoUsuario)
    direccion=models.OneToOneField(Direccion)
    class Meta:
        db_table="USUARIO_REGISTRADO"

    def is_fan(self):
            return self.tipo_usuario.nombre=="Fan"

    def is_musico(self):
        return self.tipo_usuario.nombre=="Musico"

    def is_complejo(self):
        return self.tipo_usuario.nombre=="Complejo"

class Fan(UsuarioRegistrado):
    class Meta:
        db_table="FAN"
