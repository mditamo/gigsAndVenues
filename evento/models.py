from django.db import models
from complejo.models import Complejo
from sede.models import Sede
from fan.models import Fan
from banda.models import Banda


class Evento(models.Model):
    nombre=models.CharField(max_length=200)
    fecha=models.DateField()
    hora_inicio=models.CharField(max_length=10);
    descripcion=models.CharField(max_length=500)
    nombre_complejo=models.CharField(max_length=200)
    complejo=models.ForeignKey(Complejo)
    sede=models.ForeignKey(Sede)
    fans= models.ManyToManyField(Fan, through="AsistenciaFan")
    bandas=models.ManyToManyField(Banda,through="Participacion")
    banda_ex=models.CharField(max_length=500)

    def direccion_sede(self):
        return self.sede.direccion_mapa();

    class Meta:
        db_table="EVENTO"

    def __unicode__(self):
        return self.nombre
    
class Participacion(models.Model):
    evento=models.ForeignKey(Evento)
    banda=models.ForeignKey(Banda)
    #hora=models.CharField(max_length=5)
    estado=models.CharField(max_length=200)
    
    class Meta:
        db_table="PARTICIPACION"    
    
    def __unicode__(self):
        return self.nombre
    
class AsistenciaFan(models.Model):
    evento=models.ForeignKey(Evento)
    fan=models.ForeignKey(Fan)
    
    class Meta:
        db_table="ASISTENCIA_FAN"