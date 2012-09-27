from django.db import models
from banda.models import Banda
from tema.models import TemaBanda

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


