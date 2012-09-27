from django.db import models
from usuario.models import UsuarioRegistrado

class Complejo(UsuarioRegistrado):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="COMPLEJO"

class LikeComplejo(models.Model):
    complejo=models.ForeignKey(Complejo,related_name="ID")
    usuario=models.ForeignKey(UsuarioRegistrado)
    
    class Meta:
        db_table="LIKE_COMPLEJO"
            