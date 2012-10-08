from django.db import models

class Tipo_Condicion(models.Model):
    nombre=models.CharField(max_length=20)
    
    class Meta:
        db_table="TIPO_CONDICION"   
     
    def __unicode__(self):
        return self.nombre    

class CondicionUnitaria(models.Model):
    descripcion=models.CharField(max_length=50)
    tipoCondicion=models.ForeignKey(Tipo_Condicion)
    valor=models.CharField(max_length=50)
    
    class Meta:
        db_table="CONDICION_UNITARIA"    
    
    def __unicode__(self):
        return self.nombre
