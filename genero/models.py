from django.db import models
from usuario.models import UsuarioRegistrado

class Genero(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="GENERO"
    
    def __unicode__(self):
        return self.nombre        

class LikeGenero(models.Model):
    genero=models.ForeignKey(Genero)
    usuario=models.ForeignKey(UsuarioRegistrado)
    
    class Meta:
        db_table="LIKE_GENERO"
            