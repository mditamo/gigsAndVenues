from django.db import models
from evento.models import Evento
from fan.models import Fan

class ConfiguracionEntradaEvento(models.Model):
    evento=models.ForeignKey(Evento)
    nombre=models.CharField(max_length=200)
    cantidad_entradas_disponibles=models.IntegerField()
    cantidad_entradas_reserva=models.IntegerField()
    precio_entrada=models.IntegerField()
    class Meta:
        db_table="CONFIGURACION_ENTRADA_EVENTO"
    
    def __unicode__(self):
        return self.nombre
   

class EstadoReserva(models.Model):
    nombre=models.CharField(max_length=200)
    
    class Meta:
        db_table="ESTADO_RESERVA"

    def __unicode__(self):
        return self.nombre
        
class ReservaEvento(models.Model):
    tipo_entrada=models.ForeignKey(ConfiguracionEntradaEvento)
    fan=models.ForeignKey(Fan)
    codigo_retiro=models.IntegerField()
    cantidad_entradas=models.IntegerField()
    fecha_vencimiento=models.DateField()
    estado=models.ForeignKey(EstadoReserva)
    class Meta:
        db_table="RESERVA_EVENTO"
        
