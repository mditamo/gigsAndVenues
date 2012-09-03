from django.db import models
from banda.models import Banda

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