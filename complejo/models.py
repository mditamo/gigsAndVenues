from django.db import models
from django.contrib.auth.models import User
from usuario.models import UsuarioRegistrado
from direccion.models import Direccion

class Complejo(UsuarioRegistrado):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="COMPLEJO"

class LikeComplejo(models.Model):
    complejo=models.ForeignKey(Complejo,related_name="COMPLEJO_ID")
    usuario=models.ForeignKey(UsuarioRegistrado)
    
    class Meta:
        db_table="LIKE_COMPLEJO"
        
class TipoSede(models.Model):
    nombre=models.CharField(max_length=200)
    
    class Meta:
        db_table="TIPO_SEDE"
    def __unicode__(self):
        return self.nombre
        
class Sede(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=500)
    telefono=models.CharField(max_length=12)
    horario_apertura=models.CharField(max_length=5)
    horario_cierre=models.CharField(max_length=5)
    capacidad_maxima_personas=models.IntegerField()
    fecha_habilitacion=models.DateField()
    direccion=models.ForeignKey(Direccion,related_name="DIRECCION_ID")
    tipo_sede=models.ForeignKey(TipoSede)
    complejo=models.ForeignKey(Complejo)
    
    class Meta:
        db_table="SEDE"

class ConfiguracionSede(models.Model):
    nombre=models.CharField(max_length=200)
    cantidad_entradas_disponibles=models.IntegerField()
    cantidad_entradas_reserva=models.IntegerField()
    sede=models.ForeignKey(Sede)
    
    class Meta:
        db_table="CONFIGURACION_SEDE"
    


    