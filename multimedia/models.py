from django.db import models
from usuario.models import UsuarioRegistrado
from banda.models import Banda
from sede.models import Sede

class TipoRecursoMultimedia(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TIPO_RECURSO_MULTIMEDIA"
    def __unicode__(self):
        return self.nombre    
    
class RecursoMultimediaBanda(models.Model):
    banda=models.ForeignKey(Banda)
    tipo=models.ForeignKey(TipoRecursoMultimedia)
    nombre=models.CharField(max_length=200)
    recurso=models.ImageField(upload_to="recursos_banda")
    class Meta:
        db_table="RECURSO_MULTIMEDIA_BANDA"
        
class RecursoMultimediaSede(models.Model):
    sede=models.ForeignKey(Sede)
    tipo=models.ForeignKey(TipoRecursoMultimedia)
    nombre=models.CharField(max_length=200)
    recurso=models.ImageField(upload_to="recursos_sede")
    class Meta:
        db_table="RECURSO_MULTIMEDIA_SEDE"
        
