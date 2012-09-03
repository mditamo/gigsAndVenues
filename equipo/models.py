from django.db import models
from musico.models import Musico

class ClasificacionEquipo(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="CLASIFICION_EQUIPO"

    def __unicode__(self):
        return self.nombre    
        
class Equipo(models.Model):
    nombre=models.CharField(max_length=200)
    clasificacion_equipo=models.ForeignKey(ClasificacionEquipo)
    class Meta:
        db_table="EQUIPO"

    def __unicode__(self):
        return self.nombre     
      
class EquipoMusico(models.Model):
    musico=models.ForeignKey(Musico)
    equipo=models.ForeignKey(Equipo)
    class Meta:
        db_table="EQUIPO_MUSICO"

    def __unicode__(self):
            return self.musico.username  