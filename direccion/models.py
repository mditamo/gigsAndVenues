from django.db import models

class Provincia(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="PROVINCIA"

    def __unicode__(self):
        return self.nombre

class Barrio(models.Model):
    nombre=models.CharField(max_length=200)
    provincia=models.ForeignKey(Provincia)
    class Meta:
        db_table="BARRIO"

    def __unicode__(self):
        return self.nombre

class Direccion(models.Model):
    calle=models.CharField(max_length=200)
    numero=models.IntegerField()
    barrio=models.ForeignKey(Barrio)
    class Meta:
        db_table="DIRECCION"
    def __unicode__(self):
        return u'%s %s (%s)' % (self.calle, self.numero, self.barrio)
