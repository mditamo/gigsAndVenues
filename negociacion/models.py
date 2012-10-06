from django.db import models
from complejo.models import Complejo
from banda.models import Banda
from sede.models import Sede
from evento.models import Evento
from condiciones.models import CondicionUnitaria


class Estado(models.Model):
    nombre=models.CharField(max_length=15)

    class Meta:
        db_table="Estado"

class Negociacion(models.Model):
    nombre=models.CharField(max_length=200)
    inicio_negociacion=models.CharField(max_length=1)
    fecha=models.DateField(null=True)    
    hora=models.CharField(max_length=10);
    bandas=models.ManyToManyField(Banda,null=True,through="NegociacionBanda")
    condiciones=models.ManyToManyField(CondicionUnitaria,null=True,through="CondicionNegociacion")
    complejo=models.ForeignKey(Complejo,null=True)
    sede=models.ForeignKey(Sede,null=True)
    evento=models.ForeignKey(Evento,null=True)
    monto=models.DecimalField('Monto',None, 10, 2,null=True)
    estado=models.ForeignKey(Estado,null=True)

    class Meta:
        db_table="NEGOCIACION"
      
class CondicionNegociacion(models.Model):
    negociacion=models.ForeignKey(Negociacion)
    condicionUnitaria=models.ForeignKey(CondicionUnitaria)
    
    class Meta:
        db_table="CONDICION_NEGOCIACION"        

class NegociacionBanda(models.Model):
    negociacion=models.ForeignKey(Negociacion)
    banda=models.ForeignKey(Banda)
    
    class Meta:
        db_table="NEGOCIACION_BANDA"    
    
    def __unicode__(self):
        return self.nombre
    
