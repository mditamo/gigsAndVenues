from django.db import models
from complejo.models import Complejo
from banda.models import Banda
from sede.models import Sede
from evento.models import Evento
from test.test_imageop import MAX_LEN


class Estado(models.Model):
    nombre=models.CharField(max_length=15)

    class Meta:
        db_table="Estado"

class Negociacion(models.Model):
    nombre=models.CharField(max_length=200)
    inicio_negociacion=models.CharField(max_length=1)
    fecha=models.DateField(null=True)    
    hora=models.CharField(max_length=10);
    banda=models.ForeignKey(Banda,null=True)
    complejo=models.ForeignKey(Complejo,null=True)
    sede=models.ForeignKey(Sede,null=True)
    evento=models.ForeignKey(Evento,null=True)
    monto=models.DecimalField('Monto',None, 10, 2,null=True)
    estado=models.ForeignKey(Estado,null=True)

    class Meta:
        db_table="Negociacion"
    
class CondicionNegociacion(models.Model):
    valor=models.CharField(max_length=200)
    banda=models.ForeignKey(Banda)
    complejo=models.ForeignKey(Complejo)
    sede=models.ForeignKey(Sede)
    negociacion=models.ForeignKey(Negociacion)
    
    class Meta:
        db_table="Condicion_Negociacion"

class TipoCondicion(models.Model):
    nombre=models.CharField(max_length=20)
    
    class Meta:
        db_table="Tipo_Condicion"
