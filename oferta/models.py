from django.db import models
from complejo.models import Complejo
from banda.models import Banda
from sede.models import Sede
from negociacion.models import EstadoNegociacion,Negociacion
from condiciones.models import CondicionUnitaria


class Oferta(models.Model):
    monto=models.DecimalField('',None, 10, 2,null=True)
    fecha=models.DateField(null=True)
    descripcion=models.CharField(max_length=200)
    usuario_oferta=models.CharField(max_length=1,null=True)
    is_ultima_oferta=models.IntegerField(max_length=1,null=True)
    is_penultima_oferta=models.IntegerField(max_length=1,null=True)
    banda=models.ForeignKey(Banda,null=True)
    complejo=models.ForeignKey(Complejo,null=True)
    sede=models.ForeignKey(Sede,null=True)
    negociacion=models.ForeignKey(Negociacion,null=True)
    
    estado=models.ForeignKey(EstadoNegociacion,null=True)
    condiciones=models.ManyToManyField(CondicionUnitaria,null=True,through="CondicionOferta") 

    class Meta:
        db_table="OFERTA"

class CondicionOferta(models.Model):
    oferta=models.ForeignKey(Oferta)
    condicionUnitaria=models.ForeignKey(CondicionUnitaria)
    
    class Meta:
        db_table="CONDICION_OFERTA"


