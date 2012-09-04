from musico.models import *
from django.contrib import admin
from equipo.models import EquipoMusico

class EquipoMusicoInline(admin.StackedInline):
    model = EquipoMusico

class MusicoAdmin(admin.ModelAdmin):
    list_display  = ('username','first_name','last_name','posicion','estilo')
    search_fields = ['nombre']
    inlines = [EquipoMusicoInline]

admin.site.register(Estilo)
admin.site.register(Posicion)
admin.site.register(Musico,MusicoAdmin)

