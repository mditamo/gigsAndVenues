from django.db import models
from usuario.models import UsuarioRegistrado

class Posicion(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="POSICION"

    def __unicode__(self):
        return self.nombre

class Estilo(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="ESTILO"

    def __unicode__(self):
        return self.nombre

class Musico(UsuarioRegistrado):
    posicion=models.ForeignKey(Posicion, null=True)
    estilo=models.ForeignKey(Estilo, null=True)
    class Meta:
        db_table="MUSICO"
        
class LikeMusico(models.Model):
    musico=models.ForeignKey(Musico,related_name="ID")
    usuario=models.ForeignKey(UsuarioRegistrado)
    
    class Meta:
        db_table="LIKE_MUSICO"
              
