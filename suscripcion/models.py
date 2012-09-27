from django.db import models
from usuario.models import UsuarioRegistrado
from banda.models import Banda
from complejo.models import Complejo
from genero.models import Genero
from musico.models import Musico

class Periodicidad(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="PERIODICIDAD"
    def __unicode__(self):
        return self.nombre    
    
    
class SuscripcionBanda(models.Model):
    banda=models.ForeignKey(Banda)
    periodicidad=models.ForeignKey(Periodicidad)
    usuario=models.ForeignKey(UsuarioRegistrado)
    class Meta:
        db_table="SUSCRIPCION_BANDA"
        
class SuscripcionComplejo(models.Model):
    complejo=models.ForeignKey(Complejo,related_name="COMPLEJO_ID")
    periodicidad=models.ForeignKey(Periodicidad)
    usuario=models.ForeignKey(UsuarioRegistrado)
    class Meta:
        db_table="SUSCRIPCION_COMPLEJO"
        
class SuscripcionGenero(models.Model):
    genero=models.ForeignKey(Genero)
    periodicidad=models.ForeignKey(Periodicidad)
    usuario=models.ForeignKey(UsuarioRegistrado)
    class Meta:
        db_table="SUSCRIPCION_GENERO"

class SuscripcionMusico(models.Model):
    musico=models.ForeignKey(Musico,related_name="MUSICO_ID")
    periodicidad=models.ForeignKey(Periodicidad)
    usuario=models.ForeignKey(UsuarioRegistrado)
    class Meta:
        db_table="SUSCRIPCION_MUSICO"