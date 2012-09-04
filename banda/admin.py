from banda.models import *
from django.contrib import admin
from disco.models import TemaBanda

class BandaGeneroInline(admin.StackedInline):
    model = BandaGenero


class ComposicionBandaInline(admin.StackedInline):
    model = ComposicionBanda

class TemaBandaInline(admin.StackedInline):
    model = TemaBanda

class BandaAdmin(admin.ModelAdmin):
    list_display  = ('nombre','tipo_banda','fecha_creacion')
    search_fields = ['nombre']
    inlines = [BandaGeneroInline,ComposicionBandaInline, TemaBandaInline]


admin.site.register(TipoBanda)
admin.site.register(Banda,BandaAdmin)
admin.site.register(EstadoComposicionBanda)

