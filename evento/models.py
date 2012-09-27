from django.db import models
from complejo.models import Complejo
from sede.models import Sede
from fan.models import Fan


class Evento(models.Model):
    nombre=models.CharField(max_length=200)
    fecha=models.DateField()
    hora_inicio=models.CharField(max_length=10);
    descripcion=models.CharField(max_length=500)
    nombre_complejo=models.CharField(max_length=200)
    complejo=models.ForeignKey(Complejo)
    sede=models.ForeignKey(Sede)
    fans= models.ManyToManyField(Fan, through="AsistenciaFan")


    class Meta:
        db_table="EVENTO"

class AsistenciaFan(models.Model):
    evento=models.ForeignKey(Evento)
    fan=models.ForeignKey(Fan)
    
    class Meta:
        db_table="ASISTENCIA_FAN"