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