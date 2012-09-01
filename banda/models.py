from django.db import models
from musico.models import Musico, Posicion

class Genero(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="GENERO"

    def __unicode__(self):
        return self.nombre

class TipoBanda(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TIPO_BANDA"

    def __unicode__(self):
        return self.nombre

class Banda(models.Model):
    tipo_banda=models.ForeignKey(TipoBanda)
    nombre=models.CharField(max_length=200)
    fecha_creacion=models.DateField();
    musicos= models.ManyToManyField(Musico, through="ComposicionBanda")
    generos= models.ManyToManyField(Genero, through="BandaGenero")
    class Meta:
        db_table="BANDA"
    def __unicode__(self):
        return self.nombre

class EstadoComposicionBanda(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="ESTADO_COMPOSICION_BANDA"

    def __unicode__(self):
        return self.nombre

    def is_pendiente(self):
            return self.nombre=="Pendiente"

    def is_confirmado(self):
        return self.nombre=="Confirmado"

    def is_denegado(self):
        return self.nombre=="Denegado"
		
class ComposicionBanda(models.Model):
    musico=models.ForeignKey(Musico)
    banda=models.ForeignKey(Banda)
    posicion=models.ForeignKey(Posicion,null=True)
    fecha_inicio=models.DateField(null=True)
    fecha_fin=models.DateField(null=True)
    estado=models.ForeignKey(EstadoComposicionBanda)
    class Meta:
        db_table="COMPOSICION_BANDA"

    def __unicode__(self):
            return self.musico.username


class BandaGenero(models.Model):
    genero=models.ForeignKey(Genero)
    banda=models.ForeignKey(Banda)
    class Meta:
        db_table="BANDA_GENERO"


