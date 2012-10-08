from django.db import models
from direccion.models import Direccion
from complejo.models import Complejo
        
class TipoSede(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TIPO_SEDE"

    def __unicode__(self):
        return self.nombre

class Sede(models.Model):
    complejo=models.ForeignKey(Complejo)
    tipo_sede=models.ForeignKey(TipoSede)
    nombre=models.CharField(max_length=200)
    direccion=models.OneToOneField(Direccion)
    capaxidad_maxima_personas=models.IntegerField()
    fecha_habilitacion=models.DateField()
    descripcion=models.TextField()
    telefono=models.CharField(max_length=20)
    avatar=models.ImageField(upload_to="avatar")
    def direccion_mapa(self):
        return self.direccion.direccion_mapa();
    
    class Meta:
        db_table="SEDE"
        
    def __unicode__(self):
        return self.nombre    
    
    def imagen_avatar(self):
        return self.avatar or 'avatar/default.jpg'
    
class ConfiguracionSede(models.Model):
    sede=models.ForeignKey(Sede)
    nombre=models.CharField(max_length=200)
    cantidad_entradas_disponibles=models.IntegerField()
    cantidad_entradas_reserva=models.IntegerField()
    class Meta:
        db_table="CONFIGURACION_SEDE"
