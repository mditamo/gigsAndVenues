from entrada.models import *
from django.contrib import admin

class ReservaEventoAdmin(admin.ModelAdmin):
    list_display  = ('tipo_entrada','fan','estado','codigo_retiro', 'cantidad_entradas', 'fecha_vencimiento')

class ConfiguracionEntradaEventoAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'evento', 'cantidad_entradas_disponibles','cantidad_entradas_reserva','precio_entrada')

     
admin.site.register(ConfiguracionEntradaEvento,ConfiguracionEntradaEventoAdmin)
admin.site.register(EstadoReserva)
admin.site.register(ReservaEvento, ReservaEventoAdmin)
