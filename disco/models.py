from django.db import models

from banda.models import *

class Tema(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TEMA"

    def __unicode__(self):
        return self.nombre

class TemaBanda(models.Model):
    tema=models.ForeignKey(Tema)
    banda=models.ForeignKey(Banda)
    duracion=models.CharField(max_length=20)
    class Meta:
        db_table="TEMA_BANDA"

    def __unicode__(self):
        return self.tema.nombre

class Disco(models.Model):
    nombre=models.CharField(max_length=200)
    fecha_publicacion=models.DateField(null=True)
    discografica=models.CharField(max_length=200)
    banda=models.ForeignKey(Banda)
    temas= models.ManyToManyField(TemaBanda, through="ComposicionDisco")
    class Meta:
        db_table="DISCO"

    def __unicode__(self):
        return self.nombre
		
class ComposicionDisco(models.Model):
    tema_banda=models.ForeignKey(TemaBanda)
    disco=models.ForeignKey(Disco)
    posicion=models.IntegerField(null=True)

    class Meta:
        db_table="COMPOSICION_DISCO"

    def __unicode__(self):
        return self.tema_banda.tema.nombre


