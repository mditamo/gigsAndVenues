from django.db import models
from complejo.models import Complejo
from banda.models import Banda
from sede.models import Sede
from evento.models import Evento


class Estado(models.Model):
    nombre=models.CharField(max_length=15)

    class Meta:
        db_table="Estado"

class Oferta(models.Model):
    motivo_rechazo=models.CharField(max_length=200)
    inicio_negociacion=models.CharField(max_length=1)
    monto=models.DecimalField('',None, 10, 2)
    fecha=models.DateField()
    hora=models.CharField(max_length=10);
    banda=models.ForeignKey(Banda)
    complejo=models.ForeignKey(Complejo)
    sede=models.ForeignKey(Sede)
    estado=models.ForeignKey(Estado)

    class Meta:
        db_table="Negociacion"

class CondicionOferta(models.Model):
    valor=models.CharField(max_length=200)
    banda=models.ForeignKey(Banda)
    complejo=models.ForeignKey(Complejo)
    sede=models.ForeignKey(Sede)
    oferta=models.ForeignKey(Oferta)
    
    class Meta:
        db_table="Condicion_Oferta"

"""class TipoCondicion(models.Model):
    nombre=models.CharField(max_length=20)
    
    class Meta:
        db_table="Tipo_Condicion"""

