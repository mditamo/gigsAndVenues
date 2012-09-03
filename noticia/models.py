from django.db import models
from banda.models import Banda
from usuario.models import Complejo

class TipoNoticia(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="TIPO_NOTICIA"

    def __unicode__(self):
        return self.nombre

class EstadoNoticia(models.Model):
    nombre=models.CharField(max_length=200)
    class Meta:
        db_table="ESTADO_NOTICIA"

    def __unicode__(self):
        return self.nombre
    
    def is_borrador(self):
            return self.nombre=="Borrador"

    def is_publicado(self):
        return self.nombre=="Publicado"

    def is_archivado(self):
        return self.nombre=="Archivado"
    
class NoticiaBanda(models.Model):
    banda=models.ForeignKey(Banda)
    tipo_noticia=models.ForeignKey(TipoNoticia)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_publicacion=models.DateField()
    estado=models.ForeignKey(EstadoNoticia)
    class Meta:
        db_table="NOTICIA_BANDA"

    def __unicode__(self):
            return self.titulo

class NoticiaComplejo(models.Model):
    complejo=models.ForeignKey(Complejo)
    tipo_noticia=models.ForeignKey(TipoNoticia)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha_publicacion=models.DateField()
    estado=models.ForeignKey(EstadoNoticia)
    class Meta:
        db_table="NOTICIA_COMPLEJO"

    def __unicode__(self):
            return self.titulo
